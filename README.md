# Physics-Based Energy and Efficiency Analysis of a Plug-In Hybrid Vehicle (PHEV)

## Project Overview

This project analyzes real-world trip data from a Plug-In Hybrid Electric Vehicle (PHEV) test campaign.  
The objective is to reconstruct total energy input, evaluate energy efficiency per trip, and analyze how driving conditions influence energy consumption.

The analysis is physics-based and focuses on energy flow reconstruction rather than purely statistical modeling.

---

## Objectives

- Convert fuel consumption to thermodynamic energy input
- Combine fuel and battery energy into total energy per trip
- Compute specific energy consumption (Wh/km)
- Estimate drivetrain efficiency
- Analyze the influence of speed and driving regime
- Extend analysis with uncertainty propagation and regression modeling

---

## Dataset

Dataset: JRC PHEV Test Campaign

Each row represents an individual trip and contains:

- Trip duration
- Distance [km]
- Fuel consumed [liters]
- Battery energy [kWh]
- Motor energy [kWh]
- State of charge (SOC) variation
- Mean velocity
- Acceleration statistics
- Urban / rural / motorway share
- Ambient temperature

This is aggregated trip-level data, not high-frequency time series data.

---

## Physical Assumptions

Fuel energy conversion:

Gasoline lower heating value (LHV) is assumed as:

LHV ≈ 8.9 kWh per liter

Total energy input per trip:

E_total = E_fuel + E_battery

Specific energy consumption:

Wh/km = (E_total × 1000) / Distance

Drivetrain efficiency (engineering estimate):

η ≈ Motor energy / Total energy input

Note:
Motor energy is used as an approximation of mechanical output. This assumes drivetrain and inverter losses are partially embedded in measured values.

---

## Repository Structure


```
PHEV_Energy_Analysis/
│
├── data/
│   └── JRC_Dataset_PHEV_test_campaign_20240920.xlsx
│
├── src/
│   ├── load_data.py
│   ├── energy_analysis.py
│   ├── efficiency_models.py
│   ├── uncertainty_analysis.py
│   ├── regression_model.py
│   └── visualization.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── results/
│   ├── figures/
│   └── tables/
│
├── main.py
├── requirements.txt
└── README.md
```


---

## Branch Structure

- `main`  
  Stable version with physics-based energy reconstruction and visualization.

- `feature/uncertainty-propagation`  
  Monte Carlo analysis of uncertainty in fuel LHV and battery measurement.

- `feature/regression-analysis`  
  Predictive model for energy consumption based on driving metrics.

- `exploratory-analysis`  
  Early-stage exploratory notebook work.

---

## Key Questions

- How much of total trip energy comes from fuel vs battery?
- How does mean velocity affect Wh/km?
- Does higher urban share increase or decrease efficiency?
- How sensitive is energy consumption to uncertainty in fuel properties?
- Can energy consumption be predicted from measurable driving metrics?

---

## Methods

1. Data cleaning and preprocessing
2. Energy conversion from physical units
3. Specific energy normalization
4. Efficiency estimation
5. Monte Carlo uncertainty propagation
6. Linear regression modeling (physics-informed features)

---

## Example Results (To Be Populated)

- Energy consumption vs mean speed
- Energy consumption vs urban share
- Distribution of drivetrain efficiency
- Monte Carlo uncertainty bounds
- Regression coefficients and model performance

---

## Tools and Technologies

- Python
- pandas
- numpy
- matplotlib
- scikit-learn

---

## Engineering Discussion

This project emphasizes:

- Energy conservation principles
- Hybrid powertrain energy pathways
- Sensitivity to driving regime
- Uncertainty propagation in engineering systems
- Modular and reproducible computational modeling

The analysis framework can be extended to:
- Parameter estimation 
- Comparison of hybrid strategies
- Sensitivity analysis
- Optimization of driving efficiency

---

