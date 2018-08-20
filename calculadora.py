def soma(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def menu():
    print()
    print("***************   CALCULADORA   ***************")
    print("*Isira dois numeros e depois a operacao*")
    numA = float(input("*Insira o numero A: *"))
    numB = float(input("*Insira o numero B: *"))
    op = input("*Insira a operacao[+,-,/,*]: ")
    if(op == '+'):
        print("A soma de %f com %f eh: %f" %(numA, numB, soma(numA,numB)))
    elif(op == '-'):
        print("A sub de %f com %f eh: %f" %(numA, numB, sub(numA,numB)))
    elif(op == '/'):
        print("A div de %f com %f eh: %f" %(numA, numB, div(numA,numB)))
    elif(op == '*'):
        print("A mult de %f com %f eh: %f" %(numA, numB, mult(numA,numB)))
    else:
        print("*OPERACAO INEXISTENTE*")

while(True):
    menu()
    
