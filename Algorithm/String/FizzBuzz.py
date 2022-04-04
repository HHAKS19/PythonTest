def fizzbuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz' # result = 'Fizz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    # else: ,result = input, return result
    return input

print(fizzbuzz(30))
'''
for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0 ):
        print('FizzBuzz')
    elif ....
    else:
        print(i)
'''