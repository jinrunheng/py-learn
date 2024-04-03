a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

# 内存地址
print(hex(id(a)))
print(hex(id(b)))

c = {1, 2, 3}
d = {2, 1, 3}
print(c == d)  # True

e = (1, 2, 3)
f = (1, 2, 3)
print(e == f)  # True
print(e is f)  # True

print('----------')
## isinstance 用法
s = 'abc'
print(isinstance(s, str))
print(isinstance(s, (str, int, float)))
print(isinstance(s, (int, float)))
