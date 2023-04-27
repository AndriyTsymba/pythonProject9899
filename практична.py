def average(*args):
    return sum(args) / len(args)
print(average(1,2,3,4,5,6,7,8,))
#2
def max_length(*args):
    max_len = 0
    for arg in args:
        if len(arg) > max_len:
            max_len = len(arg)
    return max_len
print(max_length("hfgfdyf","twtehdg",))
#3
def auws(*args):
    a = " ".join(args)
    print(a)
auws("appel","banana","dog","hellow world")
#4
people = [("Nikita",15),("Glebus",45),("Vlad",1)]
def create_dict(*args):
    name_age ={}
    if args:
        for name,age in args:
            name_age[name] = age

            return name_age
print(create_dict(people))