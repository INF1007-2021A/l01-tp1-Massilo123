def fizzBuzz(n):
    if n%3==0 and n%5==0:
        resultat1 = "fizzbuzz"
        print(resultat1)
    elif n%3==0:
        resultat2 = "fizz"
        print(resultat2)
    elif n%5==0:
        resultat3 = "buzz"
        print(resultat3)
    else:
        resultat4 = "ce nombre n'est pas un multiple de 3 ou de 5"
        return resultat4

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
