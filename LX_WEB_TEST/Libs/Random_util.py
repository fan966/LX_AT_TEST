# -*-coding:utf-8-*-
import random
class RandomUtil:
    first_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                  '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
                  '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                  '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                  '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                  '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                  '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    last_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
                   '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
                   '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
                   '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
                   '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
                   '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
                   '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
                   '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
                   '将', '月', '十', '实', '向', '声', '车', '全',]


    def full_bankno(self):
        '''
        随机生成18位的银行卡号
        :param self:
        :return:
        '''
        bankno = random.randint(111111111111111111, 999999999999999999)
        return "{}".format(bankno)
    def random_name(self):
        '''
        获取随机姓名
        :return:
        '''
        str1 = random.choice(self.first_names)
        str2 = random.choice(self.last_names)
        name = str1 + str2
        return name

    def get_random_info_str(self,item):
        '''
        根据参数随机获取item个字符串
        :return:
        '''
        text = '0123456789qwertyuiopasdfghjklzxcvbnm'
        str_info = random.sample(text, item)
        temp = ''.join(str_info)
        return temp

    def get_random_int(self,miu_num,max_num):
        '''
        两个数值内随机取一个整数型
        :param miu_num:
        :param max_num:
        :return:
        '''
        num = random.randint(int(miu_num),int(max_num))
        return num
    def get_random_info_int(self,item):
        '''
        根据传参司机获取item个数字字符串
        :param item:
        :return:
        '''
        text =  '0123456789'
        str_info = random.sample(text, item)
        temp = ''.join(str_info)
        return temp

    def random_number_list(self,item,type_='|'):
        '''
        随机获取范围内数字返回字符串list
        :return:
        '''

        item = int(item)
        list = []
        i = 1
        while True:
            num = random.randint(1,9)
            num = '0' + (str(num))
            if num not in list:
                list.append(num)
                i += 1
                if i > item:
                    if type_ == '|':
                        return '|'.join(list)
                    elif type_ == ',':
                        return ','.join(list)
                    else:
                        return ''.join(list)

    def random_number_list1(self, item, type_='|'):
        '''
        去掉0字符串拼接
        随机获取范围内数字返回字符串list
        :return:
        '''

        list = []
        i = 1
        while True:
            num = random.randint(1, 9)
            num = (str(num))
            if num not in list:
                list.append(num)
                i += 1
                if i > item:
                    if type_ == '|':
                        return '|'.join(list)
                    elif type_ == ',':
                        return ','.join(list)
                    else:
                        return ''.join(list)



if __name__ == "__main__":
    r = RandomUtil()
    # # print(r.get_random_info_str(6))
    # print(r.get_random_info_int(4))
    # print(type(r.get_random_info_int(4)))
    # temp = r.random_number_list(1,type_='')
    # print(temp)
    # print(r.get_random_int(1.111,100))
    t = "100.1254"
    t = float(t)
    print(int(t))

