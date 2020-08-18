# quantity = 10

# x = 0
# y = 1
# print(x)
# print(y)

# for i in range(quantity):
#     print(x + y)
#     x, y = y, x+y


# a = [1, 0, 0, 2]
# b = a[::-1]
# print(b)

# q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# p = q[4:8]

# print(p)
# # print(q)

# text = ['tobi', 'tola', 'tosin']
# txt = text[-1]

# print(txt)

students_scores = [

    ["atha",
     [
         ["m", 30],
         ["e", 30]
     ],
     [
         ["singing", "50%"],
         ["cooking", "50%"]
     ]
     ],

    ["bolu",
     [
         ["m", 30],
         ["e", 30]
     ],
     [
         ["playing", "20%"],
         ["jogging", "65%"]
     ]
     ],

    ["seun",
     [
         ["m", 30],
         ["e", 30]
     ],
     [
         ["driving", "85%"],
         ["browsing", "130%"]
     ]
     ]

]


seun_hobby_one = students_scores[2][2][0][1]
seun_hobby_one_score = int(seun_hobby_one[:-1])
# print(seun_hobby_one_score)

seun_hobby_two = students_scores[2][2][1][1]
seun_hobby_two_score = int(seun_hobby_two[:-1])
# print(seun_hobby_two_score)

if seun_hobby_one_score > seun_hobby_two_score:
    print(f"Driving: {seun_hobby_one_score} ")
else:
    print(f"Browsing: {seun_hobby_two_score} ")
