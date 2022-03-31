lst = [1,2,7,23,38,55,62,88,99,102,122,135,204]

def EvenCheck(num):
    if num > 100 and num < 200:
        return True
    else:
        return False

filtered_lst = filter(EvenCheck,lst)
even_lst = []
for number in filtered_lst:
    even_lst.append(number)
print(even_lst)
