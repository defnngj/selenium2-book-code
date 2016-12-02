from zope.interface import Interface
from zope.interface.declarations import implementer


# 定义接口
class IAnimal(Interface):

    def cry(self,host):
        """Say good morning to host"""


@implementer(IAnimal) #继承接口
class Parrot:

    def cry(self, host):
        """Say good morning to host"""
        return "Good morning, %s!" % host


if __name__ == '__main__':
    h = Parrot()
    hi = h.cry('Tom')
    print(hi)