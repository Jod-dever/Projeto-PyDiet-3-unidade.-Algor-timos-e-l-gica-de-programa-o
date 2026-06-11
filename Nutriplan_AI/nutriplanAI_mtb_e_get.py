def mtb_get (pacientes):
    resposta_mtb = ''
    while resposta_mtb != '0':
        print('##############################################################################')
        print('##  CÁLCULO DE METABOLISMO BASAL (TMB) E GASTO ENERGÉTICO TOTAL (GET)       ##')
        print('##  O que você quer fazer?                                                  ##')
        print('##  Selecione uma das opções a seguir                                       ##')
        print('##  1 - Cálculo para paciente já cadastrado                                 ##')
        print('##  2 - Consulta rápida                                                     ##')
        print('##  0 - Voltar ao menu principal                                            ##')
        resposta_mtb = input('## Escolha a sua opcão: ')
        print()

        if resposta_mtb == '1':
            nome = input('Qual o nome do paciente? ').lower()
            print()
              
            if pacientes[nome]['sexo'] == 'masculino':
                tmb = (float(pacientes[nome]['peso']) * 13.75) + (float(pacientes[nome]['altura']) * 5.003 * 100) - (int(pacientes[nome]['idade']) * 6.75) + 66.5
                print()
                if pacientes[nome]['nivel_atv'] == '1':
                    get = tmb * 1.2
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de pouco ou nenhum exercício,')
                    print('o seu gasto energético total é de {:.2f}.'.format(get))
                    print()
                
                elif pacientes[nome]['nivel_atv'] == '2':
                    get = tmb * 1.375
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de exercício leve ou')
                    print('atividade leve diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print() 

                elif pacientes[nome]['nivel_atv'] == '3':
                    get = tmb * 1.55
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de exercício moderado ou')
                    print('atividade moderada diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()    

                elif pacientes[nome]['nivel_atv'] == '4':
                    get = tmb * 1.725
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de exercício intenso ou')
                    print('atividade intensa diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()

                elif pacientes[nome]['nivel_atv'] == '5':
                    get = tmb * 1.9
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de exercício muito intenso ou')
                    print('trabalho físico pesado diário, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()
                        
            elif pacientes[nome]['sexo'] == 'feminino':
                tmb = (float(pacientes[nome]['peso']) * 9.563) + (float(pacientes[nome]['altura']) * 1.85 * 100) - (int(pacientes[nome]['idade']) * 4.676) + 665.1
                print()
                if pacientes[nome]['nivel_atv'] == '1':
                    get = tmb * 1.2
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de pouco ou nenhum exercício,')
                    print('o seu gasto energético total é de {:.2f}.'.format(get))
                    print()
                        
                elif pacientes[nome]['nivel_atv'] == '2':
                    get = tmb * 1.375
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de exercício leve ou')
                    print('atividade leve diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()
                        
                elif pacientes[nome]['nivel_atv'] == '3':
                    get = tmb * 1.55
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de exercício moderado ou')
                    print('atividade moderada diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()    

                elif pacientes[nome]['nivel_atv'] == '4':
                    get = tmb * 1.725
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de exercício intenso ou')
                    print('atividade intensa diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()
                
                elif pacientes[nome]['nivel_atv'] == '5':
                    get = tmb * 1.9
                    print('A taxa de metabolismo basal do paciente {} é de {:.2f} e já que '.format(nome,tmb))
                    print('o nível de atividade física dele é de exercício muito intenso ou')
                    print('trabalho físico pesado diário, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()

        elif resposta_mtb == '2':
            print()

        elif resposta_mtb == '0':
            print()

        else:
            print('Resposta inválida!')

