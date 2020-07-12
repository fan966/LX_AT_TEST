import os
import yaml
import random
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 获取到当前的工程路径
data_path = os.path.join(path,'Verify')
game_data_path = os.path.join(os.path.join(data_path,'Game'),'game_bet_play_data.yaml')
#print(game_data_path)
#
f = open(game_data_path,encoding='utf-8')
datas = yaml.load(f)
print(datas)
qq = datas.__contains__('前三直选复式')
print(qq)

with open(game_data_path,'r',encoding='utf-8') as f:
    datas =yaml.safe_load(f.read())
print(datas)

if datas.__contains__('大小单双'):
    print(datas['大小单双'])
    if isinstance(datas['大小单双'],dict):
        # print(list(datas['大小单双'].keys())[0])
        # print(type(list(datas['大小单双'].keys())[0]))
        # print(list(datas['大小单双'].values())[0])
        #print(type(list(datas['大小单双'].values())[0]))
        list1 = list(datas['大小单双'].values())[0]
        print(list(list1))

#o = [{'三码 1102': {'前三直选复式': 21044}}, {'三码 1102': {'前三直选单式': 21045}}, {'三码 1102': {'前三组选复式': 21046}}, {'三码 1102': {'前三组选单式': 21047}}, {'二码 1106': {'前二直选复式': 21048}}, {'二码 1106': {'前二直选单式': 21049}}, {'二码 1106': {'前二组选复式': 21050}}, {'二码 1106': {'前二组选单式': 21051}}, {'不定胆 1110': {'前三位': 21052}}, {'定位胆 1111': {'第一位': 21053}}, {'定位胆 1111': {'第二位': 21317}}, {'定位胆 1111': {'第三位': 21318}}, {'定位胆 1111': {'第四位': 21319}}, {'定位胆 1111': {'第五位': 21320}}, {'趣味型 1112': {'5单0双': 21054}}, {'趣味型 1112': {'0单5双': 21321}}, {'趣味型 1112': {'1单4双': 21322}}, {'趣味型 1112': {'4单1双': 21323}}, {'趣味型 1112': {'2单3双': 21324}}, {'趣味型 1112': {'3单2双': 21325}}, {'趣味型 1112': {'3,9': 21055}}, {'趣味型 1112': {'4,8': 21326}}, {'趣味型 1112': {'5,7': 21327}}, {'趣味型 1112': {'6': 21328}}, {'任选单式 1114': {'一中一': 21056}}, {'任选单式 1114': {'二中二': 21057}}, {'任选单式 1114': {'三中三': 21058}}, {'任选单式 1114': {'四中四': 21059}}, {'任选单式 1114': {'五中五': 21060}}, {'任选单式 1114': {'六中五': 21061}}, {'任选单式 1114': {'七中五': 21062}}, {'任选单式 1114': {'八中五': 21063}}, {'任选复式 1115': {'一中一': 21064}}, {'任选复式 1115': {'二中二': 21065}}, {'任选复式 1115': {'三中三': 21066}}, {'任选复式 1115': {'四中四': 21067}}, {'任选复式 1115': {'五中五': 21068}}, {'任选复式 1115': {'六中五': 21069}}, {'任选复式 1115': {'七中五': 21070}}, {'任选复式 1115': {'八中五': 21071}}]
# 分分彩
def gen_combinations(iterable, r, max_gen_count=100):
    """
    生成一个序列中的特定数量的组合
    :param iterable: 序列 (列表、元组)
    :param r: 指定多少组合数量
    :param max_gen_count: 最大生成多少种组合数（默认：100种组合）
    :return:
    """
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    random.shuffle(iterable)   # 打乱排序
    print(iterable)
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)

    while True:
        if max_gen_count == 0:
            break
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)
        max_gen_count -= 1

if __name__ == '__main__':
    pass