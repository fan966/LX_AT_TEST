# coding = utf-8
from util.read_exce_data import Excel_data
from util.gjz_keyword import Gjzmethod
from selenium import webdriver
class KeywordCase(object):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.action_method = Gjzmethod(self.driver)  # 实例化执行关键字方法的对象


    def run_main(self):
        self.action_method = Gjzmethod()
        handle_excel = Excel_data('F:\python\config\keyword.xls')
        # 拿到行数
        rows = handle_excel.get_rows()
        # 循环行数，去执行每一行的case
        if rows != None:
            for i in range(1,rows):


                # case是否执行
                is_run = handle_excel.get_cell_value(i,2)
                if is_run == "yes":
                    # 拿到执行方法
                    method = handle_excel.get_cell_value(i,4)
                    # 拿到输入数据
                    send_value = handle_excel.get_cell_value(i, 5)
                    # 拿到操作元素
                    handle_value = handle_excel.get_cell_value(i, 6)
                    # 拿到预期结果方法
                    expected_result_method = handle_excel.get_cell_value(i,7)
                    # 拿到实际结果值
                    expected_result_value = handle_excel.get_cell_value(i,8)

                    # 调用执行方法run_method
                    self.run_method(method,send_value,handle_value)

                    # 判断是否有预期结果方法
                    if expected_result_value != "":
                        data_list = self.get_expected_result_value(expected_result_value)
                        #print(data_list)
                        if data_list[0] == "text":
                            temp = self.run_method(expected_result_method)
                            if data_list[1] in temp: # 预期结果值是否存在于预期中
                                handle_excel.write_datas(i,"pass")
                            else:
                                handle_excel.write_datas(i,"false")
                        elif data_list[0] == "element":

                            temp = self.run_method(expected_result_method,data_list[1]) # 是否按元素属性查找到element
                            if temp:
                                handle_excel.write_datas(i,"pass")
                            else:
                                handle_excel.write_datas(i,"false")
                    else:
                        pass

    # 获取预期结果值
    def get_expected_result_value(self,value):
        data_list = value.split("=") # 以=号分割成列表

        return data_list

    def run_method(self,method,send_value = "",handle_value = ""):

        method_value = getattr(self.action_method,method) # 获取对象的属性值 可百度getattr  python内置函数
        #print(method_value)
        # 是否有输入数据
        result = None
        if send_value != "" and handle_value != "":
            #print(send_value)
            # 执行方法（输入数据，操作元素）
            result = method_value(send_value,handle_value)

        elif send_value == "" and handle_value != "":
            # 执行方法（操作元素）
            result = method_value(handle_value)
        elif send_value != "" and handle_value == "":
            result = method_value(handle_value)
        elif send_value == "" and handle_value == "":
            result = method_value()
        else:
            pass
        return result

if __name__ == "__main__":
    case = KeywordCase()
    case.run_main()