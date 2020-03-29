# 2020-03-29 11:01:28
def test_yield():
    for i in range(5):
        yield i

ty = test_yield()
# print(ty)

"""
函数中可以有多个 yield
以追加的形式形成生成器
~
存入是从上到下依次存入
取出是从先到后依次取出
即“从上到下”、“先入先出”
"""

def test_yield_2():
    for i in range(5):
        yield i

    for j in ['a', 'b', 'c']:
        yield j

ty2 = test_yield_2()
# print(ty2)

# for t in ty2:
#     print(type(t), t)

def test_yield_3():
    for i in range(5):
        yield i

    for j in ['a', 'b', 'c']:
        yield j

    for m in ['我', '爱', '你', '啊']:
        yield m

ty3 = test_yield_3()

for t in ty3:
    print(type(t), t)


