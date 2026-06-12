from datetime import datetime

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
            nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
            hoje = datetime.today()
            idade = hoje.year - nascimento.year
            if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
                idade -= 1
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
                print()
                print('Telefone:', pacientes[nome]['telefone'])
                print()
                print('Email:', pacientes[nome]['email'])
                print()
                print('Data de nascimento:', pacientes[nome]['data_nascimento'])
                print()
                print('idade:', pacientes[nome]['idade'])
                print()
                print('altura:', pacientes[nome]['altura'])
                print()
                print('Peso:', pacientes[nome]['peso'])
                print()
                print('Gênero:', pacientes[nome]['sexo'].title())
                print()
                print('Circunferência do pescoço:', pacientes[nome]['circ_pesc'])
                print()
                print('Circunferência da cintura:', pacientes[nome]['circ_cint'])
                print()
                print('Circunferência do quadril:', pacientes[nome]['circ_quad'])
                print()
                if pacientes[nome]['nivel_atv'] == '1':
                    print('Sedentário')
                    print()
                elif pacientes[nome]['nivel_atv'] == '2':
                    print('Levemente ativo')
                    print()
                elif pacientes[nome]['nivel_atv'] == '3':
                    print('Moderadamente ativo')
                    print()
                elif pacientes[nome]['nivel_atv'] == '4':
                    print('Muito ativo')
                    print()
                elif pacientes[nome]['nivel_atv'] == '5':
                    print('Extremamente ativo')
                    print()               
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
                    print('## 1  -> Nome do paciente                          ##')
                    print('## 2  -> Telefone do paciente                      ##')
                    print('## 3  -> Email do paciente                         ##')
                    print('## 4  -> Data de nascimento do paciente            ##')
                    print('## 5  -> Altura do paciente                        ##')
                    print('## 6  -> Peso do paciente                          ##')
                    print('## 7  -> Circunferência do pescoço                 ##')
                    print('## 8  -> Circunferência do cintura                 ##')
                    print('## 9  -> Circunferência do quadril                 ##')
                    print('## 10 -> Nível de atividade física                 ##')
                    print('## 11 -> Objetivo do paciente                      ##')
                    print('## 0  -> Voltar ao menu dos pacientes              ##')
                    resposta_pac_at = input('## Escolha a sua opção: ')
                    print()

                    if resposta_pac_at == '1':
                        novo_nome = input('Novo nome do paciente: ').lower()
                        pacientes[novo_nome] = pacientes[nome]
                        del pacientes[nome]
                        nome = novo_nome
                        print()
                        print('Nome do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '2':
                        pacientes[nome]['telefone'] = input('Novo telefone: ')
                        print()
                        print('Telefone do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '3':
                        pacientes[nome]['email'] = input('Novo Email: ')
                        print()
                        print('Email do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '4':
                        pacientes[nome]['data_nascimento'] = input('Nova data de nascimento: ')
                        print()
                        print('Data de nascimento do paciente atualizado com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '5':
                        pacientes[nome]['altura'] = input('Nova altura: ')
                        print()
                        print('Altura do paciente atualizado com sucesso!')
                        print()
                    
                    elif resposta_pac_at == '6':
                        pacientes[nome]['peso'] = input('Novo peso: ')
                        print()
                        print('Peso do paciente atualizado com sucesso!')
                        print()

                    elif resposta_pac_at == '7':
                        pacientes[nome]['circ_pesc'] = input('Nova circunferência do pescoço: ')
                        print()
                        print('Circunferência do pescoço do paciente atualizada com sucesso!')
                        print()

                    elif resposta_pac_at == '8':
                        pacientes[nome]['circ_cint'] = input('Nova circunferência da cintura: ')
                        print()
                        print('Circunferência da cintura do paciente atualizada com sucesso!')
                        print()

                    elif resposta_pac_at == '9':
                        pacientes[nome]['circ_quad'] = input('Nova circunferência do quadril: ')
                        print()
                        print('Circunferência do quadril do paciente atualizada com sucesso!')
                        print()
                  
                    elif resposta_pac_at == '10':
                        print('### qual o nível de atividade física do paciente ###')
                        print('##  1 - Sedentário -> pouco ou nenhum exercício                                   ##')
                        print('##  2 - Levemente ativo -> exercício leve ou atividade leve diária                ##')
                        print('##  3 - Moderadamente ativo -> exercício moderado ou atividade moderada diária    ##')
                        print('##  4 - Muito ativo -> exercício intenso ou atividade intensa diária              ##')
                        print('##  5 - Extremamente ativo -> exercício muito intenso ou trabalho físico pesado   ##')
                        pacientes[nome]['nivel_atv'] = input('Novo nível de atividade física: ')
                        print()
                        print('Nível de atividade física do paciente atualizado com sucesso!')
                        print()

                    elif resposta_pac_at == '11':
                        pacientes[nome]['objetivo'] = input('Novo objetivo do paciente: ')
                        print()
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

         