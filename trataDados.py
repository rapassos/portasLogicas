def entradaBinaria(txt, txtInvalido):
    while True:
        try:
            entrada = int(input(txt))
            if not 0 <= entrada <= 1:
                raise ValueError(txtInvalido)
        except ValueError as e:
            print(txtInvalido)
        else:
            break
return entrada;


def entradaInt0a100(txt, txtInvalido):
    while True:
        try:
            entrada = int(input(txt))
            if not 0 <= entrada <= 100:
                raise ValueError(txtInvalido);
        except ValueError as e:
            print(txtInvalido);
        else:
            break;

    return entrada;


def entradaInt1a3(txt, txtInvalido):
    while True:
        try:
            entrada = int(input(txt))
            if not 1 <= entrada <= 3:
                raise ValueError(txtInvalido);
        except ValueError as e:
            print(txtInvalido);
        else:
            break;

    return entrada;

def comparaInt(a, b):
    if (a>b):
        retorno = ">";
    elif(a<b):
        retorno = "<";
    else:
        retorno = "=";
    return retorno;