import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

# Load the Excel file (using raw string r'' to handle special characters and parentheses safely)
# Make sure your file is in the same folder as this script, or use the full path.
file_path = r'C:\VED\codeVED1\(2026)5. Data Visualisasi Part 1.xlsx'
data = pd.read_excel(file_path)

# Get the frequency of each product category
frekuensi = data['Kategori Produk'].value_counts()

#Pie Chart
import matplotlib.pyplot as plt
frekuensi = data['Kategori Produk'].value_counts()
plt.pie(frekuensi.values,labels=frekuensi.index,autopct='%1.1f%%')
plt.title('Proporsi Kategori Produk')
plt.show()



#Bar Chart
frekuensi = data['Kategori Produk'].value_counts()
plt.bar(frekuensi.index,frekuensi.values)
plt.title('Jumlah Transaksi berdasarkan Kategori Produk')
plt.xlabel('Kategori Produk')
plt.ylabel('Frekuensi')
plt.show()

#Word CLoud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
frekuensi = data['Kategori Produk'].value_counts()
wordcloud = WordCloud(width=800,height=400,background_color='white').generate_from_frequencies(frekuensi.to_dict())
plt.figure(figsize=(10,5))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title('Kategori Produk yang Dominan')
plt.show()