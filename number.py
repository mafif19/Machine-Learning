import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Generate dua set data contoh
data1 = np.random.rand(100)  # Data acak antara 0 dan 1
data2 = np.random.rand(100)  # Data acak antara 0 dan 1

# Menghitung koefisien korelasi antara dua set data
correlation_coefficient = np.corrcoef(data1, data2)[0, 1]

# Membuat plot scatter dari dua set data
plt.scatter(data1, data2, color='blue', label=f'Korelasi: {correlation_coefficient:.2f}')

# Menambahkan garis regresi linier
slope, intercept, r_value, p_value, std_err = linregress(data1, data2)
plt.plot(data1, slope*data1 + intercept, color='red', label='Garis Regresi Linier')

# Menambahkan label sumbu dan judul plot
plt.xlabel('Data 1')
plt.ylabel('Data 2')
plt.title('Grafik Scatter dengan Garis Regresi Linier')

# Menambahkan legenda
plt.legend()

# Menampilkan plot
plt.grid(True)
plt.show()


