# 1.可迭代对象
# 以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list，tuple，dict，set，str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代队象：Iterable

# 2.判断是否可以迭代
from collections import Iterable
print(isinstance([], Iterable)) #列表是不是Iterable的实例
print(isinstance(100, Iterable))

# 3.迭代器
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator
print(isinstance([], Iterator))
print(isinstance((x for x in range(10)), Iterator))

# 4.iter()函数
# 生成器都是Iterator对象，但是list，dict，str虽然是Iterable，却不是Iterator。
# 把list，dict，str等Iterable变成Iterator可以使用iter()函数：

print(isinstance(iter([]), Iterator))

# 迭代器仅仅只是一个地址，比可迭代对象省内存


