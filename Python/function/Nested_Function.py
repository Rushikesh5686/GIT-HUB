# a=[10,20]
# b= a
# b+=[30,40]
# print(a)

# def x(values):
#     values[0]=1
# v=[2,3,4]
# x(v)
# print(v)

def outer_fun(x):
    def inner_fun(y):
        return y*x
    return inner_fun
my_fun=outer_fun(2)
print(my_fun(3))
