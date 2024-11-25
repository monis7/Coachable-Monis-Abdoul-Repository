"""134. Gas Station"""
from typing import List

class Solution:
    """Solution Class"""
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       total_tank = 0
       current_tank = 0
       start = 0
       for i in range(len(gas)):
           total_tank += gas[i] - cost[i]
           current_tank += gas[i] - cost[i]
           if current_tank < 0:
               current_tank = 0
               start = i + 1
       return start if total_tank >= 0 else -1
