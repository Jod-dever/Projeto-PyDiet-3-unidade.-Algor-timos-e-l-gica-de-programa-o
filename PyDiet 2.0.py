##### Um sistema de planejamento de dieta #####
pacientes = {
    'João Augusto': {
        'telefone': '99999-1111',
        'email': 'joaoaugusto@ufrn.edu.br',
        'data_nascimento': '22/10/2005',
        'peso': '93.3',
        'objetivo': 'Emagrecimento'
    },
    'José': {
        'telefone': '99999-2222',
        'email': 'jose@ufrn.edu.br',
        'data_nascimento': '30/03/2008',
        'peso': '98',
        'objetivo': 'Emagrecimento'
    },
    'Artur': {
        'telefone': '99999-3333',
        'email': 'artur@ufrn.edu.br',
        'data_nascimento': '12/06/2007',
        'peso': '80.7',
        'objetivo': 'Ganho de massa muscular'
    },
}

consultas = {
    'Lucas': {
        'telefone': '99999-5555',
        'email': 'lucas@ufrn.edu.br',
        'data_nascimento': '09/08/2006',
        'peso': '90',
        'objetivo': 'Manter o peso',
        'dia_consulta': '30/05/2026'
    },
    'Joan': {
        'telefone': '99999-4444',
        'email': 'joan@ufrn.edu.br',
        'data_nascimento': '03/04/2005',
        'peso': '87',
        'objetivo': 'Ganho de massa muscular',
        'dia_consulta': '21/02/2026'
    },
}

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
         print('##  0 - Voltar ao menu principal      ##')
         resposta1 = input('## Escolha a sua opcão: ')
      
         if resposta1 == '1':
            print()
            print('Cadastro de paciente no sistema')
            print()
            nome = input('Nome do paciente: ')
            telefone = input('Telefone: ')
            email = input('E-mail: ')
            data_nascimento = input('Data de nascimento: ')
            peso = input('Peso do paciente em kg: ')
            objetivo = input('Objetivo do paciente: ')
            pacientes[nome] = {
               'telefone': telefone,
               'email': email,
               'data_nascimento': data_nascimento,
               'peso': peso,
               'objetivo': objetivo
            }
            print('Paciente cadastrado com sucesso!')
            print()
          
         elif resposta1 == '2':
            print()
            print('Informações do paciente no sistema')
            print()
            nome = input('Qual o nome do paciente? ')
            
            if nome in pacientes:
               print('Nome:', nome)
               print('Telefone:', pacientes[nome]['telefone'])
               print('Email:', pacientes[nome]['email'])
               print('Data de nascimento:', pacientes[nome]['data_nascimento'])
               print('Peso:', pacientes[nome]['peso'])
               print('Objetivo:', pacientes[nome]['objetivo'])
               print()
            else:
               print('Paciente não encontrado.')
               print()
         
         elif resposta1 == '3':
            print()
            print('Atualização de cadastro de paciente no sistema')
            print()
            nome = input('Qual o nome do paciente que deseja atualizar? ')
            if nome in pacientes:
               resposta2 = ''
               while resposta2 != '0':
                  print('####################################################')
                  print('##  O que você quer atualizar?            ##########')
                  print('##  Selecione uma das opções a seguir ##############')
                  print('##  1 - Telefone do Paciente                      ##')
                  print('##  2 - Email do paciente                         ##')
                  print('##  3 - Data de nascimento do paciente            ##')
                  print('##  4 - Peso do paciente                          ##')
                  print('##  5 - Objetivo do paciente                      ##')
                  print('##  0 - Voltar ao menu dos pacientes              ##')
                  resposta2 = input('## Escolha a sua opção: ')

                  if resposta2 == '1':
                     pacientes[nome]['telefone'] = input('Novo telefone: ')
                     print('Telefone do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '2':
                     pacientes[nome]['email'] = input('Novo Email: ')
                     print('Email do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '3':
                     pacientes[nome]['data_nascimento'] = input('Nova data de nascimento: ')
                     print('Data de nascimento do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '4':
                     pacientes[nome]['peso'] = input('Novo peso: ')
                     print('Peso do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '5':
                     pacientes[nome]['objetivo'] = input('Novo objetivo: ')
                     print('Objetivo do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '0':
                     print()
               
            else:
               print('Paciente não encontrado')      
   
         elif resposta1 == '4':
            print()
            print('Remoção de paciente do sistema')
            print()
            nome = input('Qual o nome do paciente que deseja remover? ')

            if nome in pacientes:
               del pacientes[nome]
               print('Paciente removido com sucesso!')
               print()
            
            else:
               print('Paciente não encontrado.')
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
   
   elif resposta == '3':
      resposta3 = ''
      while resposta3 != '0':
         print('####################################################')
         print('##  O que você quer fazer?            ##############')
         print('##  Selecione uma das opções a seguir ##############')
         print('##  1 - Cadastrar consulta            ##')
         print('##  2 - Informações sobre consulta    ##')
         print('##  3 - Atualizar consulta            ##')
         print('##  4 - Excluir consulta              ##')
         print('##  0 - Voltar ao menu principal      ##')
         resposta3 = input('## Escolha a sua opcão: ')

         if resposta3 == '1':
            print()
            print('Cadastro de paciente no sistema')
            print()
            nome = input('Nome do paciente: ')
            telefone = input('Telefone: ')
            email = input('E-mail: ')
            data_nascimento = input('Data de nascimento: ')
            peso = input('Peso do paciente em kg: ')
            objetivo = input('Objetivo do paciente: ')
            dia_consulta = input('Dia da consulta: ')
            consultas[nome] = {
               'telefone': telefone,
               'email': email,
               'data_nascimento': data_nascimento,
               'peso': peso,
               'objetivo': objetivo,
               'dia_consulta': dia_consulta
            }
            print('Consulta cadastrada com sucesso!')
            print()
         
         elif resposta3 == '2':
            print()
            print('Informações da consulta no sistema')
            print()
            nome = input('Qual o nome do paciente? ')
            
            if nome in consultas:
               print('Nome:', nome)
               print('Telefone:', consultas[nome]['telefone'])
               print('Email:', consultas[nome]['email'])
               print('Data de nascimento:', consultas[nome]['data_nascimento'])
               print('Peso:', consultas[nome]['peso'])
               print('Objetivo:', consultas[nome]['objetivo'])
               print('Dia da consulta:', consultas[nome]['dia_consulta'])
               print()
            else:
               print('Paciente não encontrado.')
               print()

         elif resposta3 == '3':
            print()
            print('Atualização de cadastro de paciente no sistema')
            print()
            nome = input('Qual o nome do paciente que deseja atualizar? ')
            if nome in consultas:
               resposta4 = ''
               while resposta4 != '0':
                  print('####################################################')
                  print('##  O que você quer atualizar?            ##########')
                  print('##  Selecione uma das opções a seguir ##############')
                  print('##  1 - Telefone do Paciente                      ##')
                  print('##  2 - Email do paciente                         ##')
                  print('##  3 - Data de nascimento do paciente            ##')
                  print('##  4 - Peso do paciente                          ##')
                  print('##  5 - Objetivo do paciente                      ##')
                  print('##  6 - Dia da consulta                           ##')
                  print('##  0 - Voltar ao menu das consultas              ##')
                  resposta4 = input('## Escolha a sua opção: ')

                  if resposta4 == '1':
                     consultas[nome]['telefone'] = input('Novo telefone: ')
                     print('Telefone do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta4 == '2':
                     consultas[nome]['email'] = input('Novo Email: ')
                     print('Email do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta4 == '3':
                     consultas[nome]['data_nascimento'] = input('Nova data de nascimento: ')
                     print('Data de nascimento do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta4 == '4':
                     consultas[nome]['peso'] = input('Novo peso: ')
                     print('Peso do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta4 == '5':
                     consultas[nome]['objetivo'] = input('Novo objetivo: ')
                     print('Objetivo do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta4 == '6':
                     consultas[nome]['dia_consulta'] = input('Novo dia da consulta: ')
                     print('Consulta do paciente atualizada com sucesso!')
                     print()
                  
                  elif resposta4 == '0':
                     print()

         elif resposta3 == '4':
            print()
            print('Remoção de consulta do sistema')
            print()
            nome = input('Qual o nome do paciente que deseja remover a consulta? ')

            if nome in consultas:
               del consultas[nome]
               print('consulta removida com sucesso!')
               print()
            
            else:
               print('Paciente não encontrado.')
               print()

         elif resposta3 == '0':
            print()
   
   elif resposta == '0':
      print()
   
   else:
     print()
     print('Opção inválida, escolha alguma da opções de 1 a 5!')
     print()

print('Fim do programa, Obrigado por usar o PyDiet!')