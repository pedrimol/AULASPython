def main():
    num = int(input(" Numeros primos"))

    i = 2

    while num != i:
        if num % i == 0:
            break

        i += 1

    if num == i:
       print("O numero", num, " é primo")
    elif num == 1:
         print("O numero 1 não é primo")
    else:
        print("O numero", num, "não é primo porque e divisivel por", i)

 

    return 0
main()