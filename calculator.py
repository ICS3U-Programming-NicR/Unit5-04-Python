#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 9 2022
# calculates the average percentage


def calculate(operator, first_number, second_number):
    match operator:
        case "+":
            answer = first_number + second_number
        case "-":
            answer = first_number - second_number
        case "/":
            answer = first_number / second_number
        case "*":
            answer = first_number * second_number
        case "%":
            answer = first_number % second_number
    return answer


def main():
    while True:
        # define variables
        operator = input(
            "Enter the operator you want to calculate(+,-,/,*,%): "
        ).strip()
        first_number_str = input(
            "Enter the first number you want to calculate: "
        ).strip()
        second_number_str = input(
            "Enter the second number you want to calculate: "
        ).strip()
        if (
            operator == "+"
            or operator == "-"
            or operator == "/"
            or operator == "*"
            or operator == "%"
            or operator == "%"
        ):
            try:
                first_number = int(first_number_str)
                second_number = int(second_number_str)
                answer = calculate(operator, first_number, second_number)
                print(
                    "{} {} {} = {}".format(
                        first_number, operator, second_number, answer
                    )
                )
            except:
                print("you have to input an integer in for the numbers")
        else:
            print("You have to input a valid operator")
        # try again loop
        input("If you would like to calculate again just press <enter>: ")


if __name__ == "__main__":
    main()
