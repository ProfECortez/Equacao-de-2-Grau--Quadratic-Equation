import math

print("### CALCULADORA DE EQUAÇÕES DE 2º GRAU ###")

print("\n\nOrientações: as equações de 2º grau tem o formato ax² + bx + c = 0. Você deverá fornecer o valor de \'a\', \'b\' e \'c\' e este programa irá retornar o valor x")

print("\n\n")

a = float(input("Forneça o valor de a: "))
b = float(input("\nForneça o valor de b: "))
c = float(input("\nForneça o valor de c: "))

delta = (b**2) - (4*a*c)

print("\n\nDelta = ", delta)

if delta < 0:
    print("\n\nValor de delta negativo; não há raízes reais para essa equação.")
else:
    x1 = ((-1*b) + math.sqrt(delta))/2*a
    x2 = ((-1*b) - math.sqrt(delta))/2*a
    if x1 == x2:
        print("\n\nx = ", x1)
    else:
        print("\n\n\possíveis valores de x: ", x1, " e ", x2)
