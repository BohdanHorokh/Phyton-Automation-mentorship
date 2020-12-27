class AppDriver:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, klass=None):
        self.__dict__['_driver'] = obj._driver
        return self
