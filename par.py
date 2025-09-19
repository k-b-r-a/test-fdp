def get_number():
    return int(input("Enter a number positive: "))


def main():

    num = get_number()

    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


main()
