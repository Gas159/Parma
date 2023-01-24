class ThreadData: # thread - поток
    __shared_attrs = {'name': 'thread1', 'date': {}, 'id': 1}

    def __init__(self):
        self.__dict__ = self.__shared_attrs
