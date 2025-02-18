class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets= []
        closeBrackets= {')':'(', ']':'[', '}':'{'}
    
        if len(s)%2==1:
            return False
    
        for i in range(0,len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                openBrackets.append(s[i])
                continue
            
            if s[i]==')' or s[i]==']' or s[i]=='}':
                try:
                    if openBrackets.pop() != closeBrackets.get(s[i]):
                        return False
                except: return False
        
        if len(openBrackets)!=0:
            return False
        
        return True