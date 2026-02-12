def estimate_drivetrain_efficiency(df):
    # Using motor energy as mechanical output estimate
    df["Estimated Efficiency"] = (
        df["Motor energy [kWh]"] / df["Total Energy Input [kWh]"]
    )
    return df
