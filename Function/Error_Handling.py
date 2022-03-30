class ZeroCubeError(Exception):
    '''0 can\'t be passed as a cube.'''

class Cube():
    def __init__(self,num):
        num = int(num)
        if num != 0:
            self.qub = num **3
        else:
            # pass
            raise ZeroCubeError

try:
    num = Cube(input('Number: '))
except ZeroCubeError:
    print(ZeroCubeError.__doc__)
except ValueError:
    print('Check the value')
except:
    print('Something went wrong.Check it again.')
else:
    print('Cube Value: ', num.qub )
finally:
    print('Execution complete')


        

# def Cube(n):
#     '''This function cubes numbers'''
#     print(n**3)

# print(help(Cube))


