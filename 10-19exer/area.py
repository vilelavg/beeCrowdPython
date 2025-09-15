a=float(input())
b=float(input())
c=float(input())

#primeiro, vamos calcular a area do triangulo retangulo
area_triangulo=(a*c)/2

#agora, area do circulo
area_circulo=3.14159*(c**2)

#area do trapezio
area_trapezio=((a+b)*c)/2

#area do quadrado
area_quadrado=b**2

#area do retangulo
area_retangulo=a*b

print("TRIANGULO: %.3f" %area_triangulo)
print("CIRCULO: %.3f" %area_circulo)
print("TRAPEZIO: %.3f" %area_trapezio)
print("QUADRADO: %.3f" %area_quadrado)
print("RETANGULO: %.3f" %area_retangulo)