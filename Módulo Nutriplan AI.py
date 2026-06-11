def nutriplan():
    
    print('#############################################################################################')
    print('##  Este é o mais novo NutriPlan AI!                                                    #####')
    print('##                                                                                      #####')
    print('##  Aqui iremos fazer um cálculo de calorias que sua dieta precisa exatamente para que  #####')
    print('##  você alcance seu objetivo com sucesso. Para isso, ultilizaremos sua taxa de         #####')
    print('##  metabolismo basal(TMB) calculada pela fórmula de Harris-Benedict.                   #####')
    print('##                                                                                      #####')
    print('##  Você só precisará responder algumas perguntas para que você saiba exatamente        #####')
    print('##  quantas calorias serão necessárias na sua dieta, para que você consiga atingir      #####')
    print('##  seu objetivo final com qualidade                                                    #####')
    print('#############################################################################################')
    print()

    idade = int(input('Digite sua idade: '))
    peso = float(input('Digite seu peso em quilogramas(kg): '))
    altura = int(input('Qual a sua altura em centímetros(cm): '))
    sexo = input('Qual o seu gênero (m/f): ')
    print()

    print('### Nível de atividade física ###')
    print('##  1 - Sedentário -> pouco ou nenhum exercício                                   ##')
    print('##  2 - Levemente ativo -> exercício leve ou atividade leve diária                ##')
    print('##  3 - Moderadamente ativo -> exercício moderado ou atividade moderada diária    ##')
    print('##  4 - Muito ativo -> exercício intenso ou atividade intensa diária              ##')
    print('##  5 - Extremamente ativo -> exercício muito intenso ou trabalho físico pesado   ##')
    nivel_atv = input('Escolha uma das opções: ')
    if nivel_atv == '1':
        nivel_atv = 1.2
    elif nivel_atv == '2':
        nivel_atv = 1.375
    elif nivel_atv == '3':
        nivel_atv = 1.55
    elif nivel_atv == '4':
        nivel_atv = 1.725
    elif nivel_atv == '5':
        nivel_atv = 1.9
    print()

    print('##  Objetivo da dieta            ##')
    print('##  1 - Emagrecimento             ##')
    print('##  2 - Ganho de massa muscular   ##')
    print('##  3 - Manter o meu peso         ##')
    obj_dieta = input('Selecione uma opção: ')


    ##### Calculadora de TMB (Taxa Metabólica Basal) para homens #####
    if sexo in ['M','m']:
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.75 * idade) 
        tmb = tmb * nivel_atv
        if obj_dieta == '1':
            kcal_dieta = tmb - 400
            print()
            print('Sua taxa de metabolismo basal é de {:.2f} e já que o objetivo da sua dieta'.format(tmb))
            print('é o emagracimento, iremos fazer um déficit calórico de 400 calorias, para que assim')
            print('você matenha sua massa muscular e alcance seu objetivo com qualidade.')
            print('Logo, as calorias que suas dieta deve ter são {:.2f}!'''.format(kcal_dieta))
            print()
            
        elif obj_dieta == '2':
            kcal_dieta = tmb + 400
            print()
            print('Sua taxa de metabolismo basal é de {:.2f} e já que o objetivo da sua dieta'.format(tmb))
            print('é o ganho de massa muscular, iremos fazer um superávit caórico de 400 calorias, para que assim')
            print('você aumente sua massa muscular e não ganhe tanta gordura, alcançando assim seu objetivo com qualidade.')
            print('Logo, as calorias que suas dieta deve ter são {:.2f}!'''.format(kcal_dieta))
            print()
            
        elif obj_dieta == '3':
            kcal_dieta = tmb
            print()
            print('Sua taxa de metabolismo basal é de {:.2f} e já que o objetivo da sua dieta é manter'.format(tmb))
            print('o peso, iremos fazer com que você gaste no dia as calorias que você come, para que assim')
            print('você matenha sua massa muscular e matenha seu peso com qualidade.')
            print('Logo, as calorias que suas dieta deve ter são {:.2f}!'.format(kcal_dieta))
            print()


        ##### Calculadora de TMB (Taxa Metabólica Basal) para mulheres #####
    elif sexo in ['F','f']:
        tmb = 655.1 + (9.563 * peso) + (1.85 * altura) - (4.676 * idade)
        tmb = tmb * nivel_atv
        if obj_dieta == '1':
            kcal_dieta = tmb - 400
            print()
            print('Sua taxa de metabolismo basal é de {:.2f} e já que o objetivo da sua dieta'.format(tmb))
            print('é o emagracimento, iremos fazer um déficit calórico de 400 calorias, para que assim')
            print('você matenha sua massa muscular e alcance seu objetivo com qualidade.')
            print('Logo, as calorias que suas dieta deve ter são {:.2f}!'.format(kcal_dieta))
            print()
            
        elif obj_dieta == '2':
            kcal_dieta = tmb + 400
            print()
            print('Sua taxa de metabolismo basal é de {:.2f} e já que o objetivo da sua dieta'.format(tmb))
            print('é o ganho de massa muscular, iremos fazer um superávit caórico de 400 calorias, para que assim')
            print('você aumente sua massa muscular e não ganhe tanta gordura, alcançando assim seu objetivo com qualidade.')
            print('Logo, as calorias que suas dieta deve ter são {:.2f}!'''.format(kcal_dieta))
            print()
            
        elif obj_dieta == '3':
            kcal_dieta = tmb
            print()
            print('Sua taxa de metabolismo basal é de {:.2f} e já que o objetivo da sua dieta é manter'.format(tmb))
            print('o peso, iremos fazer com que você gaste no dia as calorias que você come, para que assim')
            print('você matenha sua massa muscular e matenha seu peso com qualidade.')
            print('Logo, as calorias que suas dieta deve ter são {:.2f}!'''.format(kcal_dieta))
            print()