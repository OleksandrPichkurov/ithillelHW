from functionality import users_input_number, users_input_operation, calculation



try:
    first_num = users_input_number()
    second_num = users_input_number()
    operation = users_input_operation()
except ValueError:
    print('Something went wrong!')
else:
    result = calculation(first_num, second_num, operation)
    print(f'Result of {first_num} {operation} {second_num} = {result}')