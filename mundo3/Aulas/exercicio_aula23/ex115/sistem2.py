from time import sleep

def menu_principal():
    listas = ["Isac", 12, "Pedro", 14, "Bruno", 16]  # Lista inicial
    while True:
        print("_" * 20)
        print("   MENU PRINCIPAL!   ")
        print("_" * 20)
        print("=" * 34)
        print("1- Ver pessoas cadastradas")
        print("2- Cadastrar uma nova pessoa")
        print("3- Sair do Sistema")
        print("=" * 34)

        try:
            resp = int(input("Sua Opção: "))
        except ValueError:
            print("Erro: Digite apenas as opções listadas acima (1, 2 ou 3).")
            continue  # Reinicia o loop se houver erro na entrada
        if resp == 1:
            # Mostrar pessoas cadastradas
            print("=" * 20)
            print("     Pessoas Cadastradas     ")
            print("=" * 20)
            for i in range(0, len(listas), 2):
                print(f"Nome: {listas[i]}, Idade: {listas[i + 1]}")
                sleep(0.5)
            print("=" * 20)
            sleep(1)

        elif resp == 2:
            # Cadastrar uma nova pessoa
            print("=" * 20)
            try:
                nome = str(input("Digite o Nome da Pessoa: ").strip())
                idade = int(input("Digite a Idade da Pessoa: "))  # Recebe idade como inteiro
                listas.append(nome)
                listas.append(idade)
                print(f"{nome} cadastrado(a) com sucesso!")
            except ValueError:
                print("Erro: Digite um nome válido e uma idade numérica.")
            sleep(1)

        elif resp == 3:
            print("Sistema encerrado. Obrigado por usar!")
            break

        else:
            print("Erro: Digite apenas 1, 2 ou 3.")

menu_principal()
