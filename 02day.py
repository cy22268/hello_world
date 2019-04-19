# 定义变量，并使用print函数打印出来
my_name = '刘德华'
print(my_name)

'''
 整数运算
'''
# 加法
add = 3 + 4
print('3+4的值是{}'.format(add))

# 减法
sub = 10 - 8
print('10-8的值是{}'.format(sub))

# 乘法
multi = 23 * 3
print('23*3的值是{}'.format(multi))

# 除法
div = 10 / 2
print('10/2的值是{}'.format(div))

# 取模，返回除法的余数
delivery = 7 % 3
print('7%3的值是{}'.format(delivery))

# 取整除，返回商的整数
round_number = 7 // 3
print('7//3的值是{}'.format(round_number))

# 幂运算--x的几次方
power = 7 ** 3
print('7**3的值是{}'.format(power))

'''
  浮点数运算
'''
# 加法
add = 0.2 + 0.1
print('0.2+0.1的值是{}'.format(add))

# python3.6以上版本为了减少{},可以使用f'的方法
com = 'Complex'
comp = 'complicated'

# 3.6以下的用法
print('\n 3.6以下的用法')
print('{}is better than {}'.format(com, comp))

# 3.6以上的用法
print('\n 3.6以上用法')
print(f'{com} is better than {comp}')

# 减法
sub = 10.9 - 8.1
print('10.9 - 8.1 的值是{}'.format(sub))

# 乘法
multi = 0.1 * 3
print(f'0.1*3={multi}')

# 除法
div = 10.0 / 2.0
print(f'10.0/2.0={div}')

# 取模
delivery = 7 % 4.3
print(f'7%4.3={delivery}')

# 取整除
round_number = 7 // 4.3
print(f'7//4.3={round_number}')

# 幂运算
power = 7 ** 2.0
print(f'7**2.0={power}')

'''
布尔类型
'''
a = True
print(a and 'a=T' or 'a=F')

'''
  字符串
'''
# 转意字符串(\n)
command = 'Let\'s go!'
print('\n 使用转移字符输出 ： ', command)

# 添加空白 \n 表示换行 \t 表示制表符，把文字空两格输出
# 制表符可以组合使用
print("欢迎来到python 实战圈,\n")
print('\t 你想要学习 PYTHON 的哪方面内容，请留言 ')

# 链接字符串,使用加号 +
log_1_str = 'The error is a bug.'
log_2_str = ' We should fix it.'
log_str = log_1_str + log_2_str
print('\n 拼接后的字符串就是：', log_str)

# 字符串大小写转换
welcome = "Hello,welcome to python"
# 将每个单词的首字母大写
print('\n 每个单词首字母大写', welcome.title())
# 段落的首字母大写
print('\n 段落的首字母大写', welcome.capitalize())
# 所有字母小写
print('\n 所有字母小写', welcome.lower())
# 所有字母大写
print('\n 所有字母大写', welcome.upper())
# 大写转小写，小写转大写
print('\n 大写转小写，小写转大写', welcome.swapcase())
# 判断字符串是否全部为数字或英文，符合就返回True，不符合就返回False，如果里面包含有符号或者空格之类的特殊字符也会返
# 回False。
print('\n 判断字符串是否全部为数字或英文', welcome.isalnum())
# 判断字符串是否全部为整数
print('\n 判断字符串是否全部为整数', welcome.isdigit())

# 字符串分割
string_example = 'Now is better than never'
# 分割
print('分割字符串', string_example.split())
# 按照某一个字母分割
print('按照指定字母分割字符串', string_example.split('n'))
# 去掉换行符，以换行符分割成列表
# splitlines() 以换行为分割
print('以换行符为分割', '1+2\n+3+4'.splitlines())

# 删除两边的空白
love_python = ' Hello, Python Practical Circle '
# 去除字符串两端的空白
print('去除字符串两端的空白', love_python.strip())
# 去除字符串右侧的空白
print('去除字符串右侧的空白', love_python.rstrip())
# 去除字符串左侧的空白
print('去除字符串左侧的空白', love_python.lstrip())

# 字符串切片 slice
letter = 'abcdefghijklmnopqrstuvwxyz'
print(letter[-3:])

# 字符串编码
# encode('utf-8')

'''
各个数据类型转换
'''
print('\n 各个数值类型的转换')
number = 100

# number 的数据类型是 整型，用int 表示
print('number 的数据类型是：')
print(type(number))

# 将整数转化为浮点数
float_number = float(number)
print('\nfloat_number 的数据类型是:')
print(type(float_number))

# 将整型转化为字符串数
print('\nnumber 转化为字符串类型')
str_number = str(number)
print('str_number 的数据类型是:')
print(type(str_number))

# 将字符串转换为整型int()或者浮点数float()
print('\nstr_number 转化为数字类型')
int_str_number = int(str_number)
float_str_number = float(str_number)
print('int_str_number 的数据类型是：')
print(type(int_str_number))
print('float_str_number 的数据类型是:')
print(type(float_str_number))

name = 'python实战圈,希望圈子越来越好'
print('我参加的是{}'.format(name))
