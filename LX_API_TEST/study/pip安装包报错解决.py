# python中pip安装自带库时报错：ERROR: Could not find a version that satisfies the requirement flask (from versions: none)
# ERROR: No matching distribution found for flask  找不到回应版本
'''
这个时候就需要升级pip版本了
# python -m pip install --upgrade pip # 此命令用来升级pip版本

再次尝试安装 pip install 包名 # 如果再次失败
然后继续尝试发现还是不行，会报相同的错误，这时考虑到是网络的问题，我的网有时候是不稳定的，这时我们用国内的镜像源来加速

使用如下命令再次尝试
pip install redis-py-cluster==1.3.6 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

--trusted-host pypi.douban.com 这是为了获得ssl证书的认证


'''