cadena='Geringoso'
capadepenapa=''
sumo_letra=''
for c in cadena:
    if c=='a':
        sumo_letra='apa'
    elif c=='e':
        sumo_letra='epe'
    elif c=='i':
        sumo_letra='ipi'
    elif c=='o':
        sumo_letra='opo'
    elif c=='u':
        sumo_letra='upu'
    else:
        sumo_letra=c

    capadepenapa+=sumo_letra

print(capadepenapa)
