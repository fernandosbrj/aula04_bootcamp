nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False
adicional:float = 1000

while not nome_valido:

    try:
        nome: str = input("Digite o seu nome completo.")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não pode conter dígitos")
        else:
            print("Nome válido: ", nome)
            nome_valido = True
    
    except ValueError as e:
        print(e)

while not salario_valido:
    try:
        salario: float = float(input("digite o seu salário: "))
        if salario < 0:
            print("Valor inválido. Digite um número positivo.")
        else:
            print("salário válido")
            salario_valido = True
    except ValueError as e:
        print(e)


while not bonus_valido:
    try:
        bonus: float = float(input("Digite o valor do seu bônus."))
        if bonus < 0:
            print("O valor não pode ser negativo.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

valor_total: float = adicional + salario + bonus

print(f"{nome}, seu salário é R${salario:.2f} e você receberá {valor_total:.2f} ao total.")