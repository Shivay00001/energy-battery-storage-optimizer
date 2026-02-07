import numpy as np
import pandas as pd

def generate_price_curve(hours=24):
    """Generates a synthetic electricity price curve (Duck Curve shape)."""
    # Low prices in early morning and midday (solar), high in evening peak
    prices = []
    for h in range(hours):
        if 0 <= h < 6:
            p = np.random.uniform(20, 30) # Night
        elif 6 <= h < 10:
            p = np.random.uniform(40, 60) # Morning ramp
        elif 10 <= h < 16:
            p = np.random.uniform(10, 25) # Midday Solar Depression
        elif 16 <= h < 21:
            p = np.random.uniform(80, 150) # Evening Peak
        else:
            p = np.random.uniform(30, 40) # Late night
        prices.append(round(p, 2))
    return prices
