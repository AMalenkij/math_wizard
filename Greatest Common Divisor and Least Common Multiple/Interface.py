from main import Calculator
while True:
    print("""
______________________________________________________________________________
Calculator: Enter 2 or more whole numbers separated by commas or spaces.
        """)
    user_input = input("Plz type in your calc: ")
    user_input = user_input.strip().split()
    user_input = tuple(map(int, user_input))

    massege = ' '.join(str(x) for x in user_input)
    print(f' {massege} ')
    massege = ' '.join(str(x) for x in [Calculator().factor(_) for _ in user_input])
    print(f' {massege}')
    massege = ' * '.join(str(x) for x in Calculator().prime_factorization_lcm(*user_input))
    print(f' {massege} = {Calculator().lcm(*user_input)} LCM: The least common multiple')
    massege = ' * '.join(str(x) for x in Calculator().prime_factorization_gcd(*user_input))
    print(f' {massege} = {Calculator().gcd(*user_input)} GCD: The greatest common divisor')

    further_calc = input(f" Do you want to make any further calc?: ")

    if further_calc.lower()[0] == "y":
        continue
    else:
        break
