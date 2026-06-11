def imc (pacientes):
    resposta_imc = ''
    while resposta_imc != '0':
        print('##############################################################################')
        print('##  CÁLCULO DE IMC                                                          ##')
        print('##  O que você quer fazer?                                                  ##')
        print('##  Selecione uma das opções a seguir                                       ##')
        print('##  1 - Cálculo para paciente já cadastrado                                 ##')
        print('##  2 - Consulta rápida                                                     ##')
        print('##  0 - Voltar ao menu principal                                            ##')
        resposta_imc = input('## Escolha a sua opcão: ')
        print()
                
        if resposta_imc == '1':
            nome = input('Qual o nome do paciente? ').lower()
            print()
                
            if nome in pacientes:
                imc = float(pacientes[nome]['peso'])/(float(pacientes[nome]['altura'])**2)
                if imc <= 18.5:
                    print('### O paciente {} encontra-se abaixo do peso de acordo com a tabela de IMC'.format(nome.title()))
                    print('### pois o seu IMC é igual a {:.1f}.'.format(imc))
                    print()
                    
                elif 18.6 <= imc <= 24.9 :
                    print('### O paciente {} encontra-se saudável de acordo com a tabela de IMC'.format(nome.title()))
                    print('### pois o seu IMC é igual a {:.1f}.'.format(imc))
                    print()
                                
                elif 25.0 <= imc <= 29.9:
                    print('### O paciente {} encontra-se com sobrepeso de acordo com a tabela de IMC'.format(nome.title()))
                    print('### pois seu IMC é igual a {:.1f}.'.format(imc))
                    print()
                    
                elif 30.0 <= imc <= 34.9:
                    print('### O paciente {} encontra-se com obesidade grau 1 de acordo com a tabela de IMC'.format(nome.title()))
                    print('### pois seu IMC é igual a {:.1f}.'.format(imc))
                    print()
                    
                elif 35 <= imc <= 39.9:
                    print('### O paciente {} encontra-se com obesidade grau 2 de acordo com a tabela de IMC'.format(nome.title()))
                    print('### pois seu IMC é igual a {:.1f}.'.format(imc))
                    print()
                    
                elif imc >= 40.0:
                    print('### O paciente {} encontra-se com obesidade grau 2 de acordo com a tabela de IMC'.format(nome.title()))
                    print('### pois seu IMC é igual a {:.1f}.'.format(imc))
                    print()
                        
                else:
                    print('Paciente não encontrado!')
                    print()
                
        elif resposta_imc == '2':
            peso = float(input('informe o peso em kg: '))
            altura = float(input('informa a altura em metros: '))
            imc = peso/(altura**2)
            print()
                    
            if imc <= 18.5:
                print('### O indivíduo encontra-se abaixo do peso de acordo com a tabela de IMC')
                print('### pois o seu IMC é igual a {:.1f}.'.format(imc))
                print()
                    
            elif 18.6 <= imc <= 24.9 :
                print('### O indivíduo encontra-se saudável de acordo com a tabela de IMC')
                print('### pois o seu IMC é igual a {:.1f}.'.format(imc))
                print()
                                
            elif 25.0 <= imc <= 29.9:
                print('### O indivíduo encontra-se com sobrepeso de acordo com a tabela de IMC')
                print('### pois seu IMC é igual a {:.1f}.'.format(imc))
                print()
                    
            elif 30.0 <= imc <= 34.9:
                print('### O indivíduo encontra-se com obesidade grau 1 de acordo com a tabela de IMC')
                print('### pois seu IMC é igual a {:.1f}.'.format(imc))
                print()
                    
            elif 35 <= imc <= 39.9:
                print('### O indivíduo encontra-se com obesidade grau 2 de acordo com a tabela de IMC')
                print('### pois seu IMC é igual a {:.1f}.'.format(imc))
                print()
                    
            elif imc >= 40.0:
                print('### O indivíduo encontra-se com obesidade grau 2 de acordo com a tabela de IMC')
                print('### pois seu IMC é igual a {:.1f}.'.format(imc))
                print()

        elif resposta_imc == '0':
            print()
                    
        else:
            print('Opção inválida, escolha alguma da opções de 0 a 2!')
            print()