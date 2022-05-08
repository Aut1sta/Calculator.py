print('Hi, this is a calculator program. Write the operation and it will be solved')

def getOperator(expression, listOfOperators):
    for i in range(len(expression)):
        for j in range(len(listOfOperators)):
            if listOfOperators[j] == expression[i]:
                return expression[i]

def getValues(expression, listOfOperators):
    for i in range(len(expression)):
        for j in range(len(listOfOperators)):
            if listOfOperators[j] == expression[i]:
                return expression.replace(expression[i], ' ').split(' ')

def sum(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 -n2

def mul(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def operations(argument, n1, n2):
    switcher = {
        '+': sum(n1, n2),
        '-': minus(n1, n2),
        'x': mul(n1, n2),
        '/': divide(n1, n2)
    }
    return switcher.get(argument)

def main():
    expression = ''
    listOperators = ['+','-','x','/']
    result = 0
    while expression != 'exit':
        expression = input('What is the operation? ')
        if expression != 'exit':

            valueA = getValues(expression, listOperators)[0]
            valueB = getValues(expression, listOperators)[1]
            operator = getOperator(expression, listOperators)
            if valueA != '':
                result += operations(operator, int(valueA), int(valueB)) 
            else:
                result = operations(operator, result, int(valueB)) 
            print(round(result))
    else:
        print('Thank you for using our calculator software')

main()

#aaaaaaaaaaaaaaaaaaaa