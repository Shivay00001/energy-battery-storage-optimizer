# Energy Battery Storage Optimizer

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Optimization](https://img.shields.io/badge/Method-Linear_Programming-green.svg)](https://en.wikipedia.org/wiki/Linear_programming)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade energy optimization engine** for Battery Energy Storage Systems (BESS). This repository utilizes Linear Programming (PuLP) to determine the optimal charge/discharge schedule for a battery asset, maximizing revenue against day-ahead electricity market prices.

## 🚀 Features

- **Revenue Maximization**: Optimizes arbitrage opportunities (Buy Low, Sell High).
- **Constraints Handling**: Respects physical limits (Charge Rate, Capacity, Efficiency).
- **Day-Ahead Planning**: Generates 24-hour dispatch schedules.
- **Visualization**: Plots optimal dispatch against price curves (ASCII or Matplotlib).

## 📁 Project Structure

```
energy-battery-storage-optimizer/
├── src/
│   ├── optimizer.py      # LP Solver Logic
│   ├── market_data.py    # Price simulation
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/energy-battery-storage-optimizer.git

# Install
pip install -r requirements.txt

# Run Optimizer
python src/main.py --capacity 100 --power 50
```

## 📄 License

MIT License
