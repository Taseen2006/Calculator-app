def main():
    print("Welcome to the calculator app!")
    while True:
        calculation = input("Enter your calculation starting with 2 numbers:")
        print(f'calulation is ' + calculation)
        splitted = calculation.split()
        print(splitted)
        input1 = int(splitted[0])
        input2 = int(splitted[2])
        if splitted[1] == "x":
            answer = input1 * input2
        elif splitted[1] == "+":
            answer = input1 + input2
        elif splitted[1] == "-":
            answer = input1 - input2
        elif splitted[1] == "/":
            answer = input1 / input2
        else:
            print("invalid operator")

        print("answer is: " + str(answer))
        resume = input("would you like to continue? Y or N: ")
        if resume == "N":
            break


main()
