salario_base, horas_extras, tiene_bonificacion=input().split()
salario_base=float(salario_base)
horas_extras=int(horas_extras)
tiene_bonificacion=int(tiene_bonificacion)
bonificacion = 0.05
if tiene_bonificacion ==1:
   vrbonificacion = salario_base * bonificacion
else:
     vrbonificacion = salario_base * 0
vhe1 = salario_base / 192 * 0.25
vhef = salario_base / 192 + vhe1
vrhorasextras = horas_extras * vhef
dctosalud = 0.035
dctopension= 0.04
dctcaja = 0.01
salario_total = (salario_base + vrhorasextras + vrbonificacion)
vrdcts = salario_total * dctosalud
vrdctp = salario_total * dctopension
vrdctc = salario_total * dctcaja
salario_totaldcto = (salario_base + vrhorasextras + vrbonificacion - vrdcts - vrdctp - vrdctc)
print(round(salario_totaldcto,1))
