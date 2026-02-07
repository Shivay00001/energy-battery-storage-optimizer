import argparse
from src.optimizer import BatteryOptimizer
from src.market_data import generate_price_curve

def main():
    parser = argparse.ArgumentParser(description="Battery Storage Optimizer")
    parser.add_argument("--capacity", type=float, default=100.0, help="Battery Capacity (MWh)")
    parser.add_argument("--power", type=float, default=50.0, help="Max Power (MW)")
    
    args = parser.parse_args()
    
    print(f"Running Optimization for {args.capacity}MWh / {args.power}MW System...")
    
    prices = generate_price_curve()
    optimizer = BatteryOptimizer(capacity_mwh=args.capacity, power_mw=args.power)
    
    results = optimizer.optimize(prices)
    
    print("\n--- Optimization Results (24h) ---")
    print(results.to_markdown(index=False, floatfmt=".2f"))
    
    total_revenue = sum((results['discharge_mw'] * results['price']) - (results['charge_mw'] * results['price']))
    print(f"\n💰 Total Daily Profit: ${total_revenue:,.2f}")

if __name__ == "__main__":
    main()
