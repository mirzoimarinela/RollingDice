import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generarea datelor
np.random.seed(42)
zile = pd.date_range(start="2023-01-01", periods=365, freq="D")
temperatura = np.random.randint(5, 36, size=365)
umiditate = np.random.randint(30, 91, size=365)
viteza_vantului = np.random.randint(0, 21, size=365)

# Crearea DataFrame-ului
df_meteo = pd.DataFrame({
    'Data': zile,
    'Temperatura': temperatura,
    'Umiditate': umiditate,
    'Viteza Vantului': viteza_vantului
})

# 2. Procesarea datelor
df_meteo['Temperatura Resimtita'] = df_meteo['Temperatura'] - 0.7 * (df_meteo['Umiditate'] / 100)
zi_max_temp_resimtita = df_meteo.loc[df_meteo['Temperatura Resimtita'].idxmax()]
zi_min_temp_resimtita = df_meteo.loc[df_meteo['Temperatura Resimtita'].idxmin()]

# 3. Vizualizare
# Grafic temperatura vs temperatura resimțită
plt.figure(figsize=(10, 6))
plt.plot(df_meteo['Data'], df_meteo['Temperatura'], label='Temperatura', color='red')
plt.plot(df_meteo['Data'], df_meteo['Temperatura Resimtita'], label='Temperatura Resimțită', color='blue')
plt.xlabel('Ziua')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura vs Temperatura Resimțită')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafic temperatura medie lunară
df_meteo['Luna'] = df_meteo['Data'].dt.month
temperatura_lunara = df_meteo.groupby('Luna')['Temperatura'].mean()

plt.figure(figsize=(10, 6))
temperatura_lunara.plot(kind='bar', color='green')
plt.xlabel('Luna')
plt.ylabel('Temperatura Medie (°C)')
plt.title('Temperatura Medie Lunara')
plt.tight_layout()
plt.show()
