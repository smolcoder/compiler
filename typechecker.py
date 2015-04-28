from ast import BaseASTListener


class TypeCheckListener(BaseASTListener):
    def __init__(self):
        self.errors = []


