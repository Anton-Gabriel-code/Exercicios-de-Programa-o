#Programa que recebe a pontuação do jogador e classifica ele como "Iniciante", "INtermédiario" ou "Avançado".
pontos = int(input("Insira sua pontuação: "))
if pontos < 1000:
  print("Você é iniciante!")
elif pontos >= 1000 and pontos <= 5000:
  print("BOA! Você é intermediário!")
elif pontos > 5000:
  print("PARABÉNS!!! Você é avançado!")


#Programa que lê a média do aluno e mostra se ele está "Aprovado", "Em recuperação" ou "Reprovado".
m = float(input("Insira sua primeira nota: "))
m1 = float(input("Insira sua segunda nota: "))
media = (m + m1)/2
print(media)
if media >= 7:
  print("Parabéns!!! Você está aprovado!")
elif media >= 5 and  media <= 6.9:
  print("Que pena, você está de recuperação!")
elif media < 5:
  print("Que pena, você está reprovado!")


#Programa que calcula o imposto de renda.
renda = float(input("Informe sua renda anual: R$ "))
a_b = 0.15
a_a = 0.50
if renda <= 50000:
    imposto = renda * a_b
elif renda >= 50000:
    imposto = renda * a_a
print(f"O valor do imposto de renda a ser pago é de R$ {imposto:.2f}")


#programa que classifica o produto entre Barato, Moderado ou Caro.
p = float(input("Insira o preço do seu produto: "))
if p <100:
  print("Este produto está barato!")
elif p>=100 and p <=500:
  print("Este produto está com o preço moderado!")
elif p> 500:
  print("Este produto está caro!")

p1 = float(input("Insira o preço do seu produto: "))
if p1 <100:
  print("Este produto está barato!")
elif p1>=100 and p1 <=500:
  print("Este produto está com o preço moderado!")
elif p1> 500:
  print("Este produto está caro!")

p2 = float(input("Insira o preço do seu produto: "))
if p2 <100:
  print("Este produto está barato!")
elif p2>=100 and p2 <=500:
  print("Este produto está com o preço moderado!")
elif p2> 500:
  print("Este produto está caro!")


#programa avaliador de crédito.
renda = float(input("Insira a sua renda: "))
if renda < 3000:
  print("Crédito negado!")
elif renda >=3000 and renda <=7000:
  print("Crédito parcialmente aprovado!")
elif renda > 7000:
  print("Crédito aprovado!")
