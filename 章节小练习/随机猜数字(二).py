#   案例需求:定义一个数字(1~10,随机产生),通过3次判断来猜出来数字
#   案例要求:
# 1.数字随机产生,范围:1~10
# 2.有3次机会猜测数字,通过3层嵌套判断实现
# 3.每次猜不中,会提示大了或者小了

import random
num = random.randint(1,10)

guess_num = int(input("请输入你猜测的数字:"))
if guess_num == num:
    print("恭喜你,第一次就猜对了!")
else:
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")

    guess_num = int(input("请输入你猜测的数字:"))
    if guess_num == num:
        print("恭喜,猜对了!")
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

        guess_num = int(input("最后一次猜数字:"))
        if guess_num == num:
            print("恭喜,最后一次猜对了!")
        else:
            print("三次机会用完了,给你机会你也不中用啊!!")
