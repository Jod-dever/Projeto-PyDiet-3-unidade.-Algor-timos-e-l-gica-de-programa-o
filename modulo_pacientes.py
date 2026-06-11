def modulopacientes(pacientes):
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
        print()
      
        if resposta1 == '1':
            print('Cadastro de paciente no sistema')
            print()
            nome = input('Nome do paciente: ').lower()
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
            nome = input('Qual o nome do paciente? ').lower()
            print()
            
            if nome in pacientes:
               print('Nome:', nome.title())
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
            nome = input('Qual o nome do paciente que deseja atualizar? ').lower()
            print()
            if nome in pacientes:
               resposta2 = ''
               while resposta2 != '0':
                  print('####################################################')
                  print('##  O que você quer atualizar?            ##########')
                  print('##  Selecione uma das opções a seguir ##############')
                  print('##  1 - Nome do paciente                          ##')
                  print('##  2 - Telefone do paciente                      ##')
                  print('##  3 - Email do paciente                         ##')
                  print('##  4 - Data de nascimento do paciente            ##')
                  print('##  5 - Peso do paciente                          ##')
                  print('##  6 - Objetivo do paciente                      ##')
                  print('##  0 - Voltar ao menu dos pacientes              ##')
                  resposta2 = input('## Escolha a sua opção: ')
                  print()

                  if resposta2 == '1':
                     novo_nome = input('Novo nome do paciente: ').lower()
                     pacientes[novo_nome] = pacientes[nome]
                     del pacientes[nome]
                     nome = novo_nome
                     print('Nome do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '2':
                     pacientes[nome]['telefone'] = input('Novo telefone: ')
                     print('Telefone do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '3':
                     pacientes[nome]['email'] = input('Novo Email: ')
                     print('Email do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '4':
                     pacientes[nome]['data_nascimento'] = input('Nova data de nascimento: ')
                     print('Data de nascimento do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '5':
                     pacientes[nome]['peso'] = input('Novo peso: ')
                     print('Peso do paciente atualizado com sucesso!')
                     print()
                  
                  elif resposta2 == '6':
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
            nome = input('Qual o nome do paciente que deseja remover? ').lower()
            print()

            if nome in pacientes:
               del pacientes[nome]
               print('Paciente removido com sucesso!')
               print()
            
            else:
               print('Paciente não encontrado.')
               print()
           
        elif resposta1 == '0':
            print()