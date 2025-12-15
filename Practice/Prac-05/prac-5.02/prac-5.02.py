str = 'Hello, World!'

if str == 'Hello, World!':
    print('True, the string is equal to Hello, World!')
else:
    print('False, the string is not equal to Hello, World!')

user = 'Admin'

if user.lower() == 'admin':
    print('True, the user lower is admin.')
else:
    print('False, the user lower is not admin.')

age = 18

if age == 18:
    print('True, the age is 18.')
else:
    print('False, the age is not 18.')

if age < 18:
    print('True, the age is less than 18.')
else:
    print('False, the age is not less than 18.')

if age <= 18:
    print('True, the age is less than or equal to 18.')
else:
    print('False, the age is not less than or equal to 18.')

if age > 18:
    print('True, the age is greater than 18.')
else:
    print('False, the age is not greater than 18.')

if age >= 18:
    print('True, the age is greater than or equal to 18.')
else:
    print('False, the age is not greater than or equal to 18.')

if age != 18:
    print('True, the age is not equal to 18.')
else:
    print('False, the age is equal to 18.')

age_01 = 18
age_02 = 21

if age_01 == 18 and age_02 == 21:
    print('True, the age_01 is 18 and the age_02 is 21.')
else:
    print('False, the age_01 is not 18 or the age_02 is not 21.')

if age_01 > 20 or age_02 < 42:
    print('True, the age_01 is greater than 20 or the age_02 is less than 42.')
else:
    print('False, the age_01 is not greater than 20 and the age_02 is not less than 42.')

cars = ['audi', 'bmw', 'subaru', 'toyota']
if 'bmw' in cars:
    print('True, bmw is in the list of cars.')
else:
    print('False, bmw is not in the list of cars.')

if 'audi' not in cars:
    print('True, audi is not in the list of cars.')
else:
    print('False, audi is in the list of cars.')

