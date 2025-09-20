from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def recur(txt:str) -> dict:
            heap = []
            counts = defaultdict(int)

            lens = len(txt)
            x = 0
            while x<lens:

                cur_el = txt[x]
                x+=1
                if cur_el == '(':
                    heap.append(counts)
                    counts = defaultdict(int)
                    continue

                if cur_el.isupper():
                    while x<lens and txt[x].islower():                        
                        cur_el += txt[x]
                        x += 1

                cur_num = ''
                while x<lens and txt[x].isnumeric():
                    cur_num += txt[x]
                    x+=1
                cur_num = int(cur_num) if cur_num else 1

                if cur_el != ')':
                    counts[cur_el] += cur_num
                    continue

                # is bracket multiplier
                old_counts = heap.pop()
                for elem, cnt in counts.items():
                    old_counts[elem] += cnt * cur_num
                counts = old_counts
            return counts

        counts = recur(formula)

        output=''
        for elem in sorted(counts.keys()):
            output += elem
            if counts[elem] > 1:
                output+=str(counts[elem])
        return output


engine = Solution()

txt = formula = "K4(ON(SO3)2)2"
print(formula)
print(engine.countOfAtoms(txt))
