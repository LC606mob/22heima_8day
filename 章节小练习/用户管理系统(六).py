def create_user(name, role="guest", **extra_info):
    user = {"name": name, "role": role}
    user.update(extra_info)  # 合并额外信息
    return user

# 创建用户（使用默认角色和额外信息）
user1 = create_user("Alice", age=30, email="alice@example.com")
user2 = create_user("Bob", "admin", department="IT")

print(user1)
print(user2)



# 输出: {'name': 'Alice', 'role': 'guest', 'age': 30, 'email': 'alice@example.com'}
# 输出: {'name': 'Bob', 'role': 'admin', 'department': 'IT'}