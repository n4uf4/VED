import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Membaca data
file_path = r'C:\VED\codeVED2\(2026)6. Data Latihan.csv'
data = pd.read_csv(file_path)

#Mengatur tema tampilan
sns.set_theme(style="whitegrid")

#Histogram 
plt.figure(figsize=(10, 5))
sns.histplot(data=data, x='Jumlah_Unit', bins=25, color='steelblue')
plt.title('Distribusi Data Jumlah Unit (Histogram)')
plt.xlabel('Jumlah Unit')
plt.ylabel('Frekuensi')
plt.tight_layout()
plt.show()

#Boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(
    data=data, 
    x='Metode_Pengiriman', 
    y='Jumlah_Unit', 
    palette='Set2'
)
plt.title('Sebaran Jumlah Unit Berdasarkan Metode Pengiriman (Box Plot)')
plt.xlabel('Metode Pengiriman')
plt.ylabel('Jumlah Unit')
plt.tight_layout()
plt.show()

#Scaterplot
plt.figure(figsize=(10, 5))
sns.scatterplot(data=data, x='Jumlah_Unit', y='Biaya_Logistik_Juta', color='cornflowerblue', alpha=0.6)
plt.title('Hubungan antara Jumlah Unit dan Biaya Logistik')
plt.xlabel('Jumlah Unit')
plt.ylabel('Biaya Logistik (Juta Rupiah)')
plt.tight_layout()
plt.show()

#Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, 
    x='Metode_Pengiriman', 
    y='Jumlah_Unit', 
    hue='Status_Pengiriman', 
    palette='Set2'
)
plt.title('Sebaran Jumlah Unit Berdasarkan Metode dan Status Pengiriman')
plt.xlabel('Metode Pengiriman')
plt.ylabel('Jumlah Unit')
plt.legend(title='Status Pengiriman')
plt.tight_layout()
plt.show()