import pandas as pd

# ============================================================
# 1. CARREGAMENTO DOS DADOS
# ============================================================
# Lê o Excel original. A planilha tem 289 vendas de dezembro/2024.
df = pd.read_excel('Vendas_2024.xlsx')

print("=" * 60)
print("INSPEÇÃO INICIAL")
print("=" * 60)
print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
print(f"\nColunas: {list(df.columns)}")
print(f"\nValores nulos por coluna:\n{df.isnull().sum()}")
print(f"\nLinhas duplicadas: {df.duplicated().sum()}")


# ============================================================
# 2. LIMPEZA DE STRINGS — REMOÇÃO DE ESPAÇOS
# ============================================================
# Várias colunas têm espaços sobrando no início/fim (ex.: 'RENAULT '
# aparecia como marca diferente de 'RENAULT'). O .str.strip() resolve.
colunas_texto = ['Marca', 'Modelo', 'Bairro', 'Município', 'UF',
                 'Loja', 'Endereço da loja']
for col in colunas_texto:
    df[col] = df[col].astype(str).str.strip()


# ============================================================
# 3. CORREÇÃO DE ERRO DE CADASTRO ESPECÍFICO
# ============================================================
# Encontramos um modelo cadastrado como "GOL 2024-06-01 00:00:00 +0000"
# Claramente uma data vazou no campo Modelo. Corrigimos para "GOL".
mascara_erro = df['Modelo'].str.contains('2024-', na=False)
print(f"\nLinhas com data vazada no Modelo: {mascara_erro.sum()}")
df.loc[mascara_erro, 'Modelo'] = 'GOL'


# ============================================================
# 4. CONVERSÃO DE TIPOS — DATA
# ============================================================
# A coluna 'Data da venda' veio como texto. Convertemos para datetime
# para conseguir fazer análises temporais (por dia, semana, etc.).
df['Data da venda'] = pd.to_datetime(df['Data da venda'])


# ============================================================
# 5. PADRONIZAÇÃO DE MAIÚSCULAS NO MODELO
# ============================================================
# Modelos em CAIXA ALTA ficam mais consistentes pro Power BI agrupar.
df['Modelo'] = df['Modelo'].str.upper()


# ============================================================
# 6. CRIAÇÃO DE COLUNA — CATEGORIA (Carro vs Moto)
# ============================================================
# Identificamos que YAMAHA é a única marca exclusivamente de motos
# (modelos NEO e XTZ150 CROSSER). Demais marcas no dataset = Carro.
marcas_moto = ['YAMAHA']
df['Categoria'] = df['Marca'].apply(
    lambda x: 'Moto' if x in marcas_moto else 'Carro'
)


# ============================================================
# 7. EXTRAÇÃO — SEPARAR "Endereço da loja" EM CIDADE + UF
# ============================================================
# A coluna vinha no formato "Cidade - UF". Quebramos em duas colunas
# novas: 'Cidade da loja' e 'UF da loja'.
df[['Cidade da loja', 'UF da loja']] = (
    df['Endereço da loja'].str.split(' - ', expand=True)
)


# ============================================================
# 8. COLUNAS DERIVADAS DE DATA — PARA ANÁLISE TEMPORAL
# ============================================================
# Estas colunas ajudam o Power BI a fatiar as vendas por dia da
# semana e semana do mês (útil pro gráfico de linha temporal).
dias_pt = {
    'Monday': 'Segunda', 'Tuesday': 'Terça', 'Wednesday': 'Quarta',
    'Thursday': 'Quinta', 'Friday': 'Sexta', 'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}
df['Dia da semana'] = df['Data da venda'].dt.day_name().map(dias_pt)
df['Dia do mês'] = df['Data da venda'].dt.day


# ============================================================
# 9. RENOMEIA "Valor do veículo" PARA NOME MAIS CURTO
# ============================================================
# Facilita escrever fórmulas DAX no Power BI depois.
df = df.rename(columns={'Valor do veículo': 'Valor'})


# ============================================================
# 10. VALIDAÇÃO FINAL
# ============================================================
print("\n" + "=" * 60)
print("APÓS O TRATAMENTO")
print("=" * 60)
print(f"Marcas únicas: {df['Marca'].nunique()} (antes: 16, agora deve ser 15)")
print(f"Categorias: {df['Categoria'].value_counts().to_dict()}")
print(f"UFs: {df['UF'].value_counts().to_dict()}")
print(f"Faturamento total: R$ {df['Valor'].sum():,.2f}")
print(f"Ticket médio: R$ {df['Valor'].mean():,.2f}")
print(f"\nColunas finais: {list(df.columns)}")


# ============================================================
# 11. EXPORTAÇÃO PARA O POWER BI
# ============================================================
df.to_csv('Vendas_2024_tratado.csv', index=False, encoding='utf-8-sig')
df.to_excel('Vendas_2024_tratado.xlsx', index=False)
print("\n✅ Arquivos exportados: Vendas_2024_tratado.csv e .xlsx")
