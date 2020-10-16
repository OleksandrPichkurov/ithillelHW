from functionality import users_input_number, users_input_operation


s1 = str(users_input_number())
s2 = str(users_input_operation())
s3 = str(users_input_number())
s4 = str(users_input_operation())
s5 = str(users_input_number())

str_result = s1+s2+s3+s4+s5
print(str_result)
print(f'Your result : {eval(str_result)}')

