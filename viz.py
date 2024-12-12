import pandas as pd
import matplotlib.pyplot as plt

# Simulated dataset for global temperature anomalies
data = pd.DataFrame({
    'Year': [1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020],
    'Temperature_Anomaly': [-0.12, -0.10, -0.16, -0.20, -0.14, -0.06, 0.03, 0.02, 0.06, 0.14, 0.24, 0.38, 0.45, 0.64, 0.98]
})

# Calculate decade-wise averages
data['Decade'] = (data['Year'] // 10) * 10
decade_avg = data.groupby('Decade')['Temperature_Anomaly'].mean().reset_index()

# Create the main figure and small panels
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Main figure: Global temperature anomalies over time
axs[0, 0].plot(data['Year'], data['Temperature_Anomaly'], color='grey', label='1880-1999', linewidth=2)
recent_years = data[data['Year'] >= 2000]
axs[0, 0].plot(recent_years['Year'], recent_years['Temperature_Anomaly'], color='red', label='2000-2020', linewidth=3)
axs[0, 0].set_title("Global Temperature Change (1880-2020)", fontsize=14)
axs[0, 0].set_xlabel("Year", fontsize=12)
axs[0, 0].set_ylabel("Temperature Anomaly (°C)", fontsize=12)
axs[0, 0].legend()
axs[0, 0].grid(True)

# Small panel 1: Zoomed-in view of recent years (2000-2020)
axs[0, 1].plot(recent_years['Year'], recent_years['Temperature_Anomaly'], color='red', linewidth=3)
axs[0, 1].set_title("Recent Years (2000-2020)", fontsize=14)
axs[0, 1].set_xlabel("Year", fontsize=12)
axs[0, 1].set_ylabel("Temperature Anomaly (°C)", fontsize=12)
axs[0, 1].grid(True)

# Small panel 2: Decade-wise average temperature anomalies
axs[1, 0].bar(decade_avg['Decade'], decade_avg['Temperature_Anomaly'], color='skyblue', edgecolor='black')
axs[1, 0].set_title("Decade-wise Average Temperature Anomalies", fontsize=14)
axs[1, 0].set_xlabel("Decade", fontsize=12)
axs[1, 0].set_ylabel("Temperature Anomaly (°C)", fontsize=12)
axs[1, 0].grid(True)

# Hide the unused subplot
axs[1, 1].axis('off')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
