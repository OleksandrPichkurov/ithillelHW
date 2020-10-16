def users_input_number():
    number = int(input('Enter number: '))
    return number

def users_input_operation(): 
    operation = input('Enter operation (+, -, *, /, **): ')
    valid_operators = ['+', '-', '*', '/', '**'] 
    for _ in valid_operators:
        if operation in valid_operators:
            return operation
        else:   
            print("This is invalid operation")
            break

def calculation(first_num, second_num, users_input_operation):

    if users_input_operation == '+':
        return first_num + second_num
    elif users_input_operation == '-':
        return first_num - second_num
    elif users_input_operation == '*':
        return first_num * second_num
    elif users_input_operation == '**':
        return first_num ** second_num
    elif users_input_operation == '/':
        try:
            return first_num / second_num
        except ZeroDivisionError:
            print('division by 0 is not possible!')

            