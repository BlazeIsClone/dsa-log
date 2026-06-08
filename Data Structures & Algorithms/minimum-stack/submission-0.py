class MinStack:

    def __init__(self):
        self.items = []
        self.min = None

    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        self.items.pop()        

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        min = None
        for item in self.items:
            if min == None or item < min:
                min = item
        return min
        
