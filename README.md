# 🚗 Análise de Vendas de Veículos — Lions Seminovos

> Projeto de Extensão | Disciplina de Big Data | Universidade Estácio de Sá — Campus Nova América

Aplicação prática de **Big Data** e **Business Intelligence** para análise de vendas de veículos seminovos da rede [Lions Seminovos](https://lionsseminovos.com.br) (Lions Pre-Owned S.A.), referente ao mês de dezembro de 2024.

---

## 📊 Sobre o Projeto

O projeto consiste no ciclo completo de tratamento e análise de dados sobre a base operacional de vendas da Lions Seminovos:

- **Ingestão** dos dados a partir do sistema interno da empresa (formato `.xlsx`)
- **Tratamento** com Python + Pandas, aplicando limpeza, padronização e enriquecimento
- **Geração de dado simulado** (tabela de Metas) via script Python
- **Auditoria automatizada** de qualidade dos dados via script Python
- **Visualização** interativa em Microsoft Power BI Desktop

O dashboard final foi apresentado à gestão da Lions Seminovos, com avaliação documentada via Google Forms.

---

## 🗂️ Estrutura do Repositório

```
.
├── README.md                          # Este arquivo
├── requirements.txt                   # Dependências Python
│
├── tratamento_vendas.py               # Script de tratamento da base bruta
├── gerar_metas.py                     # Script gerador da tabela simulada de Metas
├── auditoria_inconsistencias.py       # Script de auditoria de qualidade
│
├── Vendas_2024.xlsx                   # Base bruta (entrada)
├── Vendas_2024_tratado.csv            # Base tratada (saída — para Power BI)
├── Vendas_2024_tratado.xlsx           # Base tratada (cópia em Excel)
├── Metas_2024.csv                     # Tabela de metas (dado simulado)
├── Metas_2024.xlsx                    # Tabela de metas (cópia em Excel)
├── Auditoria_Dados.csv                # Resumo da auditoria (para Power BI)
├── Auditoria_Dados.xlsx               # Resumo da auditoria (cópia em Excel)
│
└── Dashboard_Lions_Seminovos.pbix     # Dashboard Power BI Desktop
```

---

## 🔧 Tecnologias Utilizadas

| Camada | Ferramenta | Função |
|--------|-----------|---------|
| **Ingestão** | Python 3.11 + Pandas | Leitura do arquivo Excel da Lions |
| **Processamento** | Pandas, openpyxl | Limpeza, padronização e enriquecimento |
| **Armazenamento** | CSV (UTF-8 BOM) + XLSX | Formato compatível com Power BI |
| **Visualização** | Microsoft Power BI Desktop | Dashboard interativo |
| **Versionamento** | Git + GitHub | Controle de versão do código |

---

## 📋 A Base de Dados

A base bruta contém **289 registros** de vendas realizadas em dezembro de 2024, distribuídos entre **9 unidades** da rede:

| Código | Loja | Localização |
|--------|------|-------------|
| IT | Intendente Magalhães | Rio de Janeiro / RJ |
| DC | Duque de Caxias | Duque de Caxias / RJ |
| CG | Campo Grande | Rio de Janeiro / RJ |
| NI | Nova Iguaçu | Nova Iguaçu / RJ |
| NT | Niterói | Niterói / RJ |
| BM | Barra Mansa | Barra Mansa / RJ |
| MT | Matriz (Coelho Neto) | Rio de Janeiro / RJ |
| VP | Vila Prudente | São Paulo / SP |
| OS | Osasco | Osasco / SP |

**Colunas originais:** Valor do veículo, Marca, Modelo, Bairro, Município, UF, Data da venda, Loja, Endereço da loja.

---

## 🧹 Scripts Python — O Que Cada Um Faz

### 🔹 `tratamento_vendas.py` — Limpeza da base bruta

Aplica 8 transformações sobre `Vendas_2024.xlsx`:

1. **Remoção de espaços indevidos** em todas as colunas de texto (`.str.strip()`)
2. **Correção de erro pontual** de cadastro: modelo `"GOL 2024-06-01 00:00:00 +0000"` → `"GOL"`
3. **Conversão de tipo** da coluna `Data da venda` de texto para `datetime`
4. **Padronização de capitalização** dos modelos para CAIXA ALTA
5. **Criação da coluna** `Categoria` (Carro / Moto) baseada na marca
6. **Separação** da coluna `Endereço da loja` em duas: `Cidade da loja` e `UF da loja`
7. **Colunas derivadas de data**: `Dia da semana` e `Dia do mês`
8. **Renomeação** de `Valor do veículo` para `Valor` (facilita DAX)

**Saída:** `Vendas_2024_tratado.csv` e `Vendas_2024_tratado.xlsx`

### 🔹 `gerar_metas.py` — Geração do dado simulado (Metas)

Gera a tabela de **Metas mensais por loja**, que atende ao requisito de "dado simulado" do trabalho mínimo. As metas foram definidas com base no faturamento real, propositadamente colocando algumas acima e outras abaixo do realizado, criando uma narrativa interessante de "lojas que bateram" vs "lojas que não bateram".

> 💡 Originalmente a tabela foi construída dentro do Power BI pelo recurso "Inserir Dados". Este script reproduz o mesmo conteúdo de forma programática, permitindo versionamento e reuso futuro.

**Saída:** `Metas_2024.csv` e `Metas_2024.xlsx`

### 🔹 `auditoria_inconsistencias.py` — Auditoria de qualidade dos dados

Percorre a base bruta e gera um relatório consolidado com **todas as inconsistências encontradas**, classificadas em duas gravidades: **Crítico** e **Médio**. Imprime no terminal um overview no formato `* erro (X registros)` e exporta a tabela usada pelo gráfico de "Inconsistências por Gravidade" do dashboard.

**Saída:** `Auditoria_Dados.csv` e `Auditoria_Dados.xlsx`

Exemplo de saída no terminal:

```
🚨 ACHADOS CRÍTICOS
  * UF inconsistente com município cadastrado (3 registros)
  * Bairro como placeholder TEMPORÁRIO (3 registros)
  * Data vazada para o campo Modelo (1 registro)
  * Bairro contendo nome de cidade (1 registro)

⚠️  ACHADOS MÉDIOS
  * Espaços indevidos em Modelos (146 registros)
  * Espaços indevidos em Bairros (5 registros)
  * Espaço indevido na coluna Marca (1 registro)
  * Espaços duplos no interior de strings (16 registros)
```

### Como executar

```bash
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/lions-bigdata.git
cd lions-bigdata

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar os scripts (em qualquer ordem após o tratamento)
python tratamento_vendas.py             # gera a base tratada
python gerar_metas.py                   # gera a tabela de metas
python auditoria_inconsistencias.py     # gera o resumo de auditoria
```

---

## 📈 Dashboard Power BI

O arquivo `Dashboard_Lions_Seminovos.pbix` contém o dashboard final, organizado em **4 páginas** com **3 KPIs** e **7 visualizações distintas**:

### Página 1 — Visão Geral
- 🎯 **KPI:** Faturamento Total (R$ 17,0 mi)
- 🎯 **KPI:** Quantidade de Vendas (289)
- 🎯 **KPI:** Ticket Médio (R$ 58,98 mil)
- 📊 Faturamento por Marca (gráfico de barras)
- 🍩 Participação por Loja (gráfico de rosca)
- 🗺️ Faturamento por Estado (mapa de bolhas)
- 📉 Evolução Diária do Faturamento (linha temporal)
- 📋 Tabela de Inconsistências por Gravidade

### Página 2 — Metas vs Realizado
- 📊 Comparação Faturamento Real × Meta por loja
- 🎯 % de Atingimento da Meta Global

### Página 3 — Auditoria de Qualidade dos Dados
- 📋 Tabela com formatação condicional listando inconsistências
- 🏷️ Classificação em duas categorias: **Crítico** e **Médio**

### Página 4 — Detalhamento de Vendas
- Visões secundárias e filtros adicionais

### Como abrir o dashboard

1. Baixe e instale o [Microsoft Power BI Desktop](https://powerbi.microsoft.com/desktop/) (gratuito, Windows)
2. Abra o arquivo `Dashboard_Lions_Seminovos.pbix`
3. As três tabelas (`Vendas_2024_tratado`, `Metas`, `Auditoria_Dados`) já estarão carregadas com os relacionamentos configurados

---

## 🔍 Principais Insights Identificados

1. **Concentração geográfica:** ~80% do faturamento da rede está concentrado no estado do Rio de Janeiro
2. **Sazonalidade semanal:** picos de vendas nos sábados (dias 7, 14, 21 e 28 de dezembro)
3. **Mix popular:** Fiat lidera com ~40% do faturamento, seguida de Renault e Volkswagen
4. **Performance heterogênea:** 97% de atingimento da meta global, mas com lojas centrais abaixo e periféricas acima
5. **Qualidade dos dados:** 175 registros (de 289) apresentam algum tipo de inconsistência, sendo 8 deles **Críticos** (afetam decisão regional)

---

## 👥 Sobre o Projeto

| Item | Detalhe |
|------|---------|
| **Disciplina** | Big Data |
| **Instituição** | Universidade Estácio de Sá — Campus Nova América |
| **Discente** | Joel Vitor Niino Campos |
| **Orientador** | Prof. Lucas Floriano |
| **Parte Interessada** | Lions Seminovos (Lions Pre-Owned S.A.) |
| **Ano** | 2026 |
| **Local** | Rio de Janeiro / RJ |

A utilização dos dados foi autorizada por termo de cooperação assinado entre a Universidade Estácio de Sá e a Lions Seminovos para fins exclusivamente acadêmicos.

---

## 📚 Referencial Teórico

- FÉLIX, B. M.; TAVARES, E.; CAVALCANTE, N. W. F. *Fatores críticos de sucesso para adoção de Big Data no varejo virtual: estudo de caso do Magazine Luiza.* Revista Brasileira de Gestão de Negócios, v. 20, 2018.
- MCAFEE, A.; BRYNJOLFSSON, E. *Big data: the management revolution.* Harvard Business Review, v. 90, n. 10, 2012.
- PROVOST, F.; FAWCETT, T. *Data Science for Business.* O'Reilly Media, 2013.

---

## 📄 Licença

Projeto desenvolvido para fins acadêmicos no âmbito da disciplina de Big Data da Estácio de Sá. Os dados utilizados são de propriedade da Lions Seminovos e foram cedidos mediante termo de cooperação institucional.
