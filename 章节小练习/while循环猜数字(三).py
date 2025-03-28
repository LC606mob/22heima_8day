# 设置一个范围1-100的随机整数变量，
# 通过while循环，配合input语句，判断输入的数字是否等于随机数
# 无限次机会，直到猜中为止
# 每一次猜不中，会提示大了或小了
# 猜完数字后，提示猜了几次

# 提示：
# 无限次机会，终止条件不适合用数字累加来判断
    # 可以考虑布尔类型本身(True or False)
# 需要提示几次猜中，就需要提供数字累加功能
# 随机数可以使用：import random


#获取范围在1-100的数字
import random
num = random.randint(1,100)

#定义一个变量,提示一共猜测了几次
count = 0

#通过一个布尔类型的变量,做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字:"))
    count += 1
    if guess_num == num:
        print("恭喜你,猜对了!")
        #设置False就是循环终止的条件
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

print(f"你一共猜测了{count}次")








