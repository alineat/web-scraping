import random


# Make a list of random values
our_list = []
for value in range(0,20):
    our_list.append(random.randint(0,100))

print(our_list)

# Making a list using list comprehension

new_list = [value for value in range(0,20)]     # [ value which is being inserted into my list -- for loop ]


new_list = [random.randint(0,100) for value in range(0,20)]

print(new_list)