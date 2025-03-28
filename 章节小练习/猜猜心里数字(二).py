#if-leif-else练习题

num = 5

if int(input("请猜一个数字:")) == num:
    print("恭喜你第一次就猜对了!")
elif int(input("猜错了,再来一次:")) == num:
    print("猜对了")
elif int(input("最后再猜一次:")) == num:
    print("恭喜你,最后一次猜对了!")
else:
    print("给你机会你也不中用啊!")









