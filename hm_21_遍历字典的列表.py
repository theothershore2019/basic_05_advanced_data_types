students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]

# 在学员列表中搜索指定的姓名
# find_name = "阿土"
find_name = "张三"

for stu_dict in students:

    print(stu_dict)

    # 判断当前遍历的字典中姓名是否为find_name
    if stu_dict["name"] == find_name:

        print("找到了 %s" % find_name)

        # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break

else:

    # 如果没有发现要搜索的目标，还需要一个统一的提示，
    print("没有找到 %s" % find_name)

print("循环结束")
