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

