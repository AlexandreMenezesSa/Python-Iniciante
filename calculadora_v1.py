# Calculadora em Python

print("\n******************* Python Calculator *******************")
print('Selecione o número da operação Desejada:')
print('\n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n')

def soma(num1,num2):
    print(num1,' + ',num2,'=' ,int(num1) + int(num2));

def sub(num1,num2):
    print(num1,' - ',num2,'=' ,int(num1) - int(num2));  

def mult(num1,num2):
    print(num1,' * ',num2,'=' ,int(num1) * int(num2));  
    
def div(num1,num2):
    print(num1,' / ',num2,'=' ,int(num1) / int(num2)); 

print('Digite a sua opção (1/2/3/4): ') 
opcao = input()

if int(opcao) > 4:
    print("Digite uma Opção Valida")
 
print('Digite o primeiro número')
nume1 = input()
print('Digite o segundo número')
nume2 = input()

if int(opcao) == 1:
    soma(nume1,nume2)
elif int(opcao) == 2:
    sub(nume1,nume2)
elif int(opcao) == 3:
    mult(nume1,nume2)
elif int(opcao) == 4:
 div(nume1,nume2)
      



