# -*-coding:utf-8-*-


#比如这个源码中，有三层iframe嵌套，如果我们想定位到id="eWebEditor"这一层，代码如下：
# driver.switch_to.frame("inden_main")
# driver.switch_to.frame("Editor1")
# driver.switch_to.frame("eWebEditor")
# 那么如果我们又想切换到上一层呢，driver.switch_to.parent_frame()，表示从当前的子iframe切换到父iframe，即上级iframe。
# # 切换到第一层iframe
# driver.switch_to.frame("inden_main")
# # 切换到第二层iframe
# driver.switch_to.frame("Editor1")
# 切换到第三层iframe
# driver.switch_to.frame("eWebEditor")
# 重新切换到父iframe，即切换到第二层iframe
# driver.switch_to.parent_frame()
#总结：遇到iframe时，需要先切换到iframe框架内，再进行定位；多层嵌套的，层层切换iframe；在iframe框架内，定位主文档的元素，需切回到主文档再定位。