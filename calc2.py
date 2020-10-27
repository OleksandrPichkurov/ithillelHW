from functionality import users_input_number, users_input_operation, calculation

count = 0

user_count = float(input('How much number you want to canculate? max(1-3): '))

if user_count == 1:
    first_num = users_input_number()
    second_num = users_input_number()
    operator = users_input_operation()
    result = calculation(first_num, second_num, operator)
    print(f'Your result {result}: ')
    
if user_count == 2:
    first_num = users_input_number()
    second_num = users_input_number()
    operator = users_input_operation()
    third_num = users_input_number()
    operator2 = users_input_operation()
    result = (calculation(calculation(first_num, second_num, operator),third_num, operator2))
    print(f'Your result {result}: ')
    
if  user_count == 3:
    first_num = users_input_number()
    second_num = users_input_number()
    operator = users_input_operation()
    third_num = users_input_number()
    operator2 = users_input_operation()
    fouth_number = users_input_number()
    operator3 = users_input_operation()
    resultop = (calculation(calculation(calculation(first_num, second_num, operator), third_num, operator2), fouth_number, operator3))
    print(f'Your result {resultop}: ')
    

