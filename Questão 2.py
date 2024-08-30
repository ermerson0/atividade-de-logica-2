def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mmc(a, b, mdc):
    return (a * b) // mdc

def calcular_mdc_mmc():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))


    mdc = calcular_mdc(a, b)


    mmc = calcular_mmc(a, b, mdc)


    print(f"MDC({a}, {b}) = {mdc}")
    print(f"MMC({a}, {b}) = {mmc}")

calcular_mdc_mmc()

#Explicação das perguntas

#algoritmo de Euclides (MDC): Este algoritmo funciona com base na ideia de que o MDC de dois números não muda se o maior número for substituído pelo resto da divisão entre eles.
#Isso é repetido até que o resto seja zero, e o último divisor é o MDC.

##Esse Algoritmo Funciona para Todos os Casos?
#Sim, este algoritmo funciona para todos os pares de números inteiros positivos e zero, com algumas considerações:
#Se qualquer um dos números for zero, o MDC é o valor absoluto do outro número (por exemplo, MDC(0, 𝑏 ) = 𝑏 MDC(0,b)=b).
#Se ambos os números forem zero, o MDC não está bem definido. Neste caso, o algoritmo precisaria de um tratamento especial.
#O MMC é indefinido se qualquer um dos números for zero, pois o zero não tem múltiplos.


#Como Verificar a Comprovação para Todos os Casos de Testes Possíveis?
#Para verificar se o algoritmo funciona para todos os casos possíveis, podemos: Fazer teste de unidades e Testar Limites.
