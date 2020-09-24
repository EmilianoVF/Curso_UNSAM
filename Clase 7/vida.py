import datetime


fecha_nacimiento = '08/01/1989'


def vida(fecha_nacimiento):
    '''
    fecha_nacimiento = en formato 'dd/mm/AAAA'
    (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales)
    '''
    momento_actual = datetime.datetime.now()
    naciste_en = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
    return (momento_actual-naciste_en).total_seconds()


print(vida(fecha_nacimiento))
