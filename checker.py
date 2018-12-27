**************
A palindrome checker by user id Jatin268
*************
class Checker:
    def __init__(self,x):
        self.x = x  
        
    def no_nums(self, x):
        y = []
        nums = "1234567890"
        for i in range(len(x)):
            if x[i] not in nums:
                y.append(x[i])
        return y
       
        
    def no_repeat(self, y):
        z = []
        for i in range(len(y)):
            if i != len(y)-1 and y[i+1] != y[i]:
            
                z.append(y[i])
        z.append(y[-1])
        return z   
    
    def is_palindrome(self):
        y = no_nums(self.x)
        y = no_repeat(y)
        self.x = self.no_nums(self.x)
        self.x = self.no_repeat(self.x)
        y = y[::-1]
        
        if y == self.x:
            print("True, palindrome word")
        else:
            print("False, not palindrome")
  
  print("thanks, jatin268")      

Test = Checker(input())
Test.is_palindrome()
