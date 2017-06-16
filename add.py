def add(a, b):
    return a + b

def get_number():
    while True:
        try:
            a = int(input('Please give an integer: '))
            return a
        except ValueError:
            print('Invalid input!')
            continue

def main():
    a = get_number()
    b = get_number()
    result = add(a, b)
    print(result)

main()
