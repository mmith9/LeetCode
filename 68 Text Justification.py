from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result:List[str] = []

        while words:
            word = words.pop(0)
            line = word
            curr_words = [word]
            num_words = 1
            cur_len = len(word)
            while words and cur_len + len(words[0]) < maxWidth:
                word = words.pop(0)
                curr_words.append(word)
                cur_len += len(word) + 1
                num_words+=1

            need_spaces_total = maxWidth - cur_len + num_words - 1
            if words: #not last line
                if num_words == 1:
                    line = curr_words[0] + ' '*need_spaces_total
                else:
                    need_spaces = int(need_spaces_total/(num_words-1))
                    extra_spaces = need_spaces_total - need_spaces * (num_words -1)
                    line = curr_words.pop(0)
                    while curr_words:
                        word = curr_words.pop(0)
                        if extra_spaces > 0:
                            line += ' '*(need_spaces +1) + word
                            extra_spaces-=1
                        else:
                            line += ' '* need_spaces  + word
            else:
                line = ' '.join(curr_words) 
                need_spaces_total = maxWidth - len(line)
                line = line + ' '*need_spaces_total
            result.append(line)
        return result
    
