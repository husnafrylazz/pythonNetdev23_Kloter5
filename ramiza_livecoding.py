#Angka yang merupakan kelipatan 3 dengan kata "Fizz".
#Angka yang merupakan kelipatan 5 dengan kata "Buzz".
#ngka yang merupakan kelipatan baik 3 maupun 5 dengan kata "FizzBuzz".
#Angka yang bukan kelipatan 3 atau 5 dengan angka itu sendiri.

angka = int(input('Masukkan angka: '))

for i in range(1, angka+1):
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)