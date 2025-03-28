#需要操作的文件:bill.txt
# 需要做的内容:
'''
读取文件
将文件写出到bill.txt.bak文件作为备份
同时,将文件内标记为"测试"的数据行丢弃
'''
"""
文件备份
"""
# 读取文件
fr = open("bill.txt","r",encoding="UTF-8")
# 写入文件
fw = open("bill.txt.bak","w",encoding="UTF-8")
# for循环读取文件
for line in fr:
    line.strip()
    # 判断内容，将满足的内容写出
    if line.split(",")[4] =="测试":
        continue #进入下一次循环
    # 将内容写出去
    fw.write(line)
    # 由于前面内容进行了strip()的操作，所以要手动的写出换行符
    fw.write("\n")
fr.close()
fw.close()