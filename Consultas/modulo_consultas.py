def moduloconsultas(consultas):
    resposta_con = ''
    while resposta_con != '0':
        print('##########################################')
        print('##  O que você quer fazer?              ##')
        print('##  Selecione uma das opções a seguir   ##')
        print('##  1 - Cadastrar consulta              ##')
        print('##  2 - Informações sobre consulta      ##')
        print('##  3 - Atualizar consulta              ##')
        print('##  4 - Excluir consulta                ##')
        print('##  0 - Voltar ao menu principal        ##')
        resposta_con = input('## Escolha a sua opcão: ')
        print()

        if resposta_con == '1':
            print('Cadastro de paciente no sistema')
            print()
            nome = input('Nome do paciente: ').lower()
            telefone = input('Telefone: ')
            email = input('E-mail: ')
            data_nascimento = input('Data de nascimento: ')
            dia_consulta = input('Dia da consulta: ')
            consultas[nome] = {
               'telefone': telefone,
               'email': email,
               'data_nascimento': data_nascimento,
               'dia_consulta': dia_consulta
            }
            print('Consulta cadastrada com sucesso!')
            print()
         
        elif resposta_con == '2':
            print('Informações da consulta no sistema')
            print()
            nome = input('Qual o nome do paciente? ').lower()
            
            if nome in consultas:
                print('Nome:', nome.title())
                print('Telefone:', consultas[nome]['telefone'])
                print('Email:', consultas[nome]['email'])
                print('Data de nascimento:', consultas[nome]['data_nascimento'])
                print('Dia da consulta:', consultas[nome]['dia_consulta'])
                print()
            else:
                print('Consulta não encontrada.')
                print()

        elif resposta_con == '3':
            print('Atualização de cadastro de paciente no sistema')
            print()
            nome = input('Qual o nome do paciente que deseja atualizar? ').lower()
            if nome in consultas:
                resposta_con_at = ''
                while resposta_con_at != '0':
                    print('####################################################')
                    print('##  O que você quer atualizar?            ##########')
                    print('##  Selecione uma das opções a seguir     ##########')
                    print('##  1 - Nome do paciente                          ##')
                    print('##  2 - Telefone do paciente                      ##')
                    print('##  3 - Email do paciente                         ##')
                    print('##  4 - Data de nascimento do paciente            ##')
                    print('##  5 - Dia da consulta                           ##')
                    print('##  0 - Voltar ao menu das consultas              ##')
                    resposta_con_at = input('## Escolha a sua opção: ')
                    print()

                    if resposta_con_at == '1':
                        novo_nome = input('Novo nome do paciente: ').lower()
                        consultas[novo_nome] = consultas[nome]
                        del consultas[nome]
                        nome = novo_nome
                        print('Nome do paciente atualizado com sucesso!')
                        print()
                    
                    elif resposta_con_at == '2':
                        consultas[nome]['telefone'] = input('Novo telefone: ')
                        print('Telefone do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_con_at == '3':
                        consultas[nome]['email'] = input('Novo Email: ')
                        print('Email do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_con_at == '4':
                        consultas[nome]['data_nascimento'] = input('Nova data de nascimento: ')
                        print('Data de nascimento do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_con_at == '5':
                        consultas[nome]['dia_consulta'] = input('Novo dia da consulta: ')
                        print('Consulta do paciente atualizada com sucesso!')
                        print()
                  
                    elif resposta_con_at == '0':
                        print()

                    else:
                        print('Opção inválida, escolha alguma da opções de 0 a 5!')
                        print()

        elif resposta_con == '4':
            print('Remoção de consulta do sistema')
            print()
            nome = input('Qual o nome do paciente que deseja remover a consulta? ').lower()

            if nome in consultas:
                del consultas[nome]
                print('Consulta removida com sucesso!')
                print()
            
            else:
                print('Consulta não encontrada.')
                print()

        elif resposta_con == '0':
            print()
                
        else:
            print()
            print('Opção inválida, escolha alguma da opções de 0 a 4!')
            print()