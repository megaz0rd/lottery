from random import randint


def user_numbers():
    """Get 6 unique numbers from user

    Every input must be an int in in range(1, 50)

    :rtype list
    :return list of six integers
    """
    numbers = []
    tries = 0
    while tries != 6:
        try:
            number = int(input('Give your number: '))
            if number in range(1, 50):
                if number not in numbers:
                    numbers.append(number)
                    tries += 1
                else:
                    print(f'You picked {number} before. Choose another one!')
            else:
                print("You can choose only between 1-49.")
        except ValueError:
            print("Only numbers!")
        numbers.sort()

    return numbers


def lottery():
    """Pick 6 unique random numbers

    Use randint to make a list of 6 unique integers

    :rtype list
    :return list of six integers
    """
    drawing_list = []
    i = 0
    while i < 6:
        pick = randint(1, 50)
        if pick not in drawing_list:
            drawing_list.append(pick)
            i += 1
        drawing_list.sort()
    return drawing_list


def print_function(picks):
    """Format list of numbers

    Make list of integers into string

    :rtype str
    """
    return ", ".join(str(value) for value in picks)


def results():
    """Main function for results"""
    print("Choose six unique numbers between 1-49")

    user_picks = user_numbers()
    comp_picks = lottery()

    print(f"Your picks are: {print_function(user_picks)}")
    print(f"Today's lottery numbers are: {print_function(comp_picks)}")

    match = 0
    for number in user_picks:
        if number in comp_picks:
            match += 1

    print(f"You guessed {match} number(s)!")


if __name__ == '__main__':
    results()
