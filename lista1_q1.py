'''1) Ler uma temperatura em graus Celsius e apresentá-la convertida
em graus Fahrenheit. A fórmula de conversão é F ← (9 * C + 160) / 5,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.'''

C = float( input("Temperatura Celsius: ") )

F = (9 * C + 160) / 5

print(f"Temperatura Fahrenheit: {F}°F")