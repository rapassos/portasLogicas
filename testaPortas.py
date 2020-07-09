import portas;

# Dados de entrada
a = [0, 0, 1, 1];
b = [0, 1, 0, 1];

# Porta AND
print("Porta AND");
for count in range(0,4):
    print("a = ",a[count]," b = ",b[count]," => a AND b =",portas.portaAnd(a[count],b[count]));
print("");

# Porta OR
print("Porta OR");
for count in range(0,4):
    print("a = ",a[count]," b = ",b[count]," => a OR b =",portas.portaOr(a[count],b[count]));
print("");

# Porta NOT
print("Porta NOT");
print("a = 0 => a NOT = ",portas.portaNot(0));
print("a = 1 => a NOT = ",portas.portaNot(1));
print("");

# Porta NAND
print("Porta NAND");
for count in range(0,4):
    print("a = ",a[count]," b = ",b[count]," => a NAND b =",portas.portaNand(a[count],b[count]));
print("");

# Porta NOR
print("Porta NOR");
for count in range(0,4):
    print("a = ",a[count]," b = ",b[count]," => a OR b =",portas.portaNor(a[count],b[count]));
print("");

# Porta XOR
print("Porta XOR");
for count in range(0,4):
    print("a = ",a[count]," b = ",b[count]," => a XOR b =",portas.portaXor(a[count],b[count]));
print("");

# Porta XNOR
print("Porta XNOR");
for count in range(0,4):
    print("a = ",a[count]," b = ",b[count]," => a XNOR b =",portas.portaXnor(a[count],b[count]));
print("");