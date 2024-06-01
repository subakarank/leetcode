class MovingAverage():
    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.sum = 0.0

    def next(self, val: int):
        if len(self.window) == self.size:
            remove_val = self.window.pop(0)
            self.sum -= remove_val
        self.sum += val
        self.window.append(val)
        return self.sum / len(self.window)