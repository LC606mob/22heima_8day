#全局变量初始化
balance = 10000
user_name = None

#函数定义
def show_menu():
    """显示主菜单"""
    print("\n====== ATM系统 ======")
    print("1. 查询余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 退出")
    return int(input("请输入选项(1-4):"))

def check_balance():
    """查询余额"""
    global balance
    print("当前余额为%.2f" % balance)

def deposit(amount):
    """存款操作"""
    global balance
    balance += amount
    print(f"成功存入 ¥{amount:.2f}，当前余额: ¥{balance:.2f}")

def withdraw(amount):
    """取款操作"""
    global balance
    if balance >= amount:
        balance -= amount
        print(f"成功取出 ¥{amount:.2f}，当前余额: ¥{balance:.2f}")
    else:
        print("余额不足")



#主程序逻辑
user_name = input("请输入你的用户名:")
print(f"欢迎你{user_name}!")

while True:
    choice = show_menu()
    if choice == 1:
        check_balance()
    elif choice == 2:
        amt = float(input("请输入你要存如的金额:"))
        deposit(amt)
    elif choice == 3:
        amt = float(input("请输入你要取出的金额:"))
        withdraw(amt)
    elif choice == 4:
        print("感谢使用,bye!")
        break
    else:
        print("无效选项,请重新输入")



