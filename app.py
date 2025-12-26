import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Prediksi Iklan", page_icon="📊", layout="wide")

# Title
st.title("📊 Prediksi Efektivitas Media Periklanan")
st.write("Aplikasi untuk memprediksi hasil sales berdasarkan budget iklan di TV, Radio, dan Newspaper")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Pengaturan")
    menu = st.radio("Menu:", ["🎯 Prediksi", "📊 Visualisasi", "ℹ️ Info"])
    st.markdown("---")
    st.info("**Dataset:** Advertising\n\n**Model:** Linear Regression")

# Load model dan scaler
try:
    model = joblib.load('prediksi_model.pkl')
    scaler = joblib.load('scaler.pkl')
except:
    st.error("❌ Model atau scaler tidak ditemukan! Pastikan file 'prediksi_model.pkl' dan 'scaler.pkl' tersedia")
    st.stop()

# MENU PREDIKSI
if menu == "🎯 Prediksi":
    st.header("🎯 Prediksi Penjualan")
    
    st.subheader("💰 Masukkan Budget Iklan")
    st.info("💡 Masukkan nilai budget dalam ribuan dollar (K$). Contoh: 230 = $230,000")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        tv = st.number_input("📺 Budget TV (K$)", min_value=0.0, max_value=300.0, value=150.0, step=5.0,
                            help="Budget iklan untuk media televisi dalam ribuan dollar")
    
    with col2:
        radio = st.number_input("📻 Budget Radio (K$)", min_value=0.0, max_value=50.0, value=25.0, step=1.0,
                               help="Budget iklan untuk media radio dalam ribuan dollar")
    
    with col3:
        newspaper = st.number_input("📰 Budget Koran (K$)", min_value=0.0, max_value=120.0, value=30.0, step=5.0,
                                   help="Budget iklan untuk media surat kabar dalam ribuan dollar")
    
    total_budget = tv + radio + newspaper
    st.metric("💵 Total Budget", f"${total_budget:,.1f}K")
    
    # Predict button
    if st.button("🚀 Prediksi Sekarang", type="primary", use_container_width=True):
        # Transform input dengan scaler
        input_data = pd.DataFrame([[tv, radio, newspaper]], 
                                 columns=['TV', 'Radio', 'Newspaper'])
        input_scaled = scaler.transform(input_data)
        
        # Prediksi
        prediction = model.predict(input_scaled)[0]
        
        st.markdown("---")
        
        # Display hasil prediksi
        st.subheader("📊 Hasil Prediksi")
        
        col_center = st.columns([1, 2, 1])
        with col_center[1]:
            st.metric(
                label="💰 Estimasi Pendapatan Penjualan", 
                value=f"${prediction/10:,.2f}M",
                help="Prediksi pendapatan penjualan dalam jutaan dollar"
            )
        
        st.markdown("---")
        
        # Metrics budget
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📺 Budget TV", f"${tv:,.1f}K", f"{(tv/total_budget*100):.0f}%")
        with col2:
            st.metric("📻 Budget Radio", f"${radio:,.1f}K", f"{(radio/total_budget*100):.0f}%")
        with col3:
            st.metric("📰 Budget Koran", f"${newspaper:,.1f}K", f"{(newspaper/total_budget*100):.0f}%")
        with col4:
            # ROI = (Pendapatan - Biaya) / Biaya * 100
            revenue_in_k = prediction * 100
            roi = ((revenue_in_k - total_budget) / total_budget) * 100 if total_budget > 0 else 0
            st.metric("💹 ROI", f"{roi:.0f}%", "Estimasi", 
                     help="ROI (Return on Investment): Persentase keuntungan dari investasi iklan. Formula: (Pendapatan - Biaya) / Biaya × 100%")
        
        st.markdown("---")
        
        # Visualisasi distribusi budget
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Distribusi Budget")
            fig, ax = plt.subplots(figsize=(6, 6))
            sizes = [tv, radio, newspaper]
            labels = ['TV', 'Radio', 'Koran']
            colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
            explode = (0.05, 0.05, 0.05)
            
            ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                   autopct='%1.1f%%', shadow=True, startangle=90)
            ax.axis('equal')
            st.pyplot(fig)
        
        with col2:
            st.subheader("💡 Rekomendasi")
            
            if tv > 50:
                st.success("✅ Budget TV sudah cukup untuk meningkatkan brand awareness")
            else:
                st.warning("⚠️ Pertimbangkan untuk menambah budget TV")
            
            if radio > 20:
                st.success("✅ Budget Radio sudah optimal")
            else:
                st.info("ℹ️ Radio bisa ditingkatkan untuk jangkauan yang lebih luas")
            
            if newspaper < 40:
                st.success("✅ Budget Koran efisien")
            else:
                st.warning("⚠️ Budget Koran cukup tinggi, periksa ROI-nya")
            
            st.markdown("---")
            st.markdown(
                f"**Kesimpulan:** Dengan total budget iklan **\${total_budget:,.1f}K**, "
                f"estimasi pendapatan penjualan mencapai **\${prediction/10:,.2f}M** "
                f"dengan ROI sekitar **{roi:.0f}%**"
            )

# MENU VISUALISASI
elif menu == "📊 Visualisasi":
    st.header("📊 Visualisasi Data")
    
    # Load data
    try:
        df = pd.read_csv('data_clean.csv')
        
        tab1, tab2 = st.tabs(["📈 Distribusi Data", "🔗 Korelasi"])
        
        with tab1:
            st.subheader("Distribusi Variabel")
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.hist(df['TV'], bins=30, color='#ff6b6b', alpha=0.7, edgecolor='black')
                ax.set_title('Distribusi Budget TV', fontweight='bold')
                ax.set_xlabel('TV Budget')
                ax.set_ylabel('Frekuensi')
                ax.grid(alpha=0.3)
                st.pyplot(fig)
                
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.hist(df['Radio'], bins=30, color='#4ecdc4', alpha=0.7, edgecolor='black')
                ax.set_title('Distribusi Budget Radio', fontweight='bold')
                ax.set_xlabel('Radio Budget')
                ax.set_ylabel('Frekuensi')
                ax.grid(alpha=0.3)
                st.pyplot(fig)
            
            with col2:
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.hist(df['Newspaper'], bins=30, color='#45b7d1', alpha=0.7, edgecolor='black')
                ax.set_title('Distribusi Budget Newspaper', fontweight='bold')
                ax.set_xlabel('Newspaper Budget')
                ax.set_ylabel('Frekuensi')
                ax.grid(alpha=0.3)
                st.pyplot(fig)
                
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.hist(df['Sales'], bins=30, color='#96ceb4', alpha=0.7, edgecolor='black')
                ax.set_title('Distribusi Sales', fontweight='bold')
                ax.set_xlabel('Sales')
                ax.set_ylabel('Frekuensi')
                ax.grid(alpha=0.3)
                st.pyplot(fig)
        
        with tab2:
            st.subheader("Matriks Korelasi")
            
            # Filter out Unnamed columns
            df_corr = df.loc[:, ~df.columns.str.contains('Unnamed|ID', case=False)]
            
            fig, ax = plt.subplots(figsize=(10, 8))
            corr = df_corr.corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm', center=0,
                       square=True, linewidths=2, fmt='.3f', ax=ax,
                       cbar_kws={"shrink": 0.8})
            ax.set_title('Correlation Heatmap', fontsize=14, fontweight='bold')
            st.pyplot(fig)
            
            st.markdown("---")
            
            # Korelasi dengan Sales
            if 'Sales' in df_corr.columns:
                st.subheader("🔍 Korelasi dengan Sales")
                corr_sales = df_corr.corr()['Sales'].sort_values(ascending=False)[1:]
                
                for var, val in corr_sales.items():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**{var}**")
                    with col2:
                        if val > 0.5:
                            st.success(f"{val:.3f}")
                        elif val > 0.3:
                            st.info(f"{val:.3f}")
                        else:
                            st.warning(f"{val:.3f}")
        
        # Statistik
        st.markdown("---")
        st.subheader("📋 Statistik Deskriptif")
        st.dataframe(df.describe(), use_container_width=True)
        
    except:
        st.error("❌ Data tidak ditemukan! Upload file 'data_clean.csv'")

# MENU INFO
elif menu == "ℹ️ Info":
    st.header("ℹ️ Tentang Aplikasi")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📖 Deskripsi")
        st.write("""
        Aplikasi ini digunakan untuk memprediksi efektivitas media periklanan 
        berdasarkan budget yang dialokasikan pada berbagai media (TV, Radio, Koran).
        
        **Model:** Linear Regression dengan StandardScaler
        
        **Fitur:**
        - Prediksi penjualan berdasarkan input budget
        - Visualisasi distribusi budget
        - Analisis korelasi antar variabel
        - Rekomendasi alokasi budget
        - Perhitungan ROI (Return on Investment)
        
        **Dataset:** Advertising Dataset dari Kaggle
        """)
        
        st.markdown("---")
        
        st.subheader("📚 Penjelasan Istilah")
        
        with st.expander("💹 Apa itu ROI?"):
            st.write("""
            **ROI (Return on Investment)** adalah persentase keuntungan yang didapat dari investasi iklan.
            
            **Formula:**  
            ROI = (Pendapatan - Biaya) / Biaya × 100%
            
            **Contoh:**  
            - Budget iklan: $200,000  
            - Pendapatan penjualan: $1,400,000  
            - ROI = ($1,400,000 - $200,000) / $200,000 × 100% = **600%**
            
            Artinya setiap $1 yang diinvestasikan menghasilkan keuntungan $6.
            """)
        
        with st.expander("📊 Apa itu Linear Regression?"):
            st.write("""
            **Linear Regression** adalah model machine learning yang memprediksi nilai 
            berdasarkan hubungan linear antar variabel.
            
            Model ini mencari pola hubungan antara budget iklan (TV, Radio, Koran) 
            dengan hasil penjualan untuk membuat prediksi.
            """)
        
        with st.expander("⚖️ Apa itu StandardScaler?"):
            st.write("""
            **StandardScaler** adalah teknik normalisasi data agar semua fitur 
            memiliki skala yang sama.
            
            Ini penting karena budget TV (0-300K), Radio (0-50K), dan Koran (0-120K) 
            memiliki rentang yang berbeda. Normalisasi membuat model lebih akurat.
            """)
        
        st.markdown("---")
        
        st.subheader("📊 Performa Model")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("R² Score", "0.89-0.90", help="Akurasi model (0-1), semakin tinggi semakin baik")
        with col_b:
            st.metric("MAE", "~1.25", help="Mean Absolute Error - rata-rata kesalahan prediksi")
        with col_c:
            st.metric("RMSE", "~1.66", help="Root Mean Square Error - ukuran kesalahan prediksi")
    
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", width=200)
        
        st.markdown("---")
        
        st.info("""
        **Praktikum DGX**  
        Universitas Gunadarma  
        FIKOM - 2025
        """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>© 2025 Praktikum DGX | FIKOM Universitas Gunadarma</p>", unsafe_allow_html=True)