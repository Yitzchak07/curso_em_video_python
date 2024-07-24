from datetime import date
ano_nascimento = int(input("informe seu ano de nascimento:"))
atual = date.today().year
idade = atual - ano_nascimento
print(idade)

if idade < 18:
    anos = 18 - idade
    print('voce ainda vai se alista')
    print('falta {} ano'.format(anos))
    

elif idade == 18:
    print('voce precisa se alista agora voce tem {} de idade'.format(idade))
    print('pode ir agora msm')

elif idade > 18:
    saldo = idade - 18
    print('ja passou da hora de voce se alista voce ja tem {} anos'.format(idade))
    print('o prazo ja passou tem {} anos'.format(saldo))


