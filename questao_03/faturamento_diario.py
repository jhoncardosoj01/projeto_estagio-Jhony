# faturamento_diario.py
import json

# Exemplo de faturamento diário (json)
faturamento_diario_json = '''
{
    "faturamento": [1500, 2300, 0, 3500, 2700, 4000, 0, 5000]
}
'''
data = json.loads(faturamento_diario_json)
faturamento_diario = data['faturamento']

# Cálculo
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
media_faturamento = sum(faturamento_diario) / len([x for x in faturamento_diario if x > 0])
dias_acima_da_media = len([x for x in faturamento_diario if x > media_faturamento])

print(f"Menor Faturamento: R${menor_faturamento:.2f}")
print(f"Maior Faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias acima da média: {dias_acima_da_media}")
