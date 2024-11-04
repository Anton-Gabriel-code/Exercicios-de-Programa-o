pontos = int(input("Insira sua pontuação: "))
if pontos < 1000:
  print("Você é iniciante!")
elif pontos >= 1000 and pontos <= 5000:
  print("BOA! Você é intermediário!")
elif pontos > 5000:
  print("PARABÉNS!!! Você é avançado!")
