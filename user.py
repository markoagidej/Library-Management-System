
class User:
    def __init__(self, name, UUID):
        self.name = name
        self._UUID = UUID
        self._borrow_history = []
