def dicionarios_pacientes():
    pacientes = {
        'joão augusto': {
            'telefone': '99999-1111',
            'email': 'joaoaugusto@ufrn.edu.br',
            'data_nascimento': '22/10/2005',
            'idade': '20',
            'altura': '1.75',
            'peso': '93.3',
            'sexo': 'masculino',
            'circ_pesc': '35',
            'circ_cint': '80',
            'circ_quad': '85',
            'nivel_atv': '3',
            'objetivo': 'ganho de massa muscular',
            'quant_proteinas': '2.2',
            'get': ''
        },
        'josé': {
            'telefone': '99999-2222',
            'email': 'jose@ufrn.edu.br',
            'data_nascimento': '30/03/2008',
            'idade': '18',
            'altura': '1.75',
            'peso': '98',
            'sexo': 'masculino',
            'circ_pesc': '38',
            'circ_cint': '87',
            'circ_quad': '97',
            'nivel_atv': '3',
            'objetivo': 'emagrecimento'
            'quant_proteinas': '2',
            'get': ''
        },
        'maria clara': {
            'telefone': '99999-6666',
            'email': 'mariaclara@ufrn.edu.br',
            'data_nascimento': '01/12/2007',
            'idade': '18',
            'altura': '1.60',
            'peso': '60.2',
            'sexo': 'feminino',
            'circ_pesc': '32',
            'circ_cint': '66',
            'circ_quad': '88',
            'nivel_atv': '3',
            'objetivo': 'manter o peso'
            'quant_proteinas': '1.5',
            'get': ''
        }
    } 
    return pacientes

def dicionario_consultas():
    consultas = {
        'lucas': {
            'telefone': '99999-5555',
            'email': 'lucas@ufrn.edu.br',
            'data_nascimento': '09/08/2006',
            'dia_consulta': '30/05/2026'
        },
        'joan': {
            'telefone': '99999-4444',
            'email': 'joan@ufrn.edu.br',
            'data_nascimento': '03/04/2005',
            'dia_consulta': '21/02/2026'
        },
        'artur': {
            'telefone': '99999-3333',
            'email': 'artur@ufrn.edu.br',
            'data_nascimento': '12/06/2007',
            'dia_consulta': '29/06/2026'
        }
    }
    return consultas

def dicionario_alimentos():
    alimentos = {
        'proteinas': {
            'frango': {
                'proteina': 31.0,
                'carboidrato': 0.0,
                'gordura': 3.6,
                'fibra': 0.0,
                'kcal': 165
            },
            'patinho': {
                'proteina': 26.0,
                'carboidrato': 0.0,
                'gordura': 8.0,
                'fibra': 0.0,
                'kcal': 180
            },
            'tilapia': {
                'proteina': 26.0,
                'carboidrato': 0.0,
                'gordura': 2.7,
                'fibra': 0.0,
                'kcal': 128
            },
            'atum': {
                'proteina': 29.0,
                'carboidrato': 0.0,
                'gordura': 1.0,
                'fibra': 0.0,
                'kcal': 132
            },
            'ovo': {
                'proteina': 13.0,
                'carboidrato': 1.1,
                'gordura': 11.0,
                'fibra': 0.0,
                'kcal': 143
            }
        
        },
        'carboidratos': {
            'arroz': {
                'proteina': 2.7,
                'carboidrato': 28.0,
                'gordura': 0.3,
                'fibra': 0.4,
                'kcal': 130
            },
            'batata_doce': {
                'proteina': 1.6,
                'carboidrato': 20.0,
                'gordura': 0.1,
                'fibra': 3.0,
                'kcal': 86
            },
            'macarrao': {
                'proteina': 5.0,
                'carboidrato': 31.0,
                'gordura': 1.1,
                'fibra': 1.8,
                'kcal': 158
            },
            'pao_integral': {
                'proteina': 13.0,
                'carboidrato': 43.0,
                'gordura': 4.2,
                'fibra': 6.9,
                'kcal': 247
            },
            'tapioca': {
                'proteina': 0.2,
                'carboidrato': 43.0,
                'gordura': 0.0,
                'fibra': 0.0,
                'kcal': 168
            }
        },

        'gorduras' : {
            'abacate': {
                'proteina': 2.0,
                'carboidrato': 9.0,
                'gordura': 15.0,
                'fibra': 7.0,
                'kcal': 160
            },
            'castanha_do_para': {
                'proteina': 14.0,
                'carboidrato': 12.0,
                'gordura': 66.0,
                'fibra': 8.0,
                'kcal': 659
            },
            'amendoim': {
                'proteina': 26.0,
                'carboidrato': 16.0,
                'gordura': 49.0,
                'fibra': 8.5,
                'kcal': 567
            },
            'azeite': {
                'proteina': 0.0,
                'carboidrato': 0.0,
                'gordura': 100.0,
                'fibra': 0.0,
                'kcal': 884
            },
            'manteiga': {
                'proteina': 0.9,
                'carboidrato': 0.1,
                'gordura': 81.0,
                'fibra': 0.0,
                'kcal': 717
            }
        },
        
        'frutas' : {
            'banana': {
                'proteina': 1.1,
                'carboidrato': 22.8,
                'gordura': 0.3,
                'fibra': 2.6,
                'kcal': 89
            },
            'mamao': {
                'proteina': 0.5,
                'carboidrato': 10.8,
                'gordura': 0.3,
                'fibra': 1.7,
                'kcal': 43
            },
            'morango': {
                'proteina': 0.7,
                'carboidrato': 7.7,
                'gordura': 0.3,
                'fibra': 2.0,
                'kcal': 32
            },
            'melao': {
                'proteina': 0.8,
                'carboidrato': 8.2,
                'gordura': 0.2,
                'fibra': 0.9,
                'kcal': 34
            },
            'maca': {
                'proteina': 0.3,
                'carboidrato': 13.8,
                'gordura': 0.2,
                'fibra': 2.4,
                'kcal': 52
            }
        }
    }
    return alimentos