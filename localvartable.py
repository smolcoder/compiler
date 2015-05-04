class LocalVariableTable:
    def __init__(self):
        self.table = {}
        self.reversed_table = {}
        self.counter = 0

    def put(self, name, _type=None, ast=None):
        """
        :rtype: int, str
        """
        if name in self.table:
            return None, None
        self.table[name] = {
            'number': self.counter,
            'type': _type,
            'ast': ast}
        self.reversed_table[self.counter] = name
        self.counter += 1
        return self.counter - 1, name

    def putInternal(self, _type, ast):
        name = '___i{}'.format(self.counter)
        while name in self.table:
            self.counter += 1
            name = '___i{}'.format(self.counter)
        return self.put(name, _type, ast)

    def get(self, name):
        """
        :rtype: dict or None
        """
        return self.table.get(name)

    def __str__(self):
        return str(self.table)