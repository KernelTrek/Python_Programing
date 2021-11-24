# def add_num(a, b):
#     return a + b
#
# print('start')
# r = add_num(10, 20)
# print('end')
# print(r)
#
# # 함수의 전과 후에 기능을 넣고 싶을떄 사용.
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
#
# f = print_info(add_num)
# print(f(10, 20))

# 2번째, 간단하게 하는법
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
#
# @print_info
# def add_num(a, b):
#     return a + b
#
# f = add_num(10, 20)
# print(f)
#
# @print_info
# def sub_num(a, b):
#     return a - b
#
# f = sub_num(20, 10)
# print(f)

## 3번쨰
# 간단하게 하는법
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# 제일 처음 보고 싶은 대상을 위에 올린다.
@print_info
@print_more
def add_num(a, b):
    return a + b

f = add_num(10, 20)
print(f)