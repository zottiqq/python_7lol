number = int(input('Введите число от 1 до 100 '))
if number>100 or number<1:
    print('error')
elif number%3==0:
    print('Fizz')
elif number%5==0:
    print('Buzz')
elif number%3==0 and number%5==0:
    print('FizzBuzz')