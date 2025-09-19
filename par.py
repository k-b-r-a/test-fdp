def get_number():
    return int(input("Enter a number positive: "))


def is_even(num):
    return num % 2 == 0


def main():

    num = get_number()

    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


main()
