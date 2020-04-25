# coding = utf-8
import logging
import time
class Login(object):
    def __init__(self):
        # 实例化logging模块对象
        self.log = logging.getLogger()
        # 设置log的等级
        self.log.setLevel(logging.DEBUG)

        # 文件名以路径+日期的格式命名
        # 相对路径
        log_file_path = "../report/log/"
        # 获取当前时间
        times = time.strftime("%y-%m-%d"+".log") # 以年月日的格式+文件后缀
        file_name = log_file_path + times
        #print(file_name)

        # 文件输出日志
        # 配置文件流--相当于对象
        self.file_handle = logging.FileHandler(file_name,mode='a', encoding='utf-8')
        # 添加日志格式 （给对象添加一些格式）
        # %(asctime)s 当前时间
        # %(filename)s 文件名
        # %(module)s 模块
        # %(funcName)s 方法名
        # %(lineno)d  行数
        # %(levelname)s 日志等级名
        # %(message)s  日志输出信息
        formatter = logging.Formatter('%(asctime)s: %(filename)s--%(module)s--%(funcName)s--%(lineno)d--%(levelname)s-----%(message)s')
        # 添加输入格式属性
        self.file_handle.setFormatter(formatter)

        # 控制台输出日志
        consle_handle = logging.StreamHandler()  # logging的流
        # 添加控制台输出日志格式
        formatter1 = logging.Formatter(fmt='%(filename)-20s line:[%(lineno)d:] %(message)s')
        consle_handle.setFormatter(formatter1)


        # 添加文件，控制台输出流
        self.log.addHandler(self.file_handle)
        self.log.addHandler(consle_handle)  # 添加流输出日志在consle控制台
        # 日志信息
        #self.log.debug("test111111123555")



    def  get_log(self):
        return self.log
    def log_close(self):
        # 关闭流
        self.file_handle.close()
        # 移除流
        self.log.removeHandler(self.file_handle)
if __name__ == "__main__":
    l = Login()
    logi = l.get_log()
    logi.info("测试开始")
    logi.info("执行中")
    logi.info("测试结束")
    l.log_close()
