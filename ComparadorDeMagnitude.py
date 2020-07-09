import portas, trataDados

# Dados de entrada
a = []
b = []

#Entrada A
for i in range(0, 4):
    a.append(trataDados.entradaBinaria("Entre com o valor de A["+str(i)+"]:","Valor inválido!"))

#Entrada B
for i in range(0, 4):
    b.append(trataDados.entradaBinaria("Entre com o valor de B[" + str(i) + "]:", "Valor inválido!"))

# Exibir Entradas
#for i in range(0, 4):
#    print("A[",i,"] = ", a[i], " =>  B[",i,"] = ", b[i])

print("a = ",a[3],a[2],a[1],a[0])
print("b = ",b[3],b[2],b[1],b[0])

# Fase 1 - GT e EQ
#print("Fase 1 => GT e EQ")
gt = []
eq = []
for i in range(0, 4):
    gt.append(portas.portaAnd(a[i], portas.portaNot(b[i])))
    eq.append(portas.portaXnor(a[i], b[i]))

print("")

# Fase 2 - A > B
# U10
u10 = portas.portaAnd(gt[0], eq[1])

# U11
u11 = portas.portaOr(u10, gt[1])

# U12
u12 = portas.portaAnd(u11, eq[2])

# U13
u13 = portas.portaOr(u12, gt[2])

# U14
u14 = portas.portaAnd(u13, eq[3])

# U15
u15 = portas.portaOr(u14, gt[3])


# Fase 3 - A = B
# U17
u17 = portas.portaAnd(eq[0], eq[1])

# U18
u18 = portas.portaAnd(eq[2], eq[3])

# U19
u19 = portas.portaAnd(u17, u18)

# Fase 4 - A < B
# U16
u16 = portas.portaNor(u15, u19)

# Resultados
print("A > B => ", u15)
print("A = B => ", u19)
print("A < B => ", u16)