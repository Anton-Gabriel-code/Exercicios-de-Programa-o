def intro():
  print("Fazendo nossa priemiro função")
intro()

def calcular_imposto(valor):
  if valor < 1000:
     imposto = valor * 0,1
  elif valor < 2000:
      imposto = valor * 0.2
  else:
       imposto = valor * 0.3
  return imposto
calcular_imposto(4000)
