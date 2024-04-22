#1. OOP: Static Class Attributes........................
# Static attribute use case: 

# class A: 
# # class attributes/static(class) attributes 
#     count = 0
#     def __init__ (self, id)-> None: 
#         self.id = id
#         A.count +=1

# if __name__=='__main__':
#     a1 = A(1)
#     a2 = A(2)
#     a3 = A(3)

    
#     print(f'Objects created: {A.count}')




# 2. Class Method............. 
# Метод в класа: 
# Декораторът променя функцията (@)

# class A:
#     @classmethod
#     def foo(cls, obj): 
#         # Проверяваме дали едното е равно на другото 
#         print(cls==obj)
#         print('Foo')

# print(A)
# # a1 = A()
# # a1.foo(a1)
# # A.foo(a1)


# Вариант 2 
# class A: 

#     def __init__(self, id, name)-> None: 
#         self.id= id
#         self.name = name 

#     @classmethod
#     def from_dict (cls, data):
#         return cls(data['id'], data['name'])


# a1 = A(id=1, name='a1')
# a2_data={'id':2, 'name':'a2'}
# a2 = A.from_dict(a2_data)

# print(a2.id)
