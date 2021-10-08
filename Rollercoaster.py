print('Welcome to the rollercoaster!')
height = int(input('Whats your hight in cm? '))
bill = 0

if height >= 120:
    print('U can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('Child tickets are $5.')
    elif age <= 18:
        bill = 7
        print('Teenager tickets are $7.')
    elif age >= 45 and age <= 55:
        bill = 0
        print('Everything is going to be ok. Have a ride on us!')
    else:
        bill = 12
        print('Adult tickets are $12.')

    wants_photo = input('Do you want a photo? Y or N. ')
    if wants_photo == 'Y':
        bill += 3

    print(f'Your final bill {bill}')

else:
    print('Sorry, u have to grow taller before u can ride.')