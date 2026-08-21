---
tags: [config, mind]
criado: 2026-07-23
atualizado: 2026-07-23
---
# Configuração do Mind

[](https://github.com/Lipefsk05/mind/blob/main/config.md#configura%C3%A7%C3%A3o-do-mind)

Perguntas de configuração inicial de como o Claude deve trabalhar com este vault e com o usuário — respondidas uma vez, na primeira conversa depois de clonar o vault (ou quando o usuário quiser mudar algo aqui depois). Diferente de `claude-user/CLAUDE.md` (regras de trabalho específicas — convenções de commit, formato de resposta) e de `MIND.md` (índice de conhecimento): este arquivo é só a configuração inicial de funcionamento.

**Se alguma resposta abaixo estiver como `(ainda não respondido)`**, pergunte ao usuário essa(s) pergunta(s) logo no início da conversa (pode agrupar via `AskUserQuestion`), e grave a resposta aqui — substituindo o marcador, não apagando a pergunta.

## Idioma de conversa

[](https://github.com/Lipefsk05/mind/blob/main/config.md#idioma-de-conversa)

Em qual idioma o Claude deve responder por padrão? Opções sugeridas: português, inglês, ou outro (texto livre).

**Resposta:** Português.

## Como quer ser chamado

[](https://github.com/Lipefsk05/mind/blob/main/config.md#como-quer-ser-chamado)

Nome ou apelido que o Claude deve usar ao se referir ao usuário nas respostas.

**Resposta:** Felipe.

## Fuso horário

[](https://github.com/Lipefsk05/mind/blob/main/config.md#fuso-hor%C3%A1rio)

Pra interpretar datas relativas ("amanhã", "sexta") e registrar tarefas/memórias com a data certa.

**Resposta:** América/São_Paulo (BRT, UTC-3) — Belo Horizonte.

## Tom / formalidade das respostas

[](https://github.com/Lipefsk05/mind/blob/main/config.md#tom--formalidade-das-respostas)

Ex.: direto e casual vs. mais formal.

**Resposta:** Direto e casual, sem formalidade, frases curtas.

## Papel / profissão principal

[](https://github.com/Lipefsk05/mind/blob/main/config.md#papel--profiss%C3%A3o-principal)

O que a pessoa faz — bootstrap rápido pra calibrar explicações técnicas desde a primeira conversa (complementa memórias tipo "user" que se acumulam aos poucos com o tempo).

**Resposta:** Estudante de Ciência da Computação (em processo de avaliar troca pra Sistemas de Informação ou ADS) + estagiário no Grupo Fácil (IA/automação). Ver [carreira/carreira.md](https://github.com/Lipefsk05/mind/blob/main/carreira/carreira.md).

## Ver também

[](https://github.com/Lipefsk05/mind/blob/main/config.md#ver-tamb%C3%A9m)

- [MIND.md](https://github.com/Lipefsk05/mind/blob/main/MIND.md)
- [claude-user/CLAUDE.md](https://github.com/Lipefsk05/mind/blob/main/claude-user/CLAUDE.md) — regras de trabalho (diferente disto aqui, que é configuração inicial)