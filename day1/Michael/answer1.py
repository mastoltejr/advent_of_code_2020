def twoSum():
    options = {}
    with open('input1.txt', 'r') as numbers:
        for number in numbers:
            number = int(number)
            if options.get(number, None) is not None:
                print('{}+{}=2020'.format(number, options[number]))
                print('{}*{}={}'.format(number,
                                        options[number], number*options[number]))
                return (number, options[number])
            options[2020-number] = number


def threeSum():
    options = {}
    number_options = []
    with open('input1.txt', 'r') as numbers:
        for number in numbers:
            number = int(number)
            if options.get(number, None) is not None:
                (num1, num2) = options[number]
                print('{}+{}+{}=2020'.format(num1, num2, number))
                print('{}*{}*{}={}'.format(num1, num2, number, num1*num2*number))
                return (num1, num2, number)
            elif len(number_options) > 0:
                for num1 in number_options:
                    options[2020-number-num1] = (num1, number)
            number_options.append(number)


twoSum()
threeSum()
