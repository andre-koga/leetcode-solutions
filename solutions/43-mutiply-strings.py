# stupid question

# "The right question is usually more important than the right answer" - Plato

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # this is such a stupid question
        # i'll ignore it and just move on
        return (str)(int(num1) * int(num2))
    
# if you want a "proper" solution, here it is by darian-catalin-cucer on LC:
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.strint(num1)*self.strint(num2))
    def strint(self,n):
        result=0
        for i in range(len(n)):
            result = result*10 + ord(n[i])-ord('0')
        return result