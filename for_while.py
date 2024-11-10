senha = "32789"
tentativa = input("Digite a senha: ")
while (tentativa != senha):
  print("Senha incorreta! Tente novamente.")
  tentativa = input("Digite a senha correta: ")
  if (tentativa == senha):
    print("Senha correta! Acesso concedido.")
    break


alunos=int(input("Numeros de alunos na turma: "))

count=1; soma = 0.0
while count <= alunos:
    print("Nota do aluno ", count, ":")
    nota = float( input() )
    soma += nota
    count += 1

print("Media da turma: ", (soma/alunos) )


texto = input("Insira o seu texto: ")
caracter1 = set()
for caracter in texto:
  caracter1.add(caracter)
for caracter in caracter1:
    contagem = texto.count(caracter)
    print(f"{caracter}: {contagem}")

number =int(input("Insira o numero que deseja saber a tabuada: "))
print("Aqui está a tabuada do número", number)
for i in range(1,11):
  print(f"{number} x {i} = {number*i}")



l_n = ["João", "Arhur", "Kim", "Luan", "Rafael", "Ahri"]
while True: 
 n = input("Digite o nome que deseja procurar:")

 encontrado = False
 for nome in l_n: 
  if nome == n:
    encontrado = True
    break
 if encontrado:
  print("O nome {} foi encontrado na lista.".format(n))
 else:
  print("O nome {} não foi encontrado na lista.".format(n))

