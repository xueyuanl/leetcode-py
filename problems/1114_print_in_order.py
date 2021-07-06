from threading import Lock
class Foo(object):
    def __init__(self):
        self.locks = (Lock(),Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.locks[0].release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """

        # printThird() outputs "third". Do not change or remove this line.
        with self.locks[1]:
            printThird()
