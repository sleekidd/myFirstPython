'''
numbers = [50, 10, 100, 99, 80, 80, 30]
numbers_deviation = []
numbers_deviation_squared = []

n = len(numbers)

mean = sum(numbers) / n

for number in numbers:

    numbers_deviation.append(number - mean)
    # print(number - mean)

    numbers_deviation_squared.append((number - mean)**2)

print(numbers_deviation_squared)

'''
# file_name = "loops/buhari.txt"
# file = open(file_name, "r", errors='ignore')

# data = file.read()
# # print(data)

# lines = data.replace("-", " ").splitlines()
# # print(lines)
# longest_word_in_buhari = ''

# for line in lines:

#     words = line.split(" ")
#     # print(words)

#     for word in words:
#         if len(word) > len(longest_word_in_buhari):
#             longest_word_in_buhari = word

# print(longest_word_in_buhari)

# file_name = "loops/obama.txt"
# file = open(file_name, "r", errors='ignore')

# data = file.read()
# # print(data)

# lines = data.replace("-", " ").splitlines()
# # print(lines)
# longest_word_in_obama = ''

# for line in lines:

#     words = line.split(" ")
#     # print(words)

#     for word in words:
#         if len(word) > len(longest_word_in_obama):
#             longest_word_in_obama = word

# print(longest_word_in_obama)


# longest_word = "Buhari" if len(longest_word_in_buhari) > len(
#     longest_word_in_obama) else "Obama"

# print(longest_word)

# start = 0
# end = 100000

# while True:
#     start += 1
#     print(start)
#     if start == end:
#         break

# file_name = "num_file.csv"
# file = open(file_name, "w")

# numbers = [50, 10, 100, 99, 80, 80, 30]

# file.write("Scores, Passed\n")
# for number in numbers:
#     file.write(f"{number}, {number >= 50} \n")
#     # file.write(str(number) + str(number) >= 50)

# numbers = [50, 10, 100, 99, 80, 80, 30]
# numbers_deviation = []
# numbers_deviation_squared = []

# n = len(numbers)

# mean = sum(numbers) / n

# for number in numbers:

#     numbers_deviation.append(number - mean)
#     # print(number - mean)

#     numbers_deviation_squared.append((number - mean)**2)

# print(numbers_deviation_squared)

# file.write("Score, x-x, x_xx")
# for number in numbers_deviation:
#     file.write(f"{number}, {number >= 50} \n")
