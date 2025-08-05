'''
https://leetcode.com/problems/moving-average-from-data-stream/description/
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
'''

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