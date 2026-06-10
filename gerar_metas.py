"""
============================================================
 GERAÇÃO DO DADO SIMULADO — TABELA DE METAS
 Projeto Big Data - Lions Seminovos
============================================================

Objetivo: gerar a tabela de Metas mensais por loja, atendendo
ao requisito de "dado simulado" do trabalho mínimo da disciplina.

Esta tabela foi originalmente construída manualmente dentro do
Power BI pelo recurso "Inserir Dados". Este script reproduz o
mesmo conteúdo de forma programática, permitindo versionamento
e reuso em ciclos futuros (ex: gerar metas para janeiro/2025
com regras automatizadas baseadas em histórico).
"""

import pandas as pd

# ============================================================
# 1. DEFINIÇÃO DAS METAS POR LOJA
# ============================================================
# As metas foram definidas com base no faturamento real de
# dezembro de 2024, propositadamente colocando algumas acima
# e outras abaixo do realizado, para criar uma narrativa
# interessante de "lojas que bateram" vs "lojas que não bateram".
metas = [
    {"Loja": "DC", "Meta": 4_000_000},  # Duque de Caxias - meta abaixo do real (superou)
    {"Loja": "NT", "Meta": 3_000_000},  # Niterói - meta acima (quase atingiu)
    {"Loja": "NI", "Meta": 2_400_000},  # Nova Iguaçu - meta abaixo (superou)
    {"Loja": "IT", "Meta": 2_500_000},  # Intendente - meta acima (não atingiu)
    {"Loja": "CG", "Meta": 2_000_000},  # Campo Grande - meta acima (não atingiu)
    {"Loja": "VP", "Meta": 1_800_000},  # Vila Prudente SP - meta acima (não atingiu)
    {"Loja": "OS", "Meta": 1_300_000},  # Osasco SP - meta abaixo (superou)
    {"Loja": "BM", "Meta":   500_000},  # Barra Mansa - meta próxima (quase)
    {"Loja": "MT", "Meta":   100_000},  # Matriz Coelho Neto - meta simbólica
]

# ============================================================
# 2. CRIAÇÃO DO DATAFRAME
# ============================================================
df_metas = pd.DataFrame(metas)

print("=" * 60)
print("TABELA DE METAS GERADA")
print("=" * 60)
print(df_metas.to_string(index=False))
print(f"\nMeta total da rede: R$ {df_metas['Meta'].sum():,.2f}")


# ============================================================
# 3. EXPORTAÇÃO
# ============================================================
df_metas.to_csv("Metas_2024.csv", index=False, encoding="utf-8-sig")
df_metas.to_excel("Metas_2024.xlsx", index=False)
print("\n✅ Arquivos exportados: Metas_2024.csv e Metas_2024.xlsx")
print("   → Importar no Power BI como tabela 'Metas'")
print("   → Criar relacionamento 'Metas[Loja] → Vendas[Loja]' (1:N)")
