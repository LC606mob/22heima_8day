#一.面向对象
# 1.类与对象基础
#类定义
class Student:
    name = None
    age = None

#对象实例化
stu = Student()
stu.name = "张三"
stu.age = 18
print(f"{stu.name}今年{stu.age}岁")

#初识对象
# 1．设计一个类（类比生活中:设计一张登记表)
class Student:
    name = None
    gender = None
    age = None
#2．创建一个对象（类比生活中:打印一张登记表)
stu_1 = Student()
#3.对象属性进行赋值（类比生活中:填写表单)
stu_1.name = "张三"
stu_1.gender = "男"
stu_1.age = 18
#4．获取对象中记录的信息
print(stu_1.name,stu_1.gender,stu_1.age)



# 2.成员方法与self关键字
class BankAccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"存入{amount}元,当前余额{self.balance}")

account = BankAccount()
account.deposit(1000)   # 存入1000元，当前余额：1000

"""
演示面向对象类中的成员方法定义和使用
"""

#定义一个带有成员方法的类
class Student:
    name = None
    gender = None
    age = None
    def say_hi(self):
        print(f"hi~~,我是{self.name}")
    def say_hi2(self,msg):
        print(f"hi~~,我是{self.name},{msg}")
stu_1 = Student()
stu_1.name = "张三"
stu_1.gender = "男"
stu_1.age = 18
stu_1.say_hi()
stu_2 = Student()
stu_2.name = "李四"
stu_2.say_hi()
stu_2.say_hi2("真不错小伙子！！")



# 3.类和对象
"""
演示类和对象的关系，即面向对象的编程套路（思想)
"""
#设计一个闹钟类
class Clock:
    id = None #序列号
    price = None #价格
    def ring(self):
       import winsound
       winsound.Beep(2000,1000)
                    #频率      响铃的持续时间

#构建2个闹钟对象并让其工作(可以构建多个对象)
clock_1 = Clock()
clock_1.id = "00232"
clock_1.price = 19.9
print(f"闹钟的序列号是{clock_1.id}，闹钟的价格是{clock_1.price}")
clock_1.ring()




# 4.构造方法
class MobilePhone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

iphone = MobilePhone("Apple", 8999)
print(f"{iphone.brand}手机售价为{iphone.price}元")

"""
演示类的构造方法
"""
#演示使用构造方法对成员变量进行赋值
# #构造方法的名称: __init__
class Student:
    """
    可省略
    name = None
    age = None
    tel = None
    """
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")
stu = Student("张三",18,"198")
print(stu.name,stu.age,stu.tel)



# 5.魔术方法
#字符串方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student类对象,name:{self.name},age:{self.age}"
stu = Student("张三", 18)
print(stu)

#lt方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __lt__(self,other):
        return self.age < other.age
stu1 = Student("张三",18)
stu2 = Student("李四",19)
print(stu1 < stu2)

#le方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __le__(self, other):
        return self.age<other.age
stu1 = Student("张三",20)
stu2 = Student("李四",19)
stu3 = Student("王五",19)
print(stu2<=stu3)

#eq方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age<other.age
stu1 = Student("张三",20)
stu2 = Student("李四",19)
stu3 = Student("王五",19)
print(stu2==stu3)



# 6.封装与私有成员
class SmartWatch:
    __battery = 100

    def check_battery(self):
        print(f"剩余电量:{self.__battery}%")

    def use(self,hours):
        if self.__battery >= hours * 10:
            self.__battery -= hours * 10
        else:
            print("电量不足")

watch = SmartWatch()
watch.use(2)# 实际使用：__battery = 80
watch.check_battery()# 剩余电量：80%

"""
演示面向对象封装思想中私有成员的使用
"""
#定义一个类，内含私有成员变量和私有成员方法
class Phone:
    __current_voltage = 1 #当前手机运行电压
    def __keep_single_core(self):
        print("让CPU单核运行")
    def call_by_5G(self):
        if self.__current_voltage >=1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足无法使用5G，已切换为单核")
phone = Phone()
# phone.__keep_single_core()
phone.call_by_5G()

#练习题
class Phone:
    __is_5G_enable = True
    def __check_5G(self):
        if self.__is_5G_enable:
            print("5G开启")
        else:
            print("5G关闭,使用4G网络")
    def call_by_5G(self):
        self.__check_5G()
        print("正在通话中")
phone = Phone()
phone.call_by_5G()


# 7.继承
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪"

class Cat(Animal):
    def speak(self):
        return "喵~"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())
animal_sound(Dog())


"""
演示面向对象:继承的基础语法
"""


#演示单继承
class Phone:
    IMEI = None #序列号
    producer = "iphone"
    def call_by_4g(self):
        print("4g通话")
class Phone2023(Phone):
    faceId ="1000" #面部识别id
    def call_by_5g(self):
        print("5g通话")
phone = Phone2023()
phone.call_by_4g()
print(phone.producer)
#演示多继承
class  NFCReader:
    nfc_type = "第五代"
    producer = "iphone"
    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")
class RemoteControl:
    rc_type = "红外遥控器"
    def control(self):
        print("红外遥控开启了")

class Myphone(Phone,NFCReader,RemoteControl):
    pass
print("++++++++++++++")
my_phone = Myphone()
my_phone.call_by_4g()
my_phone.read_card()
my_phone.write_card()
my_phone.control()



# 8.继承中的复写
class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类,复写父类成员
class Myphone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启CPU单核模式,确保通话的时候省电")
        #方式1
        # print(f"父类的产商是:{Phone.producer}")#使用成员变量:父类名.成员变量
        # Phone.call_by_5g(self)#使用成员方法:父类名.成员方法(self)
        #方式2
        print(f"父类的产商是:{super().producer}")#使用成员变量: super().成员变量
        super().call_by_5g()#使用成员方法: super().成员方法()
        print("关闭CPU单核模式,确保性能")


phone = Myphone()
phone.call_by_5g()
print(phone.producer)



# 9.变量的类型注解
from typing import Union  # 导入Union类型

# 1️⃣ 定义一个商品类
class Product:
    def __init__(self, name: str, price: float):
        self.name = name   # 商品名称（字符串类型）
        self.price = price # 价格（浮点型）

# 2️⃣ 定义展示商品信息的函数
def show_info(item: Union[Product, str]) -> str:
    # 参数item可以是Product对象或字符串 ✨
    if isinstance(item, Product):
        # 如果是Product对象   isinstance() :运行时动态检查对象类型
        return f"{item.name} 售价：¥{item.price}"
    else:
        # 如果是其他类型（这里主要是字符串）
        return "无效商品"

# 3️⃣ 使用演示
print(show_info(Product("鼠标", 199.0)))  # 创建Product对象并传入



"""
演示变量的类型注解
"""
import json
import random

#基础数据类型注解
var_1:int = 10
var_2:str = "itheima"
var_3:bool = True
#类对象类型注解
class Student:
    pass
stu:Student = Student()
#基础容器类型注解
my_list:list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"itcasst":666}
#容器类型详细注解
my_list:list[int] = [1,2,3]
my_tuple:tuple[int,str,bool](1,"itheima",True)
my_dict:dict[str,int] = {"itheima":666}
#在注释中进行类型注解
var_4 = random.randint(1,10) #type:int
var_5 = json.loads('{"name:zhangsan"}')  #type:dict[str,str]
def func():
    return 10
var_6 = func()  #type:int
#类型注解的限制
var_7:int = "itheima"
var_8:str = 1


# 10.函数的类型注解
"""
演示对两数(方法)进行类型注解
"""
#对形参进行类型注解
def add(a:int , b:int):
    return a + b
add(1, 2)
#对返回值进行类型注解
def func(data:list) -> list:
    return data



# 11.Union类型
"""
演示Union联合类型注解
"""
#使用Union类型，必须先导包
from typing import Union
my_list:list[Union[int,str]] = [1, 2, "itcast", "itheima"]

def func(data: Union[int,str]) -> Union[int, str]:
    pass
func()



# 12.多态
class Animal:
    def speak(self): pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

make_noise(Dog())
make_noise(Cat())

# 抽象类示例
class AC:
    def cool_wind(self):
        pass

class MideaAC(AC):
    def cool_wind(self):
        print("美的制冷")

def make_cool(ac:AC):
    ac.cool_wind()

make_cool(MideaAC())

"""
演示面向对象的多态特性以及抽象类(接口）的使用
"""
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    """制造噪音，需要传入Animal对象"""
    animal.speak()
#演示多态，使用2个子类对象来调用函数
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

print("-----------------")
#演示抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_l_r(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的制冷")
    def hot_wind(self):
        print("美的制热")
    def swing_l_r(self):
        print("美的左右摆风")
class Gree_AC(AC):
    def cool_wind(self):
        print("格力制冷")
    def hot_wind(self):
        print("格力制热")
    def swing_l_r(self):
        print("格力左右摆风")
def make_cool(ac:AC):
    ac.cool_wind()
gree = Gree_AC()
meidea = Midea_AC()
make_cool(gree)
make_cool(meidea)






