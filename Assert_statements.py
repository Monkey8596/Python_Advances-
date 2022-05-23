
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0: 
            divisors.append(i)
    return divisors


def run():
        num = input('Write a number: ')
        assert int(num) > 0, 'Only positive numbers'
        assert num.isnumeric(), 'It has to be a number'
        print(divisors(int (num)))
        print('Program finished')



if __name__ == '__main__':
    run()