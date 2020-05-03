# -*-coding:utf-8-*-
list = []
# 获取整个元素的HTML然后在切割数据 el.get_attribute('outerHTML')
text = '<ul class="flip "><li class="flip-clock-before"><a href="#"><div class="up"><div class="shadow"></div><div class="inn">9</div></div><div class="down"><div class="shadow"></div><div class="inn">9</div></div></a></li><li class="flip-clock-active"><a href="#"><div class="up"><div class="shadow"></div><div class="inn">0</div></div><div class="down"><div class="shadow"></div><div class="inn">1</div></div></a></li></ul>'
text2 = '<ul class="flip  play"><li class="flip-clock-before"><a href="#"><div class="up"><div class="shadow"></div><div class="inn">3</div></div><div class="down"><div class="shadow"></div><div class="inn">3</div></div></a></li><li class="flip-clock-active"><a href="#"><div class="up"><div class="shadow"></div><div class="inn">2</div></div><div class="down"><div class="shadow"></div><div class="inn">2</div></div></a></li></ul>'
num = len(text)
print(num)
print(text[num-27])

for i in text,text2:
    time = int(i[len(i)-27])
    list.append(time)
print(list)
game_time_ = 0
game_time = list[0]*60*10
game_time_ += game_time
print(game_time)
game_time = list[1]*60
game_time_ += game_time
print(game_time_)
#print(int(text[num-27]:text[num-26]))
