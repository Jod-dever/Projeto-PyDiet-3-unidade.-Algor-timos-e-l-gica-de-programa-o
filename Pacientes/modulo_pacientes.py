from Pacientes.script_idade import idade_pac

def modulopacientes(pacientes):
    resposta_pac = ''  
    while resposta_pac != '0':
        print('####################################################')
        print('##  O que você quer fazer?            ##############')
        print('##  Selecione uma das opções a seguir ##############')
        print('##  1 - Cadastrar Paciente            ##')
        print('##  2 - Informações sobre paciente    ##')
        print('##  3 - Atualizar paciente            ##')
        print('##  4 - Excluir paciente              ##')
        print('##  0 - Voltar ao menu principal      ##')
        resposta_pac = input('## Escolha a sua opcão: ')
        print()
      
        if resposta_pac == '1':
            print('Cadastro de paciente no sistema')
            print()
            nome = input('Nome do paciente: ').lower()
            print()
            telefone = input('Telefone: ')
            print()
            email = input('E-mail: ')
            print()
            data_nascimento = input('Data de nascimento (dd/mm/aaaa): ')
            print()
            idade = idade_pac()
            print()
            altura = input('Altura do paciente em metros (m):') 
            print()
            peso = input('Peso do paciente em quilogramas (kg): ')
            print()
            sexo = input('Gênero do paciente (Masculino/Feminino): ').lower()
            print()
            circ_pesc = input('Circunferência do pescoço do paciente em centímetros (cm):')
            print()
            circ_cint = input('Circunferência da cintura do paciente em centímetros (cm):')
            print()
            circ_quad = input('Circunferência do quadril do paciente em centímetros (cm):')
            print()
            print('### qual o nível de atividade física do paciente ###')
            print('##  1 - Sedentário -> pouco ou nenhum exercício                                   ##')
            print('##  2 - Levemente ativo -> exercício leve ou atividade leve diária                ##')
            print('##  3 - Moderadamente ativo -> exercício moderado ou atividade moderada diária    ##')
            print('##  4 - Muito ativo -> exercício intenso ou atividade intensa diária              ##')
            print('##  5 - Extremamente ativo -> exercício muito intenso ou trabalho físico pesado   ##')
            nivel_atv = input('Escolha uma das opções: ') 
            print()
            print('### qual o objetivo do paciente?  ##')
            print('##  Emagrecimento                 ##')
            print('##  Ganho de massa muscular       ##')
            print('##  Manter o peso                 ##')
            objetivo = input('Objetivo do paciente: ')
            print()
            pacientes[nome] = {
               'telefone': telefone,
               'email': email,
               'data_nascimento': data_nascimento,
               'idade': idade,
               'altura': altura,
               'peso': peso,
               'sexo': sexo,
               'circ_pesc': circ_pesc,
               'circ_cint': circ_cint,
               'circ_quad': circ_quad,
               'nivel_atv': nivel_atv,
               'objetivo': objetivo
            }
            print('Paciente cadastrado com sucesso!')
            print()
          
        elif resposta_pac == '2':
            print('Informações do paciente no sistema')
            print()
            nome = input('Qual o nome do paciente? ').lower()
            print()
            
            if nome in pacientes:
                print('Nome:', nome.title())
                print('Telefone:', pacientes[nome]['telefone'])
                print('Email:', pacientes[nome]['email'])
                print('Data de nascimento:', pacientes[nome]['data_nascimento'])
                print('idade:', pacientes[nome]['idade'])
                print('altura:', pacientes[nome]['altura'])
                print('Peso:', pacientes[nome]['peso'])
                print('Gênero:', pacientes[nome]['sexo'])
                print('Circunferência do pescoço:', pacientes[nome]['circ_pesc'])
                print('Circunferência da cintura:', pacientes[nome]['circ_cint'])
                print('Circunferência do quadril:', pacientes[nome]['circ_quad'])
                if pacientes[nome]['nivel_atv'] == '1':
                    print('Sedentário')
                elif pacientes[nome]['nivel_atv'] == '2':
                    print('Levemente ativo')
                elif pacientes[nome]['nivel_atv'] == '3':
                    print('Moderadamente ativo')
                elif pacientes[nome]['nivel_atv'] == '4':
                    print('Muito ativo')
                elif pacientes[nome]['nivel_atv'] == '5':
                    print('Extremamente ativo')               
                print('Objetivo:', pacientes[nome]['objetivo'])
                print()
            else:
                print('Paciente não encontrado.')
                print()
         
        elif resposta_pac == '3':
            print('Atualização de cadastro de paciente no sistema')
            print()
            nome = input('Qual o nome do paciente que deseja atualizar? ').lower()
            print()
            if nome in pacientes:
                resposta_pac_at = ''
                while resposta_pac_at != '0':
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
                    resposta_pac_at = input('## Escolha a sua opção: ')
                    print()

                    if resposta_pac_at == '1':
                        novo_nome = input('Novo nome do paciente: ').lower()
                        pacientes[novo_nome] = pacientes[nome]
                        del pacientes[nome]
                        nome = novo_nome
                        print('Nome do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '2':
                        pacientes[nome]['telefone'] = input('Novo telefone: ')
                        print('Telefone do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '3':
                        pacientes[nome]['email'] = input('Novo Email: ')
                        print('Email do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '4':
                        pacientes[nome]['data_nascimento'] = input('Nova data de nascimento: ')
                        print('Data de nascimento do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '5':
                        pacientes[nome]['peso'] = input('Novo peso: ')
                        print('Peso do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '6':
                        pacientes[nome]['objetivo'] = input('Novo objetivo: ')
                        print('Objetivo do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '0':
                        print()

                    else:
                        print('Opção inválida, escolha alguma da opções de 0 a 6!')
                        print()
               
            else:
               print('Paciente não encontrado')      
   
        elif resposta_pac == '4':
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
           
        elif resposta_pac == '0':
            print()
         
        else:
            print('Opção inválida, escolha alguma da opções de 0 a 4!')
            print()

         