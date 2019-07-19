'''
carts = [['toothpaste','shoes','bread'],['pencils','erasers','notebook'],['meat','fruit','vegetables']]
# OU
person1 = ['toothpaste','shoes','bread']
person2 = ['pencils','erasers','notebook']
person3 = ['meat','fruit','vegetables']
carts = [person1,person2,person3]
'''
'''
person1 cart
person2 cart
person3 cart
'''

#print(carts[0][0])      # row       column

'''
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
'''

# Make a 2-D List with the following values

'''
0   1  2  3  4
5   6  7  8  9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
'''
task_list = []

for row in range(0,25,5):
    inner_list = []
    for column in range(row,row+5):
        inner_list.append(column)
    task_list.append(inner_list)

for row in task_list:
    #print(row)
    pass


# Use list comprehension to make the same 2-d List

new_list = [[column for column in range(row,row+5)]for row in range(0,25,5)]           # [ value which is to be added -- loop ]

for row in new_list:
    print(row)

