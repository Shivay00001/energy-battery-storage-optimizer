import pulp
import pandas as pd
from typing import List

class BatteryOptimizer:
    def __init__(self, capacity_mwh: float, power_mw: float, efficiency: float = 0.9):
        self.capacity = capacity_mwh
        self.power = power_mw
        self.eff = efficiency

    def optimize(self, prices: List[float]):
        """
        Solves the LP problem to maximize revenue.
        Constraints:
        1. SOC limits (0 <= SOC <= Capacity)
        2. Power limits (0 <= Charge <= Power, 0 <= Discharge <= Power)
        3. Energy Balance (SOC_t = SOC_{t-1} + Charge*Eff - Discharge/Eff)
        """
        hours = len(prices)
        
        # Problem
        prob = pulp.LpProblem("Battery_Arbitrage", pulp.LpMaximize)
        
        # Variables
        charge = pulp.LpVariable.dicts("Charge", range(hours), 0, self.power)
        discharge = pulp.LpVariable.dicts("Discharge", range(hours), 0, self.power)
        soc = pulp.LpVariable.dicts("SOC", range(hours + 1), 0, self.capacity)
        
        # Objective Function: Maximize (Revenue - Cost)
        prob += pulp.lpSum([discharge[t] * prices[t] - charge[t] * prices[t] for t in range(hours)])
        
        # Constraints
        prob += soc[0] == self.capacity * 0.5 # Start at 50%
        
        for t in range(hours):
            # Energy Balance
            # Next SOC = Current SOC + Charge * eff - Discharge / eff
            prob += soc[t+1] == soc[t] + charge[t] * self.eff - discharge[t] / self.eff
            
            # Constraint: Cannot Charge and Discharge heavily (LP naturally handles this by price, but physical limit is implicit in Net Power if we modeled that)
            # Actually standard LP for storage without binary variables might allow simultaneous charge/discharge if prices are negative, 
            # but here prices are positive so it won't do both.
            
        prob.solve(pulp.PULP_CBC_CMD(msg=0))
        
        # Extract Results
        results = []
        for t in range(hours):
            results.append({
                "hour": t,
                "price": prices[t],
                "charge_mw": charge[t].varValue,
                "discharge_mw": discharge[t].varValue,
                "soc_mwh": soc[t+1].varValue
            })
            
        return pd.DataFrame(results)
