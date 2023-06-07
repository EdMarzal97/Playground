vuelto_dollar = int(input("ingrese su vuelto de dolares : "))
vuelto_soles = int(input("ingrese cuanto le queda de soles: "))

dolar_euro = vuelto_dollar * 0.94
sol_euro = vuelto_soles * 0.25

presupuesto_euros = dolar_euro + sol_euro

print("te queda : ", presupuesto_euros, "Euros")
