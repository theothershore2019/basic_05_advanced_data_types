# 格式化字符串后面的‘（）’本质上就是元组
print("%s 的年龄是 %d岁 身高是 %.2fm" % ("小明", 18, 1.75))

info_tuple = ("小明", 18, 1.75)

print("%s 的年龄是 %d岁 身高是 %.2fm" % info_tuple)

info_str = "%s 的年龄是 %d岁 身高是 %.2fm" % info_tuple

print(info_str)
