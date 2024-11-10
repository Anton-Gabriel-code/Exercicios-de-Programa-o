number =int(input("Insira a quantidade de termos que você deseja ver: "))
n1 = 0
n2 = 1
print ("{}---{}". format(n1, n2), end = "")
count = 3
while count <= number:
  n3 = n1 + n2
  print ("---{}". format(n3), end ="")
  n1 = n2
  n2 = n3
  count += 1
print("\nFim da sequência!")
