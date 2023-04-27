#теорія
def black_hole(*args):
    print(type(args))
    print(args)
    for agumente in args:
        print(agumente)
black_hole(234,"Earth","rusnya","time",673)
#2
def black_hole_named(**kwags):
    print(type(kwags))
    print(kwags)
    for agument in kwags:
        print(agument)
black_hole_named(name= "Gleb",planet= "Earth",number=5)
#3
def black_hole_named(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
black_hole_named(name= "Gleb",planet= "Earth",number=5)
#4
def black_hole_full(*args,**kwargs):
    if not args: #для перевірки наявності на іменнованих аргументів
        return 0
    for agumente in args:
        print(agumente)
        for key, value in kwargs.items():
            print(key, value)
black_hole_full(234,"gfytdytysd","time",6776,name= "Gleb",planet= "Earth",number=5)
#5
def black_hole_full(var1,*args,varg2 = 2,**kwargs):
    if not args: #для перевірки наявності на іменнованих аргументів
        return 0
    for agumente in args:
        print(agumente)
        for key, value in kwargs.items():
            print(key, value)
black_hole_full(234,"gfytdytysd","time",65656,name= "Gleb",planet= "Earth",number=5)
#6
lst = [2,3,4]
dict={'n':1,"b":2,"n1":3}
def fun(var_1,var_2,var_3):
    print(var_1,var_2,var_3)
fun(*lst)
def fun_dict(n,b,n1):
    print(1,2,3)
fun_dict(**dict)
