# 列表相加
skills1 = ['月之降临', '月神冲刺']
skills2 = ['点燃', '虚弱']
skills = skills1 + skills2
print(skills)

# 列表乘法
skills3 = skills2 * 3
print(skills3)

# 元组
tuple1 = (1, 'haha', True)
print(tuple1[1])
print(tuple1[0:2])

# 单个元组表示必须在要在末尾加逗号
tuple2 = (1)
print(type(tuple2))  # int
tuple3 = (1,)
print(type(tuple3))  # tuple

# 切片
points = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(points[3:8])  # 输出: (4, 5, 6, 7, 8)
print(points[1::2])  # 输出: (2, 4, 6, 8, 10)，步长为2的切片
print(points[0:8:2])  # 输出: (1, 3, 5, 7) 0 ~ 8  前开后闭，步长为 2
print(points[::-2])  # 输出: (10, 8, 6, 4, 2)
