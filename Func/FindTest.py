print('Module Start')

def find_str(search_lst,target):
    for ind, value in enumerate(search_lst):
        if value == target:
            return ind

    return False
