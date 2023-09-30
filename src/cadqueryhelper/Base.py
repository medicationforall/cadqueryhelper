class Base:
    def __init__(self):
        self.make_called = False
        self.parent = None

    def make(self, parent=None):
        self.parent = parent
        self.make_called = True

    def build(self):
        if self.make_called == False:
            raise Exception('Make has not been called')