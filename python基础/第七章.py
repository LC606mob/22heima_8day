#文件的操作步骤:打开文件 读写文件 关闭文件
#一.文件读取操作
# 打开文件    open(文件路径\文件名, 模式, 编码)
f = open('data.txt', 'r',encoding='utf-8')
# 文件读取操作
with open("data.txt", "r", encoding="UTF-8") as f:
    print(f.read(10))  # 读取前10字节
    print(f.readlines())  # 读取剩余所有行（列表形式）
    f.seek(0)  # 重置指针到文件开头
    print(f.readline())  # 读取第一行
# 自动关闭文件
with open("data.txt", "r", encoding="UTF-8") as f:
    content = f.read()
# 退出with块后自动关闭文件


#二.文件写入与追加
#w :覆盖写入（文件不存在则创建）          a:追加写入（文件不存在则创建）
with open("output.txt", "w", encoding="UTF-8") as f:
    f.write("hello world\n")
    f.flush

with open("logs.txt","a", encoding="UTF-8") as f:
    f.write("2023-10-01:system started\n")
# 写入内容先暂存内存缓冲区，调用 flush() 或 close() 时写入磁盘。

