num = 1
name = 'Mike'
is_ok =True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 형변환

is_ok = name

print(is_ok, type(is_ok))
print(num, type(num))

# 3.6 버전 부터는 아래 기능이 지원되나 안씀
num2:int = 2
print(num2,type(num2))