

def read():
    numbers = []
    with open('./Files/Numbers.txt', 'r', encoding='utf-8' ) as f:
        for line in f:
            numbers.append( int (line))
        print (numbers)


def write():
    names = ['Ángel','Álvaro','Lina','Lala','Santiago','Diego']
    with open('./Files/Names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    write()


if __name__ == '__main__':
    run()