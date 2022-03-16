
def is_prime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            


def app():
    num = int(input('Write a number: '))
    result = is_prime(num)

    if result is True:
        print('The number is prime!!')
    else:
        print('The number is not prime!!')


if __name__ == '__main__':
    app()
