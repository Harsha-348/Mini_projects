##1-Basic_calculator

##DEFINE THE FUNCTIONS: ADD,SUB,MUL,DIV
def add(a,b):
    answer= a + b
    print(str("a")+"+"+str("b")+"="+str(a+b) + "\n")

def sub(a,b):
    answer= a - b
    print(str("a")+"-"+str("b")+"="+str(a-b) + "\n")

def mul(a,b):
    answer=a*b
    print(str("a")+"*"+str("b")+"="+str(a*b) + "\n")

def div(a,b):
    answer=a/b
    print(str("a")+"/"+str("b")+"="+str(a/b) + "\n")

##PRINT OPTIONS 
while True:
    print("-------"+"a.Addition"+"----------")
    print("-------"+"b.subtraction"+"-------")
    print("-------"+"c.multiplication"+"----")
    print("-------"+"d.division"+"----------")
    print("-------"+"e.The_End"+"----------")
    
    choice=(input("Enter the option:"))+"\n"
    
    ##    choices based on options
    if choice=="a" or choice=="A":
        print("Addition")
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        add(a,b)
    
    elif choice=="b" or choice=="B":
        print("Subtraction")
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        sub(a,b)
    
    elif choice=="c" or choice=="C":
        print("multiplication")
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        mul(a,b)
    
    elif choice=="d" or choice=="D":
        print("division")
        a=int(input("enter the first number:"))
        b=int(input("enter the second number:"))
        div(a,b)

    elif choice=="e" or choice=="E":
        print("The End")
        quit()
