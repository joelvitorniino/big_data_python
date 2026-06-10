"""
============================================================
 AUDITORIA DE QUALIDADE DOS DADOS
 Projeto Big Data - Lions Seminovos
============================================================

Objetivo: percorrer a base bruta de vendas (Vendas_2024.xlsx)
e gerar um relatório consolidado com todas as inconsistências
encontradas, classificadas por gravidade (Crítico ou Médio).

Este script alimenta o gráfico de "Inconsistências por Gravidade"
do dashboard Power BI e o Relatório de Auditoria entregue à
gestão da Lions Seminovos.

Saída: imprime no terminal um resumo no formato:
        * Nome do erro (X registros)
       e exporta para Auditoria_Dados.csv para uso no Power BI.
"""

import pandas as pd

# ============================================================
# 1. CARREGAMENTO DA BASE BRUTA
# ============================================================
df = pd.read_excel("Vendas_2024.xlsx")
total = len(df)

print("=" * 60)
print("AUDITORIA DE QUALIDADE — BASE Vendas_2024.xlsx")
print(f"Total de registros analisados: {total}")
print("=" * 60)


# ============================================================
# 2. VERIFICAÇÕES — ACHADOS CRÍTICOS
# ============================================================
# Críticos são erros que afetam diretamente decisões de negócio.

achados = []

# --- 2.1 UF inconsistente com município cadastrado ---
df["_uf_no_municipio"] = (
    df["Município"].astype(str).str.extract(r" - ([A-Z]{2})")[0]
)
qtd_uf_inconsistente = (
    (df["_uf_no_municipio"].notna()) & (df["UF"] != df["_uf_no_municipio"])
).sum()
if qtd_uf_inconsistente > 0:
    achados.append(("Crítico", "UF inconsistente com município cadastrado",
                    qtd_uf_inconsistente))

# --- 2.2 Bairro cadastrado como placeholder "TEMPORÁRIO" ---
qtd_temporario = (
    df["Bairro"].astype(str).str.strip().str.upper() == "TEMPORÁRIO"
).sum()
if qtd_temporario > 0:
    achados.append(("Crítico", "Bairro como placeholder TEMPORÁRIO",
                    qtd_temporario))

# --- 2.3 Data vazada para o campo Modelo ---
qtd_data_no_modelo = df["Modelo"].astype(str).str.contains(
    r"\d{4}-\d{2}-\d{2}", regex=True, na=False
).sum()
if qtd_data_no_modelo > 0:
    achados.append(("Crítico", "Data vazada para o campo Modelo",
                    qtd_data_no_modelo))

# --- 2.4 Bairro contendo nome de cidade ---
nomes_cidade_como_bairro = ["SÃO JOÃO DE MERITI", "DUQUE DE CAXIAS",
                            "NOVA IGUAÇU", "NITERÓI"]
qtd_bairro_cidade = df["Bairro"].astype(str).str.strip().str.upper().isin(
    nomes_cidade_como_bairro
).sum()
if qtd_bairro_cidade > 0:
    achados.append(("Crítico", "Bairro contendo nome de cidade",
                    qtd_bairro_cidade))


# ============================================================
# 3. VERIFICAÇÕES — ACHADOS MÉDIOS
# ============================================================
# Médios são problemas de digitação que comprometem confiabilidade.

# --- 3.1 Espaços indevidos em Modelos ---
qtd_esp_modelo = (
    df["Modelo"].astype(str) != df["Modelo"].astype(str).str.strip()
).sum()
if qtd_esp_modelo > 0:
    achados.append(("Médio", "Espaços indevidos em Modelos",
                    qtd_esp_modelo))

# --- 3.2 Espaços indevidos em Bairros ---
qtd_esp_bairro = (
    df["Bairro"].astype(str) != df["Bairro"].astype(str).str.strip()
).sum()
if qtd_esp_bairro > 0:
    achados.append(("Médio", "Espaços indevidos em Bairros",
                    qtd_esp_bairro))

# --- 3.3 Espaço indevido na coluna Marca ---
qtd_esp_marca = (
    df["Marca"].astype(str) != df["Marca"].astype(str).str.strip()
).sum()
if qtd_esp_marca > 0:
    achados.append(("Médio", "Espaço indevido na coluna Marca",
                    qtd_esp_marca))

# --- 3.4 Espaços duplos no interior de strings ---
qtd_esp_duplos = 0
for col in ["Modelo", "Bairro"]:
    qtd_esp_duplos += df[col].astype(str).str.contains(
        r"  +", regex=True, na=False
    ).sum()
if qtd_esp_duplos > 0:
    achados.append(("Médio", "Espaços duplos no interior de strings",
                    qtd_esp_duplos))


# ============================================================
# 4. IMPRESSÃO DO OVERVIEW (formato pedido pelo professor)
# ============================================================
print("\n🚨 ACHADOS CRÍTICOS")
print("-" * 60)
for nivel, descricao, qtd in achados:
    if nivel == "Crítico":
        print(f"  * {descricao} ({qtd} registros)")

print("\n⚠️  ACHADOS MÉDIOS")
print("-" * 60)
for nivel, descricao, qtd in achados:
    if nivel == "Médio":
        print(f"  * {descricao} ({qtd} registros)")

total_afetados = sum(qtd for _, _, qtd in achados)
print("\n" + "=" * 60)
print(f"RESUMO: {len(achados)} categorias distintas | "
      f"{total_afetados} registros afetados (com sobreposições)")
print("=" * 60)


# ============================================================
# 5. EXPORTAÇÃO PARA O POWER BI
# ============================================================
df_auditoria = pd.DataFrame(
    achados, columns=["Categoria", "Inconsistência", "Registros"]
)
df_auditoria.to_csv("Auditoria_Dados.csv", index=False, encoding="utf-8-sig")
df_auditoria.to_excel("Auditoria_Dados.xlsx", index=False)
print("\n✅ Arquivos exportados: Auditoria_Dados.csv e Auditoria_Dados.xlsx")
print("   → Importar no Power BI como tabela 'Auditoria_Dados'")
print("   → Não criar relacionamento (tabela autônoma de metadados)")
