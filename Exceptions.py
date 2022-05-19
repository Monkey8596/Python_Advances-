

# word= input('Write a word: ')

# if word == word [::-1]:
#     try:
#         print(word(1))
#     except TypeError:
#         print('Only strings are acceptable')
    
# for string in word:
#     if word == word [::-1]:
#         try:
#             print(word(1))
#         except TypeError:
#             print('Only strings are acceptable')
        
#     else:
#         print(string)

# Try and Except 

# def palindrome(string):
#     return string == string[::-1]

# try:
#     print(palindrome(1))
# except TypeError:
#     print('Only strings are acceptable')


# Raise 

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError ('is empty')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindrome(''))
except TypeError:
    print('Only strings')



# Finally

try:
    f=open('archivo.txt')
finally:
    f.close()

