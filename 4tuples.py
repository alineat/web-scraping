#A tuple is a package containing different values

#Syntax

person = 'Samy',27,'brown'      # tuple             boxing

name,age,hair_color = person            # un boxing un packing


# Looping

for value in person:
    print(value)


# Nested tuples

person = 'Samy',('brown','black'),27
print(person[1])

# One important thing about a tuple is that it's immutable

person[0] = 'new name'
print(person)