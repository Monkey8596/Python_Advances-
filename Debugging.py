
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0: 
            divisors.append(i)
    return divisors


def run():

    try:
        num = int(input('Write a number: '))
        print(divisors(num))
        print('Program finished')
    except ValueError:
        print('Only numbers')



if __name__ == '__main__':
    run()