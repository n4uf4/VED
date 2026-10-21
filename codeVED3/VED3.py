import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
data=pd.read_excel(r'C:\VED\codeVED3\(2026)7. Data Studi Kasus.xlsx')
data_harga=data['Harga/unit']
data_harga.describe()

#Ukuran pemusatan
rata_rata=data_harga.mean() #menghitung rata-rata
median=data_harga.median() #menghitung median
modus=data_harga.mode() #menghitung modus
#Ukuran Penyebaran
standar_deviasi=data_harga.std() #menghitung standar deviasi
varians=data_harga.var() #menghitung varians
range=data_harga.max()-data_harga.min() #menghitung range
inter_quartile_range=data_harga.quantile(0.75)-data_harga.quantile(0.25)
print("UKURAN PEMUSATAN")
print("Rata-Rata:",rata_rata)
print("Median:",median)
print("Modus:",modus)
print("UKURAN PENYEBARAN")
print("Standar Deviasi:",standar_deviasi)
print("Varians:",varians)
print("Range:",range)
print("Inter Quartile Range:",inter_quartile_range)

#Bentuk Distribusi
skewness=data_harga.skew() #menghitung skewness
kurtosis=data_harga.kurt()
print("Skewness:",skewness)
print("Kurtosis:",kurtosis)

#Analisis Korelasi
koefisien_korelasi=data_harga.corr(data['Qty'], method="pearson")
print("Koefisien Korelasi:",koefisien_korelasi)
#method yang lain: kendall, spearman

#Analisis Kovarian
kovarian=data_harga.cov(data['Qty'])
print("Kovarian:",kovarian)

# Memulihkan fungsi built-in 'range' jika sebelumnya tertimpa oleh variabel biasa
if 'range' in globals() and not isinstance(globals()['range'], type):
    del globals()['range']

x = data['Qty']
# 1. Menghitung ukuran dasar
n = len(x)
minimum = int(x.min())
maksimum = int(x.max())
R = maksimum - minimum

# 2. Menentukan jumlah kelas (Sturges)
k = max(1, round(1 + 3.322 * np.log10(n)))

# 3. Menentukan panjang kelas untuk data diskrit
lebar = max(1, math.ceil((R + 1) / k))

# 4. Membentuk interval kelas otomatis
jumlah_kelas = math.ceil((R + 1) / lebar)
batas = [minimum - 0.5 + i * lebar for i in range(jumlah_kelas + 1)]
label = [f"{minimum + i*lebar}-{minimum + (i+1)*lebar-1}" for i in range(jumlah_kelas)]
kelas = pd.cut(x, bins=batas, labels=label)

# 5. Menghitung frekuensi
frekuensi = kelas.value_counts(sort=False)
tabel = pd.DataFrame({"Frekuensi": frekuensi})
tabel["Persentase (%)"] = (tabel["Frekuensi"] / n * 100).round(2)
tabel["Frekuensi Kumulatif"] = (tabel["Frekuensi"].cumsum())
tabel["Persentase Kumulatif (%)"] = (tabel["Persentase (%)"].cumsum()).round(2)

# 6. Menampilkan hasil
print("Jumlah Data:", n)
print("Minimum:", minimum)
print("Maximum:", maksimum)
print("Range:", R)
print("Jumlah Kelas Sturges:", k)
print("Panjang Kelas:", lebar)
print(tabel)

# Distribusi frekuensi relatif berdasarkan Produk
tabel = pd.DataFrame({"Frekuensi": data["Status"].value_counts(), "Proporsi": data["Status"].value_counts(normalize=True)})
# Menghitung persentase
tabel["Persentase (%)"] = tabel["Proporsi"] * 100
print(tabel.round(2))

#Tabulasi Silang dua variabel kategori
tabel_silang = pd.crosstab(index=data["Status"], columns=data["Channel"] ,margins=True, margins_name="Total")
print(tabel_silang)

#Ringkasan statistik Qty berdasarkan Channel
ringkasan = data.groupby("Channel")["Qty"].agg(Frekuensi="count",
                                               Total="sum", 
                                               Mean="mean", 
                                               Median="median", 
                                               Standar_Deviasi="std",
                                               Minimum="min",
                                                Maximum="max")
print(ringkasan.round(2))

# Ringkasan statistik Qty berdasarkan Channel dan Status
ringkasan = data.groupby(["Channel", "Status"])["Qty"].agg(["count","sum", "mean", "std"])
print(ringkasan.round(2))

# Membuat pivot tabel pendapatan bruto
pivot = pd.pivot_table(data, values="bruto", index="Status", columns="Channel", aggfunc="sum", fill_value=0, margins=True, margins_name="Total")
print(pivot)

#Looping 1: EDA Univariate
#Bagaimana distribusi jumlah penjualan
#Teknik visualisasi Boxplot
data1=data['Qty']
sns.boxplot(data1)
plt.show()

ringkasan = data1.describe()
skewness=data1.skew()
print("Summary Statistics:", ringkasan)
print("Skewness:", skewness)

# Melakukan grouping berdasarkan 'Channel' menjumlahkan kolom 'Qty'
data["Qty"]=data["Qty"].replace(40,4)
data.groupby("Channel")["Qty"].sum()

# Menghitung ringkasan grup terlebih dahulu agar menjadi daftar ringkasan yang lebih mudah dibaca
ringkasan_df = data.groupby("Channel")["Qty"].sum().reset_index()

sns.barplot(x="Channel", y="Qty", data=ringkasan_df, errorbar=None)

plt.title("Total Qty berdasarkan Channel")
plt.xlabel("Channel")
plt.ylabel("Total Qty (unit)")
plt.show()

#Looping 3 : EDA Multivariate
#Qty berdasarkan Channel dan Status transaksi
#salin data agar tidak mengubah data asli
data3 = data.copy()
# Simulasi perubahan transaksi T007
data3['Qty']=data['Qty'].replace(40,4)
#Membuat ringkasan multivariate
pivot = pd.pivot_table(data3, values="Qty", index="Channel", columns="Status", aggfunc="sum", fill_value=0)
# Menentukan urutan kategori
status = ["Selesai", "Return", "Cancel"]
pivot = pivot.reindex(index=["Online", "Store"], columns=status, fill_value=0)
#Menambahkan Total
pivot["Total"] = pivot.sum(axis=1)
pivot.loc["Total"] = pivot.sum(axis=0)
print(pivot)

fig = px.treemap(data3, path=["Channel", "Status"], values="Qty", color="Qty", color_continuous_scale="Blues", title="Treemap Total Qty berdasarkan Channel dan Status, dengan wrna = bruto")
fig.show()
