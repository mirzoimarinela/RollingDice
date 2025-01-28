import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generarea datelor
np.random.seed(42)
id_utilizatori = np.random.randint(1, 1001, size=10000)
id_filme = np.random.randint(1, 101, size=10000)
ratinguri = np.random.randint(1, 6, size=10000)

# Crearea DataFrame-ului
df_ratinguri = pd.DataFrame({
    'ID Utilizator': id_utilizatori,
    'ID Film': id_filme,
    'Rating': ratinguri
})

# 2. Procesarea datelor
rating_medii = df_ratinguri.groupby('ID Film')['Rating'].mean()
primele_5_filme = rating_medii.nlargest(5)
filme_sub_3_5 = df_ratinguri.groupby('ID Film').filter(lambda x: len(x) > 50 and x['Rating'].mean() < 3.5)

# 3. Vizualizare
# Histogramă pentru ratinguri
plt.figure(figsize=(10, 6))
plt.hist(df_ratinguri['Rating'], bins=5, color='purple', edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Frecvență')
plt.title('Distribuția Ratingurilor Filmelor')
plt.tight_layout()
plt.show()

# Grafic de tip bară pentru primele 5 filme cu cel mai mare rating
plt.figure(figsize=(10, 6))
primele_5_filme.plot(kind='bar', color='cyan')
plt.xlabel('ID Film')
plt.ylabel('Rating Mediu')
plt.title('Primele 5 Filme cu Cel Mai Mare Rating Mediu')
plt.tight_layout()
plt.show()

# Scatter pentru numărul de evaluări vs. rating mediu
numar_evaluari = df_ratinguri.groupby('ID Film').size()
plt.figure(figsize=(10, 6))
plt.scatter(numar_evaluari, rating_medii, color='red')
plt.xlabel('Număr de Evaluări')
plt.ylabel('Rating Mediu')
plt.title('Număr de Evaluări vs Rating Mediu')
plt.tight_layout()
plt.show()
