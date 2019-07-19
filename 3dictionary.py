#Lists as we saw are indexed by numbers or indexes, dictionaries are a data structure which are indexed by keys
#Keys can be anything, from strings to integers to objects

#syntax to declare an empty dictionary in python is





my_dict = {'school':'definition of school','coding':'definition of coding','python':'definition of python'}



'''

item1,item2,item3,....          a-z

Each item contains
key - value

item1
school -- key
definition of school -- value

item2
coding - key
definition of coding - value

item3
python - key
definition of python - value

'''




'''
Commonly used method :

--> items()


'''


for key,value in my_dict.items():
    #print(key,'    ',value)
    pass

my_dict[2] = 'the key is 2'

print(my_dict[2])
