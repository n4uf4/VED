import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from statsmodels.graphics.mosaicplot import mosaic 


file_path = r'C:\VED\codeVED2\(2026)6. Data Latihan.csv'
data = pd.read_csv(file_path)

sns.countplot(data=data,x='Wilayah',hue="Status_Pengiriman")

plt.title('Wilayah vs Status Pengiriman')
plt.show()

#Membuat Mosaic Plot
fig, rects = mosaic(data.dropna(subset=['Wilayah', 'Status_Pengiriman']),
    index=['Wilayah', 'Status_Pengiriman'], 
    title='Mosaic Plot: Wilayah vs Status Pengiriman',
        gap=0.03,
        labelizer=lambda k: k[1],
        label_rotation=15
)

fig.set_size_inches(11, 6)
plt.show()

#Rugplot
plt.figure(figsize=(10, 3))
sns.rugplot(data=data, x='Nilai_Penjualan_Juta', height=0.15, color='red')
plt.title('Rug Plot Nilai Penjualan')
plt.xlabel('Nilai Penjualan (Juta Rupiah)')
plt.tight_layout()
plt.show()

#Histogram
plt.figure(figsize=(10, 5))
sns.histplot(data=data, x='Nilai_Penjualan_Juta', bins=20, color='steelblue')
plt.title('Histogram Nilai Penjualan')
plt.xlabel('Nilai Penjualan (Juta Rupiah)')
plt.ylabel('Frekuensi')
plt.show()

#Density plot
plt.figure(figsize=(10, 5))
sns.kdeplot(data=data, x='Nilai_Penjualan_Juta', fill=True, color='red', bw_adjust=1)
plt.title('Density Plot Nilai Penjualan')
plt.xlabel('Nilai Penjualan (Juta Rupiah)')
plt.ylabel('Density')
plt.show()

#boxplot
plt.figure(figsize=(7, 5))
sns.boxplot(data=data, y='Nilai_Penjualan_Juta', color='skyblue',width=0.3,showfliers=True)
plt.title('Boxplot Nilai Penjualan')
plt.ylabel('Nilai Penjualan (Juta Rupiah)')
plt.show()

#violinplot
plt.figure(figsize=(7, 5))
sns.violinplot(data=data, y='Nilai_Penjualan_Juta', color='lightgreen', inner='quartile', cut=0)
plt.title('Violin Plot Nilai Penjualan')
plt.ylabel('Nilai Penjualan (Juta Rupiah)')
plt.show()

#scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Nilai_Penjualan_Juta", y="Biaya_Logistik_Juta", color="steelblue", alpha=0.7)
plt.title("Scatter Plot Penjualan vs Biaya Logistik")
plt.xlabel("Nilai Penjualan (Juta Rupiah)")
plt.ylabel("Biaya Logistik (Juta Rupiah)")
plt.tight_layout()
plt.show()

#Heatmap menggunakan nilai matriks

#memilih variabel numerik
data_num = data[["Nilai_Penjualan_Juta", "Biaya_Logistik_Juta"]]
#Membuat matriks korelasi
matriks_korelasi = data_num.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(matriks_korelasi, annot=True, cmap='coolwarm',fmt=".2f",vmin=1,vmax=1, center=0, linewidths=0.5)
plt.title("Heatmap Korelasi Nilai Penjualan dan Biaya Logistik")
plt.tight_layout()
plt.show()

#side by side boxplot
plt.figure(figsize=(9, 5))
sns.boxplot(data=data[["Nilai_Penjualan_Juta", "Biaya_Logistik_Juta"]], palette="Set2", legend=False)
plt.title("Box Plot Penjualan Berdasarkan Wilayah")
plt.xlabel("Wilayah")
plt.ylabel("Nilai Penjualan (Juta)")
plt.show()

# Menghitung total penjualan setiap wilayah
data_tree = data.groupby("Wilayah", as_index=False)["Nilai_Penjualan_Juta"].sum()
# Membuat Treemap
fig = px.treemap(
    data_tree, 
    path=["Wilayah"], 
    values="Nilai_Penjualan_Juta", 
    color="Wilayah", 
    color_discrete_sequence=px.colors.qualitative.Set2,
    title="Treemap Total Penjualan Berdasarkan Wilayah"
)

# Menampilkan label, nilai, dan persentase
fig.update_traces(textinfo="label+value+percent root")

fig.update_layout(width=950, height=550)

fig.show()


# X1 = Wilayah
# X2 = Status Pengiriman
# X3 = Jumlah Unit

# membuat data frame bantuan
data_sankey = data.groupby(["Wilayah", "Status_Pengiriman"], as_index=False)["Jumlah_Unit"].sum()

# Labeling input dan otput
source_nodes = ["Wilayah: " + str(x) for x in data["Wilayah"].dropna().unique()]
target_nodes = ["Status: " + str(x) for x in data["Status_Pengiriman"].dropna().unique()]
labels = source_nodes + target_nodes

node_map = {name: i for i, name in enumerate(labels)}
source = [node_map["Wilayah: " + str(x)] for x in data_sankey["Wilayah"]]
target = [node_map["Status: " + str(x)] for x in data_sankey["Status_Pengiriman"]]
value = data_sankey["Jumlah_Unit"].tolist()

# pendefinisian besar/kecil aliran
fig = go.Figure(go.Sankey(node=dict(pad=20, thickness=20, label=labels), link=dict(source=source, target=target, value=value)))
fig.update_layout(title="Sankey Wilayah & Status (Bobot Jumlah Unit)", font_size=12, width=950, height=500)
fig.show()

#Treemap 3 variabel kategori

# Menghitung frekuensi kombinasi 3 kategori
data_tree = (data.groupby(["Kanal_Penjualan", "Gudang_Pemenuhan", "Status_Pengiriman"]).size().reset_index(name="Frekuensi"))
# Membuat Treemap
fig = px.treemap(data_tree, path=["Kanal_Penjualan", "Gudang_Pemenuhan", "Status_Pengiriman"], values="Frekuensi", color="Kanal_Penjualan",
                 color_discrete_sequence=px.colors.qualitative.Set2,
                 title="Treemap Kanal Penjualan, Gudang, dan Status"
)

fig.update_traces(textinfo="label+value+percent parent")
fig.update_layout(width=1100, height=650)
fig.show()
