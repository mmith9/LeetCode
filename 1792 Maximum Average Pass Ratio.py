from typing import List

#no heap, 
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # for x in classes:
        #     x.append((x[0]+1)/(x[1]+1) - x[0]/x[1])

        classes = [[a,b,(a+1)/(b+1)-a/b] for a,b in classes]
        classes.sort(key=lambda x:x[2])

        while True:
            st_pas, st_all, cl_pot = classes[-1] # students passed, students all, class_potential if one added
            next_cl_pot = classes[-2][2]

            while cl_pot >= next_cl_pot and extraStudents:
                st_pas += 1; st_all += 1; cl_pot = (st_pas+1)/(st_all+1) - st_pas/st_all
                extraStudents -=1
            classes[-1] = [st_pas, st_all, cl_pot]

            if extraStudents == 0:
                break

            tail_p = cl_pot
            index = len(classes) - 2
            st_pas, st_all, cl_pot = classes[-2]
            next_cl_pot = classes[-3][2] if index>0 else -1
            tail_m = 1

            while True:
                while extraStudents:
                    st_pas += 1; st_all += 1; cl_pot = (st_pas+1)/(st_all+1) - st_pas/st_all
                    extraStudents -=1
                    if cl_pot < next_cl_pot or cl_pot < tail_p: #is false on loop entry
                        break
                classes[index] = [st_pas, st_all, cl_pot]

                if extraStudents == 0:
                    break # exit to count avgs

                index -= 1
                next_cl_pot = classes[index-1][2] if index>0 else -1
                tail_m = min(tail_m, cl_pot)
                if next_cl_pot < tail_p:
                    while index>0 and classes[index][2] > tail_m:
                        index-=1
                    classes[index:] = sorted(classes[index:], key=lambda x:x[2])                        
                    break # exit back to end of tail
                st_pas, st_all, cl_pot = classes[index]

        avg_sum = 0
        for clas in classes:
            avg_sum+= clas[0]/clas[1]
        return avg_sum / len(classes)
    
    