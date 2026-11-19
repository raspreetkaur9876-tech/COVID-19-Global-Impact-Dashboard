
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
country = pd.read_csv("dataset/country_summary.csv")
daily = pd.read_csv("dataset/daily_trends.csv")

# Set graph style
sns.set_theme(style="whitegrid")

# Graph 1: Top 10 countries by cases
top_cases = country.sort_values(
    "Confirmed", ascending=False
).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_cases, x="Confirmed",
            y="Country/Region")
plt.title("Top 10 Countries - Confirmed COVID-19 Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("visualizations/top_cases.png")
plt.show()

# Graph 2: Top 10 countries by deaths
top_deaths = country.sort_values(
    "Deaths", ascending=False
).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_deaths, x="Deaths",
            y="Country/Region")
plt.title("Top 10 Countries - COVID-19 Deaths")
plt.xlabel("Deaths")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("visualizations/top_deaths.png")
plt.show()

# Graph 3: Global cases trend
plt.figure(figsize=(12, 6))
plt.plot(daily["ObservationDate"],
         daily["Confirmed"])
plt.title("Global COVID-19 Cases Trend")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/cases_trend.png")
plt.show()

# Graph 4: Deaths and recoveries trend
plt.figure(figsize=(12, 6))
plt.plot(daily["ObservationDate"], daily["Deaths"],
         label="Deaths")
plt.plot(daily["ObservationDate"], daily["Recovered"],
         label="Recovered")
plt.title("Global Deaths and Recoveries Trend")
plt.xlabel("Date")
plt.ylabel("Total")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/deaths_recovered.png")
plt.show()

print("All COVID-19 graphs created successfully!")
