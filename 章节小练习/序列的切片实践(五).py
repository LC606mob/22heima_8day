#有字符串:"万过薪月，员序程马黑来，nohtyP学"
#请使用学过的任何方式,得到"黑马程序员"
my_str = "万过薪月，员序程马黑来，nohtyP学"
my_str_1 = my_str[::-1]
my_str_2 = my_str_1[9:14:1]
print(my_str_1)
print(my_str_2)


my_str='万过薪月，员序程马黑来，nohtyP学'
start = my_str.index('员')
end = my_str.index("黑")
new_str = my_str[start:end+1:]
print(new_str[::-1])
#对比两段代码的输出语句
my_str='万过薪月，员序程马黑来，nohtyP学'
start = my_str.index('员')
end = my_str.index("黑")
print(my_str[start:end + 1:][::-1])
#通过字符串分隔
print(my_str.split("，")[1].replace("来","")[::-1])