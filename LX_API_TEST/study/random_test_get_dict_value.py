# 随机获取可迭代对象的值
import random
import json
listb = [{'age':18},{'name':'ttt'},{'type':'list'}]

# data = random.sample(listb,1)
# print(data)
# data = random.choice(listb)
# print(data)

q = {'时时彩': {'北京时时彩': 57}}
print(list(q.keys())[0])
#print(list(tt)[0])
# if '快'in list(t.keys())[0]:
#     print(t.keys())
#     print('zailimian ')

#print(b)

p={'ID': 'B005', 'CaseName': '官方游戏下注', 'ScriptName': 'Api_Game_OfficialAddOrders_Case.py', 'Precondition': None, 'NeedLogin': 'YES', 'Desc': '官方游戏下注', 'NewVerifParmsData': {'PeriodId': '181663920', 'OrderList': [{'a': 2.0, 'c': '01', 'i': 21053, 'k': '0', 'm': 1, 'n': 1, 't': 1, 'ts': 1593542951}], 'GameId': 206}, 'ExpectResult': {'Status': True, 'Info': '投注成功！', 'Code': 0}, 'AssociateInterface': '游戏相关-官方游戏下注', 'IsRun': 'YES', 'ApplyEnv': '全部', 'RunResult': None}
q = json.dumps(p,ensure_ascii=False)
# print(type(p))
# print(q)
# w = {"PeriodId":"181663920","OrderList":"[{\"a\":2.0,\"c\":\"01\",\"i\":21053,\"k\":\"0\",\"m\":1,\"n\":1,\"t\":1,\"ts\":1593542951}]","GameId":"320"}
# e = {"PeriodId":"181663920","OrderList":[{"a":2.0,"c":"01","i":21053,"k":"0","m":1,"n":1,"t":1,"ts":1593542951}],"GameId":"320"}
# r = json.dumps(e,ensure_ascii=False)
# print(r)
# print(w)