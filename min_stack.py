'''This method Implements a min stack using two approaches.
1. Two Stacks->One tracks and max stack and the other, a min stack.
2. Second approach deals with one stack and tracking a min value
'''

'''Method 1: Using two stacks
Time Complexity: 
Push: O(1)
Pop: O(1)
Peak: O(1)
getMin O(1)

Space Complexity: O(n)
'''

class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self,val):
        self.stk.append(val)
        if not self.min_stk or val <= self.min_stk[-1]:
            self.min_stk.append(val)
    
    def pop(self):
        elem = self.stk.pop()
        if elem==self.min_stk[-1]:
            self.min_stk.pop()
        
    def peak(self):
        return self.stk[-1]
    
    def getMin(self):
        return self.min_stk[-1]

'''Method 2: Using Single Stack with a variable
Time Complexity: 
Push: O(1)
Pop: O(1)
Peak: O(1)
getMin O(1)

Space Complexity: O(n)
'''

class MinStack:

    def __init__(self):
        self.stk = []
    
    def push(self, val):
        if not self.stk:
            self.stk.append((val,val))
            return
        else:
            curr_min = self.stk[-1][1]
            self.stk.append((val, min(val, curr_min)))
        
    def pop(self):
        self.stk.pop()
    
    def peak(self):
        return self.stk[-1][0]
    
    def getMin(self):
        return self.stk[-1][1]

        


