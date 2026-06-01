##### Um sistema de planejamento de dieta #####
lista_nomes = ['João Augusto','José','Artur','Joan','Lucas']
lista_telefones = ['99999-1111', '99999-2222', '99999-3333', '99999-4444', '99999-5555']
lista_emails = ['joaoaugusto@ufrn.edu.br','jose@ufrn.edu.br','artur@ufrn.edu.br','joan@ufrn.edu.br','lucas@ufrn.edu.br']
lista_dia_nasc = ['22/10/2005','30/03/2008','12/06/2007','03/04/2005','09/08/2006']
lista_peso = ['93.3','98','80.7','87','90']
lista_obj = ['Emagrecimento','Emagrecimento','Ganho de massa muscular','Ganho de massa muscular','Manter o peso']




resposta = ''

while resposta != '0':
  print('####################################################')
  print('#####  Seja bem vindo ao PyDiet                #####')
  print('#####  O seu sistema de planejamento de dietas #####')
  print('####################################################')
  print('##  Selecione uma das opções a seguir ##############')
  print('##  1 - Pacientes           ##')
  print('##  2 - NutriPlan AI        ##')
  print('##  3 - Consultas           ##')
  print('##  4 - Relatórios          ##')
  print('##  5 - Sobre o sistema     ##')
  print('##  0 - Sair                ##')
  resposta = input('##  Escolha sua opção: ')
  print()
  
  if resposta == '1':
    resposta1 = ''  
    while resposta1 != '0':
      print('####################################################')
      print('##  O que você quer fazer?            ##############')
      print('##  Selecione uma das opções a seguir ##############')
      print('##  1 - Cadastrar Paciente            ##')
      print('##  2 - Informações sobre paciente    ##')
      print('##  3 - Atualizar paciente            ##')
      print('##  4 - Excluir paciente              ##')
      print('##  0 - Voltar ao menu                ##')
      resposta1 = input('## Escolha a sua opcão: ')

      if resposta1 == '1':
         print()
         print('Cadastro de paciente no sistema')
         print()
         nome  = input('Nome do paciente: ')
         telefone  = input('Telefone: ')
         email = input('E-mail: ')
         dia_nasc = input('Data de nascimento  : ')
         peso = input('Peso do paciente em kg:')
         obj = input('Objetivo do paciente: ')
         lista_nomes += [nome]
         lista_telefones += [telefone]
         lista_dia_nasc += [dia_nasc]
         lista_emails += [email]
         lista_peso += [peso]
         lista_obj += [obj]
         print()
         print('O paciente foi cadastrado com sucesso!')
         print()
      
      elif resposta1 == '2':
         print()
         print('Informações do paciente no sistema')
         print()
         nome = input('Qual o nome do paciente que você deseja visualizar? ')
         tamanho = len(lista_nomes)
         posicao = 0
         achou = False
         while (posicao < tamanho) and (not achou):
          if nome == lista_nomes[posicao]:
            achou = True
          else:
            posicao += 1
         if achou:
           print('Nome:', lista_nomes[posicao])
           print('Telefone:', lista_telefones[posicao])
           print('Data de nascimeto:', lista_dia_nasc[posicao])
           print('Email:', lista_emails[posicao])
           print('Peso:', lista_peso[posicao])
           print('Objetivo:',lista_obj[posicao])
           print()
         else:
            print()
            print('{} não se encontra nos pacientes cadastrados no sistema'.format(nome))
            print()
      
      elif resposta1 == '3':
         print()
         print('Atualização de cadastro de paciente no sistema')
         print()
         nome = input('Qual o nome do paciente que você deseja atualizar? ')
         tamanho = len(lista_nomes)
         posicao = 0
         achou = False
         while (posicao < tamanho) and (not achou):
          if nome == lista_nomes[posicao]:
            achou = True
          else:
            posicao += 1
         if achou:
           del lista_nomes[posicao]
           del lista_telefones[posicao]
           del lista_dia_nasc[posicao]
           del lista_emails[posicao]
           del lista_peso[posicao]
           del lista_obj[posicao]
           nome  = input('Nome do paciente atualizado: ')
           telefone  = input('Telefone atualizado: ')
           email = input('E-mail atualizado: ')
           dia_nasc = input('Data de nascimento atualizada: ')
           peso = input('Peso do paciente em kg atualizado: ')
           obj = input('Objetivo do paciente atualizado: ')
           lista_nomes += [nome]
           lista_telefones += [telefone]
           lista_dia_nasc += [dia_nasc]
           lista_emails += [email]
           lista_peso += [peso]
           lista_obj += [obj]
           print()
           print('Os dados do paciente foram atualizados com sucesso!')
           print()
           
  
      elif resposta1 == '4':
         print()
         print('Remoção de paciente do sistema')
         print()
         nome = input('Qual o nome do paciente que você deseja remover? ')
         tamanho = len(lista_nomes)
         posicao = 0
         achou = False
         while (posicao < tamanho) and (not achou):
          if nome == lista_nomes[posicao]:
            achou = True
          else:
            posicao += 1
         if achou:
           del lista_nomes[posicao]
           del lista_telefones[posicao]
           del lista_dia_nasc[posicao]
           del lista_emails[posicao]
           del lista_peso[posicao]
           del lista_obj[posicao]
           print()
           print('Os dados do paciente foram removidos com sucesso!')
           print()
           
      elif resposta1 == '0':
         print()
  
  elif resposta == '2':
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

    print('##  Obejetivo da dieta            ##')
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

  elif resposta == '0':
    print()
  
  else:
     print()
     print('Opção inválida, escolha alguma da opções de 1 a 5!')
     print()

print('Fim do programa, Obrigado por usar o PyDiet!')