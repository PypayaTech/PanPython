

class Step:
    def __init__(self):
        pass

    def calculate_position(self, engine):
        raise NotImplementedError()

    def execute(self, engine):
        raise NotImplementedError()
