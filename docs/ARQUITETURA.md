# Mind — Arquitetura

Este documento descreve a arquitetura e as decisões de design do Mind: por que a estrutura é essa, quais mecanismos do Gemini CLI cada peça usa, e o que ainda está em aberto. Leia antes de propor uma mudança estrutural nova — a maior parte das decisões abaixo já foi validada e não precisa ser redescutida do zero.

---

## 1. O que é o Mind

O Mind é uma base de conhecimento pessoal, organizada como uma árvore de arquivos Markdown com um índice central e subarquivos por tema — pensada pra ser editada visualmente (ex: Obsidian) e consultada pelo Gemini CLI sob demanda.

Tem dois usos simultâneos:

1. **PKM pessoal** ("segundo cérebro"): vida pessoal, hobbies, conhecimentos e contexto de projetos, tudo pesquisável e navegável.
2. **Base de conhecimento pro Gemini CLI**: em qualquer conversa, o Gemini deve conseguir consultar esse conhecimento **sem carregar a árvore inteira no contexto** — só o(s) arquivo(s) relevante(s) pra pergunta feita.

Um complemento opcional (ver seção 9) é um "time" de agentes especializados pra
desenvolver software — não faz parte do Mind em si, mas pode ser plugado por cima.

**Princípio orientador, vale pra toda decisão de arquitetura:** tudo que for construído no Mind — estrutura de pastas, formato e tamanho dos nós, granularidade dos arquivos — precisa funcionar bem tanto pra leitura/edição humana quanto pra consulta sob demanda pelo Gemini (incluindo por voz, se houver essa integração — seção 8). Não vale otimizar pensando só numa das pontas.

---

## 2. Mecanismos do Gemini CLI usados

| Necessidade                                            | Mecanismo                             | Como funciona                                                                                                                                                                                                             |
| ------------------------------------------------------ | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Base de conhecimento consultada sob demanda            | **Skill** (`SKILL.md`)                 | Só a descrição fica na memória da sessão o tempo todo; o corpo completo (e arquivos de referência que ele apontar) só é lido quando a pergunta bate com a descrição — via ferramenta `Read`, não automático              |
| Time de agentes especializados                          | **Subagente** (`.gemini/agents/*.md`)  | Cada um roda numa janela de contexto isolada, com prompt de sistema, lista de ferramentas e modelo próprios. O agente geral decide quando delegar com base na `description` de cada subagente                            |
| Config/instrução leve sempre presente                  | `GEMINI.md` do projeto/usuário         | Deve ficar enxuto: descreve a estrutura e instrui a consultar a Skill — não deve conter conteúdo pesado carregado sempre                                                                                                  |

Uma decisão descartada: implementar o índice via `GEMINI.md` com `@import` de subarquivos. Esse mecanismo carrega todos os arquivos importados no início da sessão, recursivamente, independente de serem relevantes pra pergunta feita — o oposto de "sob demanda".

Skills e Subagentes existem em dois níveis:
- **Nível de usuário** (`~/.gemini/skills/`, `~/.gemini/agents/`): disponíveis em qualquer projeto, independente de qual está ativo.
- **Nível de projeto** (`.gemini/skills/`, `.gemini/agents/` dentro do repo): só valem quando aquele projeto está ativo.

Como o Mind deve estar disponível não importa em qual projeto estiver ativo, a Skill de conhecimento e o gatilho de captura (seção 7) vivem em **nível de usuário**.

---

## 3. Onde o vault mora

**Regra:** o vault deve viver num caminho fixo e estável, versionado em git.

**Motivo:** se houver integração por voz (seção 8), o roteador que troca de "projeto ativo" normalmente resolve o nome falado casando com uma subpasta direta de uma raiz de projetos conhecida — o vault precisa estar dentro dessa raiz pra isso funcionar. Mesmo sem integração por voz, um caminho estável evita quebrar os symlinks descritos na seção 6.

Recomendações gerais:
- **Links dentro do vault**: preferir links relativos (`[texto](caminho/arquivo.md)`) a `[[wikilink]]` puro, ou garantir nomes de arquivo únicos no vault inteiro — isso deixa a navegação do Gemini (via `Read`/`Grep`) determinística.
- **Não duplicar documentação que já existe em outro repo**: um nó sobre um projeto externo deve **apontar** para o documento vivo daquele projeto (ex: um `PROGRESS.md` já mantido lá), não copiar o conteúdo — evita os dois desalinharem.

O caminho concreto usado em cada instalação fica na seção 10.

---

## 4. Estrutura de pastas

```
mind/
├── docs/
│   └── ARQUITETURA.md          (este arquivo)
├── MIND.md                     (índice raiz: só links + 1 linha de descrição cada, sem conteúdo pesado)
├── config.md                   (configuração de funcionamento — idioma, como chamar o usuário, fuso, tom, papel; não é nó de conhecimento)
├── <categoria-1>/              (ex: vida-pessoal/, conhecimentos/, projetos/ — nomes livres)
│   └── <categoria-1>.md
├── .gemini/                    (Skills/Subagentes/settings de PROJETO — só valem com mind ativo)
│   ├── skills/
│   ├── agents/
│   └── settings.json
├── .gemini/                (armazém real das Skills/Subagentes/GEMINI.md de USUÁRIO — ver seção 6)
│   ├── GEMINI.md
│   ├── skills/
│   └── agents/
└── scripts/
    └── setup-symlinks.sh       (recria os symlinks de .gemini/ em ~/.gemini/ após um git clone)
```

**Regra: crescimento orgânico, sem pré-scaffold.** O diagrama acima é ilustrativo, não uma árvore pra pré-criar de uma vez. Não se cria pasta/nó vazio ("stub") antes de ter conteúdo real — a árvore cresce um nó de cada vez, conforme o sistema de captura (seção 7) ou edição direta no vault. `MIND.md` começa praticamente vazio (só a instrução de como crescer) e ganha uma linha por nó real conforme surgirem.

**`config.md`:** perguntas de configuração inicial de funcionamento (idioma de conversa, como chamar o usuário, fuso horário, tom das respostas, papel/profissão), cada uma com resposta `(ainda não respondido)` até você preencher. Um hook `SessionStart` em `.gemini/settings.json` faz `grep` por esse marcador e injeta um lembrete no contexto pra Gemini perguntar assim que detectar alguma em aberto — garante que você seja perguntado logo na primeira sessão depois de clonar, sem depender do skill `mind` ser acionado por algum outro gatilho primeiro.

---

## 5. Frontmatter e convenções de nó

Todo nó novo leva frontmatter mínimo (padrão Obsidian):

```yaml
---
tags: [tag1, tag2]
criado: AAAA-MM-DD
atualizado: AAAA-MM-DD
---
```

Tags livres, mas reaproveitando as que já existirem em nós parecidos em vez de inventar sinônimo novo.

**Regra de tamanho/split (de cima pra baixo):** se um nó passar de ~120-150 linhas ou claramente virar dois assuntos distintos, ele vira uma pasta com índice próprio no mesmo padrão do `MIND.md` (ex.: `tema/tema.md` vira o índice, e os subtópicos viram `tema/subtopico-a.md`). Mantém os nós curtos o bastante pra funcionar bem também por voz, se essa integração existir.

**Regra de reagrupamento (de baixo pra cima):** ao ler o índice de um nível (raiz ou subpasta), se dois ou mais nós/pastas daquele nível compartilharem um tema mais amplo, ou se aquele nível acumulou muitas entradas soltas sem estrutura (regra de bolso: ~6-8+), é sinal de que falta uma pasta intermediária nova. Nunca mover/reorganizar arquivos sem confirmação — sempre propor primeiro (quais nós agrupar, sob que nome, por quê) e só executar depois de aprovado, corrigindo os links relativos afetados.

**Tasks/pendências centralizadas em `tarefas/`:** qualquer item acionável — algo que falta fazer, uma decisão pendente — vive só em `tarefas/pessoal.md` ou `tarefas/empresa.md`, nunca como lista solta dentro de outro nó (ex.: uma seção `## Pendências` dentro de um nó de projeto). Nós de projeto/conhecimento descrevem fatos ("Estado atual"), e apontam pra `tarefas/` quando o fato tem uma ação pendente associada — não duplicam o item. Motivo: task espalhada em dois lugares tende a desalinhar, porque só um dos dois é atualizado quando o item avança.

**Links "Ver também":** ao criar ou editar um nó, checar se ele se relaciona com outro nó existente e, se sim, adicionar um link cruzado nos dois (seção `## Ver também`, link relativo). É isso que faz o vault funcionar como grafo, não como uma pilha de arquivos soltos.

**Higiene de links:** nem toda relação vira link. Dois critérios:
- **Relação real, não trivia genérica.** "Mesmo padrão de stack" ou "mesmo tipo de projeto" entre dois nós-irmãos não é motivo suficiente pra uma aresta — não ajuda a decidir se vale abrir o outro arquivo. Se o fato for relevante, vira prosa no nó mais geral que já cobre os dois (ex.: a empresa-mãe descreve que os produtos dela usam a mesma stack), não um link entre os irmãos.
- **Sem duplicar "Depende de"/"Consumido por".** Essas seções já são a aresta do grafo (uma metade de cada lado). Repetir o mesmo link em "Ver também" é redundante — só entra ali uma relação diferente da já coberta.

---

## 6. Armazém único: Skills/Subagentes de usuário moram dentro do vault

**Decisão:** Skills, Subagentes e o `GEMINI.md` de nível usuário não ficam só em `~/.gemini/` — o conteúdo real mora dentro do próprio vault (`mind/.gemini/`, espelhando a estrutura de `~/.gemini/`), e `~/.gemini/` aponta pra lá via **symlink**.

**Motivo:** o vault é versionado em git e clonável em outra máquina. Se essas Skills/Subagentes ficassem só em `~/.gemini/` (fora do repo), não acompanhariam a migração e teriam que ser recriadas do zero em cada máquina nova.

Mecanismo (padrão "dotfiles", não é recurso novo do Gemini CLI — é symlink comum):

- `~/.gemini/skills/mind` e `~/.gemini/agents/*.md`, por exemplo, viram symlinks apontando pra dentro de `mind/.gemini/...`. O Gemini CLI continua lendo normalmente de `~/.gemini/` (onde ele espera encontrar Skills/Subagentes de usuário), mas o conteúdo de verdade — e o histórico de versão — vive no repo do vault.
- `scripts/setup-symlinks.sh` recria esses symlinks a partir do que estiver em `.gemini/`. Depois de um `git clone` numa máquina nova, rodar esse script é o único passo manual necessário (além de clonar no caminho esperado, se houver integração por voz — seção 3).
- Os symlinks em si não são commitados (não sobrevivem bem entre setups/SOs diferentes); o script os recria a partir do conteúdo versionado.
- Skills/Subagentes de **projeto** (só valem com `mind` ativo) não precisam desse truque: já moram nativamente em `mind/.gemini/`, sem symlink.

O script foi validado simulando uma máquina nova (clone real + execução com `$HOME` redirecionado) e é idempotente — rodar mais de uma vez não quebra nada.

---

## 7. Captura proativa de conhecimento

**Decisão:** durante qualquer conversa — não só quando `mind` é o projeto ativo — o Gemini presta atenção a informação durável (fatos, decisões, contexto de outro projeto, ou regras de como o Gemini deve trabalhar) e **pergunta** antes de salvar. Se confirmado, decide se edita um nó existente ou cria um novo, e mantém `MIND.md` atualizado.

Isso é conceitualmente parecido com um sistema de memória interno de assistente (que observa a conversa e propõe salvar aprendizados), mas com um alvo diferente: em vez de um formato interno não editável pelo usuário, escreve nos arquivos Markdown do próprio vault — legível/editável fora do Gemini e versionado.

**Por que o gatilho não fica só no `GEMINI.md` de projeto do mind:** se ficasse, só dispararia com `mind` como projeto ativo, perdendo o caso de uso mais comum (comentar algo relevante enquanto se trabalha em outro projeto). Por isso o desenho é em duas camadas:

- **Gatilho** (curto, sempre carregado, observa a conversa e decide quando oferecer): `GEMINI.md`, nível usuário — vale em qualquer projeto ativo via symlink em `~/.gemini/GEMINI.md`.
- **Procedimento** (pesado, só lido quando o gatilho aciona): `.gemini/skills/mind/SKILL.md` — como decidir nó existente vs. nó novo, convenções de pasta/frontmatter, split e reagrupamento (seção 5), não duplicar docs de outros projetos.

Regras explícitas do gatilho: nunca escrever sem confirmação prévia; não interromper a conversa por qualquer detalhe pequeno, só quando parecer que vale a pena persistir; a captura **nunca** dá `git add`/`commit` sozinha — commitar é sempre decisão manual, pra revisar o diff antes.

**Regra de escopo — o Mind também guarda regras de trabalho, não só fatos:** o gatilho cobre explicitamente "regras de como o Gemini deve trabalhar" (convenções de commit, formato de resposta, o que evitar/repetir), não só conhecimento sobre a vida do usuário. O princípio geral: nenhuma informação durável desse tipo deve ficar presa só num sistema de memória interno não versionado quando ela deveria estar no Mind — isso recriaria em paralelo o mesmo problema que o Mind existe pra resolver. Regras de trabalho curtas moram direto na seção correspondente do `GEMINI.md`; se crescerem demais, aplica-se a regra de split (seção 5).

**Regra de trabalho pode ser de projeto, não só global:** nem toda regra de trabalho vale pra qualquer projeto — "nesse repo, sempre faça X" é diferente de "sempre faça X, em qualquer projeto". Regra de projeto vai no `GEMINI.md` da raiz daquele repo (mecanismo nativo do Gemini CLI, nível projeto — carregado só quando aquele projeto está ativo, ver seção 2), não no `GEMINI.md` do vault (nível usuário, carregado sempre, em qualquer projeto). Ao capturar uma regra de trabalho, decidir esse escopo antes de escrever é parte do procedimento — ver `.gemini/skills/mind/SKILL.md`.

---

## 8. Integração por voz (opcional)

O Mind funciona sozinho só com Gemini CLI (teclado) e um editor de Markdown. Uma extensão possível é um assistente de voz externo que resolve "projeto ativo" por voz escaneando uma raiz de projetos conhecida e rodando o Gemini CLI CLI apontado pra ela — nesse caso, dizer o nome do vault já troca o projeto ativo pra ele, sem precisar de código novo específico pro Mind, desde que:

- o vault esteja dentro da raiz de projetos que o assistente escaneia (ver seção 3);
- exista um `.gemini/settings.json` de projeto no vault (mesmo que mínimo), já que é isso que o assistente espera encontrar pra reconhecer a pasta como projeto válido.

**Risco conhecido:** reconhecimento de voz pode errar a transcrição do nome do vault ao trocar de projeto — escolher um nome foneticamente distinto dos demais projetos ajuda. Vale testar ao vivo como qualquer integração nova.

Detalhes concretos da integração usada em cada instalação (se houver) ficam na seção 10, não aqui — esta seção descreve só o padrão geral.

---

## 9. Time de agentes de desenvolvimento (opcional)

O Mind, por padrão, só ajuda a organizar conhecimento pessoal — não inclui um time de
subagentes pra desenvolver software. Se além de usar o Mind você também constrói
produtos/MVPs (apps, sites, etc.) e quer um padrão de agentes especializados
(orquestrador + especialistas — produto, design, mobile, backend, devops, QA, etc.)
pra acelerar esse trabalho, existe um complemento pronto e opcional pra isso:
[Café Labs Forge](https://github.com/CafeLabsCorp/forge) — extraído e generalizado de
um setup real usado em produção, sem referência a nenhum produto/empresa específico.

É totalmente desacoplado do Mind: vive no próprio repositório, com seu próprio script
de symlink (`scripts/setup-symlinks.sh`, mesmo padrão do Mind — seção 6 — mas
apontando pra `~/.gemini/agents/`), e não depende do Mind pra funcionar (nem
vice-versa). Configurar:

```bash
git clone https://github.com/CafeLabsCorp/forge.git forge
cd forge
./scripts/setup-symlinks.sh
```

**Quando faz sentido mencionar**: se durante uma conversa o usuário indicar que quer
começar a desenvolver algo (uma ideia de produto, um MVP, um app novo) e esse time de
agentes ainda não estiver configurado na máquina, vale mencionar essa opção — sem
insistir, só como algo disponível. Não é pré-requisito de nada no Mind, e quem só quer
organizar conhecimento pessoal provavelmente nunca vai precisar dele.

---

## 10. Configuração desta instância

> Preencha esta seção com os detalhes concretos da sua instalação (caminho real do vault, se o repositório já foi inicializado, se há integração por voz, etc.) conforme for configurando. É o bloco mais fácil de esquecer de genericizar se algum dia você quiser repassar este vault adiante — mantenha os detalhes pessoais concentrados aqui, em vez de espalhados pelo resto do documento.

- Caminho do vault nesta máquina: `<preencher>`.
- Repositório git: `<preencher — inicializado? em que branch?>`.
- Integração por voz: `<preencher, se houver>`.
- Time de agentes de desenvolvimento (Forge): `<preencher, se configurado — caminho do clone>`.
- Repositório privado a partir do momento em que os nós de conhecimento tiverem conteúdo pessoal real.

---

## 11. Roadmap / decisões em aberto

- **Teste ao vivo da troca de projeto por voz**, se houver integração por voz — só validável rodando o reconhecimento de fala de verdade, não por leitura de código.
- **Validação end-to-end da captura fora do projeto mind**: confirmar que, numa conversa dentro de outro projeto ativo, o gatilho de fato oferece salvar e a escrita funciona ponta a ponta.

~~Time de subagentes especializados para desenvolvimento~~ — resolvido via o
complemento opcional [Café Labs Forge](https://github.com/CafeLabsCorp/forge), ver
seção 9.

---

## 12. Recebendo atualizações do template

**Decisão:** quem clona este template pra começar o próprio vault deve configurá-lo como um fork "manual" via git — dois remotes, `upstream` (este repo) e `origin` (o repo privado da pessoa) — em vez de gerar o repo pelo botão "Use this template" do GitHub.

```bash
git clone git@github.com:CafeLabsCorp/mind-template.git mind
cd mind
git remote rename origin upstream
git remote add origin <repo-privado-da-pessoa>
git push -u origin main
```

Atualizações futuras: `git fetch upstream && git merge upstream/main`.

**Motivo de não usar "Use this template":** esse botão gera um repositório com histórico git desconectado do original — sem ancestral comum. Um `git merge` posterior vira merge de árvores não relacionadas (exige `--allow-unrelated-histories` e tem muito mais superfície pra conflito espúrio, porque o git não consegue distinguir "arquivo novo" de "arquivo modificado" sem histórico compartilhado). Clonar de verdade preserva esse histórico desde o commit zero — merges futuros tendem a ser triviais.

**Por que o merge tende a ficar limpo:** consequência direta da separação já estabelecida entre engenharia (seção 4 — `docs/`, `.gemini/`, `scripts/`, `.gemini/`) e conteúdo pessoal (`MIND.md` preenchido + nós). O template nunca toca os arquivos de conteúdo da pessoa; a pessoa normalmente não edita os arquivos de engenharia. Como os dois lados do merge tocam arquivos diferentes, o git resolve sozinho na maioria das vezes.

**Ponto de atrito conhecido:** `.gemini/settings.json` (seção 4) acumula permissões liberadas ao longo do uso — é o único arquivo de engenharia que a pessoa também edita organicamente. Se o template mudar esse arquivo e a pessoa também tiver mudado, o merge pode conflitar ali. Raro e de resolução simples (arquivo pequeno) — não justifica um mecanismo mais complexo (submodule/subtree).

---

## 13. Manutenção periódica (otimização do vault)

**Decisão:** anotações acumulam histórico redundante com o tempo — tarefa concluída sem lição durável, fato duplicado entre nós, detalhe operacional que só importava no momento em que foi feito. Por isso vale ter uma rotina de otimização periódica (cadência sugerida: semanal) que **sempre pergunta antes de rodar** — nunca edita o vault por conta própria sem confirmação da rodada.

**Mecanismo sugerido:** mesmo padrão já usado pra `config.md` (seção 4) — um hook `SessionStart` em `.gemini/settings.json` (nível projeto, dispara quando o `mind` é o projeto ativo). A cada início de conversa, um comando local lê a última data registrada em `docs/MANUTENCAO.md` (log de execuções — não é nó de conhecimento, não segue o frontmatter da seção 5) e calcula há quantos dias ela foi. Se já passou o intervalo escolhido, injeta contexto instruindo o Gemini a perguntar ao usuário, logo no início da conversa, se pode rodar uma nova otimização — só executa se ele confirmar. Não depende de nuvem, GitHub conectado ou processo externo: roda como qualquer outro hook local do repo, e só é checado quando o vault de fato é aberto (mesma limitação já aceita pelo hook do `config.md`).

**Critérios de corte/reorganização, uma vez confirmada a rodada:**
- Itens concluídos (`[x]`) cujo relato só documenta um evento pontual já resolvido, sem decisão/motivo que ainda importe daqui pra frente — compactar ou remover.
- Informação duplicada entre dois ou mais nós — manter só a fonte principal, os demais passam a referenciar por link (mesmo princípio de não duplicar da seção 3).
- Detalhe operacional excessivo (sequência exata de comandos, passo a passo de como algo foi feito) quando só o resultado/decisão interessa daqui pra frente.
- **Nunca remove:** itens de tarefa ainda abertos (`tarefas/`), decisões com racional ainda referenciado por outro nó, ou qualquer conteúdo fora desses três critérios.

**Registro:** cada rodada (manual ou via rotina) deixa uma linha em `docs/MANUTENCAO.md` com data e resumo do que mudou — é essa data que a próxima checagem usa como referência.

**Aprovação:** por padrão, uma vez confirmada a rodada em si, a otimização edita os nós diretamente e resume as mudanças ao final (não pede aprovação item a item) — commit continua sendo decisão manual, como qualquer mudança no vault (seção 7).
