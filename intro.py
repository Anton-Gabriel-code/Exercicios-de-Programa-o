#Começo da Unidade dois introdução a python
frase = input("Digite uma frase: ")
frase = frase.upper()#deixa todas as letras em maiusculo
print(frase)

a = int(input("Enter first number: ")) 
#int utilizado para inserir números inteiros no codigo
b = int(input("Enter second number: "))
z = ((a**2) + (b**2))/(a - b)**2
print(z)

frase = ("Um elefante incomoda muita gente")
frase[3:20]#fatia a string do começo da string até o final sempre conta - se de 0 a 4

x = int(input("Digite um numero: ")) #int significa que somente números inteiros vão ser adicionados
y = int(input("Digite outro numero: "))
z = (x**2 + y**2)/(x-y)**2
print(z)

salario = float(input("Digite o salário: ")) #float, usado para inserir números com virgula
reajuste = salario * 0.15
novo_salario = salario + reajuste
print(f"O novo salário é: {novo_salario}")

salario = float(input("Insira o valor do seu sálario atual em reais: ")) #float significa que tanto números interios quanto números com casas decimais podem ser adicionados
porcentagem = float(input("Insira a porcentagem de reajuste: "))
reajuste = salario * (porcentagem/100)
novo_salario = salario + reajuste
print("O valor do seu novo sálario é de: ", novo_salario)
