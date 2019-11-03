hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2. 判断是否以指定字符结束
print(hello_str.endswith("World"))

# 3.查找指定字符串
# index 方法同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))
# index 方法如果指定的字符串不存在，会报错
# find 方法如果指定的字符串不存在，会返回 -1
print(hello_str.find("abc"))

# 替换字符串
# replace 方法会返回一个新的字符串，不会该变原有字符串的内容
print(hello_str.replace("world", "python"))

print(hello_str)
