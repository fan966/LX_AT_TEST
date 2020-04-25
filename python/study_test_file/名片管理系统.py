# 名片管理系统
# 定义全局变量列表用来存储名片信息
card_info = []
# 提示操作信息
def print_info(): # 打印提示信息
    print('='*50)
    print('1:添加名片信息')
    print('2:修改名片信息')
    print('3:删除名片信息')
    print('4:显示名片信息')
    print('5:退出系统')
    print('6:名片存储')
    print('=' * 50)
def add_info():
    card_list = {}
    name = input('请输入需要添加姓名：')
    age = input('请输入需要添加年龄：')
    card_list["name"] = name
    card_list['age'] = age
    card_info.append(card_list)
    #print(card_info)
def Xs(): # 显示所有名片信息
    print(card_info)

# 名片数据存入文件
def Save_file():

    f = open('card_file.txt','w')
    f.write(str(card_info))
    f.close()
# 加载名片数据进入程序
def Load_card():
    try:
        global card_info
        f1 = open('card_file.txt')

        card_info = eval(f1.read())

        f1.close()
    except Exception:
        print("异常处理中...")
def main():
    """入口程序"""
    # 加载名片信息
    Load_card()
    print_info() # 调用打印名片系统提示方法

    while True:
        f = input('请输入操作>>>:')
        if f == '1':
            add_info()
        elif f == '4':
            Xs()
        elif f == '5':
            break
        elif f == '6':
            Save_file()

if __name__ == '__main__':
    main()


