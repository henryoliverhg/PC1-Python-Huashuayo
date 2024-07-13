Edad_cliente = int(input("¿Cuál es su edad? "))
if Edad_cliente < 4:
    print("Entra gratis!")
elif 4<= Edad_cliente <= 18:
    print("Usted debe pagar 5 dólares")
elif Edad_cliente > 18:
    print("Usted debe pagar 10 dólares")
