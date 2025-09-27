cpf = '85202095058'

nove_digito = cpf[:9]

contador_regrecivo = 10
resultado = 0
for digito in nove_digito:
    resultado += int(digito) * contador_regrecivo
    contador_regrecivo -= 1
primeiro_digito = (resultado * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos = nove_digito + str(primeiro_digito)
contador_regrecivo = 11
resultado = 0
for digito in dez_digitos:
    resultado += int(digito) * contador_regrecivo
    contador_regrecivo -= 1
segundo_digito = (resultado * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_calculado = nove_digito + str(primeiro_digito) + str(segundo_digito)

print("Primeiro dígito:", primeiro_digito)
print("Segundo dígito:", segundo_digito)
print("CPF calculado :", cpf_calculado)
print("CPF informado :", cpf)

if cpf == cpf_calculado:
    print("✅ CPF VÁLIDO")
else:
    print("❌ CPF INVÁLIDO")

