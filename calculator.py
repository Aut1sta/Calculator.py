print('Hi, this is a calculator program. Write the operation and it will be solved')

operation = input('What is the operation? ')
listOperators = ['+','-','x']

def getOperator(expression, listOfOperators):
    for i in range(len(expression)):
        for j in range(len(listOfOperators)):
            if listOfOperators[j] == expression[i]:
                return expression[i]

operator = getOperator(operation, listOperators)

def sum(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 -n2

def mul(n1, n2):
    return n1 * n2

def operations(argument):
    switcher = {
        '+': sum(2, 2),
        '-': minus(2, 2),
        'x': mul(2, 5),
    }
    return switcher.get(argument)

print(operations(operator))

def main():
    for i in range(1000):
        print(i)

if __name__ == '__main__':
    main()

# fazer um try cathc exception com o erro de n ter valor no valueA ou B
# criar switch com as operacoes e fazer um modo para guardar o ultimo valor e somalo com o proximo, tipo 1 + 1 = 2, 2 + x = y