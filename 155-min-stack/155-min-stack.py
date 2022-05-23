class MinStack:

    def __init__(self):
        self.a=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        self.a.append(val)
        if len(self.minstack)==0:
            x=val
        else:
            x=min(self.minstack[-1],val)
        self.minstack.append(x)
        

    def pop(self) -> None:
        self.a.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()