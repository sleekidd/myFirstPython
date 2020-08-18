# import datetime


# def get_timestamp():

#     time_now = datetime.datetime.now()

#     time_stamp = time_now.strftime("%a %b %d %I %M")
#     print(time_stamp)

#     return time_stamp


# # print(get_timestamp())

# # def word_count(string):
# #     tokens = string.split()
# #     n_tokens = len(tokens)
# #     print(n_tokens)

# #     return n_tokens


# def store_memory(memory, time_stamp, txt_len):

#     file = open(f"{time_stamp}-{txt_len}.txt", "w")

#     file.write(memory)
#     file.close()

#     return True


# def get_text_len(text):
#     return len(text)


# text = input("Please enter text: ")
# time_stamp = get_timestamp()
# store_memory(text, time_stamp, get_text_len(text))


word = list("alphabet")
numbers = list("12345678")

zipped_vals = zip(word, numbers)
print(next(zipped_vals))
print(list(zipped_vals))


def mini(x):
    return "A"+str(x)


def mini2(x): return "A"+str(x)


mapped_result = map(mini, numbers)
print(list(mapped_result))

mapped_result2 = map(mini2, numbers)
print(list(mapped_result2))
