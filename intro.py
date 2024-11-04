a = int(input("Enter first number: ")) 
#int utilizado para inserir números inteiros no codigo
b = int(input("Enter second number: "))
z = ((a**2) + (b**2))/(a - b)**2
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
