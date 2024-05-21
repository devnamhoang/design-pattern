
class Connection:
    pass


class Database:
    connection: any

    def __init__(self):
        self.connection = Connection()

    def getInstance(self):
        return self.connection if self.connection else Connection()
