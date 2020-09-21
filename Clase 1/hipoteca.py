saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0

while saldo > 0:
    if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
        pago = pago_mensual+pago_extra
    else:
        pago = pago_mensual

    if saldo * (1+tasa/12) <= pago:
        pago = saldo * (1+tasa/12)
        saldo = saldo * (1+tasa/12) - pago
        total_pagado = total_pagado + pago
        break

    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    mes += 1

print('Total pagado', round(total_pagado, 2), 'en', mes, 'meses')
