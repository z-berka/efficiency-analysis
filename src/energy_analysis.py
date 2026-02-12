FUEL_LHV_KWH_PER_LITER = 8.9  

def compute_fuel_energy(df):
    df["Fuel Energy [kWh]"] = df["Fuel Consumed [lt]"] * FUEL_LHV_KWH_PER_LITER
    return df

def compute_total_energy(df):
    df["Total Energy Input [kWh]"] = (
        df["Fuel Energy [kWh]"] + df["Battery energy [kWh]"]
    )
    return df

def compute_specific_energy(df):
    df["Total Energy [Wh/km]"] = (
        df["Total Energy Input [kWh]"] * 1000 / df["Distance [km]"]
    )
    return df
