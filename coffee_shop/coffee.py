
class Coffee:
    def __init__(self, name):
        #Initialize a Coffee instance with a name.
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters")
        self._name = name

    @property
    def name(self):
        #Return the coffee's name.
        return self._name