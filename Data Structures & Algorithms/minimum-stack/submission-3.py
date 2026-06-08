class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins or val < self.mins[-1]:
            self.mins.append(val)
        else:
            top = self.mins[-1]
            self.mins.append(top)

        print(self.mins)
        self.items.append(val)

    def pop(self) -> None:
        self.mins.pop()        
        self.items.pop()        

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.mins[-1]

        
