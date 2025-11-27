import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("owid-covid-data.csv")

# Filter for one country
country = "India"
data = df[df["location"] == country].copy()

# Plot total cases over time
plt.plot(data["date"], data["total_cases"])
plt.title(f"Total COVID-19 Cases in {country}")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.show()


# Plot daily new cases
plt.plot(data["date"], data["new_cases"])
plt.title(f"Daily new Covid-19 cases in {country}")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.show()

# Find peak case day
peak_day = data.loc[data["new_cases"].idxmax()]

print("Peak cases Day:", peak_day["date"].date(),
      "->", int(peak_day["new_cases"]))


# Calculate Case fatality rate(CFR)
data["cfr"] = data["total_deaths"] / data["total_cases"]
print("Latest CFR:", data["cfr"].iloc[-1])

# Compare multiple countries
countries = ["India", "United State", "Brazil"]
subset = df[df["location"].isin(countries)]
subset["date"] = pd.to_datetime(subset["date"])

for c in countries:
    temp = subset[subset["location"] == c]
    plt.plot(temp["date"], temp["total_cases"], label=c)

    plt.legend()
    plt.title("Total Cocid 19 cases by Country")
    plt.xlabel("Date")
    plt.ylabel("Total cases")
    plt.show()
