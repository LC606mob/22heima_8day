#一.函数的多返回值
def get_user_info():
    name = "Alice"
    age = 30
    is_active = True
    return name, age, is_active # 返回元组

a = get_user_info()
print(a)
print(type(a))
# 解包返回值
user_name, user_age, active_status = get_user_info()
print(f"姓名: {user_name}, 年龄: {user_age}, 活跃状态: {active_status}")
# 输出: 姓名: Alice, 年龄: 30, 活跃状态: True


#二.函数参数传递的四种方式
# 1.位置参数
def register_user(name, country, phone):
    print(f"注册用户: {name} ({country}), 电话: {phone}")

register_user("Bob", "US", "123-4567")  # 顺序必须严格对应
# 错误示例：register_user("US", "Bob", "123-4567") → 参数错位

# 2.关键字参数
def register_user(name, country, phone):
    print(f"注册用户: {name} ({country}), 电话: {phone}")

register_user(country="CN", phone="123-4567", name="Charlie")
# 可打乱顺序，但位置参数必须在关键字参数前
register_user("David", phone="555-1234", country="UK")

#3.缺省参数(默认参数)
def connect_db(host, port=3306, timeout=10):
    print(f"连接数据库: {host}:{port},超时: {timeout}")

connect_db("192.168.1.1")# 使用默认port和timeout
connect_db("10.0.0.1",port=5432)# 覆盖port

#4.不定长参数
#接收任意数量位置参数(*arg → 元组)
def calculate_sum(*numbers):
    print(f"参数的类型是{type(numbers)},内容是{numbers}")
    return sum(numbers)

a = calculate_sum(1,2,3)
print(a)
#接收任意数量关键字参数(**kwargs → 字典)
def build_profile(**details):
    print(f"details参数的类型是{type(details)},内容是{details}")
    for key, value in details.items():
        print(f"{key}: {value}")

build_profile(name="Eve", age=25, occupation="Engineer")


#三.函数作为参数传递
def process_data(data, algorithm):
    return algorithm(data)

def square_list(nums):
    return [ x** 2 for x in nums]

numbers = [1, 2, 3, 4]
result = process_data(numbers, square_list)
print(result)  # 输出: [1, 4, 9, 16]

# 直接传递lambda函数
result = process_data(numbers, lambda x: [n * 2 for n in x])
print(result)  # 输出: [2, 4, 6, 8]


#四. Lambda匿名函数
# 单行简单逻辑
add = lambda x, y: x + y
print(add(5, 3))  # 输出: 8

# 作为参数传递
points = [(1, 2), (3, 1), (5, 4)]
sorted_points = sorted(points, key=lambda point: point[1])  # 按y坐标排序
print(sorted_points)  # 输出: [(3, 1), (1, 2), (5, 4)]






























