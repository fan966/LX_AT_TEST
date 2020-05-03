# -*-coding:utf-8-*-
import re


# 特殊字符集
# 语法	说明	模式示例	匹配
# \d	匹配任意一个数字字符，等价于[0-9]	a\db	a1b
# \D	匹配任意一个非数字字符，等价于[^0-9]	a\Db	aAb
# \s	匹配任意一个空白字符，等价于[ \t\n\r\f\v]	a\sb	a b
# \S	匹配任意一个非空白字符，等价于[^ \t\n\r\f\v]	a\Sb	aAb
# \w	匹配任意一个 alphanumeric character，等价于[a-zA-Z0-9_]	a\wb	azb或aZb或a1b或a_b
# \W	匹配任意一个 non-alphanumeric character，等价于[^a-zA-Z0-9_]	a\Wb	a-b或a b

# 2.1 基本模式
# 语法	说明	模式示例	匹配
# 普通字符	普通的文本值代表自身，用于匹配非特殊字符	ab	ab
# .	匹配除换行符\n以外的任意一个字符。如果要匹配多行文本，
# 可以指定re.DOTALL标志位，或者(?:.|\n)*表示匹配.或\n，
# 且作为一个非捕获组，再指定*表示0个或多个前面的非捕获组
# ab.	匹配abc或abC，不匹配ab，因为b后面一定要有一个字符

# \	转义字符，比如要匹配点号.本身，需要转义它\.，
# 如果不转义，.将有上一行所示的特殊含义	ab\.	匹配ab.com，不匹配abc

# []	匹配中括号内的一个字符<br />1. 中括号内的字符可以全部列出，如[abc]表示匹配字符a或b或c<br />2. 也可以使用-表示范围，
# 如[a-z]表示匹配所以小写字母中的任意一个字符<br />3. 本文后续要介绍的如*、+等特殊字符在中括号内将失去特殊含义，
# 如[*+()]表示匹配字符*或+或(或)<br />4. 本文后续要介绍的特殊字符集如\d、\w等也可以放入此中括号内，继续保持特殊含义<br />5.
# 如果中括号内的字符序列前面有一个^，表示不匹配中括号内的任何一个字符，如[^0-9]表示不匹配数字，a[^0-9]c不匹配a1c，但会匹配abc<br />6.
# 要匹配字符]，可以转义它，或者把它放在中括号内的首位，如a[()[\]{}]c或a[]()[{}]c都可以匹配到a]c	a[0-9]b	a1b或a2b

# 语法	       说明	                                            模式示例        	匹配
# prev *	匹配0个或多个 prev，尽可能多地匹配，贪婪模式，等价于{0,}	ab*	        a或ab或abb或abbb，注意是匹配字符a后面跟0个或多个字符b
# prev *?	匹配0个或多个 prev，尽可能少地匹配，非贪婪模式	            ab*?	   a，非贪婪模式下匹配0个字符b
# prev +	匹配1个或多个 prev，尽可能多地匹配，贪婪模式，等价于{1,}	ab+	        ab或abb或abbb
# prev +?	匹配1个或多个 prev，尽可能少地匹配，非贪婪模式	            ab+?	    ab，非贪婪模式下匹配1个字符b
# prev ?	匹配0个或1个 prev，尽可能多地匹配，贪婪模式，等价于{0,1}	ab?	        a或ab
# prev ??	匹配0个或1个 prev，尽可能少地匹配，非贪婪模式	            ab??	    a，非贪婪模式下匹配0个字符b
# prev {m}	匹配m个连续的 prev	                                    a{3}	    aaa
# prev {m,n}	匹配m到n个连续的 prev ，尽可能多地匹配，贪婪模式。n可选，如果不指定，则表示m到无穷多个连续的 prev	a{3,5}	aaa或aaaa或aaaaa
# prev {m,n}?	匹配m到n个连续的 prev ，尽可能少地匹配，非贪婪模式	a{3,5}?	aaa
# 可以在*或+或?的后面再添加一个?，此时表示非贪婪模式匹配，Python中的正则表达式默认是贪婪模式匹配，它会在满足整个表达式要求的前提下，
# 尽可能多地去匹配字符，具体效果见后面的示例

# re.match()函数
#str1 = 'this my test'
#m = re.match('this',str1) # re.match()函数用于查看字符串是不是以正则模式开头。匹配失败返回None，匹配成功则返回匹配的对象
# print(m) # <re.Match object; span=(0, 4), match='this'>
# print(m.group())# 返回起始位置匹配的字符 this
# print(m.span()) # span() 返回匹配的坐标起始元组(0, 4)
# 只做一次匹配可以re.match()函数，但要多次匹配可以先编译正则表达式，在重复使用
#str2 = '1tisajdrrr2Msada'
# p = re.compile('[0-9]+') #[a-z]表示匹配任意一个小写字母 ‘+’ 则表示匹配一个或多个小写字母
# temp = p.match(str2) # p 此时 p 是预编译后的正则模式，它也有match等方法，只是参数不同，不需要再传入正则模式
# print(temp)
# print(temp.group())
# print(temp.span())

#search()方法   如果字符串中有多个地方与正则表达式匹配的话，search()方法返回第一次匹配到的结果
#str3 = 'wor ihfds word is  ijijij  is'
#p = re.compile('[a-z]+')  # [a-z]表示匹配任意一个小写字母 ‘+’ 则表示匹配一个或多个小写字母
# temp = p.search(str3)
# print(temp)
# print(temp.group())
# print(temp.span())
#str4 = 'http://csdqthcweb.lx901.com/?1588086998801'
#p = re.compile('Index/[0-9].*')
#print(p.search(str4))
# print(p.search(str4).group())
# print(p.search(str4).span())

# findall() 如果要查找字符串中所有的匹配项，可以使用findall()
# text = 'Today is 11/27/2012. PyCon starts 1/13/2013.'
# p1 = re.compile(r'\d+/\d+/\d+') # \d 任意数字 等价[0-9]    \d+ 指匹配一个或多个任意数字
# print(p1.search(text).group())
# print(p1.search(text))# <re.Match object; span=(9, 19), match='11/27/2012'>
# print(p1.search(text).group()) # 11/27/2012
# print(p1.search(text).span()) # (9, 19)
# print(p1.search(text).start()) # 9
# list1 = p1.findall(text)
# print(list1) # ['11/27/2012', '3/13/2013']
# print(list1[0]) # 11/27/2012
# print(list1[1]) # 3/13/2013

# finditer() 查找字符串中所有的匹配项，返回是一个迭代器，可以循环取值后用group（）来打印值
# list2 = p1.finditer(text)
# print(list2) # <callable_iterator object at 0x0000025D89EDDE08>
# for i  in list2:
#     print(i.group())
    # 打印结果
    # 11/27/2012
    # 3/13/2013

# re.split() 方法
# 字符串的str.split()方法只适应于非常简单的字符串分割情形， 它并不允许有多个分隔符或者是分隔符周围不确定的空格。
# 当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法：
# line = 'asdf fjdk;   afed,  fjek,asdf,   foo'
# str5 = re.split(r'[;,\s]\s*', line) # 正则模式表示 ;或,或空白字符且它们的后面再跟0个或多个空白字符
# print(str5) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# re.sub()方法
#对于简单的字面模式，直接使用字符串的str.replace()方法即可
# In [1]: text = 'yeah, but no, but yeah, but no, but yeah'
# In [2]: text.replace('yeah', 'yep')
# Out[2]: 'yep, but no, but yep, but no, but yep'

#对于复杂的模式，请使用re模块中的sub()，比如你想将形式为 11/27/2012 的日期字符串改成 2012-11-27
#text1 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
#sub()函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字比如\3指向前面模式的第3个捕获组，
# 此时要加r指定为原始字符串，否则会被Python自动转义为\x03

#print(re.sub('(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text1))

url = 'http://csdqthcweb.lx901.com/OtherGame/Index/319'
p = re.compile('Index/[0-9+].*',re.I) # re.I 不区分大小写匹配 . 除换行符以外的任意字符
print(p.findall(url))

# 替换
print(re.sub('#[0-9].*', '',url))























# r 不转义，字符里面的\就是字符\
#t = r'\\11ewre'
# print(t) # \\11ewre
#t1 = '23123\r111111111' # \r 回车（光标到本行行首）    打印的话前面包括自己均为空白字符，后面字符才算真正的字符
#print(t1) # 111111111
#t2 = '1\t1'
#print(t2) # 1	1   水平跳格（水平制表）
#t3 = '1\f1' #\f  \v 打印出来都是？
#print(t3)






