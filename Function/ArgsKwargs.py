def StudentInfo(*args,**kwargs): #args and kwargs are just convention names
    print(args)                 #args = positional argu, kw= keyword argu(dictionary)
    print(kwargs)
StudentInfo('Mary', 'John', name='Mary', age =11) 
StudentInfo('Mary',{'name': 'Mary', 'age': 11}) # all go to args

course = ['Python','Java']
student = {'name':'John','age': 12}
StudentInfo(course,student)
StudentInfo(*course, **student)  #star for respective arg