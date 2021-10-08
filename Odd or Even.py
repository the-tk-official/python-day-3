number = int(input('Which number do u want to check? '))

if number % 2 == 0:
    print('This is an even number')
elif number % 2 != 0:
    print('This is an odd number')
else:
    print('Incorrect input!')