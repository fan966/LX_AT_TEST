# import random
#
# class Pepole(object): # 创建人的类
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp
#         self.gun = None
#
#     def Shot(self,AK47_temp): # 拿枪方法
#         self.gun = AK47_temp
#
#     def Install_zd(self,clip_temp,bullet_temp):# 安装子弹方法
#         # 弹夹存入子弹
#         clip_temp.baocun_zd(bullet_temp)
#
#     def Install_tj(self,AK47_temp,clip_temp):# 安装弹夹方法
#         # 枪存放弹夹
#         AK47_temp.Install_dj(clip_temp)
#
#     def __str__(self):
#         if self.gun:
#             return '老王的信息：名字为%s，他有枪， %s'%(self.name,self.gun)
#         else:
#             return '老王没有枪'
#
#     def kai_q(self,AK47_temp,clip_temp,diren_temp):# 开枪方法
#         AK47_temp.shoting(clip_temp,diren_temp)
#
#     def shou_shang(self):
#         if self.hp == 0:
#             print('敌人HP值：%d，已击毙，停止射击！'%self.hp)
#         else:
#             self.hp = self.hp - bullet.shang_hai
#
# class Gun(object): # 创建枪的类
#     def __init__(self,name):
#         self.name = name
#         self.dan_jia = None # 记录弹夹 -用来指向弹夹的引用
#
#     def __str__(self):
#         return '枪的型号为：%s,%s'%(self.name,self.dan_jia) # self.dan_jia 相当于调用弹夹这个对象则会调用类Clip的str方法的描述信息
#
#     def Install_dj(self,clip_temp):
#         # 存放弹夹
#         self.dan_jia = clip_temp
#
#     def shoting(self,clip_temp,diren_temp):
#         clip_temp.fa_she(diren_temp)
#
#
#
# class Clip(object): # 创建弹夹的类
#     # 类变量
#     shengyu_roglaing = 0
#     def __init__(self,rong_liang):
#         self.rong_liang = rong_liang # 记录弹夹最大容量
#         Clip.shengyu_roglaing = self.rong_liang
#         self.danjia_list = [] # 弹夹的列表用来存放子弹（bullet）的引用
#
#     def __str__(self):
#         return '弹夹容量为%d/%d'%(Clip.shengyu_roglaing,self.rong_liang)
#
#     def baocun_zd(self,bullet_temp):
#         """保存子弹"""
#         self.danjia_list.append(bullet_temp)
#         Clip.shengyu_roglaing = Clip.shengyu_roglaing - bullet_temp.zd_rong_liang
#     def fa_she(self,diren_temp):
#        if self.danjia_list:
#            return self.danjia_list.pop()
#        else:
#            print('弹夹没子弹了')
#
#
# class Bullet(object): # 创建子弹的类
#     def __init__(self,shang_hai):
#         self.shang_hai = shang_hai # 一颗子弹破坏力
#         self.zd_rong_liang = 1
#
#     def ji_sha(self,diren_temp):
#
#         mingzhong = random.randint(0, 1)
#         if mingzhong == 1:
#             diren_temp.shou_shang()
#         else:
#             print('没击中敌人')
#
#
# # 创建老王
# laowang = Pepole("laowang",100) # 创建老王的对象
# # 创建枪
# AK47 = Gun('AK47') # 创建枪的对象
# # 创建弹夹
# clip = Clip(30) # 创建弹夹的对象
# # 创建子弹
# for i in range(20):
#     bullet = Bullet(10) # 创建子弹的对象
#
#     #老王安装子弹进入弹夹
#     laowang.Install_zd(clip,bullet)
#
# # 老王安装弹夹进入枪
# laowang.Install_tj(AK47,clip)
#
# # test弹夹
# # print(clip)
# # test--AK47
# #print(AK47)
#
# # 老王拿枪
# laowang.Shot(AK47)
# # test--laowang是否有枪
# #print(laowang)
# # 创建敌人
# diren = Pepole('diren',100)
# # kaiqiang
# for i in range(20):
#     if diren.hp:
#         laowang.kai_q(AK47,clip,diren)
#     else:
#         break
# class Switch_Windwos(object):
#     def Qie_windwos(self):
#         window_list = self.current_window_handles
#         current_window = self.window_handles
#         for i in window_list:
#             if i != current_window:
#                 self.switch_to.window(i)
#                 #if self.title in

a={'name':'tony','sex':'male'}
a['name']




























