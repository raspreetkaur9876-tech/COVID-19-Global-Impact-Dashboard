# COVID-19 Global Impact Dashboard

## 1. Project Overview

The COVID-19 Global Impact Dashboard is a data analytics project designed to analyze the global impact of the COVID-19 pandemic.

This project uses historical COVID-19 data to examine confirmed cases, deaths, recoveries and country-wise trends.

The analysis is performed using Python, Pandas, Matplotlib, Seaborn and Microsoft Power BI.

## 2. Project Objectives

- Analyze worldwide COVID-19 cases.
- Identify countries with the highest confirmed cases.
- Compare country-wise deaths.
- Understand global COVID-19 trends over time.
- Calculate the case fatality rate and recovery rate.
- Present important findings through an interactive dashboard.

## 3. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Microsoft Power BI
- Excel
- GitHub

## 4. Dataset Description

The dataset contains historical COVID-19 records from January 22, 2020, to May 29, 2021.

It includes:
- Observation Date
- Province/State
- Country/Region
- Confirmed Cases
- Deaths
- Recovered Cases

The original dataset contains 306,429 records across 229 countries/regions.
## 5. Data Cleaning and Preparation

The dataset was cleaned and prepared using Python and the Pandas library.

The following steps were performed:

- Loaded the original COVID-19 dataset using Pandas.
- Converted missing Province/State values to "Not Specified".
- Converted the ObservationDate column into datetime format.
- Checked for and removed duplicate records.
- Converted Confirmed, Deaths, and Recovered columns into numeric data types.
- Identified negative values, which may represent historical data corrections.
- Generated cleaned data and summary CSV files for Power BI.

The cleaned dataset was used for further analysis and dashboard development.

## 6. Key Performance Indicators (KPIs)

The Power BI dashboard includes the following KPIs:

- **Total Confirmed Cases:** Approximately 170 million
- **Total Deaths:** Approximately 4 million
- **Total Recovered:** Approximately 107 million
- **Fatality Rate:** Approximately 2.08%

*Note: These figures represent the historical dataset ending May 29, 2021, not current COVID-19 statistics.*

## 7. Key Findings

1. The United States, India and Brazil were among the countries with the highest confirmed COVID-19 cases in the historical dataset.
2. The United States, Brazil and India were among the countries with the highest reported deaths.
3. COVID-19 cases increased significantly during the analyzed period.
4. The dashboard compares global confirmed cases, deaths and recoveries over time.
5. The overall historical case fatality rate was approximately 2.08%.

## 8. Dashboard Features

The Power BI dashboard contains:

- Total Cases KPI Card
- Total Deaths KPI Card
- Total Recovered KPI Card
- Fatality Rate KPI Card
- Top 10 Countries by Confirmed Cases
- Top 10 Countries by Deaths
- Global COVID-19 Cases Trend
- Global Deaths vs Recoveries Trend

## 9. Conclusion

This project demonstrates how Python and Power BI can be used to transform raw COVID-19 data into meaningful insights.

Data cleaning, exploratory analysis and visualization helped identify country-wise differences and historical trends.

The project improved practical skills in data analysis, data visualization and dashboard development.

## 10. Project Limitations

- The dataset ends on May 29, 2021.
- Vaccination data is not included.
- Negative historical values require careful interpretation.
- Results depend on the completeness and accuracy of reported data.

---

**Project:** COVID-19 Global Impact Dashboard

**Tools:** Python, Pandas, Matplotlib, Seaborn and Power BI.
