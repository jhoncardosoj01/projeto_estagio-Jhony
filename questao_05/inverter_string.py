# inverter_string.py
def inverter_string(s):
    string_invertida = ''
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

entrada = input("Informe uma string: ")
print("String invertida:", inverter_string(entrada))
