
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/covid_cleaned.csv")

df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])

# Get latest available date
latest_date = df["ObservationDate"].max()

# Select latest date records
latest_data = df[df["ObservationDate"] == latest_date]

# Calculate global statistics
total_cases = latest_data["Confirmed"].sum()
total_deaths = latest_data["Deaths"].sum()
total_recovered = latest_data["Recovered"].sum()

# Calculate rates
fatality_rate = (total_deaths / total_cases) * 100 if total_cases > 0 else 0

recovery_rate = (total_recovered / total_cases) * 100 if total_cases > 0 else 0

# Display results
print("===== COVID-19 GLOBAL ANALYSIS =====")

print("Latest Date:", latest_date.date())
print("Total Confirmed Cases:", total_cases)
print("Total Deaths:", total_deaths)
print("Total Recovered:", total_recovered)

print("Case Fatality Rate:", round(fatality_rate, 2), "%")
print("Recovery Rate:", round(recovery_rate, 2), "%")

# Country-wise analysis
country_summary = latest_data.groupby("Country/Region")[
    ["Confirmed", "Deaths", "Recovered"]
].sum().reset_index()

# Sort countries by confirmed cases
country_summary = country_summary.sort_values(
    by="Confirmed", ascending=False
)

# Save country analysis
country_summary.to_csv(
    "dataset/country_summary.csv", index=False
)

# Save daily global trends
daily_trends = df.groupby("ObservationDate")[
    ["Confirmed", "Deaths", "Recovered"]
].sum().reset_index()

daily_trends.to_csv(
    "dataset/daily_trends.csv", index=False
)

print("\nTop 10 Countries by Confirmed Cases:")
print(country_summary.head(10))

print("\nAnalysis files saved successfully!")
