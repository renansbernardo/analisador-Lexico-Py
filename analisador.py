import re

p = 0
while p == 0:
    
    
    def separar(i):
        separa = re.split(r'\s', i)
        return separa
    
    def numReal(i):
        num = re.compile(r'\d*\.\d+')
        busca = re.search(num, i)
        if busca:
            return True
        else:
            return False   
        
    def numInteiro(i):
        num = re.compile('\d')
        busca = re.search(num, i)
        if busca:
            return True
        else:
            return False        
    
       
    calculo = input("Qual expressão que será analisado?")    
    palavSeparado = separar(calculo)
    
    print (f' A expressão utilizada é: \n{palavSeparado}')
    
     
    for i in palavSeparado:
        
        if i == '+':
            print (f' {i} = Operador de Soma')
        elif i == '-':
            print (f"{i} = Operador de Subtração")
        elif i == '*':
            print (f"{i} = Operador de Multiplicação")
        elif i == '/':
            print (f"{i} = Operador de Divisão")
        elif i == '(':
            print (f"{i} = Abre parênteses")
        elif i == ')':
            print (f"{i} = Fecha parênteses")
        elif numReal(i):
            print (f"{i} = Número Real")   
        elif numInteiro(i):
            print (f"{i} = Número Inteiro")
        else:
            print (f"{i} = Erro: Caractere inválido")