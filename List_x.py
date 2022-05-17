
def run():
    # list_numbers =[]

    # for i in range(1,101):
    #     if i %3 !=0:
    #         list_numbers.append(i**2)
    # print(list_numbers)

    squares =[i**2 for i in range(1, 101) if i%3!=0]
    print (squares)

if __name__ == '__main__':
    run()