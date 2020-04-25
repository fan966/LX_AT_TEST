# # 名字管理系统
# print("="*50)
# print("1:添加用户名")
# print("2:删除用户名")
# print("3:修改用户名")
# print("4:查找用户名")
# print("5:退出系统")
# print("="*50)
#
# names = [] # 定义一个空列表，用来存储数据
# # 按用户输入来执行程序功能
# while 1 :
#     name = int(input("请输入你要执行的操作："))
#     if name == 1:
#         names_n = input("请输入需要添加的用户：")
#         names.append(names_n) # append 在列表添加元素
#         print(names)
#     elif name == 2:
#         name_del = input("请输入需要删除的用户：")
#         names.remove(name_del) # 删除列表元素
#         print(names)
#     elif name == 3:
#         name_mod = input("请输入需要修改的用户：")
#         new_namemod = input("请输入需要修改的新名字：")
#         names.index(name_mod)
#         names[names.index(name_mod)] = new_namemod
#         print(names)
#     elif name == 4:
#         name_find = input("请输入需要查找的用户：")
#         if name_find in names:
#             names.index(name_find)
#             #print(names[names.index(name_find)])
#             print("你好，用户查找成功！\n%s"%name_find)
#         else:
#             print("用户查找失败！")
#     else:
#         break
#         print("退出系统成功")
# def t_menu():
#     print("="*50)
#     print("xxxxxxx")
#     print("xxxxxxx")
#     print("xxxxxxx")
#     print("="*50)
# def r_menu():
#     print("*")
#     print("*"*2)
#     print("*"*3)
#     print("*"*4)
#     print("*"*5)
# r_menu()
# t_menu()
# print("程序完结！")
# 定义函数计算两个数字之和
# def sum_2_menu(a,b):
#     rest = a + b
#     print("%d+%d=%d"%(a,b,rest))
#
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
#
# sum_2_menu(num1,num2)
# print("over!")

# def wendu_menu(): #定义函数 获取温度
#     wendu = 10
#     print("当前温度为%d"%wendu)
#     print("---4---")
#     return False
# def huashi_wendu(wendu):
#     huashidu = wendu * 7
#     print("当前华氏度为%d"%huashidu)
#     print("---5---")
# print("---1---")
# resuit = wendu_menu()
# print("---2---")
# huashi_wendu(resuit)
# print("---3---")

lb = [] # 定义全局空的列表
def print_card():

    print("="*45)
    print("1：添加一个名片")
    print("2：删除一个名片")
    print("3：修改一个名片")
    print("4：查询一个名片")
    print("5：显示一个名片")
    print("6：退出系统")
    print("="*45)
 # 打印系统提示信息
print_card()

def add_new_card():
    infor = {}
    new_name = input("请输入名字：")
    new_QQ = input("请输入QQ：")
    new_addr = input("请输入地址：")
    infor["name"] = new_name
    infor["QQ"] = new_QQ
    infor["addr"] = new_addr
    lb.append(infor)
    print(lb)
def del_card():
    del_name = input("请输入需要删除的用户：")
    for temp in lb:
        if temp["name"] == del_name:
            # print(temp)
            lb.index(temp)
            # print(lb.index(temp))
            # lb[lb.index(temp)]
            del lb[lb.index(temp)]
            print(lb)

def mod_card():
    new_infor = {}  # 定义一个空字典存储下方输入的值
    mod_infor = {}  # 定义一个修改的空字典，用来存储用户输入修改的值
    name_mod = input("请输入需要修改的用户：")
    QQ_mod = input("请输入你要修改的QQ：")
    addr_mod = input("请输入你要修改的住址：")
    # 录入用户修改的新的列表值
    modnew_name = input("请输入修改新的用户名:")
    modnew_QQ = input("请输入修改新的用QQ:")
    modnew_addr = input("请输入修改新的住址：")
    mod_infor["name"] = modnew_name
    mod_infor["QQ"] = modnew_QQ
    mod_infor["addr"] = modnew_addr
    new_infor["name"] = name_mod
    new_infor["QQ"] = QQ_mod
    new_infor["addr"] = addr_mod
    # print(new_infor)
    for temp in lb:
        if temp == new_infor:
            lb.index(temp)
            # print(lb.index(temp))
            lb[lb.index(temp)] = mod_infor
            print(lb)

def find_card():
    find_name = input("请输入查找的姓名")
    find_resout = 0  # 表示默认没有找到
    for temp in lb:
        if find_name == temp["name"]:
            print("查找成功，下方显示")
            print("%s\t%s\t%s" % (temp["name"], temp["QQ"], temp["addr"]))
            find_resout = 1
            break

    if find_resout == 0:
        print("查无此人！")


def xianshi_card():
    print("姓名\tQQ\t地址")
    for temp in lb:
        print("%s\t%s\t%s" % (temp["name"], temp["QQ"], temp["addr"]))

def out_card():
     while 1:
        #     break
    #infor = {} # 定义空的字典
            # 获取用户输入的值
        opera = input("请输入操作序号:")
            # 根据输入执行程序功能

        if opera == "1":
            add_new_card() # 调用新增函数 add_new_card

        elif opera == "2":
            del_card() # 调用删除函数del_card

        elif opera == "3":
            mod_card()


        elif opera == "4":
            find_card()

        elif opera == "5":
            xianshi_card()

        elif opera == "6":
            break
        else:
            print("输入有误，请重新输入！")
        print("")
out_card()
print(lb)









