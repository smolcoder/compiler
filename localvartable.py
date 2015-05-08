class LocalVariableTable:
    def __init__(self, startFrom=0):
        self.table = {}
        self.reversed_table = {}
        self.counter = startFrom

    def put(self, name, _type=None, ast=None, number=None):
        """
        :rtype: str
        """
        if number is None:
            n = self.counter
            self.counter += 1
        else:
            n = number
        if name in self.table:
            return None, None
        self.table[name] = {
            'number': n,
            'type': _type,
            'ast': ast,
            'name': name
        }
        self.reversed_table[n] = name
        return name

    def putInternal(self, _type, ast):
        name = '__t{}'.format(self.counter)
        while name in self.table:
            self.counter += 1
            name = '__t{}'.format(self.counter)
        return self.put(name, _type, ast)

    def get(self, name):
        """
        :rtype: dict or None
        """
        return self.table.get(name)

    def __str__(self):
        return str(self.table)