from collections.abc import Iterable

# >>1. 判断对象是否可迭代
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance("ABC", Iterable))
print(isinstance(123, Iterable))


# >>2. 自定义可迭代的对象
class MyList(object):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        myIterator = MyIterator(self)
        return myIterator


mylist = MyList()
mylist.add("张三")
mylist.add("李四")

print(isinstance(mylist, Iterable))


# >>3. 自定义迭代器对象
class MyIterator(object):
    def __init__(self, mylist):
        self.mylist = mylist
        self.current = 0

    def __next__(self):
        """
        返回下一个元素
        :return:
        """
        if self.current < len(self.mylist.items):
            item = mylist.items[self.current]
            self.current += 1
            return item
        else:
            #停止迭代
            raise StopIteration

    def __iter__(self):
        return self


for item in mylist:
    print(item)
