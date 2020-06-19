str_input_string = '12121121112111121111121121121'
print(str_input_string)
lst_input_list = str_input_string.split('2')
print(lst_input_list)
i = ""
str_output_letter = ''
str_output_str = ''
print(range(len(lst_input_list)))
for i in range(len(lst_input_list)):
    print(i)
    if lst_input_list[i] == '1':
        str_output_letter = 'a'
    elif lst_input_list[i] == '11':
        str_output_letter = 'b'
    else:
        str_output_letter = ''
    str_output_str = str_output_str + str_output_letter
print(str_output_str)

# test push and merge

print ("First merge from qwerty 2 master")