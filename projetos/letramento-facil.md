---
tags: [projeto, letramento, facil, ia, google-workspace, gems, notebooklm, colab]
criado: 2026-08-14
atualizado: 2026-08-17
---

# Letramento Fácil

O **Letramento Fácil** é uma iniciativa estratégica de capacitação e cultura em Inteligência Artificial para a equipe da **Fácil**. O programa visa integrar o uso prático de IA Generativa no fluxo de trabalho diário dos colaboradores, transformando a tecnologia de uma ferramenta ocasional de chat em um assistente de produtividade integrado e padronizado.

---

## 🎯 Objetivo e Visão Geral

O objetivo principal é democratizar e sistematizar o uso de IA na Fácil, focando no ecossistema do **Google Workspace** e ferramentas avançadas como **Custom Gems**, **NotebookLM** e **Google Colab**. 

A visão do projeto é capacitar a equipe a:
1. **Eliminar Atrito Operacional:** Automatizar tarefas repetitivas como redação de e-mails de rotina, atas de reuniões e análise simples de dados.
2. **Escalar Conhecimento e Padrões:** Usar **Gems customizados** para fixar diretrizes e garantir que toda a equipe produza com o mesmo tom de voz e qualidade institucional, em vez de depender de prompts manuais e ad-hoc.
3. **Decisões Baseadas em Dados:** Habilitar colaboradores de diferentes áreas a extrair relatórios, analisar planilhas complexas e gerar scripts de dados no Colab de forma assistida pela IA, mesmo sem background de programação.

---

## 🛠️ Pilares do Ecossistema

O letramento é estruturado em três eixos principais de atuação prática:

| Comunicação | Criação | Análise & Código |
| :--- | :--- | :--- |
| • Gmail | • Google Docs | • Google Sheets |
| • Google Meet | • Google Slides | • NotebookLM |
| • Google Chat | • Google Vids | • Google Colab |

### 1. Comunicação Inteligente
Foco na redução do tempo de triagem de informações e na aceleração da comunicação com clientes e parceiros:
* **Gmail:** Uso do *"Me ajude a escrever"* (Help me write) para redação de e-mails rápidos, mudança de tons de voz (casual para formal) e síntese instantânea de threads longas de e-mails para rápida atualização após períodos de ausência.
* **Google Meet:** Adoção da ferramenta *"Tome notas por mim"* para transcrição automática, geração de atas concisas e definição automática de responsáveis por tarefas.

### 2. Criação Ágil
Capacitação na criação de conteúdo multimídia e documentos institucionais com suporte de design e redação assistida:
* **Google Docs:** Co-criação de propostas comerciais, escopos de projetos e documentação técnica diretamente do editor.
* **Google Slides:** Geração de layouts visuais, criação automática de imagens de suporte e estruturação de apresentações executivas.
* **Google Vids:** Geração de storyboards e produção automatizada de pequenos vídeos de alinhamento ou demonstração com vozes sintéticas e trilhas sugeridas.

### 3. Análise & Tomada de Decisão
Uso de ferramentas analíticas mais robustas que auxiliam no entendimento de grandes volumes de informação:
* **Google Sheets:** Geração de fórmulas complexas por comandos naturais e estruturação automática de tabelas.
* **NotebookLM:** Criação de bases de conhecimento privadas (como manuais de integração de clientes ou especificações de produto) para consulta rápida e livre de alucinações.
* **Google Colab:** Análise de dados em Python auxiliada pelo Gemini integrado, permitindo que analistas criem gráficos e relatórios estatísticos sem dominar código.

---

## 💎 Custom Gems: O Coração da Escala

Diferente do uso do Gemini tradicional (onde cada prompt precisa ser digitado do zero e os resultados tendem a ser heterogêneos), o projeto foca intensamente na criação de **Gems Customizados**.

* **Por que adotar?** Um Gem guarda em sua memória as instruções de contexto fixas (quem ele é, qual o público-alvo, quais regras de marca seguir, quais palavras evitar e qual a estrutura de saída). O colaborador apenas insere o conteúdo bruto e obtém um resultado perfeitamente formatado e alinhado aos padrões da Fácil.
* **Exemplos em implementação na Fácil:**
  * *Gem Redator Comercial:* Traduz notas de reuniões de alinhamento em propostas estruturadas no tom Fácil.
  * *Gem Analista de Requisitos:* Converte relatos informais de bugs ou ideias de clientes em tickets detalhados com critérios de aceitação.

---

## 📂 Guias e Materiais do Projeto

Todo o material oficial de suporte está estruturado em guias passo a passo, contendo explicações teóricas, exemplos reais aplicados à Fácil, exercícios práticos e capturas de tela (prints). 

Os arquivos de planejamento, guias práticos e o gerador de PDF estão organizados e podem ser acessados diretamente:

### 📖 Planejamento & Introdução
* [01 - Plano e Diretrizes de Letramento](../../letramento-facil/md/01-plano_letramento_facil.md) (versão [PDF](../../letramento-facil/pdf/01-plano_letramento_facil.pdf)) — Racional estratégico do projeto, visão geral das ferramentas, inteligência integrada do Workspace, Custom Gems e diretrizes.

### 📝 Módulos Práticos (Passo a Passo)
* [02 - Guia de IA para Comunicação](../../letramento-facil/md/02-comunicacao.md) (versão [PDF](../../letramento-facil/pdf/02-comunicacao.pdf)) — Guia focado em Gmail, Meet e Chat (como resumir e-mails e reuniões).
* [03 - Guia de IA para Criação](../../letramento-facil/md/03-criacao.md) (versão [PDF](../../letramento-facil/pdf/03-criacao.pdf)) — Guia prático de Google Docs, Slides e Vids (produção visual e textual rápida).
* [04 - Guia de IA para Análise & Código](../../letramento-facil/md/04-analise-codigo.md) (versão [PDF](../../letramento-facil/pdf/04-analise-codigo.pdf)) — Guia avançado de Google Sheets, NotebookLM e Google Colab.

### ⚙️ Utilitários de Compilação
* [Script de Compilação convert_pdf.py](../../letramento-facil/convert_pdf.py) — Script em Python desenvolvido sob medida para compilar os guias Markdown em PDFs institucionais polidos usando o motor do navegador local (Edge/Chrome).

---

## 🔗 Ver também

- [MIND.md](../MIND.md) — Índice geral da base de conhecimento pessoal.
