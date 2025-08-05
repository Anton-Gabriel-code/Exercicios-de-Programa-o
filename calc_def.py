def soma(a, b):
 return a + b
def sub(a, b):
 return a - b
def multi(a, b):
 return a * b 
def div(a, b):
 return a/b
def calc(n1, n2, op):
    if op == 1:
      return (soma(n1,n2))
    elif op == 2:
      return (sub(n1, n2))
    elif op == 3:
      return (multi(n1,n2))
    elif op == 4:
      if n2 == 0:  
            return "ERRO: NÃO É POSSÍVEL DIVIDIR POR 0!!"
      else:
            return div(n1, n2)
    else:
        return "ERRO: Operação inválida!"

    
print("Bem Vindo a calculadora! Como podemos ajudar - lo hoje?")
print("-"*55)
print("Aqui estão disponiveis as operações que temos: ")
print("-"*55)
print("Soma = 1")
print('Sub = 2')
print("Multi = 3")
print("Div = 4 ") 
print("-"*55)
print("-"*55)
n1 = float(input("Insira o valor: "))
n2 = float(input("Insira o valor: "))
op = int(input("Insira opereção que deseja realizar (1-4): "))
resultado = calc(n1, n2, op)
print(f"Resultado: {resultado}")
