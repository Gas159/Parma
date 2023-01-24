class DataBase:
    __instance = None
    color = 'red'

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        print("Удаление экземпляра; " + str(self))
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Connection to DB:  {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Close connection for DB')

    def read(self):
        return 'Data with DB'

    def write(self, data):
        print(f'Write Data for DB {data}')


db = DataBase('root', '1234', 89)
db2 = DataBase('root2', '12345', 82)
print(id(db), id(db2))
print(db.color)
