import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 1. Generarea datelor
np.random.seed(42)
zile_actiuni = pd.date_range(start="2023-01-01", periods=730, freq="D")
pret_initial = 100
schimbari_zilnice = np.random.normal(0, 0.02, size=730)
pret_inchidere = pret_initial * np.cumprod(1 + schimbari_zilnice)
# 2. Procesarea datelor
df_actiuni = pd.DataFrame({
    'Data': zile_actiuni,
    'Schimbare Zilnică (%)': schimbari_zilnice * 100,
    'Preț de Închidere': pret_inchidere
})
df_actiuni['Media Mobilă 30'] = df_actiuni['Preț de Închidere'].rolling(window=30).mean()
df_actiuni['Media Mobilă 100'] = df_actiuni['Preț de Închidere'].rolling(window=100).mean()
# Identificarea perioadelor în care prețul a fost peste media mobilă de 100 zile
perioade_peste_media_mobila = df_actiuni[df_actiuni['Preț de Închidere'] > df_actiuni['Media Mobilă 100']]
# 3. Vizualizare
plt.figure(figsize=(10, 6))
plt.plot(df_actiuni['Data'], df_actiuni['Preț de Închidere'], label='Preț de Închidere', color='blue')
plt.plot(df_actiuni['Data'], df_actiuni['Media Mobilă 30'], label='Media Mobilă 30 zile', color='orange')
plt.plot(df_actiuni['Data'], df_actiuni['Media Mobilă 100'], label='Media Mobilă 100 zile', color='green')
plt.fill_between(df_actiuni['Data'], df_actiuni['Preț de Închidere'], df_actiuni['Media Mobilă 100'], where=(df_actiuni['Preț de Închidere'] > df_actiuni['Media Mobilă 100']), color='yellow', alpha=0.3)
plt.xlabel('Ziua')
plt.ylabel('Prețul Acțiunii ($)')
plt.title('Prețul Acțiunii și Mediile Mobile')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
