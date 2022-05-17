
from functools import reduce

#Filter

my_list = [1,4,5,6,9,13,19,21]

odd= list(filter(lambda x:x%2 !=0, my_list ))

print(odd)

#Map

# second_list = [1,2,3,4,5]

# odd_2= [i**2 for i in second_list]
# print(odd_2)

my_second_list = [1,2,3,4,5]

second_odd= list(map(lambda x:x**2, my_second_list ))

print(second_odd)


#Reduce

third_list = [2,2,2,2,2]

all_multiplied = reduce(lambda a,b: a*b, third_list)
print(all_multiplied)
