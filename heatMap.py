import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import geopandas as gpd

# Simulated global temperature anomalies (per grid or region)
shapefile_path = "./ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
world_data = gpd.read_file(shapefile_path)
# Simulated temperature change data for countries
world_data['temperature_change'] = world_data['POP_EST'] * 0.000001  # Simulated values for demonstration

# Simulated city-specific data for top 10 temperature changes
city_data = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Tokyo', 'Mumbai', 'Shanghai', 
             'London', 'Moscow', 'Sydney', 'Paris', 'Rio de Janeiro'],
    'Temperature_Change': [2.1, 1.9, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0]
})

# Simulated keywords for word cloud
keywords = {
    "greenhouse gases": 100, "fossil fuels": 80, "deforestation": 60,
    "renewable energy": 50, "carbon footprint": 40, "urbanization": 30,
    "industrialization": 20, "climate policy": 15, "ocean warming": 10,
    "air pollution": 5
}

# 1. Generate World Heatmap
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
world_data.plot(column='temperature_change', cmap='OrRd', legend=True, ax=ax, edgecolor='black')
ax.set_title("Global Temperature Changes (Simulated)", fontsize=14)
plt.show()

# 2. Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(keywords)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Keywords Impacting Global Temperature Change", fontsize=16)
plt.show()

# 3. Generate Bar Chart for Top 10 Cities
city_data_sorted = city_data.sort_values(by='Temperature_Change', ascending=False)
plt.figure(figsize=(10, 6))
bars = plt.bar(city_data_sorted['City'], city_data_sorted['Temperature_Change'], color='skyblue', edgecolor='black')
plt.title("Top 10 Cities with Highest Temperature Changes", fontsize=14)
plt.xlabel("City", fontsize=12)
plt.ylabel("Temperature Change (°C)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)

# Add values on top of bars for better context
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
             f'{bar.get_height():.1f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()
