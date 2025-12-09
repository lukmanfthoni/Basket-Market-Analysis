# Basket-Market-Analysis
Aplikasi web interaktif untuk menganalisis pola pembelian pelanggan menggunakan algoritma Apriori. Aplikasi ini membantu bisnis memahami produk mana yang sering dibeli bersama-sama dan memberikan rekomendasi strategi bisnis.


## ✨ Fitur

- 🔍 **Analisis Asosiasi** - Temukan pola pembelian produk yang sering dibeli bersama
- 📊 **Visualisasi Metrik** - Support, Confidence, dan Lift dijelaskan secara interaktif
- 🎯 **Rekomendasi Produk** - Sistem rekomendasi otomatis berdasarkan item yang dipilih
- 💡 **Strategi Bisnis** - Saran actionable untuk cross-selling, bundling, dan inventory management
- ⚙️ **Parameter Kustomisasi** - Sesuaikan minimum support dan confidence
- 📱 **Responsive Design** - Tampilan optimal di desktop dan mobile
- 📤 **Upload Data** - Kemampuan upload file CSV sendiri

## 🎬 Demo
https://basket-market-analysis-yz.streamlit.app/

## 📖 Cara Menggunakan

### 1. Memulai Aplikasi

```bash
streamlit run app.py
``` <-- untuk local

https://basket-market-analysis-yz.streamlit.app/ <-- via streamlit

### 2. Memilih Item untuk Analisis

- Pilih item dari dropdown menu
- Contoh: pilih "coffee" untuk melihat produk apa yang sering dibeli bersamaan

### 3. Mengatur Parameter (di Sidebar)

**Minimum Support (0.01 - 0.1)**
- Seberapa sering kombinasi item muncul
- Nilai rendah: lebih banyak kombinasi ditemukan
- Nilai tinggi: hanya kombinasi paling populer

**Minimum Confidence (0.1 - 1.0)**
- Probabilitas pembelian item B jika membeli item A
- Nilai tinggi (>0.5): rekomendasi lebih akurat
- Nilai rendah (<0.5): lebih banyak variasi rekomendasi

### 4. Membaca Hasil Analisis

**Metrik yang Ditampilkan:**

- **Support**: Seberapa sering kombinasi muncul dalam transaksi
- **Confidence**: Probabilitas membeli produk B saat membeli produk A
- **Lift**: Kekuatan hubungan antara dua produk
  - Lift > 1: Sering dibeli bersama
  - Lift = 1: Tidak ada hubungan khusus
  - Lift < 1: Jarang dibeli bersama

### 5. Menerapkan Rekomendasi Bisnis

Aplikasi memberikan 4 strategi utama:
1. **Cross-Selling** - Penempatan produk strategis
2. **Bundle Promotion** - Paket promosi kombinasi produk
3. **Sistem Rekomendasi** - "Frequently Bought Together"
4. **Inventory Management** - Manajemen stok yang efisien

## 📁 Struktur Proyek

```
market-basket-analysis/
│
├── app.py                      # File utama aplikasi Streamlit
├── bread basket.csv            # Dataset transaksi
├── requirements.txt            # Dependencies Python
├── README.md                   # Dokumentasi ini
│
├── notebooks/                  # (Opsional) Jupyter notebooks
│   └── market_basket_analysis.ipynb
│
└── assets/                     # (Opsional) Gambar dan aset lain
    └── demo.png
```

## 🛠 Teknologi

- **[Streamlit](https://streamlit.io/)** - Framework web app Python
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation
- **[MLxtend](http://rasbt.github.io/mlxtend/)** - Machine learning extensions (Apriori algorithm)
- **Python 3.7+** - Programming language

## 📊 Dataset

### Format Data

File CSV harus memiliki minimal 2 kolom:

| Column | Type | Description |
|--------|------|-------------|
| Transaction | Integer | ID unik untuk setiap transaksi |
| Item | String | Nama produk yang dibeli |

### Contoh Data

```csv
Transaction,Item
1,Bread
1,Coffee
2,Coffee
2,Tea
2,Cake
3,Bread
3,Pastry
```

### Dataset yang Disediakan

Dataset `bread basket.csv` berisi:
- **20,507 transaksi**
- **94 item unik**
- **9,465 transaksi unik**
- Data dari bakery/coffee shop
- Periode: Oktober 2016 - April 2017


### Top 5 Rekomendasi

| Antecedents | Consequents | Support | Confidence | Lift |
|-------------|-------------|---------|------------|------|
| coffee | bread | 0.0900 | 0.5270 | 1.6102 |
| coffee | cake | 0.0547 | 0.5269 | 1.1015 |
| coffee | pastry | 0.0475 | 0.5521 | 1.1541 |
| tea | coffee | 0.0680 | 0.4765 | 0.9959 |
| bread | coffee | 0.0900 | 0.2751 | 0.5751 |



## 👨‍💻 Author

**Your Name**
- GitHub: https://github.com/lukmanfthoni
- Email: lukman.fathoni.lf@gmail.com
- LinkedIn: https://linkedin.com/in/lukmanfthoni

