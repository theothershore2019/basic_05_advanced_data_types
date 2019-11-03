# 1. 判断空白字符
space_str = " "

print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
# 1> 都不能判断小数
num_str = "1"
# num_str = "1.1"
# num_str = "\u00b2"
# num_str = "一千零一"

print(num_str)

# 2> 只能判断阿拉伯数字
print(num_str.isdecimal())

# 3> 可以判断（1）、\u00b2字符串
print(num_str.isdigit())

# 4> 可以判断中文数字
print(num_str.isnumeric())
