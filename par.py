def get_number():
    return int(input("Enter a number positive: "))


def is_even(num):
    return num % 2 == 0


def show_result(result, num):
    if result:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


def main():

    num = get_number()
    show_result(is_even(num), num)


main()
