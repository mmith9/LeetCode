class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        cats_ord = ["electronics", "grocery", "pharmacy", "restaurant"]
        catss = set(cats_ord)
        codes = []
        for x in range(len(code)):
            if isActive[x] and businessLine[x] in catss and code[x].replace('_','a').isalnum():
                codes.append((code[x], businessLine[x]))
        
        codes.sort(key=lambda cod:(cats_ord.index(cod[1]),cod[0]))
        return [x[0] for x in codes]
