# -*-coding:utf-8-*-
# 由于本人不怎么了解js代码，对webdriver定位元素比较熟悉，所以查看了selenium调用js代码的一些博客，先用webdriver定位元素，再用js代码去掉readonly属性。
#
# 	pag=driver1.find_element_by_xpath('//*[@id="pane-first"]/div/div/ul/li[2]/ul/li[1]')
# 	driver1.execute_script("arguments[0].removeAttribute('readonly')",pag)
