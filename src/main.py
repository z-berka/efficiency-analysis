from load_data import load_dataset
from energy_analysis import (
    compute_fuel_energy,
    compute_total_energy,
    compute_specific_energy,
)
from efficiency_models import estimate_drivetrain_efficiency
from visualization import plot_energy_vs_speed

DATA_PATH = "../data/JRC_Dataset_PHEV_test_campaign_20240920.xlsx"

def main():
    df = load_dataset(DATA_PATH)
    df = compute_fuel_energy(df)
    df = compute_total_energy(df)
    df = compute_specific_energy(df)
    df = estimate_drivetrain_efficiency(df)

    plot_energy_vs_speed(df)

if __name__ == "__main__":
    main()
