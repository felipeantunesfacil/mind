---
tags: [letramento, facil, ia, analise, codigo, sheets, notebooklm, colab]
criado: 2026-08-14
atualizado: 2026-08-14
---

# Guia Prático de IA — Análise & Código (Sheets, NotebookLM, Colab)

Este tutorial prático foi desenvolvido para ajudar você a dominar as ferramentas de análise de dados, inteligência analítica e programação assistida por Inteligência Artificial do ecossistema do Google na **Fácil**. Aqui você aprenderá, passo a passo, a criar e organizar planilhas no Google Sheets, consolidar bases de dados e tirar dúvidas sem alucinação no NotebookLM, e escrever scripts analíticos e gráficos dinâmicos sem saber programar usando o Google Colab.

---

## Sumário

1. [1. Google Sheets: Inteligência de Dados e Planilhas](#1-google-sheets-inteligencia-de-dados-e-planilhas)
   - [Ativando o Gemini no Sheets](#ativando-o-gemini-no-sheets)
   - [Criando Tabelas Inteligentes](#criando-tabelas-inteligentes)
   - [Gerando Fórmulas com IA](#gerando-formulas-com-ia)
2. [2. NotebookLM: O Cérebro Corporativo Inteligente](#2-notebooklm-o-cerebro-corporativo-inteligente)
   - [Criando seu Primeiro Caderno e Carregando Fontes](#criando-seu-primeiro-caderno-e-carregando-fontes)
   - [Fazendo Perguntas com Citações](#fazendo-perguntas-com-citacoes)
   - [Gerando Resumos em Áudio (Audio Overview / Podcast)](#gerando-resumos-em-audio-audio-overview-podcast)
3. [3. Google Colab: Ciência de Dados Simplificada](#3-google-colab-ciencia-de-dados-simplificada)
   - [Criando um Notebook no Colab](#criando-um-notebook-no-colab)
   - [Gerando e Executando Código Python](#gerando-e-executando-codigo-python)
   - [Análise de Dados e Gráficos](#analise-de-dados-e-graficos)

---

## 1. Google Sheets: Inteligência de Dados e Planilhas <a name="1-google-sheets-inteligencia-de-dados-e-planilhas"></a>

O Gemini atua no Sheets ajudando você a estruturar cronogramas de tarefas, planejar orçamentos e escrever fórmulas complexas a partir de explicações simples em linguagem natural.

### Ativando o Gemini no Sheets <a name="ativando-o-gemini-no-sheets"></a>

1. Abra uma planilha em branco ou existente no Google Sheets.
2. No canto superior direito, clique no ícone do **Gemini** (as três estrelas brilhantes) para abrir o painel lateral de assistência.

---

### Criando Tabelas Inteligentes <a name="criando-tabelas-inteligentes"></a>

1. No painel lateral do Gemini, você verá opções rápidas ou um campo de texto aberto.
2. Escreva o que você precisa que sua planilha contenha. Exemplo:
   > *"Crie um rastreador de tarefas para a implantação de um novo software na Fácil, contendo colunas para: Nome da Tarefa, Responsável, Status, Prioridade, Data de Início e Data de Fim. Preencha com 5 exemplos práticos."*

![print-sheets-painel-lateral](print-sheets-painel-lateral.png)
*O que deve mostrar: Uma planilha em branco do Sheets com o painel lateral do Gemini aberto à direita, contendo o prompt citado acima digitado no campo de chat.*

3. O Gemini criará uma prévia da tabela. Se estiver correta, clique em **Inserir** (Insert).

![print-sheets-tabela-gerada](print-sheets-tabela-gerada.png)
*O que deve mostrar: A planilha do Sheets agora preenchida com a tabela estruturada gerada pela IA, destacando os cabeçalhos das colunas formatados e as linhas com dados de exemplo realistas.*

---

### Gerando Fórmulas com IA <a name="gerando-formulas-com-ia"></a>

Não precisa mais decorar comandos complicados do Excel/Sheets:
1. No painel lateral do Gemini, pergunte como fazer a fórmula desejada. Exemplo:
   > *"Como escrevo uma fórmula para calcular a diferença de dias entre a coluna E (Data de Fim) e a coluna D (Data de Início) e se a diferença for maior que 10, exibir 'Alerta'?"*
2. O Gemini fornecerá a fórmula exata (ex: `=IF(E2-D2>10; "Alerta"; "OK")`). Basta copiar e colar na célula correspondente!

---

## 2. NotebookLM: O Cérebro Corporativo Inteligente <a name="2-notebooklm-o-cerebro-corporativo-inteligente"></a>

O **NotebookLM** é o caderno de pesquisa avançado do Google. Ele trabalha estritamente com os documentos que você envia (PDFs, links, textos), garantindo respostas precisas e livres de "alucinações" (erros inventados pela IA).

### Criando seu Primeiro Caderno e Carregando Fontes <a name="criando-seu-primeiro-caderno-e-carregando-fontes"></a>

1. Acesse o portal do [NotebookLM](https://notebooklm.google/).
2. Clique no botão de **Novo Caderno** (New Notebook).

![print-notebooklm-novos-cadernos](print-notebooklm-novos-cadernos.png)
*O que deve mostrar: A tela inicial do NotebookLM com o painel central para criar um novo caderno destacado e as opções iniciais de upload de fontes (Google Drive, PDF, Texto Copiado, Link).*

3. Faça o upload dos arquivos de sua escolha (ex: PDFs de políticas de RH, manuais técnicos de sistemas da Fácil ou planilhas de referência).

![print-notebooklm-fontes-carregadas](print-notebooklm-fontes-carregadas.png)
*O que deve mostrar: A interface do caderno ativo mostrando, na barra lateral esquerda, uma lista com as fontes recém-carregadas (ex: manual.pdf, politica-homeoffice.pdf) devidamente marcadas com um check.*

---

### Fazendo Perguntas com Citação <a name="fazendo-perguntas-com-citacoes"></a>

1. Com as fontes selecionadas, envie uma pergunta no chat inferior. Exemplo:
   > *"Com base nos documentos carregados, qual é a tolerância máxima para atrasos no envio do relatório de despesas e onde devo enviá-lo?"*
2. A IA lerá seus arquivos e gerará uma resposta precisa.
3. Repare que a resposta traz **números em pequenos balões cinzas**. Eles são as **citações**. Clique em qualquer citação para abrir o documento fonte exatamente na página e no trecho de onde a IA extraiu aquela resposta.

![print-notebooklm-chat-faq](print-notebooklm-chat-faq.png)
*O que deve mostrar: A janela de chat central do NotebookLM exibindo a pergunta enviada e a resposta detalhada da IA com os números de citações destacados, e um trecho do documento de origem aparecendo em uma janela sobreposta ao clicar em uma citação.*

---

### Gerando Resumos em Áudio (Audio Overview / Podcast) <a name="gerando-resumos-em-audio-audio-overview-podcast"></a>

Excelente recurso para acelerar treinamentos e onboardings:
1. No canto superior direito do painel de fontes do NotebookLM, vá na seção do **Guia do Caderno** (Notebook Guide).
2. Na opção de **Conversa em áudio** (Audio Overview), clique no botão **Gerar** (Generate).
3. Aguarde alguns minutos. A IA criará uma conversa realista entre dois apresentadores (em formato de podcast profissional) explicando com clareza os pontos principais das fontes que você forneceu!

![print-notebooklm-audio-overview](print-notebooklm-audio-overview.png)
*O que deve mostrar: O painel lateral direito do Notebook Guide destacando a caixa do "Audio Overview" com os botões de reproduzir (Play), pausa, e indicador de tempo do podcast gerado.*

---

## 3. Google Colab: Ciência de Dados Simplificada <a name="3-google-colab-ciencia-de-dados-simplificada"></a>

O Google Colab permite escrever e rodar blocos de código Python diretamente no navegador. Com a assistência do Gemini integrado, você consegue programar, fazer limpezas em planilhas gigantes e analisar dados de forma automatizada apenas conversando.

### Criando um Notebook no Colab <a name="criando-um-notebook-no-colab"></a>

1. Acesse o portal do [Google Colab](https://colab.google/).
2. Faça login com sua conta institucional e clique em **Novo Notebook** (New Notebook).

![print-colab-novo-notebook](print-colab-novo-notebook.png)
*O que deve mostrar: A interface principal do Google Colab com um novo notebook aberto, mostrando a barra superior de ferramentas, a primeira célula de código em branco e o ícone redondo brilhante do Gemini de assistência de código visível.*

---

### Gerando e Executando Código Python <a name="gerando-e-executando-codigo-python"></a>

1. Clique na célula de código e clique no botão de assistência do Gemini (ou use `Ctrl + I`).
2. Digite o que você quer que o script faça. Exemplo:
   > *"Gere um script em Python usando Pandas para criar um faturamento mensal fictício para a Fácil com dados de Janeiro a Dezembro, adicionando colunas para faturamento bruto e líquido."*

![print-colab-codigo-gerado](print-colab-codigo-gerado.png)
*O que deve mostrar: A célula de código do Colab preenchida com o script Python gerado pelo Gemini, exibindo comentários didáticos explicativos e destacando o botão circular de "Play" (executar) no canto esquerdo da célula.*

3. Clique no botão de **Play** à esquerda da célula para rodar o código. A saída aparecerá logo abaixo.

---

### Análise de Dados e Gráficos <a name="analise-de-dados-e-graficos"></a>

Podemos pedir para o Gemini gerar gráficos estatísticos completos em segundos:
1. Adicione uma nova célula de código abaixo da anterior.
2. Peça ao Gemini:
   > *"Gere um gráfico de barras comparativo usando Matplotlib mostrando o faturamento líquido mês a mês de acordo com a tabela criada na célula anterior. Use cores azuis nas barras e adicione títulos e rótulos nos eixos."*
3. Execute a célula. O gráfico colorido aparecerá imediatamente na tela.

![print-colab-grafico-resultado](print-colab-grafico-resultado.png)
*O que deve mostrar: A tela do Colab exibindo o gráfico de barras estatístico colorido recém-gerado e renderizado logo abaixo da célula de código correspondente.*

---

## Ver também

- [letramento-facil.md](../letramento-facil.md) — Índice do projeto Letramento Fácil.
- [03-comunicacao.md](03-comunicacao.md) — Guia prático de IA para Comunicação (Gmail, Meet, Chat).
- [04-criacao.md](04-criacao.md) — Guia prático de IA para Criação de Documentos, Slides e Vídeos.
- [MIND.md](../../../MIND.md) — Índice geral do cérebro.
