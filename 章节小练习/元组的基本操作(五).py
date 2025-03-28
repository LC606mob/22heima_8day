tuple = ('周杰伦',11,['football','music'])

#查询其年龄所在位置
print(tuple.index(11))
#查询学生姓名
print(tuple[0])
#删除学生爱好中的football
del tuple[2][0]
print(tuple)
#增加爱好:coding到爱好list里面
tuple[2].append("coding")
print(tuple)











