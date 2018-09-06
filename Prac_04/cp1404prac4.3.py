def main():
    numbers = []
    list_length = int(5)

    for counter in range(1, list_length + 1 ):
        number = float(input("Please enter the " + str(counter) + ":"))
        numbers.append(number)
    for counter in range (1, list_length +1):
        number = numbers[counter - 1]
        print(number)
        print(number[0])


main()