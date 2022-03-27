from main import Calculator

while True:
    print("""
______________________________________________________________________________
 Calculator: Enter 2 or more whole numbers separated by spaces.
        """)
    user_input = input(" Plz type in your calc: ")
    print("")
    if user_input.isnumeric():
        print('Not an integer')
        break
    elif type(user_input) == float:
        print('float, Not an integer')
        break
    user_input = user_input.strip().split()
    user_input = tuple(map(int, user_input))

    for index, _ in enumerate(user_input):
        temp_message = [x for x in [Calculator().factor(_) for _ in user_input]]
        print(f' Prime factors: {_}  = {temp_message[index]}')
    print("")
    temp_message = ' * '.join(str(x) for x in Calculator().prime_factorization_lcm(*user_input))
    print(f' The least common multiple: {temp_message} = {Calculator().lcm(*user_input)} ')
    temp_message = ' * '.join(str(x) for x in Calculator().prime_factorization_gcd(*user_input))
    print(f' The greatest common divisor: {temp_message} = {Calculator().gcd(*user_input)} \n ')

    further_calc = input(f" Do you want to make any further calc?:[y/n] ")

    if further_calc.lower()[0] == "y":
        continue
    else:
        break
