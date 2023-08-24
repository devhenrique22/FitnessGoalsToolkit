# Autor: Carlos Henrique Fernandes
# Data: 24/08/23
# Instagram: @henrique_fds1
# Descrição: Um programa para calcular taxas metabólicas, IMC e recomendações nutricionais.
# Git: github.com/devhenrique22/

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

def main():
    print("DIGITE SUAS INFORMAÇÕES ABAIXO\n")

    nome = input("NOME => ")
    idade = int(input("IDADE => "))
    peso = float(input("PESO (kg) => "))
    altura = float(input("ALTURA (m) => "))

    sexo = get_valid_sex()
    objetivo = get_valid_goal()

    calculo = calculate_bmr(peso, altura, idade, sexo)

    print_results(calculo, peso, altura, objetivo)

def get_valid_sex():
    while True:
        sexo = input("QUAL SEU SEXO: F (FEMININO) M (MASCULINO) => ").upper()
        if sexo in ['F', 'M']:
            return sexo
        else:
            print("Opção inválida. Use F (FEMININO) ou M (MASCULINO)")

def get_valid_goal():
    while True:
        objetivo = input("Qual é o seu objetivo? EMAGRECIMENTO ou GANHO DE MASSA MUSCULAR? => ").upper()
        if objetivo in ['EMAGRECIMENTO', 'GANHO DE MASSA MUSCULAR']:
            return objetivo
        else:
            print("Opção inválida. Use EMAGRECIMENTO ou GANHO DE MASSA MUSCULAR")

def calculate_bmr(peso, altura, idade, sexo):
    centimetros = altura * 100
    if sexo == 'M':
        return 10 * peso + 6.25 * centimetros - 5 * idade + 5
    else:
        return 10 * peso + 6.25 * centimetros - 5 * idade - 161

def print_results(calculo, peso, altura, objetivo):
    print(f"\nSua taxa de metabolismo basal é {Color.GREEN}{calculo:.2f} calorias{Color.ENDC}")
    imc = peso / altura ** 2
    print(f"Seu IMC é {Color.GREEN}{imc:.2f}{Color.ENDC}")

    print_imc_status(imc)
    print_calories_and_macros(calculo, peso, objetivo)

def print_imc_status(imc):
    if imc < 18.5:
        print(f"Você está {Color.RED}abaixo do peso ideal{Color.ENDC}.")
    elif 18.5 <= imc < 24.9:
        print(f"Você está com o {Color.GREEN}peso ideal{Color.ENDC}.")
    elif 25 <= imc < 29.9:
        print(f"Você está com o peso {Color.YELLOW}acima do ideal{Color.ENDC}.")
    else:
        print(f"Você está {Color.RED}obeso{Color.ENDC}.")

def print_calories_and_macros(calculo, peso, objetivo):
    if objetivo == "EMAGRECIMENTO":
        calorias_objetivo = calculo - 500
        print(f"Para emagrecimento, você precisa consumir aproximadamente {Color.GREEN}{calorias_objetivo:.2f} calorias{Color.ENDC} por dia.")
    else:
        calorias_objetivo = calculo + 300
        print(f"Para ganho de massa muscular, você precisa consumir aproximadamente {Color.GREEN}{calorias_objetivo:.2f} calorias{Color.ENDC} por dia.")

    proteina = peso * (1.2 if objetivo == "EMAGRECIMENTO" else 1.5)
    carboidrato = calorias_objetivo * (0.4 if objetivo == "EMAGRECIMENTO" else 0.5) / 4
    gordura = calorias_objetivo * (0.3 if objetivo == "EMAGRECIMENTO" else 0.25) / 9

    print("\nPara o seu objetivo, os macros recomendados são:")
    print(f"Proteínas: {Color.GREEN}{proteina:.2f}g por dia{Color.ENDC}")
    print(f"Carboidratos: {Color.GREEN}{carboidrato:.2f}g por dia{Color.ENDC}")
    print(f"Gorduras: {Color.GREEN}{gordura:.2f}g por dia{Color.ENDC}")

if __name__ == "__main__":
    main()
