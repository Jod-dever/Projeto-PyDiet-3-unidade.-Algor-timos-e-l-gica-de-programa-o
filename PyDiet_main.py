##### Um sistema de planejamento de dieta #####

from Dicionarios.modulo_dicionarios import dicionarios_pacientes,dicionario_consultas
from Pacientes.modulo_pacientes import modulopacientes
from Consultas.modulo_consultas import moduloconsultas
from Nutriplan_AI.nutriplanAI_imc import imc
from Nutriplan_AI.nutriplanAI_mtb_e_get import mtb_get

pacientes = dicionarios_pacientes()
consultas = dicionario_consultas()

resposta = ''

while resposta != '0':
    print('####################################################')
    print('#####  Seja bem vindo ao PyDiet                #####')
    print('#####  O seu sistema de planejamento de dietas #####')
    print('####################################################')
    print('##  Selecione uma das opções a seguir ##############')
    print('##  1 - Pacientes           ##')
    print('##  2 - Consultas           ##')
    print('##  3 - NutriPlan AI        ##')
    print('##  4 - Relatórios          ##')
    print('##  5 - Sobre o sistema     ##')
    print('##  0 - Sair                ##')
    resposta = input('##  Escolha sua opção: ')
    print()
  
    if resposta == '1':
        modulopacientes(pacientes)
     
    elif resposta == '2':
        moduloconsultas(consultas)

    elif resposta == '3':
        resposta_nu = ''
        while resposta_nu != '0':
            print('##############################################################################')
            print('##  O que você quer fazer?                                                  ##')
            print('##  Selecione uma das opções a seguir                                       ##')
            print('##  1 - Cálculo de IMC                                                      ##') ### resposta4 ###
            print('##  2 - Cáculo de metabolismo basal (TMB) e gasto energético total (GET)    ##') ### resposta5 ###
            print('##  3 - Cálculo de percentual de gordura corporal                           ##')
            print('##  4 - Planejamento de dieta                                               ##')
            print('##  0 - Voltar ao menu principal                                            ##')
            resposta_nu = input('## Escolha a sua opcão: ')
            print()

            if resposta_nu == '1':
                imc(pacientes)

            elif resposta_nu == '2':
                mtb_get(pacientes)
    
    elif resposta == '0':
        print('###################################')
        print('## Fim do programa               ##')
        print('## Obrigado por usar o PyDiet!   ##')
        print('###################################')
        print()

    else:
        print('Resposta inválida, esxolha alguma das opções de 0 a 5!')