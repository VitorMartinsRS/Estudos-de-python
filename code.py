def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    peso: em kg
    altura: em metros
    """
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Acima do peso"
    else:
        return "Obesidade"

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificar_imc(imc)}")