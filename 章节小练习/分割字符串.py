str = "itheima itcast boxuegu"
#统计字符串内有多少个"it"字符
#将字符内的空格,全部替换为字符"|"
#按照"|"进行字符串分割,得到列表

count = str.count("it")
print(count)
str_1 = str.replace(" ", "|")
print(str_1)
str_2 = str.split("|")
print(str_2)



str = "itheima itcast boxuegu"
print(f"有{str.count('it')}个it字符")
new_str = str.replace(" ","|")
print(f"原来的字符串{str}，被替换后的字符串{new_str}")
list = str.split("|")
print(f"字符串{str}按照 | 分割后的结果为：{list}")