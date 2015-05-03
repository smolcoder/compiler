class LocalVariableTable:
    def __init__(self):
        self.table = {}
        self.reversed_table = {}
        self.counter = 0

    def put(self, name):
        if name in self.table:
            return None
        self.table[name] = self.counter
        self.reversed_table[self.counter] = name
        self.counter += 1
        return self.counter - 1

    def get(self, name):
        return self.table.get(name)

    def __str__(self):
        return str(self.table)