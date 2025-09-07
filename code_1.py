#If /elif /else
enter= input(f'Você deseja entrar ou "sair"? \n' )

if enter =="entrar":
    print("Você entrou no sistema")
elif enter == "sair":
    print("Você saiu do sistema")   
else:
    print(f"{enter} não é um comando inválido")
    