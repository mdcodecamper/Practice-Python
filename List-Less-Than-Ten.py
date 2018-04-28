if __name__ == '__main__':
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    new_numbers = []
    new_list = []

    for num in numbers:
        if num <= 10:
            new_numbers.append(num)

    print(new_numbers)

    # Extras
    check = int(input("Please Enter the number: "))

    for num in numbers:
        if num <= check:
            new_list.append(num)

    print(new_list)
