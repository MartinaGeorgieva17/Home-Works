# OPP Examples...............

# 1.1.......................
# class A:
#     # class attribute
#     name ='A object'

#     # class method
#     def powerClass(x):
#         #  s =a1
#         # x=3
#         return x**2
    
#     # instance method 
#     def powerInstance(self,x):
#         # self=a1
#         print(f'id(self):{id(self)}')
#         return x**2


# # instatiating objects of class A
# a1 = A()
# a2 = A()

# a1.id=1
# a2.id=2



# print(a1.powerInstance(3))
# print(f'id(a1):{id(a1)}')


# show object attributes 
# print(a1.__dict__)
# print(a2.__dict__)


# read class attributes
# print(a1.name)
# print(a2.name)
# print(A.name)



# a2.foo = lambda x:x**2
# print(a2.foo(2))




# 2......................................
# Methods...................................


# Instance Method...................

# class A:
#     def instance_method(self):
#      #self = a1
#         print(self)


# a1 = A()
# a2=A()
# print(a1)
# print(a2)
# a1.instance_method()
# a2.instance_method() #object a1 , function instance_method



# 3..Examples ..................................

# class Person: 
#     def greet(self):
#         print("Hi there! i'm", self.name)

# # create some objects of class Person: 
# maria = Person()
# maria.name = 'Maria Popova'

# pesho = Person()
# pesho.name = 'Pesho'


# # call greet 
# maria.greet()
# pesho.greet()




# 4. ''Constuctor'' == __init__()method   ............................
# Дъндър Init ............................


# class A:
#     def __init__(self, id):
#         print('A constructor is called!')
#         self.id = id


# a1 = A(1)
# # a1.id = 1 - тук конструктора го прави, 
# # не се налага да го пишем, както в предния пример 
# a2 = A(2)

# print(a1.id)
# print(a2.id)




# 5.  Example __init__   ..........................


# class Person: 
#     def __init__(self, name):
#         self.name = name



#     def greet(self):
#         print("Hi there! i'm", self.name)


# # create some objects of class Person: 
# maria = Person('Maria Popova')


# pesho = Person('Pesho')


# # call greet 
# maria.greet()
# pesho.greet()



