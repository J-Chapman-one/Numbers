#ask user to input three different numbers
#then ensure all numbers are in integer(i.e number format)
#carry out four caclulations as respective four variable names refer to and print the output from these four caclualtions

while True:
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter a different number: "))
        z = int(input("Enter a different number you have not entered before: "))

        total = x + y + z
        firstnum_minus_second = x - y
        third_num_times_first_num = x * z
        all_nums_dived_by_third_num = total / z

        print("Total of numbers:", total)
        print("First number minus second number:", firstnum_minus_second)
        print("Third number times first number:", third_num_times_first_num)
        print("All numbers divided by third number:", all_nums_dived_by_third_num)

        break  # Exit the loop if input is successful

    except ValueError:
        print("One or more inputs are not valid integers. Please re-enter in number format.")