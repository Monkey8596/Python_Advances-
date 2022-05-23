
def palindrome(string):
    assert len(string) > 0, 'Is not allow empty space'
    return string == string[::-1]

print(palindrome(''))