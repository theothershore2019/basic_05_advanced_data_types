# 要求：顺序并且居中对齐以下诗句
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:

    # print(poem_str.center(10))
    print("|%s|" % poem_str.center(10, "　"))
    # print("|%s|" % poem_str.ljust(10, "　"))
    # print("|%s|" % poem_str.rjust(10, "　"))

print()
print()

poem1 = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str1 in poem:

    # 先使用 strip 方法去除字符串中的空白字符
    # 在使用 center 方法居中显示文本
    print("|%s|" % poem_str1.strip().center(10, "　"))
