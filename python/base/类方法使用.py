class A(object):
    bar = 1

    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static_foo')

        print(A.bar)


    @classmethod
    def class_foo(cls):
        print( 'class_foo')

        print(cls.bar)

        cls().foo()



# A.static_foo() # 类名可直接调用类方法
# A.class_foo()
# A.foo() # 类名不能直接调用实例方法
print(A.bar)
A().foo()
