pontos = int(input("Insira sua pontuação: "))
if pontos < 1000:
  print("Você é iniciante!")
elif pontos >= 1000 and pontos <= 5000:
  print("BOA! Você é intermediário!")
elif pontos > 5000:
  print("PARABÉNS!!! Você é avançado!")


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



renda = float(input("Informe sua renda anual: R$ "))
a_b = 0.15
a_a = 0.50
if renda <= 50000:
    imposto = renda * a_b
elif renda >= 50000:
    imposto = renda * a_a
print(f"O valor do imposto de renda a ser pago é de R$ {imposto:.2f}")

p = float(input("Insira o preço do seu produto: "))
p1 = float(input("Insira o preço do seu produto: "))
p2 = float(input("Insira o preço do seu produto: "))
if p and p1 and p2 <100:
  print("Este produtos são baratos!")
elif p and p1 and p2 >=100 or p and p1 and p2 <=500:
  print("Este produtos estão com o preço moderado!")
elif p and p1 and p2 > 500:
  print("Este produtos são caros!")
