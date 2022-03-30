data ={
        'Dad':'Soe Naing',
        'Mom':'AAK',
        'Son':'Tin Tote',
        'Daughter':'Tin Pyar'
    }
# data = ['dad','mom','gayson']
def Data():
    print(data)

def Add_Data(a):
    data.update(a)
    #if list, data.append(a)
    print(data)

# Data()
Add_Data({'daughter':'pweety'})