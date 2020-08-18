# def count_down(num):
#     if num == 0:
#         return num
#     print(num)
#     return count_down(num-1)


# count_down(100)


previous_number = 0
numbers = 20, 60, 90, 103, 109, 120

for number in numbers:
    print(number - previous_number)
    previous_number = number
