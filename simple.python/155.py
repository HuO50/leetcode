class MinStack:
    #执行用时：348 ms, 在所有 Python3 提交中击败了19.97%的用户
    #内存消耗：18.3 MB, 在所有 Python3 提交中击败了66.23%的用户
    #通过测试用例：31 / 31

    # 思路，这道题用python非常好写，不用自己定义重新定义一个栈的结构，如果是正常的情况下，
    # 应该先定义一个栈，然后再写相关的出栈入栈的操作；
    # 假如我定义一个栈的话，
    # def __init__(self):
    #   self.stack = [] 
    # 然后定义第一个入栈操作，模拟append 操作，使用要先看当前的链表长度，然后在指定长度上+1
    # 这里使用c 是最麻烦的，因为c 要重新申请长度
    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # min 第一个非空的数字
        return sorted(self.stack)[0]
        # for item in self.stack:
        #     if item is None:
        #         continue
            
        #     if item < min:
        #         min = item
        # return min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()