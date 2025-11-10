from collections import defaultdict
from functools import lru_cache
from typing import List
import math

from functools import lru_cache
from typing import List
from math import gcd

from functools import lru_cache
from typing import List
from math import gcd

#cached, gcd, pre-analyzed, optimized, beats 100% including numpy
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        if len(skill) == 1 or len(mana) == 1: 
            return sum(skill) * sum(mana) #single processing
        
        cumu = [0]; cm = 0
        for x in skill:
            cm += x; cumu.append(cm)
        lens = len(skill); s_max = max(skill)
        sm_idx1 = skill.index(s_max)
        sm_idx2 = lens - skill[::-1].index(s_max) -1

        escapist = [(cumu[sm_idx1+1], cumu[sm_idx1])]
        last = 0
        for x in range(sm_idx1):
            skil = skill[x]
            if skil > last:
                escapist.append((cumu[x+1], cumu[x]))
            last = skil

        chaser = [(cumu[lens], cumu[lens-1])]
        last = 0
        for x in range(sm_idx2,lens):
            skil = skill[x]
            if skil < last:
                chaser.append((cumu[x], cumu[x-1]))
            last = skil

        @lru_cache(maxsize=None)
        def get_delay(p1:int, p2:int) -> int:
            if p1 == p2:
                return s_max *p1
            if p1 > p2:
                iter = chaser
            else:
                iter = escapist

            delay = 0
            for a,b in iter:
                diff = p1*a - p2*b
                if diff > delay:
                    delay = diff
                           
            return delay

        clock = 0
        last_pot = mana[0]
        for pot in mana[1:]:
            the_gcd = gcd(pot, last_pot)
            p1 = last_pot//the_gcd
            p2 = pot//the_gcd
            delay = get_delay(p1,p2)

            clock += delay*the_gcd
            last_pot = pot

        clock += sum(skill) * last_pot

        return clock

#cached, gcd, pre-analyzed, beats 100% including numpy
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        if len(skill) == 1 or len(mana) == 1: 
            return sum(skill) * sum(mana) #single processing
        
        cumu = [0]; cm = 0
        for x in skill:
            cm += x; cumu.append(cm)
        lens = len(skill); s_max = max(skill)
        sm_idx1 = skill.index(s_max)
        sm_idx2 = lens - skill[::-1].index(s_max) -1

        escapist = [sm_idx1]
        last = 0
        for x in range(sm_idx1):
            skil = skill[x]
            if skil > last:
                escapist.append(x)
            last = skil

        chaser = [lens-1]
        last = 0
        for x in range(sm_idx2,lens):
            skil = skill[x]
            if skil < last:
                chaser.append(x-1)
            last = skil

        @lru_cache(maxsize=None)
        def get_delay(p1:int, p2:int) -> int:
            if p1 == p2:
                return s_max *p1
            if p1 > p2:
                iter = chaser
            else:
                iter = escapist

            delay = 0
            for x in iter:
                diff = p1*cumu[x+1] - p2*cumu[x]
                if diff > delay:
                    delay = diff
                           
            return delay

        clock = 0
        last_pot = mana[0]
        for pot in mana[1:]:
            the_gcd = gcd(pot, last_pot)
            p1 = last_pot//the_gcd
            p2 = pot//the_gcd
            delay = get_delay(p1,p2)

            clock += delay*the_gcd
            last_pot = pot

        clock += sum(skill) * last_pot

        return clock

#cached, analytic and using gcd, beats 99%
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        lens = len(skill) - 1
        if lens == 0: 
            return skill[0] * sum(mana) #single processing
       
        @lru_cache(maxsize=None)
        def get_delay(p1:int, p2:int) -> int:
            delta = p2 - p1
            delay = 0
            pref = 0
            for a in skill:
                need = (a * p1) - (pref * delta)
                if need > delay:
                    delay = need
                pref += a
            return delay

        clock = 0
        last_pot = mana[0]
        for pot in mana[1:]:
            gcd = math.gcd(pot, last_pot)
            delay = get_delay(last_pot//gcd ,pot//gcd)
            clock += delay*gcd
            last_pot = pot

        clock += sum(skill) * last_pot
        return clock

#cached, marginally better
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        maxs = len(skill) - 1
        if len(skill) == 1: 
            return skill[0] * sum(mana) #single processing
       
        pot = mana[0]
        t1 = []
        timing = 0
        for step in skill:
            timing += step*pot
            t1.append(timing)

        clock = 0
        for idx in range(1, len(mana)):
            pot = mana[idx]
            t2 = []
            timing = 0
            for step in skill:
                timing += step*pot
                t2.append(timing)

            delay = t1[0]
            for x in range(maxs):
                if t2[x] + delay < t1[x+1]:
                    delay = t1[x+1] - t2[x]
            clock += delay
            t1 = t2

        clock += t1[-1]

        return clock 
    

#mem limit exceeded
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        if len(skill) == 1: 
            return skill[0] * sum(mana) #single processing
       
        timings = []
        for pot in mana:
            timing = []
            clock = 0
            for step in skill:
                clock += step*pot
                timing.append(clock)
            timings.append(timing)                

        t1 = timings[0]

        clock = 0
        for pot in range(1, len(mana)):
            delay = t1[0]
            t2 = timings[pot]

            for x in range(len(skill)-1):
                if t2[x] + delay < t1[x+1]:
                    delay = t1[x+1] - t2[x]
            clock += delay
            t1 = t2

        clock += t1[-1]

        return clock


#naive and slow but passes 75%
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        if len(skill) == 1: 
            return skill[0] * sum(mana) #single processing
        
        clock = 0
        last_pot = mana[0]

        for pot in mana[1:]:
            delay = 0 
            t_pot = 0
            t_pot_last = 0
            for step in skill:
                if t_pot + delay < t_pot_last + step * last_pot:
                    delay = t_pot_last + step*last_pot - t_pot 
                t_pot += pot * step
                t_pot_last += last_pot * step
            clock += delay
            last_pot = pot

        clock += sum(skill) * last_pot

        return clock