def fibonacci(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)
x = int(input(" Insira o número da sequência de Fibonacci que você deseja ver: "))
print(fibonacci(x))
