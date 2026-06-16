import os

def carregar_pacientes(dicionario_pacientes):
    if os.path.exists('pacientes.txt'):

        pacientes = {}

        arq = open('pacientes.txt', 'r')

        for linha in arq:

            linha = linha.strip()

            dados = linha.split(';')

            nome = dados[0]

            pacientes[nome] = {
                'telefone': dados[1],
                'email': dados[2],
                'data_nascimento': dados[3],
                'idade': dados[4],
                'altura': dados[5],
                'peso': dados[6],
                'sexo': dados[7],
                'circ_pesc': dados[8],
                'circ_cint': dados[9],
                'circ_quad': dados[10],
                'nivel_atv': dados[11],
                'objetivo': dados[12]
            }

        arq.close()

        return pacientes

    else:
        return dicionario_pacientes()
    
def carregar_consultas(dicionario_consultas):
    if os.path.exists('consultas.txt'):

        consultas = {}

        arq = open('consultas.txt', 'r')

        for linha in arq:

            linha = linha.strip()

            dados = linha.split(';')

            nome = dados[0]

            consultas[nome] = {
                'telefone': dados[1],
                'email': dados[2],
                'data_nascimento': dados[3],
                'dia_consulta': dados[4]
            }

        arq.close()

        return consultas

    else:
        return dicionario_consultas()
    
def salvar_pacientes(pacientes):
    arq = open('pacientes.txt', 'w')

    for nome in pacientes:

        arq.write(
            nome + ';' +
            pacientes[nome]['telefone'] + ';' +
            pacientes[nome]['email'] + ';' +
            pacientes[nome]['data_nascimento'] + ';' +
            pacientes[nome]['idade'] + ';' +
            pacientes[nome]['altura'] + ';' +
            pacientes[nome]['peso'] + ';' +
            pacientes[nome]['sexo'] + ';' +
            pacientes[nome]['circ_pesc'] + ';' +
            pacientes[nome]['circ_cint'] + ';' +
            pacientes[nome]['circ_quad'] + ';' +
            pacientes[nome]['nivel_atv'] + ';' +
            pacientes[nome]['objetivo'] + ';' +
            pacientes[nome]['quant_proteinas'] + ';' +
            pacientes[nome]['get'] +
            '\n'
        )

    arq.close()

def salvar_consultas(consultas):
    arq = open('consultas.txt', 'w')

    for nome in consultas:

        arq.write(
            nome + ';' +
            consultas[nome]['telefone'] + ';' +
            consultas[nome]['email'] + ';' +
            consultas[nome]['data_nascimento'] + ';' +
            consultas[nome]['dia_consulta'] +
            '\n'
        )

    arq.close()