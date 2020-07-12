# params = {'Headers': {'ValidateToken': '_dedeb54c31104bd18bb2ac1f7a69c684'}, 'NewVerifParmsData': {}}
# print(params['NewVerifParmsData'])

# for key_ in params['NewVerifParmsData']:
#     print('111')
#
# temp = {'Headers': {'ValidateToken': '_360cd3f696ee44c4ab26e50f67dbce7c'}, 'NewVerifParmsData': {'UserName': 'zcc997', 'Password': '1c9086375811c215fd3c6880eb20cd83'}}
# print(temp['NewVerifParmsData']['UserName'])
# print(type(temp))
# if 'Headers' in temp:
#     print('test')
params = {'Headers': {'ValidateToken': '_360cd3f696ee44c4ab26e50f67dbce7c'}, 'NewVerifParmsData': {'UserName': 'zcc997', 'Password': '1c9086375811c215fd3c6880eb20cd83'}}
#print(flag.keys())
t = {
        "OnlyFlag": "136420b8915c9c2ed8ee630be818d871",
        "UserName": "faker2",
        "ClientFlag": "Android",
        "Password": "770700405783e6259aed872b89245de7",
        "ValidateCode": "9999"
    }
#print(t.keys())
for key1 in params['NewVerifParmsData'].keys():
    print(key1)
    if key1 in t.keys():
        print(t, '/' + key1, params['NewVerifParmsData'][key1])

err_code_result = int('5') == 10
print(err_code_result)
