#一.列表
#1.基础操作
#定义列表
fruits = ['apple', 'banana', 'orange', 88, True]
print(f"原始列表{fruits}")  # 输出: ['apple', 'banana', 'cherry', 88, True]

#索引访问
print(fruits[1])# 输出: banana
print(fruits[-2])# 输出: 88

#修改元素
fruits[0] = "cherry"
print(f"修改后{fruits}")

#插入元素
fruits.insert(2, "grape")
print(f"插入后{fruits}")

#删除元素
fruits = ['apple', 'banana', 'orange', 88, True]
fruits.pop(3)    # 删除索引3的元素  fruits.pop(3)有返回值,为删除的元素
print(f"列表.pop(下标) 删除后{fruits}")

fruits = ['apple', 'banana', 'orange', 88, True]
del fruits[3]
print(f"del列表[下标] 删除后{fruits}")

#删除某元素在列表中的第一个匹配项
fruits = ['apple', 'banana', 'orange','apple', 88, True]#重新定义一下
fruits.remove('apple')
print(f"列表.remove(元素) 删除后{fruits}")

#查找某元素下标
fruits = ['apple', 'banana', 'orange', 88, True]#重新定义一下
a = fruits.index('apple')
print(f"查找出\"apple\"的下标为{a}")

#清空列表内容
fruits = ['apple', 'banana', 'orange', 88, True]#重新定义一下
fruits.clear()
print(f"清空后:{fruits}")

#统计某元素在列表内的数量
fruits = ['apple', 'banana', 'orange','apple', 88, True]#重新定义一下
ap = fruits.count('apple')
ba = fruits.count('banana')
print(f"列表.count(元素) \"apple\"在列表内的数量:{ap} \n \"banana\"在列表内的数量:{ba}")

#统计列表内有多少个元素
fruits = ['apple', 'banana', 'orange', 88, True]
c = len(fruits)
print("列表里有%d个元素"%c)

#列表的遍历
# while循环遍历
i = 0
list = ["a", "b", "c"]
while i <len(list):
    print(list[i],end="")
    i += 1
print()

# for循环遍历
for i in list:
    print(i,end="")
print()

#列表推导式
squares = [x**2 for x in range(5)]
print(squares)  # 输出: [0, 1, 4, 9, 16]



#二.元组
# 1.定义元组
colors = ("red", "green", "blue")
print(colors)
print(type(colors))

# 尝试修改会报错
# colors[0] = "yellow"  # TypeError

# 嵌套元组
matrix = ((1,2), (3,4))
print(matrix[1][0]) # 输出: 3

# 定义单个元素的元组，后面必须加一个逗号，不然它的类型不是tuple而是其他
tuple_1 = (1)
print(tuple_1)# 输出1(int型)
print(type(tuple_1)) #输出<class 'int'>
#正确应该是:
tuple_1 = (1,)
print(tuple_1)# 输出(1,)
print(type(tuple_1)) #输出<class 'tuple'>

#2.元组操作
#查询某个元素的下标:元组.index(元素)
colors = ("red", "green", "blue")
index_green =colors.index("green")  #返回元组内第一个该元素的下标
print(f"\"green\"的下标是:{index_green}")

#统计某个数据在当前元组中出现的次数
colors = ("red","blue", "green", "blue")
count_blue = colors.count("blue")
print(f"\"blue\"在元组中出现了:{count_blue}次")

#统计元组内的元素个数
colors = ("red","blue", "green", "blue")
len_colors = len(colors)
print(f"元组里面有{len_colors}个元素")

#3.元组的遍历
#while遍历
colors = ("red", "green", "blue")
index = 0
while index < len(colors):
    print(f"while:元组的元素有:{colors[index]}")
    index += 1

#for遍历
colors = ("red", "green", "blue")
for  element in colors:
    print(f"for:元组的元素有:{element}")


#三.字符串
# 1.字符串下标
#通过下标索引取值
my_str = "itheima and itcast"
#通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是: {value},取下标为-16的元素。值是: {value2}")

#2.字符串常用操作
#查找子串位置(index)
sentence = "python是人工智能的首选语言"
position = sentence.index("人工")
print(f"子串'人工'的起始下标是{position}")

#替换内容(replace)  语法:字符串.replace(字符串1，字符串2)
sentence = "python是人工智能的首选语言"
new_sentence = sentence.replace("python", "java")# 原字符串不变
print(f"替换后的内容是:{new_sentence}")

#分割字符串
# 正确用法：按空格分割
data = "apple,banana,grape"
items = data.split(",")  # 使用逗号分割
print(f"分割结果: {items}")  # 输出: ['apple', 'banana', 'grape']  是一个列表对象
# # 错误用法：split参数不能为空字符串
# try:
#     data.split("")
# except ValueError as e:
#     print(f"错误信息: {e}")  # 输出: empty separator

#去除首尾字符(字符串规整)
# 去除空格
user_input = "      user@qq.com"
clean_input = user_input.strip()
print(f"清理后的邮箱是{clean_input}")
# 去除指定字符
text = "!!!警告!!!系统异常!!!"
clean_text = text.strip("!")# 只去首尾
print(f"清理后的内容是{clean_text}")# 输出: 警告!!!系统异常

#统计与长度
data = "apple,banana,grape"
count = data.count("apple")
length = len(data)
print(f"'data'中'apple'出现了{count}次,'data'的长度为{length}")

#字符串的遍历
#for遍历
for char in "Hello":
    print(char, end=" ")  # 输出: H e l l o
#while遍历
text = "Python"
i = 0
while i < len(text):
    print(text[i], end=" ")  # 输出: P y t h o n
    i += 1
print()
#3.字符串比较规则
#   按位比较（ASCII码）
print("apple" > "banana")   # 输出: False（a < b）
print("Cat" < "cat")        # 输出: True（C的ASCII码为67，c为99）
print("Hello" < "HelloWorld")  # 输出: True（长度短的小）

# #   实际应用：排序字符串列表
# words = ["apple", "Banana", "cherry", "apricot"]
# sorted_words = sorted(words, key=lambda x: x.lower())  # 不区分大小写排序
# print(sorted_words)  # 输出: ['apple', 'apricot', 'Banana', 'cherry']




#四.序列
#定义：内容连续、有序，可使用下标索引的一类数据容器
# 常见类型：列表（`list`）、元组（`tuple`）、字符串（`str`）

#切片操作
#基本语法:  序列[起始下标:结束下标:步长]

#   正向切片示例
nums = [0, 1, 2, 3, 4, 5, 6]

# 取索引1到3（包含1,不包含4）
print(nums[1:4])    # 输出: [1, 2, 3]
# 从头取到索引4，步长2
print(nums[:5:2])   # 输出: [0, 2, 4]
# 从索引2取到末尾
print(nums[2:])     # 输出: [2, 3, 4, 5, 6]

#   反向切片示例
text = "0123456"

# 反转字符串
print(text[::-1])    # 输出: "6543210"
# 从索引5反向取到索引3（不包含3）
print(text[5:2:-1])  # 输出: "543"



#五.集合
# 1.集合的定义
fruits = {"apple", "banana", "orange", "apple"} #自动去重
print(fruits)      #输出是无序的(每次运行集合里面元素的排序都不一样)
#空集合( 必须用set() )
empty_set = set()

#2.集合的基本操作
# 添加元素  集合.add(元素)
fruits = {"apple", "banana", "orange", "apple"} #自动去重
fruits.add("grape")
print(fruits)

# 移除元素
# 集合.remove(元素) ---> （存在则删除，否则报错）
fruits = {"apple", "banana", "orange", "apple"} #自动去重
fruits.remove("banana")
print(fruits)
# 安全删除（存在则删除，否则无操作）
fruits.discard("mango")

#随机弹出元素
fruits = {"apple", "banana", "orange", "apple"} #自动去重
popped = fruits.pop()
print(f"弹出元素:{popped},剩余集合:{fruits}")

#清空集合
fruits = {"apple", "banana", "orange", "apple"} #自动去重
fruits.clear()
print(fruits)              #输出:set()    ---即空集合

#统计集合个数
fruits = {"apple", "banana", "orange", "apple"} #自动去重
length = len(fruits)
print(f"集合个数为{length}")

#   集合运算
#取两个集合的差集(Difference)   语法∶集合1.difference(集合2)
set_a = {1, 2, 3}
set_b = {2, 3, 4}
#差集运算(返回新集合)
diff = set_a.difference(set_b)  # 或 set_a - set_b
print(diff)  # 输出: {1}

#交集和并集
# 交集（共同元素）
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersection = set_a.intersection(set_b)  # 或 set_a & set_b
print(intersection)  # 输出: {2, 3}

# 并集（所有元素）
set_a = {1, 2, 3}
set_b = {2, 3, 4}
union = set_a.union(set_b)  # 或 set_a | set_b
print(union)  # 输出: {1, 2, 3, 4}

# 消除两个集合的差集    集合1.difference_update(集合2)
# 功能: 对比集合1和集合2，在集合1内，删除和集合2相同的元素。
# 结果: 集合1被修改，集合2不变
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a.difference_update(set_b)
print(set_a)
print(set_b)

#3.集合遍历
#集合不支持下标索引，不能用while循环，可以用于for循环
fruits = {"apple", "banana", "orange", "apple"} #自动去重
for fruit in fruits:
    print(fruit, end=" ")

#4.集合的应用场景
# 快速去重
names = ["Alice", "Bob", "Alice", "Charlie"]
unique_names = set(names)
print(unique_names)  # 输出: {'Charlie', 'Alice', 'Bob'}

# 成员关系检查
valid_users = {"admin", "user1", "user2"}
username = "user3"
if username in valid_users:
    print("访问权限通过")
else:
    print("无权限")  # 输出: 无权限

# 数据对比
# 找出新增和删除的用户
old_users = {"user1", "user2", "user3"}
new_users = {"user2", "user3", "user4"}

added = new_users - old_users  # 新增用户
removed = old_users - new_users  # 删除用户
print(f"新增: {added}, 移除: {removed}")  # 输出: 新增: {'user4'}, 移除: {'user1'}



#六.字典
#1.字典的定义
# 定义字典(键值对结构)
student_scores = {
    "Alice":85,
    "Bob": 92,
    "Charlie": 78,
}
print(student_scores)   #输出:  {'Alice': 85, 'Bob': 92, 'Charlie': 78}
print(type(student_scores))    #输出: <class 'dict'>
#空字典
empty_dict = {}
empty_dict_v2 = dict()
print(empty_dict)
print(empty_dict_v2)    #输出:    {}

#键的不可变性 # 键必须是不可变类型（如字符串、数字、元组）
valid_dict = {
    "name": "Alice",
    101: "Room101",
    (1, 2): "坐标"
}
# # 错误示例（列表不可作为键）
# invalid_dict = {
#     ["temp"] : "value"  # TypeError
# }

# 2.字典的操作
#   增删改查
#新增键值对  语法:字典[Key]= Valuem
student_scores = {
    "Alice":85,
    "Bob": 92,
    "Charlie": 78,
}
student_scores["David"] = 88
print(student_scores)

#修改值    字典[Key] = value
student_scores["Charlie"] = 82
print(student_scores)

#删除键值对
del student_scores["Bob"]# 直接删除（若不存在会报错）
print(student_scores)
popped_scores = student_scores.pop("Alice")# 安全删除并返回值
print(f"Alice的分数: {popped_scores},删除之后的字典是: {student_scores}")

#避免KeyError的查值方式
student_scores = {
    "Alice":85,
    "Bob": 92,
    "Charlie": 78,
}
#使用get方法(推荐)
score_1 = student_scores.get("Alice")
print(f"Alice的分数: {score_1}")
score_2 = student_scores.get("Eve")#键不存在默认返回值是None
print(f"Eve的分数: {score_2}")
score_3 = student_scores.get("Eve",0)# 键不存在返回默认值0
print(f"Eve的分数: {score_3}")
# 检查键是否存在
if "Bob" in student_scores:
    print("Bob存在")

#清空元素
student_scores = {
    "Alice":85,
    "Bob": 92,
    "Charlie": 78,
}
student_scores.clear()
print(f"字典被清空了{student_scores}")

#获取全部的key或者value   字典.keys()  字典.values()
student_scores = {
    "Alice":85,
    "Bob": 92,
    "Charlie": 78,
}
print(student_scores.keys())    #输出:    dict_keys(['Alice', 'Bob', 'Charlie'])
print(student_scores.values())  #输出:    dict_values([85, 92, 78])
#遍历字典
student_scores = {
    "Alice":85,
    "Bob": 92,
    "Charlie": 78,
}
#   仅遍历键或值
#遍历所有键
for name in student_scores.keys():
    print(name)
#遍历所有值
for score in student_scores.values():
    print(score)

# 遍历键值对
for name,score in student_scores.items():
    print(f"{name}: {score}分")

#嵌套字典与复杂操作
#多层嵌套访问
employees = {
    "Alice":{
        "department": "HR",
        "salary": 5000,
    },
    "Bob":{
        "department": "IT",
        "salary": 6000,
    }
}
employees["Alice"]["salary"] = 5500# 修改嵌套值
print(employees)
# 安全访问嵌套键
bonus = employees.get("Charlie", {}).get("bonus", 0)
print(f"Charlie的奖金: {bonus}")  # 输出: 0

#合并多个字典
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}# 后者覆盖前者重复键
print(merged)# 输出: {'a': 1, 'b': 3, 'c': 4}




















