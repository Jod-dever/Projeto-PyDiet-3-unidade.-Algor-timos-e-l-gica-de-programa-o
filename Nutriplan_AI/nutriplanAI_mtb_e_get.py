def mtb_get (pacientes):
    resposta_mtb = ''
    while resposta_mtb != '0':
        print('##############################################################################')
        print('##  CÁLCULO DE METABOLISMO BASAL (TMB) E GASTO ENERGÉTICO TOTAL (GET)       ##')
        print('##  O que você quer fazer?                                                  ##')
        print('##  Selecione uma das opções a seguir                                       ##')
        print('##  1 - Cálculo para paciente já cadastrado                                 ##')
        print('##  2 - Consulta rápida                                                     ##')
        print('##  0 - Voltar ao menu do Nutriplan AI                                      ##')
        resposta_mtb = input('## Escolha a sua opcão: ')
        print()

        if resposta_mtb == '1':
            nome = input('Qual o nome do paciente? ').lower()
            print()
              
            if pacientes[nome]['sexo'] == 'masculino':
                tmb = (float(pacientes[nome]['peso']) * 13.75) + (float(pacientes[nome]['altura']) * 500.3) - (int(pacientes[nome]['idade']) * 6.75) + 66.5
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
                tmb = (float(pacientes[nome]['peso']) * 9.563) + (float(pacientes[nome]['altura']) * 185) - (int(pacientes[nome]['idade']) * 4.676) + 665.1
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
            idade = int(input('Digite a idade do paciente: '))
            print()
            peso = float(input('Digite o peso do paciente em quilogramas(kg): '))
            print()
            altura = float(input('Qual a altura do paciente em metros(m): '))
            print()
            sexo = input('Qual o gênero do paciente (m/f): ')
            print()

            print('### qual o nível de atividade física do paciente ###')
            print('##  1 - Sedentário -> pouco ou nenhum exercício                                   ##')
            print('##  2 - Levemente ativo -> exercício leve ou atividade leve diária                ##')
            print('##  3 - Moderadamente ativo -> exercício moderado ou atividade moderada diária    ##')
            print('##  4 - Muito ativo -> exercício intenso ou atividade intensa diária              ##')
            print('##  5 - Extremamente ativo -> exercício muito intenso ou trabalho físico pesado   ##')
            nivel_atv = input('Escolha uma das opções: ')
            print()

            if sexo in ['M','m']:
                tmb = 66.5 + (13.75 * peso) + (500.3 * altura) - (6.75 * idade) 
                if nivel_atv == '1':
                    get = tmb * 1.2
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de pouco ou nenhum exercício,')
                    print('o seu gasto energético total é de {:.2f}.'.format(get))
                    print()
                
                elif nivel_atv == '2':
                    get = tmb * 1.375
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de exercício leve ou')
                    print('atividade leve diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print() 

                elif nivel_atv == '3':
                    get = tmb * 1.55
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de exercício moderado ou')
                    print('atividade moderada diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()    

                elif nivel_atv == '4':
                    get = tmb * 1.725
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de exercício intenso ou')
                    print('atividade intensa diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()

                elif nivel_atv == '5':
                    get = tmb * 1.9
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de exercício muito intenso ou')
                    print('trabalho físico pesado diário, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()

            elif sexo in ['F','f']:
                tmb = 655.1 + (9.563 * peso) + (185 * altura) - (4.676 * idade)
                if nivel_atv == '1':
                    get = tmb * 1.2
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de pouco ou nenhum exercício,')
                    print('o seu gasto energético total é de {:.2f}.'.format(get))
                    print()
                
                elif nivel_atv == '2':
                    get = tmb * 1.375
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de exercício leve ou')
                    print('atividade leve diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print() 

                elif nivel_atv == '3':
                    get = tmb * 1.55
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de exercício moderado ou')
                    print('atividade moderada diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()    

                elif nivel_atv == '4':
                    get = tmb * 1.725
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de exercício intenso ou')
                    print('atividade intensa diária, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()

                elif nivel_atv == '5':
                    get = tmb * 1.9
                    print('A taxa de metabolismo basal do paciente é de {:.2f} e já que '.format(tmb))
                    print('o nível de atividade física dele é de exercício muito intenso ou')
                    print('trabalho físico pesado diário, o seu gasto energético total é de {:.2f}.'.format(get))
                    print()


        elif resposta_mtb == '0':
            print()
            
        else:
            print('Opção inválida, escolha alguma da opções de 0 a 2!')
            print()

