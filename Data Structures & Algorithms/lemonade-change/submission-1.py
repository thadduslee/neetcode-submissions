class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five +=1
            
            if bill == 10:
                change = 5
                if five == 0:
                    return False
                else:
                    five -=1
                    ten+=1
            
            if bill == 20:
                change = 15
                if five > 0 and ten > 0:
                    five -=1
                    ten -=1
                elif five >= 3:
                    five -=3
                
                else:
                    return False
        return True
                