# https://cloud.tencent.com/developer/article/1527470  Python+Requests multipart/form-data实现图片、附件上传实例
# https://blog.csdn.net/sinat_38682860/article/details/102935746  python拼接multipart/form-data类型post请求格式
'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：857662006
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''


# multipart/form-data
class MultipartFormData(object):
    """multipart/form-data格式转化"""

    @staticmethod
    def format(data, boundary="--------------WebKitFormBoundary7MA4YWxkTrZu0gW", headers={}):
        """
        form data
        :param: data:  {"req":{"cno":"18990876","flag":"Y"},"ts":1,"sig":1,"v": 2.0}
        :param: boundary: "----WebKitFormBoundary7MA4YWxkTrZu0gW"
        :param: headers: 包含boundary的头信息；如果boundary与headers同时存在以headers为准
        :return: str
        :rtype: str
        """
        print(headers)
        # 从headers中提取boundary信息
        if "content-type" in headers:
            fd_val = str(headers["content-type"])
            if "boundary" in fd_val:
                fd_val = fd_val.split(";")[1].strip()
                boundary = fd_val.split("=")[1].strip()
            else:
                raise ("multipart/form-data头信息错误，请检查content-type key是否包含boundary")
        # form-data格式定式
        jion_str = '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'
        end_str = "--{}--".format(boundary)
        args_str = ""

        if not isinstance(data, dict):
            raise ("multipart/form-data参数错误，data参数应为dict类型")
        for key, value in data.items():
            #print(key,value)
            args_str = args_str + jion_str.format(boundary, key, value)
            #print(args_str)
        args_str = args_str + end_str.format(boundary)
        args_str = args_str.replace("\'", "\"")
        return args_str

if __name__ == '__main__':
    headers = {
        'content-type':"multipart/form-data;boundary=--------------WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control':"no-cache",
    }
    file = {
        "image": ("haha.jpg", open("E:/tupian/haha.jpg", "rb"), "image/jpg"),
    }
    data = {
        "req": {"cno":"1213058673616305"},
        "appid":"dp3wY4YtycajNEz23zZpb5Jl",
        "ts":1,
        "sig":1,
        "v":2.0,

    }

    datas = MultipartFormData.format(data=data,headers=headers)
    print(datas)
