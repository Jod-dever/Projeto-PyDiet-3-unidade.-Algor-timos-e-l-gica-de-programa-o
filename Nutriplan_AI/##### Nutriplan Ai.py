#####  Nutriplan Ai   
##### * Imc
##### * metabolismo basal e gasto total
##### * Distribuição de macro nutrientes
##### * Percentual de gordura corporal
##### * Evolução do paciente 
##### * Substituição de alimentos e montagem automática de dieta

from datetime import datetime

pacientes = {
    'joão augusto': {
        'telefone': '99999-0000',
        'email': 'joaoaugusto@ufrn.edu.br',
        'idade': '21',
        'data_nascimento': '22/10/2005',
        'altura': '1.75',
        'peso': '93.3',
        'sexo': 'masculino',
        'nivel_atv': '3',
        'objetivo': 'emagrecimento'
    }
}
   
resposta3 = ''
while resposta3 != '0':
   print('##############################################################################')
   print('##  O que você quer fazer?                                                  ##')
   print('##  Selecione uma das opções a seguir                                       ##')
   print('##  1 - Cálculo de IMC                                                      ##') ### resposta4 ###
   print('##  2 - Cáculo de metabolismo basal (TMB) e gasto energético total (GET)    ##') ### resposta5 ###
   print('##  3 - Cálculo de percentual de gordura corporal                           ##')
   print('##  4 - Planejamento de dieta                                               ##')
   print('##  0 - Voltar ao menu principal                                            ##')
   resposta3 = input('## Escolha a sua opcão: ')
   print()
   
   if resposta3 == '1':
      resposta4 = ''
      while resposta4 != '0':
         print('##############################################################################')
         print('##  CÁLCULO DE IMC                                                          ##')
         print('##  O que você quer fazer?                                                  ##')
         print('##  Selecione uma das opções a seguir                                       ##')
         print('##  1 - Cálculo para paciente já cadastrado                                 ##')
         print('##  2 - Consulta rápida                                                     ##')
         print('##  0 - Voltar ao menu principal                                            ##')
         resposta4 = input('## Escolha a sua opcão: ')
         print()
         
         if resposta4 == '1':
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
         
         elif resposta4 == '2':
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

         elif resposta4 == '0':
            print()
            
         else:
                  print('Resposta inválida!')
   
   elif resposta3 == '2':
       resposta5 = ''
       while resposta5 != '0':
          print('##############################################################################')
          print('##  CÁLCULO DE METABOLISMO BASAL (TMB) E GASTO ENERGÉTICO TOTAL (GET)       ##')
          print('##  O que você quer fazer?                                                  ##')
          print('##  Selecione uma das opções a seguir                                       ##')
          print('##  1 - Cálculo para paciente já cadastrado                                 ##')
          print('##  2 - Consulta rápida                                                     ##')
          print('##  0 - Voltar ao menu principal                                            ##')
          resposta5 = input('## Escolha a sua opcão: ')
          print()

          if resposta5 == '1':
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


   else:
      print('Resposta inválida!')



      

