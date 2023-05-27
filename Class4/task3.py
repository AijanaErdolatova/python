list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in list_num:
#     if num % 2 == 0 and num != 0:
# print(num)


input_number = int(input("Please enter the number: "))
for num in list_num:
    print(f"{input_number} * {num} = {num * input_number}")
