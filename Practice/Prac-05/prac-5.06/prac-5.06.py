ages = [1, 3, 5, 16, 55, 65]

for age in ages:
    if age < 2:
        print("Your age is: %02d, you are a baby." % age)
    elif age < 4:
        print("Your age is: %02d, you are a toddler." % age)
    elif age < 13:
        print("Your age is: %02d, you are a kid." % age)
    elif age < 20:
        print("Your age is: %02d, you are a teenager." % age)
    elif age < 65:
        print("Your age is: %02d, you are an adult." % age)
    else:
        print("Your age is: %02d, you are an elder." % age)
