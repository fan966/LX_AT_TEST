from Libs.http_requests import get_json_value
temp = {'Status': 'true',
        'Info': '请求成功',
        'Data':
            {'GameShowMode': 0, # 游戏显示模式(0:分类显示,1:全部显示)
             'DefaultSltGame': 0, # 默认选中游戏(0:官方玩法,1:信用玩法,2:微投玩法)
             'MobileShowPlayItem': '0,1,2', # 游戏玩法(0:官方玩法,1:信用玩法,2:微投玩法)
             'GameData': [{'GameType': 0,
                           'GameCateList':
                               [
                                   {'FID': 36,
                                    'FCategoryName': '秒秒彩',
                                    'FCategoryCode': 'OFFICIAL_MMC',
                                    'FChannelCode': 'CPYX', 'FGroupID': 3,
                                    'FSort': 0,
                                    'FCategoryImage': 'https://demoimgqt.womenrfree.com//Content/mobile/images/icon-grop1/mmc.png',
                                    'GameInfoList':
                                        [
                                            {'FGameID': 511,
                                             'FGameName': '深圳秒秒彩',
                                             'FAbbreviation': 'CSZQGGL',
                                             'FGameCode': 'SSC', 'FSort': 2,
                                             'FGamePicture': 'https://demoimgqt.womenrfree.com//Content/mobile/images/game-icon/CSZQGGL.png',
                                             'FChannelCode': 'CPYX',
                                             'FCategoryID': 36,
                                             'FGameType': 10,
                                             'FGameTag': 'null',
                                             'FDescription': '',
                                             'FCount': 0,
                                             'FCategoryName': '秒秒彩',
                                             'FCategoryCode': 'OFFICIAL_MMC',
                                             'FHotSort': 0,
                                             'FHot': 0,
                                             'FGroupId': 3,
                                             'FPeriodDetail': ''
                                             },
                                            {
                                                'FGameID': 363,
                                                'FGameName': '豪彩重庆刮刮乐',
                                                'FAbbreviation': 'ZQGGL',
                                                'FGameCode': 'SSC',
                                                'FSort': 3,
                                                'FGamePicture': 'http://image.ahh1771.com/Img//2019/11/21/32c7d310f9714b218f15b5e8557b445c.png',
                                                'FChannelCode': 'CPYX', 'FCategoryID': 36, 'FGameType': 10, 'FGameTag': 'null', 'FDescription': '', 'FCount': 0, 'FCategoryName': '秒秒彩', 'FCategoryCode': 'OFFICIAL_MMC', 'FHotSort': 0, 'FHot': 0, 'FGroupId': 3, 'FPeriodDetail': ''}, {'FGameID': 396, 'FGameName': '快三刮刮乐', 'FAbbreviation': 'KSGGL', 'FGameCode': 'K3', 'FSort': 4, 'FGamePicture': 'https://demoimgqt.womenrfree.com//Content/mobile/images/game-icon/KSGGL.png', 'FChannelCode': 'CPYX', 'FCategoryID': 36, 'FGameType': 10, 'FGameTag': 'null', 'FDescription': '', 'FCount': 0, 'FCategoryName': '秒秒彩', 'FCategoryCode': 'OFFICIAL_MMC', 'FHotSort': 0, 'FHot': 0, 'FGroupId': 3, 'FPeriodDetail': ''}]}]}]}}
data = get_json_value(temp,'/Data/GameData')
#print(data)
for game_data in data:
    #print(game_data)
    for game_list in game_data['GameCateList']:
        print(game_list)
        for game_info in game_list:
            # 游戏大类
            # game_FCategoryName = game_info['FCategoryName']
            pass

















