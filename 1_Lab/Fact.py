class Fact:
    def __init__(self, name: str):
        self.name = name
        self.watched = False

    def __eq__(self, other):
        if not isinstance(other, Fact):
            raise ValueError()
        return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
