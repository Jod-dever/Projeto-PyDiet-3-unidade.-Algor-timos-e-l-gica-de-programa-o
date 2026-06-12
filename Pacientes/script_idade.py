def idade_pac (data_nascimento):
    from datetime import datetime

    nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.today()

    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1