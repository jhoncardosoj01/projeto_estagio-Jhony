# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a]
    while b <= n:
        fib_sequence.append(b)
        a, b = b, a + b
    return fib_sequence

numero = int(input("Informe um número: "))
fib_sequence = fibonacci(numero)

if numero in fib_sequence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
