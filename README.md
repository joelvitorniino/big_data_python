# 🚗 Análise de Vendas de Veículos — Lions Seminovos

> Projeto de Extensão | Disciplina de Big Data | Universidade Estácio de Sá — Campus Nova América

Aplicação prática de **Big Data** e **Business Intelligence** para análise de vendas de veículos seminovos da rede [Lions Seminovos](https://lionsseminovos.com.br) (Lions Pre-Owned S.A.), referente ao mês de dezembro de 2024.

---

## 📊 Sobre o Projeto

O projeto consiste no ciclo completo de tratamento e análise de dados sobre a base operacional de vendas da Lions Seminovos:

- **Ingestão** dos dados a partir do sistema interno da empresa (formato `.xlsx`)
- **Tratamento** com Python + Pandas, aplicando limpeza, padronização e enriquecimento
- **Visualização** interativa em Microsoft Power BI Desktop
- **Auditoria** de qualidade dos dados como entregável complementar

O dashboard final foi apresentado à gestão da Lions Seminovos, com avaliação documentada via Google Forms.

---

## 🗂️ Estrutura do Repositório

```
.
├── README.md                     # Este arquivo
├── requirements.txt              # Dependências Python
├── tratamento_vendas.py          # Script de tratamento dos dados
├── Vendas_2024.xlsx              # Base bruta (entrada)
├── Vendas_2024_tratado.csv       # Base tratada (saída — para Power BI)
├── Vendas_2024_tratado.xlsx      # Base tratada (cópia em Excel)
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

## 🧹 Tratamentos Aplicados no Pandas

O script `tratamento_vendas.py` aplica as seguintes transformações sobre a base bruta:

1. **Remoção de espaços indevidos** em todas as colunas de texto (`.str.strip()`)
2. **Correção de erro pontual** de cadastro: modelo `"GOL 2024-06-01 00:00:00 +0000"` → `"GOL"`
3. **Conversão de tipo** da coluna `Data da venda` de texto para `datetime`
4. **Padronização de capitalização** dos modelos para CAIXA ALTA
5. **Criação da coluna** `Categoria` (Carro / Moto) baseada na marca
6. **Separação** da coluna `Endereço da loja` em duas: `Cidade da loja` e `UF da loja`
7. **Colunas derivadas de data**: `Dia da semana` e `Dia do mês`
8. **Renomeação** de `Valor do veículo` para `Valor` (facilita DAX)

### Como executar

```bash
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/lions-bigdata.git
cd lions-bigdata

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar o tratamento
python tratamento_vendas.py
```

**Saída esperada:** geração dos arquivos `Vendas_2024_tratado.csv` e `Vendas_2024_tratado.xlsx`, prontos para serem importados no Power BI Desktop.

---

## 📈 Dashboard Power BI

O dashboard final está organizado em **4 páginas** com **3 KPIs** e **7 visualizações distintas**:

### Página 1 — Visão Geral
- 🎯 **KPI:** Faturamento Total (R$ 17,0 mi)
- 🎯 **KPI:** Quantidade de Vendas (289)
- 🎯 **KPI:** Ticket Médio (R$ 58,98 mil)
- 📊 Faturamento por Marca (gráfico de barras)
- 🍩 Participação por Loja (gráfico de rosca)
- 🗺️ Faturamento por Estado (mapa de bolhas)
- 📉 Evolução Diária do Faturamento (linha temporal)

### Página 2 — Metas vs Realizado
- 📊 Comparação Faturamento Real × Meta por loja
- 🎯 % de Atingimento da Meta Global

### Página 3 — Auditoria de Qualidade dos Dados
- 📋 Tabela com formatação condicional listando inconsistências
- 🏷️ Classificação em duas categorias: **Crítico** e **Médio**

### Página 4 — Detalhamento de Vendas
- Visões secundárias e filtros adicionais

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
