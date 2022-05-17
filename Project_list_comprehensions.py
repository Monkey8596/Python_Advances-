
def run():

    list_of_numbers = [i for i in range(1, 100000) if i % 4 ==0 if i % 6 ==0 if i % 9 ==0]
    print(list_of_numbers)

if __name__ == '__main__':
    run()
    