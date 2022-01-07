
# 3-3
ways = ["bus", "subway", "car"]
message = "I would like to own a BMW "+ways[-1]+"!"
print(message)

# 修改列表元素
motors = ["honda", "yamaha", "suzuki"]
print(motors)

motors[0] = "ducati"  # 修改列表的值
print(motors)

motors = ["honda", "yamaha", "suzuki"]
print(motors)
motors.append("ducati")
print(motors)

motors_1 = []
motors_1.append("honda")
motors_1.append("yamaha")
motors_1.append("suzuki")

print(motors_1)
# 插入
motors_1.insert(0, "dacati")  # 插入在0之前
print(motors_1)

# 删除
del motors_1[0]
print(motors_1)
