
def portaAnd(x,y):
    return (x*y);

def portaOr(x,y):
    if((x+y)>0):
        return 1;
    else:
        return 0;

def portaNot(x):
    if(x==0):
        return 1
    else:
        return 0;

def portaNand(x,y):
    return portaNot(portaAnd(x,y));

def portaNor(x,y):
    return portaNot(portaOr(x,y));

def portaXor(x,y):
    if(portaAnd(x,y) == portaOr(x,y)):
        return 0;
    else:
        return 1;

def portaXnor(x,y):
    return portaNot(portaXor(x,y));
