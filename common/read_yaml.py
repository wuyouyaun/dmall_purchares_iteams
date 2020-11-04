import yaml

# with open("demo.yml","r",encoding="utf-8") as fp:
#     t=fp.read()
# print(t)
# print(type(t))
#
# #读取的是字符串，转换成dict
#
# a=yaml.load(t)
# print(a)




with open("suppliers.yml","r",encoding="utf-8") as fp:
    b= fp.read()
# print(b)
# print(type(b))
y=yaml.load(b,Loader=yaml.FullLoader)
print(y)
# x=yaml.load(b,Loader=yaml.FullLoader)
# print(x)

# fs=x['login_business']['username']
# print(fs)
# a=[2,3,4,6,22,3,22,5]
# list = set(a)
# print(list)

# 一个文件只能是一个结构，一种对象类型








