# 📊 Prediksi Efektivitas Media Periklanan

Aplikasi prediksi efektivitas kampanye periklanan menggunakan **Linear Regression** untuk menganalisis dampak budget iklan terhadap hasil penjualan.

## 🎯 Tujuan Proyek

Proyek ini dibuat sebagai bagian dari **Forum Group Discussion (FGD)** Mata Kuliah Praktikum Unggulan untuk memahami dan menerapkan machine learning dalam konteks bisnis marketing.

## 📈 Dataset

Dataset yang digunakan berasal dari kaggle (https://www.kaggle.com/datasets/tawfikelmetwally/advertising-dataset) , yang merupakan **Advertising Dataset** yang berisi:
- **TV** - Budget iklan televisi (K$)
- **Radio** - Budget iklan radio (K$)
- **Newspaper** - Budget iklan koran (K$)
- **Sales** - Hasil penjualan/efektivitas (juta $)

## 🛠 Teknologi

- Python 3.x
- Streamlit (Web Framework)
- Scikit-learn (Machine Learning)
- Pandas (Data Processing)
- Matplotlib & Seaborn (Visualisasi)

## 📦 Instalasi

```bash
pip install -r requirements.txt
```

## 🚀 Cara Menjalankan

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## ✨ Fitur

- 🎯 **Prediksi** - Prediksi penjualan berdasarkan input budget
- 📊 **Visualisasi** - Distribusi data dan analisis korelasi
- 💡 **Rekomendasi** - Saran alokasi budget yang optimal
- 💹 **ROI Calculator** - Perhitungan return on investment

## 📚 File Proyek

```
.
├── app.py                     # Aplikasi Streamlit
├── prediksi_model.pkl         # Model Linear Regression
├── scaler.pkl                 # StandardScaler
├── Advertising.csv            # Dataset original
├── data_clean.csv             # Dataset hasil preprocessing
├── requirements.txt           # Dependencies
├── README.md                  # File ini
└── Project_FIKOM_*.ipynb      # Notebook analisis & training
```
## 🥼 Dibuat oleh

Mario Mora Siregar
Aqilla Zeba Fakhira
Kevin Budiawan

## 📝 Lisensi

Copyright © 2026 Pengelola MK Praktikum Unggulan (Praktikum DGX), Universitas Gunadarma 
