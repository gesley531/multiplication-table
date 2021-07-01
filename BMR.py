
print('\nWe all need to eat well to maintain a healthy body,\n'
      'but have you ever wondered how much we should eat a day?\n'
      'To find out, fill in the fields below...')

g = str(input('\nFirst tell us your gender (M/W): ').upper())

if g == "M" or "MALE":
    w = float(input('\nPlease, inform your weight in Kg: '))
    h = float(input('Now inform your height in cm: '))
    a = int(input('finally, inform your age: '))
    calc = 66 + (13 * w) + (5.0 * h) - (6.8 * a)
    print(f'\nYou need to eat {calc:.0f}(Kcal) per day')

elif g == "W" or "WOMAN":
    w = float(input('\nPlease, inform your weight in Kg: '))
    h = float(input('Now inform your height in cm: '))
    a = int(input('finally, inform your age: '))
    calc = 665 + (9.6 * w) + (1.8 * h) - (4.7 * a)
    print(f'\nYou need to eat {calc:.0f}(Kcal) per day')

else:
    print('Please, restart and insert a valid gender...')
