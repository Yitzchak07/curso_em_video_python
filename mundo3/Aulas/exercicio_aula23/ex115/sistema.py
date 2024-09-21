from time import sleep
def menu_principal():
    listas = []
    
    while True:
        print("_"*20)
        print("   MENU PRINCIPAL!   ")
        print("_"*20)

        print("="*34)
        print("1- Ver pessoas cadastradas!")
        print("2- Cadastrar uma nova pessoa")
        print("3- Sair Sistema")
        print("="*34)

        try:
            resp = int(input("Sua Opcao!:"))
        except ValueError:
            print("DIgite apenas as opcoes Listas acima")
            continue
        if resp == 1:
                
            print("="*20)
            print("       Pessoas Cadastradas   ")
            for i in range(0,len(listas),2):
                print(f"Nome: {listas[i]}, Idade: {listas[i + 1]}")
                sleep(0.1)
            sleep(1)
            print("="*20)
                

        elif resp == 2:
            print("="*20)
            
        
            try:
                nome = str(input("Digite o Nome da Pessoa:").strip())
                idade = int(input("DIgite a Idade da Pessoa:"))
                listas.append(nome)
                listas.append(idade)
                print(f"{nome} cadastrado(a) com sucesso!")
                
            except ValueError:
                    print("ERRO: no campo Nome digite e no idade apenas numeros interios")
            sleep(1)
                        
                        
        elif resp == 3:
            print("Sistema encerrado obrigado por usar")
            break

    
menu_principal()