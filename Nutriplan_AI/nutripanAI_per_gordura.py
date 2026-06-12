def bodyfat(pacientes):
    
    from math import log10
    
    resposta_bf = ''
    while resposta_bf !='0':
        print('##############################################################################')
        print('##  CÁLCULO DE PERCENTUAL DE GORDURA                                        ##')
        print('##  O que você quer fazer?                                                  ##')
        print('##  Selecione uma das opções a seguir                                       ##')
        print('##  1 - Cálculo para paciente já cadastrado                                 ##')
        print('##  2 - Consulta rápida                                                     ##')
        print('##  0 - Voltar ao menu do Nutriplan AI                                      ##')
        resposta_bf = input('## Escolha a sua opcão: ')
        print()

        if resposta_bf == '1':
            nome = input('Qual o nome do paciente? ').lower()
            print()

            if nome in pacientes:
                if pacientes[nome]['sexo'] == 'masculino':
                    cintura = float(pacientes[nome]['circ_cint']) / 2.54
                    pescoco = float(pacientes[nome]['circ_pesc']) / 2.54
                    altura = (float(pacientes[nome]['altura']) * 100) / 2.54
                    perc_bf = 86.010 * log10(cintura - pescoco) - 70.041 * log10(altura) + 36.76
                    print('O percentual de gordura do paciente {} é de {:.1f}!'.format(nome.title(),perc_bf))
                    print()

                elif pacientes[nome]['sexo'] == 'feminino':
                    cintura = float(pacientes[nome]['circ_cint']) / 2.54
                    pescoco = float(pacientes[nome]['circ_pesc']) / 2.54
                    quadril = float(pacientes[nome]['circ_quad']) / 2.54
                    altura = (float(pacientes[nome]['altura']) * 100) / 2.54
                    perc_bf = 163.205 * log10(cintura + quadril - pescoco) - 97.684 * log10(altura) - 78.387 
                    print('O percentual de gordura da paciente {} é de {:.1f}!'.format(nome.title(),perc_bf))
                    print()

            else:
                print('Paciente não encontrado!')        
                                                                          
