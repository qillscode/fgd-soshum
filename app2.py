import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config with custom theme
st.set_page_config(
    page_title="Advertising | Prediksi Iklan Kreatif", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with solid pastel colors and better readability
st.markdown("""
<style>
    /* Main background - solid soft cream */
    .stApp {
        background: #FFF6E9;
    }
            
    
    /* Sidebar styling using main green */
    [data-testid="stSidebar"] {
        background: #0F2854;
        border-right: 3px solid #0F2854;
    }

    /* Ensure sidebar text stays black */
    [data-testid="stSidebar"] * {
        color: #FFF6E9 !important;
    }
    
    /* Custom headers with clean fonts */
    .header-box {
    color: #ffffff !important;
    background: #0F2854;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 25px;
    text-align: center;
    }

    h1 {
        margin: 0;
    }

    .subtitle {
        color: #ffffff !important;
        margin-top: 8px;
        font-size: 25px;
    }
    
    h2 {
        color:  #000000 !important;
        font-family: 'Segoe UI', sans-serif !important;
        border-bottom: 3px solid #BDE8F5;
        padding-bottom: 10px;
        font-size: 28px !important;
    }
    
    h3 {
        color: #000000 !important;
        font-family: 'Segoe UI', sans-serif !important;
        font-size: 20px !important;
    }
    
    /* Metric containers */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-size: 28px !important;
        font-weight: bold !important;
    }
    
    /* Button styling - dark blue with bold text */
    .stButton > button {
        background: #4988C4 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 15px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
        background: #0f2f4d !important;
    }
    
    /* Input fields with clean styling */
    .stNumberInput > div > div > input {
        border-radius: 8px !important;
        border: 2px solid #BDE8F5 !important;
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 500 !important;
    }
    
    /* Info boxes with solid pastel colors */
    .stInfo {
        background-color: #BDE8F5 !important;
        border-left: 4px solid #4988C4 !important;
        border-radius: 8px !important;
        color: #000000 !important;
    }
    
    .stSuccess {
        background-color: #BDE8F5 !important;
        border-left: 4px solid #183B4E !important;
        border-radius: 8px !important;
        color: #000000 !important;
    }
    
    .stWarning {
        background-color: #BDE8F5 !important;
        border-left: 4px solid #4988C4 !important;
        border-radius: 8px !important;
        color: #000000 !important;
    }
    
    /* Tabs styling - solid colors */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #BDE8F5;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #000000;
        font-weight: bold;
    }
    
    .stTabs [aria-selected="true"] {
        background: #0F2854;
        color: #ffffff;
    }

    /* Force sidebar radio/text to stay black */
    .stRadio label {
        color: #000000 !important;
    }
    
    /* Expander header styling - FORCE VISIBLE ALWAYS */
    .streamlit-expanderHeader {
            background-color: #BDE8F5 !important;
            border-radius: 10px !important;
            color: #000000 !important;
            font-weight: bold !important;
            border-left: 4px solid #4988C4 !important;
            padding: 10px 12px !important;
            font-size: 45px !important;
    }
    
    /* Force all child elements to black */
    .streamlit-expanderHeader *,
    .streamlit-expanderHeader p,
    .streamlit-expanderHeader span,
    .streamlit-expanderHeader div,
    .streamlit-expanderHeader label {
            color: #000000 !important;
            background: transparent !important;
            font-size: 25px !important;
    }
    
    /* Force the button/summary element itself */
    .streamlit-expanderHeader button,
    .streamlit-expanderHeader summary,
    [data-testid="stExpander"] button,
    [data-testid="stExpander"] summary {
            color: #000000 !important;
            background-color: #ffffff !important;
            border:3px solid #4988C4 !important;
    }
    
    /* Target the expander label specifically */
    .streamlit-expanderHeader .st-emotion-cache-p5msec,
    [data-testid="stExpander"] label {
            color: #000000 !important;
    }
    
    .streamlit-expanderHeader svg path {
        fill: #000000 !important;
    }
    
    /* Expander content styling - MAKE SURE VISIBLE AND BLACK TEXT */
    .streamlit-expanderContent {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        background-color: #ffffff !important;
        padding: 15px !important;
        border-radius: 0 0 10px 10px !important;
        border: 2px solid #BDE8F5 !important;
        border-top: none !important;
        margin-top: -5px !important;
        height: auto !important;
        max-height: none !important;
    }
    
    .streamlit-expanderContent > div {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    .streamlit-expanderContent *,
    .streamlit-expanderContent p,
    .streamlit-expanderContent span,
    .streamlit-expanderContent div,
    .streamlit-expanderContent strong,
    .streamlit-expanderContent h4 {
        color: #000000 !important;
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        font-size: 25px !important;
        line-height: 1.8 !important;
    }
    
    /* Make sure expander is visible when expanded */
    [data-testid="stExpander"][aria-expanded="true"] {
        background: #ffffff !important;
    }
    
    [data-testid="stExpander"][aria-expanded="true"] .streamlit-expanderContent {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
            
    div[data-testid="stExpander"] {
        width: 100% !important;
    }

    div[data-testid="stExpander"] > div {
        width: 100% !important;
    }
    
    /* Radio buttons in sidebar */
    .stRadio > label {
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    
    /* Divider styling - solid */
    hr {
        border: none;
        height: 2px;
        background: #0F2854;
        margin: 30px 0;
    }
</style>
""", unsafe_allow_html=True)

# Creative Title with inspirational message
# st.markdown("""
#     <h1 style='text-align: center;'>
#         📊 Prediksi Efektivitas Media Periklanan<br>
#     <span style='font-size: 20px; font-weight: normal;'>
#     🎨 Aplikasi prediksi untuk strategi media periklanan yang efektif dan inovatif 🎨
#     </span>
#     </h1>
    
# """, unsafe_allow_html=True)

st.markdown("""
<div class="header-box">
    <h1>📊 Prediksi Efektivitas Media Periklanan</h1>
    <span class="subtitle">🎨 Aplikasi prediksi untuk strategi media periklanan yang efektif dan inovatif 🎨</span>
</div>
""", unsafe_allow_html=True)

# Aesthetic Sidebar
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <h2 style='color: #FFF6E9; font-size: 24px; border: none;'>
                🎯 Navigasi
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio(
        "Pilih menu:",
        ["🎯 Prediksi", "📊 Visualisasi", "ℹ️ Info"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # st.markdown("""
    #     <div style='background: #FFF6E9; 
    #                 padding: 15px; border-radius: 10px; margin-top: 20px;
    #                 border-left: 4px solid #4988C4;'>
    #         <p style='margin: 0; color: #000000; font-size: 13px;'>
    #             <strong>💡 Info Cepat</strong><br>
    #             Dataset: Advertising<br>
    #             Model: Linear Regression<br>
    #             Status: ✅ Siap
    #         </p>
    #     </div>
    # """, unsafe_allow_html=True)
    
    # st.markdown("<br>" * 3, unsafe_allow_html=True)
    

# Load model dan scaler
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
try:
    model = joblib.load(os.path.join(current_dir, 'prediksi_model.pkl'))
    scaler = joblib.load(os.path.join(current_dir, 'scaler.pkl'))
except Exception as e:
    st.error(f"❌ Model atau scaler tidak ditemukan! Error: {str(e)}")
    st.stop()

# MENU PREDIKSI
if menu == "🎯 Prediksi":
    
    
    # Budget Input Section with creative cards
    st.markdown("""
        <div style='background: #BDE8F5;
                    padding: 15px; border-radius: 10px; margin-bottom: 20px;
                    border-left: 4px solid #4988C4;'>
            <h3 style='color: #000000; margin: 0; font-size: 15px;'>
                💰 Input Budget Iklan Anda
            </h3>
            <p style='color: #000000; font-size: 16px; margin-top: 5px;'>
                💡 Masukkan nilai budget dalam ribuan dollar (K$). Contoh: 230 = $230,000
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style='text-align: center; padding: 12px; background: #ffff ; 
                        border-radius: 15px; margin-bottom: 10px; border: 4px solid #4988C4;'>
                <p style='font-size: 28px; margin: 0;'>📺</p>
                <p style='color: #000000; font-weight: bold; margin: 5px 0; font-size: 16px;'>Televisi</p>
            </div>
        """, unsafe_allow_html=True)
        tv = st.number_input("Budget TV (K$)", min_value=0.0, max_value=10000000.0, value=150.0, step=5.0,
                            help="Budget iklan untuk media televisi dalam ribuan dollar",
                            label_visibility="collapsed")
    
    with col2:
        st.markdown("""
            <div style='text-align: center; padding: 12px; background: #ffff ; 
                        border-radius: 15px; margin-bottom: 10px; border: 4px solid #4988C4;'>
                <p style='font-size: 28px; margin: 0;'>📻</p>
                <p style='color: #000000; font-weight: bold; margin: 5px 0; font-size: 16px;'>Radio</p>
            </div>
        """, unsafe_allow_html=True)
        radio = st.number_input("Budget Radio (K$)", min_value=0.0, max_value=100000000.0, value=25.0, step=1.0,
                               help="Budget iklan untuk media radio dalam ribuan dollar",
                               label_visibility="collapsed")
    
    with col3:
        st.markdown("""
            <div style='text-align: center; padding: 12px; background: #ffff ; 
                        border-radius: 15px; margin-bottom: 10px; border: 4px solid #4988C4;'>
                <p style='font-size: 28px; margin: 0;'>📰</p>
                <p style='color: #000000; font-weight: bold; margin: 5px 0; font-size: 16px;'>Koran</p>
            </div>
        """, unsafe_allow_html=True)
        newspaper = st.number_input("Budget Koran (K$)", min_value=0.0, max_value=100000000.0, value=30.0, step=5.0,
                                   help="Budget iklan untuk media surat kabar dalam ribuan dollar",
                                   label_visibility="collapsed")
    
    total_budget = tv + radio + newspaper
    
    # Display total budget with creative styling
    st.markdown(f"""
        <div style='background: #BDE8F5;
                    padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.08);'>
            <p style='color: #000000; margin: 0; font-size: 17px; font-weight: bold;'>
                💵 Total Budget Kampanye
            </p>
            <p style='color: #000000; margin: 10px 0 0 0; font-size: 34px; font-weight: bold;'>
                ${total_budget:,.1f}K
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Predict button
    if st.button("🚀 Prediksi Sekarang!", type="primary", use_container_width=True):
        # Transform input dengan scaler
        input_data = pd.DataFrame([[tv, radio, newspaper]], 
                                 columns=['TV', 'Radio', 'Newspaper'])
        input_scaled = scaler.transform(input_data)
        
        # Prediksi
        prediction = model.predict(input_scaled)[0]
        

        # Display hasil prediksi with creative card
        st.markdown(f"""
            <div style='background: #ffff;
                        padding: 30px; border-radius: 10px; text-align: center; margin: 20px 0;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
                <p style='color: #000000; margin: 0; font-size: 19px; font-weight: bold;'>
                    💰 Estimasi Pendapatan Penjualan
                </p>
                <p style='color: #000000; margin: 15px 0 5px 0; font-size: 48px; font-weight: bold;'>
                    ${prediction/10:,.2f}M
                </p>
                <p style='color: #000000; margin: 0; font-size: 15px; font-style: italic;'>
                    prediksi pendapatan dalam jutaan dollar
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Metrics budget with creative cards
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
                <div style='background: #ffff;
                            padding: 20px; border-radius: 8px; text-align: center;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.08);'>
                    <p style='font-size: 30px; margin: 0;'>📺</p>
                    <p style='color: #000000; font-size: 15px; margin: 5px 0; font-weight: 600;'>Budget TV</p>
                    <p style='color: #000000; font-size: 22px; font-weight: bold; margin: 5px 0;'>
                        ${tv:,.1f}K
                    </p>
                    <p style='color: #000000; font-size: 16px; margin: 5px 0;'>
                        {(tv/total_budget*100):.0f}%
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div style='background: #ffff;
                            padding: 20px; border-radius: 8px; text-align: center;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.08);'>
                    <p style='font-size: 30px; margin: 0;'>📻</p>
                    <p style='color: #000000; font-size: 15px; margin: 5px 0; font-weight: 600;'>Budget Radio</p>
                    <p style='color: #000000; font-size: 22px; font-weight: bold; margin: 5px 0;'>
                        ${radio:,.1f}K
                    </p>
                    <p style='color: #000000; font-size: 16px; margin: 5px 0;'>
                        {(radio/total_budget*100):.0f}%
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
                <div style='background: #ffff;
                            padding: 20px; border-radius: 8px; text-align: center;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.08);'>
                    <p style='font-size: 30px; margin: 0;'>📰</p>
                    <p style='color: #000000; font-size: 15px; margin: 5px 0; font-weight: 600;'>Budget Koran</p>
                    <p style='color: #000000; font-size: 22px; font-weight: bold; margin: 5px 0;'>
                        ${newspaper:,.1f}K
                    </p>
                    <p style='color: #000000; font-size: 16px; margin: 5px 0;'>
                        {(newspaper/total_budget*100):.0f}%
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        with col4:
            # ROI = (Pendapatan - Biaya) / Biaya * 100
            revenue_in_k = prediction * 100
            roi = ((revenue_in_k - total_budget) / total_budget) * 10 if total_budget > 0 else 0
            st.markdown(f"""
                <div style='background: #ffff;
                            padding: 20px; border-radius: 8px; text-align: center;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.08);'>
                    <p style='font-size: 30px; margin: 0;'>💹</p>
                    <p style='color: #000000; font-size: 15px; margin: 5px 0; font-weight: 600;'>ROI</p>
                    <p style='color: #000000; font-size: 22px; font-weight: bold; margin: 5px 0;'>
                        {roi:.0f}%
                    </p>
                    <p style='color: #000000; font-size: 13px; margin: 5px 0; font-style: italic;'>
                        Estimasi Return
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Visualisasi distribusi budget dan Rekomendasi
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
                <div style='background: #BDE8F5;
                            padding: 15px; border-radius: 10px; margin-bottom: 15px;
                            border-left: 4px solid #4988C4;'>
                    <h3 style='color: #000000; margin: 0; font-size: 20px;'>
                        📊 Distribusi Budget
                    </h3>
                </div>
            """, unsafe_allow_html=True)
            
            fig, ax = plt.subplots(figsize=(6, 6))
            fig.patch.set_facecolor('white')
            ax.set_facecolor('white')
            
            sizes = [tv, radio, newspaper]
            labels = ['📺 TV', '📻 Radio', '📰 Koran']
            colors = ['#BDE8F5', '#4988C4', '#1C4D8D']
            explode = (0.05, 0.05, 0.05)
            
            wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                   autopct='%1.1f%%', shadow=False, startangle=90,
                   textprops={'fontsize': 12, 'weight': 'bold', 'color': '#000000'})
            
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontsize(14)
                autotext.set_weight('bold')
            
            ax.axis('equal')
            st.pyplot(fig)
        
        with col2:
            st.markdown("""
                <div style='background: #BDE8F5;
                            padding: 15px; border-radius: 10px; margin-bottom: 15px;
                            border-left: 4px solid #4988C4;'>
                    <h3 style='color: #000000; margin: 0; font-size: 20px;'>
                        💡 Rekomendasi Kreatif
                    </h3>
                </div>
            """, unsafe_allow_html=True)
            
            if tv > 50:
                st.markdown("""
                    <div style='background: #ffff; padding: 14px; border-radius: 8px; margin-bottom: 8px; '>
                        <p style='color: #000000; margin: 0; font-size: 16px;'>✅ Budget TV sudah cukup untuk meningkatkan brand awareness yang luas!</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style='background: #ffff; padding: 14px; border-radius: 8px; margin-bottom: 8px; '>
                        <p style='color: #000000; margin: 0; font-size: 16px;'>⚠️ Pertimbangkan untuk menambah budget TV agar jangkauan lebih maksimal</p>
                    </div>
                """, unsafe_allow_html=True)
            
            if radio > 20:
                st.markdown("""
                    <div style='background: #ffff; padding: 14px; border-radius: 8px; margin-bottom: 8px; '>
                        <p style='color: #000000; margin: 0; font-size: 16px;'>✅ Budget Radio sudah optimal untuk engagement audiens</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style='background: #ffff; padding: 14px; border-radius: 8px; margin-bottom: 8px;'>
                        <p style='color: #000000; margin: 0; font-size: 16px;'>ℹ️ Radio bisa ditingkatkan untuk jangkauan yang lebih luas di berbagai demografi</p>
                    </div>
                """, unsafe_allow_html=True)
            
            if newspaper < 40:
                st.markdown("""
                    <div style='background: #ffff; padding: 14px; border-radius: 8px; margin-bottom: 8px;'>
                        <p style='color: #000000; margin: 0; font-size: 16px;'>✅ Budget Koran efisien dan sesuai dengan trend digital</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style='background: #ffff; padding: 14px; border-radius: 8px; margin-bottom: 8px;'>
                        <p style='color: #000000; margin: 0; font-size: 16px;'>⚠️ Budget Koran cukup tinggi, pertimbangkan realokasi ke media digital</p>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style='background: #BDE8F5;
                            padding: 20px; border-radius: 10px;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.08); border-left: 4px solid #4988C4;'>
                    <p style='color: #000000; font-weight: bold; margin: 0 0 10px 0; font-size: 16px;'>
                        📝 Kesimpulan Kampanye:
                    </p>
                    <p style='color: #000000; margin: 0; line-height: 1.6; font-size: 14px;'>
                        Dengan total budget iklan <strong>${total_budget:,.1f}K</strong>, 
                        estimasi pendapatan penjualan mencapai <strong>${prediction/10:,.2f}M</strong> 
                        dengan ROI sekitar <strong>{roi:.0f}%</strong>. 
                        <em>Tetap kreatif!</em> 🎨✨
                    </p>
                </div>
            """, unsafe_allow_html=True)

# MENU VISUALISASI
elif menu == "📊 Visualisasi":
    st.markdown("""
        <div style='background: #4988C4;
                    padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 30px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.08);'>
            <h2 style='color: #000000; margin: 0; border: none; font-size: 25px;'>
                📊 Eksplorasi Data Visual
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Load data
    try:
        df = pd.read_csv('data_clean.csv')
        column_labels = {
            'TV': 'TV',
            'Radio': 'Radio',
            'Newspaper': 'Koran',
            'Sales': 'Penjualan'
        }
        df_display = df.rename(columns=column_labels)
        
        tab1, tab2 = st.tabs(["📈 Distribusi Data", "🔗 Korelasi"])
        
        with tab1:
            st.markdown("""
                <div style='background: #BDE8F5;
                            padding: 15px; border-radius: 10px; margin-bottom: 20px;
                            border-left: 4px solid #4988C4;'>
                    <h3 style='color: #000000; margin: 0; font-size: 20px;'>
                        📈 Distribusi Variabel
                    </h3>
                    <p style='color: #000000; font-size: 15px; margin-top: 0px;'>
                        Visualisasi distribusi budget untuk setiap media periklanan
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig, ax = plt.subplots(figsize=(8, 6))
                fig.patch.set_facecolor('white')
                ax.set_facecolor('white')
                ax.hist(df['TV'], bins=30, color='#BDE8F5', alpha=0.8, edgecolor='#000000', linewidth=1.2)
                ax.set_title('📺 Distribusi Budget TV', fontweight='bold', fontsize=14, color='#000000')
                ax.set_xlabel('Budget TV', fontsize=12, color='#000000')
                ax.set_ylabel('Frekuensi', fontsize=12, color='#000000')
                ax.grid(alpha=0.2, color='#cccccc')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
                
                fig, ax = plt.subplots(figsize=(8, 6))
                fig.patch.set_facecolor('white')
                ax.set_facecolor('white')
                ax.hist(df['Radio'], bins=30, color='#0F2854', alpha=0.8, edgecolor='#000000', linewidth=1.2)
                ax.set_title('📻 Distribusi Budget Radio', fontweight='bold', fontsize=14, color='#000000')
                ax.set_xlabel('Budget Radio', fontsize=12, color='#000000')
                ax.set_ylabel('Frekuensi', fontsize=12, color='#000000')
                ax.grid(alpha=0.2, color='#cccccc')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
            
            with col2:
                fig, ax = plt.subplots(figsize=(8, 6))
                fig.patch.set_facecolor('white')
                ax.set_facecolor('white')
                ax.hist(df['Newspaper'], bins=30, color='#4988C4', alpha=0.8, edgecolor='#000000', linewidth=1.2)
                ax.set_title('📰 Distribusi Budget Koran', fontweight='bold', fontsize=14, color='#000000')
                ax.set_xlabel('Budget Koran', fontsize=12, color='#000000')
                ax.set_ylabel('Frekuensi', fontsize=12, color='#000000')
                ax.grid(alpha=0.2, color='#cccccc')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
                
                fig, ax = plt.subplots(figsize=(8, 6))
                fig.patch.set_facecolor('white')
                ax.set_facecolor('white')
                ax.hist(df['Sales'], bins=30, color='#1C4D8D', alpha=0.8, edgecolor='#000000', linewidth=1.2)
                ax.set_title('💰 Distribusi Penjualan', fontweight='bold', fontsize=14, color='#000000')
                ax.set_xlabel('Penjualan', fontsize=12, color='#000000')
                ax.set_ylabel('Frekuensi', fontsize=12, color='#000000')
                ax.grid(alpha=0.2, color='#cccccc')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                st.pyplot(fig)
        
        with tab2:
            st.markdown("""
                <div style='background: #BDE8F5;
                            padding: 15px; border-radius: 10px; margin-bottom: 20px;
                            border-left: 4px solid #4988C4;'>
                    <h3 style='color: #000000; margin: 0; font-size: 20px;'>
                        🔗 Matriks Korelasi
                    </h3>
                    <p style='color: #000000; font-size: 15px; margin-top: 0px;'>
                        Hubungan antar variabel dalam kampanye periklanan
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Filter out Unnamed columns
            df_corr = df.loc[:, ~df.columns.str.contains('Unnamed|ID', case=False)]
            
            fig, ax = plt.subplots(figsize=(10, 8))
            fig.patch.set_facecolor('white')
            corr = df_corr.corr()
            corr_display = corr.rename(index=column_labels, columns=column_labels)
            sns.heatmap(corr_display, annot=True, cmap='YlGnBu', center=0,
                       square=True, linewidths=2, fmt='.3f', ax=ax,
                       cbar_kws={"shrink": 0.8},
                       annot_kws={"size": 12, "weight": "bold", "color": "#ffffff"})
            ax.set_title('🔗 Correlation Heatmap', fontsize=16, fontweight='bold', 
                        color='#000000', pad=20)
            plt.xticks(fontsize=12, color='#000000')
            plt.yticks(fontsize=12, color='#000000')
            st.pyplot(fig)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Korelasi dengan Sales
            if 'Sales' in df_corr.columns:
                st.markdown("""
                    <div style='background: #BDE8F5;
                                padding: 10px; border-radius: 10px; margin: 20px 0;
                                border-left: 4px solid #4988C4;'>
                        <h3 style='color: #000000; margin: 0; font-size: 20px;'>
                            🔍 Korelasi dengan Penjualan
                        </h3>
                    </div>
                """, unsafe_allow_html=True)
                
                corr_sales = df_corr.corr()['Sales'].sort_values(ascending=False)[1:]
                
                for var, val in corr_sales.items():
                    badge_bg = "#4988C4" if val > 0.5 else ("#4988C4" if val > 0.3 else "#BDE8F5")
                    badge_border = "border: 2px solid #4988C4;" if 0.3 < val <= 0.5 else ""
                    st.markdown(f"""
                        <div style='display: flex; align-items: center; justify-content: space-between; 
                                    background: #f7f7f7; padding: 12px 14px; border-radius: 10px; 
                                    margin-bottom: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.06);'>
                            <span style='color: #000000; font-weight: 700; font-size: 15px;'>
                                {column_labels.get(var, var)}
                            </span>
                            <span style='background: {badge_bg}; {badge_border} padding: 6px 12px; 
                                         border-radius: 10px; color: #000000; font-weight: 800;'>
                                {val:.3f}
                            </span>
                        </div>
                    """, unsafe_allow_html=True)
        
        # Statistik
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <div style='background: #BDE8F5;
                        padding: 10px; border-radius: 10px; margin-bottom: 20px;
                        border-left: 4px solid #4988C4;'>
                <h3 style='color: #000000; margin: 0; font-size: 20px;'>
                    📋 Statistik Deskriptif
                </h3>
                <p style='color: #000000; font-size: 15px; margin-top: 0px;'>
                    Ringkasan statistik dataset periklanan
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.dataframe(df_display.describe(), use_container_width=True)
        
    except:
        st.error("❌ Data tidak ditemukan! Upload file 'data_clean.csv'")

# MENU INFO
elif menu == "ℹ️ Info":
    # st.markdown("""
    #     <div style='background: #4988C4;
    #                 padding: 25px; border-radius: 10px; text-align: center; margin-bottom: 30px;
    #                 box-shadow: 0 2px 8px rgba(0,0,0,0.08);'>
    #         <h2 style='color: #000000; margin: 0; border: none; font-size: 28px;'>
    #             ℹ️ Tentang 
    #         </h2>
    #         <p style='color: #000000; font-style: italic; margin-top: 10px; font-size: 16px;'>
    #             "pengetahuan adalah kekuatan, kreativitas adalah keajaiban"
    #         </p>
    #     </div>
    # """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 2], gap="small")

    
    with col1:
        st.markdown("""
            <div style='background: #ffff;
                        padding: 15px; border-radius: 10px; margin-bottom: 20px;
                        border: 4px solid #4988C4;'>
                <h3 style='color: #000000; margin: 0 0 5px 0; font-size: 28px;'>
                    📖 Deskripsi Aplikasi
                </h3>
                <p style='color: #000000; line-height: 1.5; margin: 0; font-size: 18px;'>
                    Aplikasi Prediksi ini digunakan untuk memprediksi efektivitas media periklanan 
                    berdasarkan budget yang dialokasikan pada berbagai media (TV, Radio, Koran).
                    Dengan pendekatan yang kreatif dan user-friendly, aplikasi ini membantu komunikator 
                    dan marketer membuat keputusan strategis yang lebih baik.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Features Section
        st.markdown("""
            <div style='background: #BDE8F5;
                        padding: 10px; border-radius: 15px; margin-bottom: 20px;border-left: 4px solid #4988C4;'>
                <h3 style='color: #000000; margin: 0 0 5px 0; font-size: 20px;'>
                    ✨ Fitur Unggulan
                </h3>
            </div>
        """, unsafe_allow_html=True)
        
        features = [
            ("🎯", "Prediksi penjualan berdasarkan input budget"),
            ("📊", "Visualisasi distribusi budget yang menarik"),
            ("🔗", "Analisis korelasi antar variabel"),
            ("💡", "Rekomendasi alokasi budget yang smart"),
            ("💹", "Perhitungan ROI (Return on Investment)"),
            ("🎨", "Interface yang aesthetic dan user-friendly")
        ]
        
        for icon, feature in features:
            st.markdown(f"""
                <div style='background: white; padding: 15px; border-radius: 8px; 
                            margin-bottom: 10px; border: 1px solid #4988C4;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.05);'>
                    <p style='color: #000000; margin: 0; font-size: 18px;'>
                        <span style='font-size: 18px;'>{icon}</span> {feature}
                    </p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
    
        
        # Educational Section
    st.markdown("""
        <div style='background: #BDE8F5;
                    padding: 15px; border-radius: 10px; margin-bottom: 20px;
                    border-left: 4px solid #4988C4; width:100%; box-sizing:border-box;'>
            <h3 style='color: #000000; margin: 0; font-size: 20px;'>
                📚 Penjelasan Istilah
            </h3>
        </div>
    """, unsafe_allow_html=True)
        
    with st.expander("💹 Apa itu ROI?"):
        st.markdown("""
            <div style='background: #ffffff; padding: 20px; border-radius: 10px; border: 3px solid #4988C4; margin: 10px 0;'>
                <h4 style='color: #000000; font-size: 18px; font-weight: bold; margin: 0 0 15px 0;'>💹 ROI (Return on Investment)</h4>
                <p style='color: #000000; line-height: 1.8; font-size: 16px; font-weight: 500;'>
                    ROI adalah <strong style='color: #000000;'>persentase keuntungan</strong> yang didapat dari investasi iklan.
                    Ini adalah metrik penting untuk mengukur efektivitas kampanye periklanan Anda.
                </p>
                <div style='background: #BDE8F5; padding: 15px; border-radius: 10px; margin: 20px 0; width:100%; box-sizing:border-box;'>
                    <p style='color: #000000; font-weight: bold; margin: 0 0 10px 0; font-size: 17px;'>📐 Formula:</p>
                    <p style='color: #000000; background: #BDE8F5; padding: 15px; border-radius: 8px; 
                              font-family: monospace; border: 3px solid #4988C4; font-size: 16px; font-weight: bold; margin: 0;'>
                        ROI = (Pendapatan - Biaya) / Biaya × 100%
                    </p>
                </div>
                <div style='background: #BDE8F5; padding: 15px; border-radius: 10px; border-left: 5px solid #4988C4;'>
                    <p style='color: #000000; font-weight: bold; margin: 0 0 10px 0; font-size: 17px;'>📝 Contoh:</p>
                    <p style='color: #000000; font-size: 16px; line-height: 1.8; margin: 0;'>
                        • Budget iklan: <strong style='color: #000000;'>$200,000</strong><br>
                        • Pendapatan penjualan: <strong style='color: #000000;'>$400,000</strong><br>
                        • ROI = (400,000 - 200,000) / 200,000 × 100% = <strong style='color: #4988C4; font-size: 18px;'>100%</strong>
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("📊 Apa itu Linear Regression?"):
        st.markdown("""
            <div style='background: #ffffff; padding: 20px; border-radius: 10px; border: 3px solid #4988C4; margin: 10px 0;'>
                <h4 style='color: #000000; font-size: 18px; font-weight: bold; margin: 0 0 15px 0;'>📊 Linear Regression</h4>
                <p style='color: #000000; line-height: 1.8; font-size: 16px; font-weight: 500;'>
                    <strong style='color: #000000;'>Linear Regression</strong> adalah model machine learning yang memprediksi nilai 
                    berdasarkan hubungan linear antar variabel. Bayangkan seperti menggambar garis lurus 
                    yang paling pas melalui sekumpulan titik data.
                </p>
                <div style='background: #BDE8F5; padding: 15px; border-radius: 10px; margin-top: 15px; border-left: 5px solid #BDE8F5;'>
                    <p style='color: #000000; line-height: 1.8; font-size: 16px; font-weight: 500; margin: 0;'>
                        Model ini mencari pola hubungan antara budget iklan (TV, Radio, Koran) 
                        dengan hasil penjualan untuk membuat prediksi yang akurat. Semakin kuat hubungannya,
                        semakin akurat prediksinya! 🎯
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("⚖️ Apa itu StandardScaler?"):
        st.markdown("""
                <div style='background: #ffffff; padding: 20px; border-radius: 10px; border: 3px solid #4988C4; margin: 10px 0;'>
                    <h4 style='color: #000000; font-size: 18px; font-weight: bold; margin: 0 0 15px 0;'>⚖️ StandardScaler</h4>
                    <p style='color: #000000; line-height: 1.8; font-size: 16px; font-weight: 500;'>
                        <strong style='color: #000000;'>StandardScaler</strong> adalah teknik normalisasi data agar semua fitur 
                        memiliki skala yang sama. Ini seperti mengubah semua ukuran menjadi bahasa yang sama!
                    </p>
                    <div style='background: #BDE8F5; padding: 15px; border-radius: 10px; margin-top: 15px; border-left: 5px solid #4988C4;'>
                        <p style='color: #000000; line-height: 1.8; font-size: 16px; font-weight: 500; margin: 0;'>
                            Ini penting karena budget TV (0-300K), Radio (0-50K), dan Koran (0-120K) 
                            memiliki rentang yang berbeda-beda. Normalisasi membuat model lebih adil dan akurat 
                            dalam mempertimbangkan semua faktor. ⚖️
                        </p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    
    with col2:
        # Model Performance
        st.markdown("""
            <div style='background: #BDE8F5;
                        padding: 10px; border-radius: 10px; margin-bottom: 20px;border-left: 4px solid #4988C4'>
                <h3 style='color: #000000; margin: 0 0 5px 0; font-size: 20px;'>
                    📊 Performa Model
                </h3>
            </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown("""
                <div style='background: #BDE8F5; padding: 20px; border-radius: 8px; text-align: center;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.08); border:3px solid #4988C4;'>
                    <p style='font-size: 30px; margin: 0;'>🎯</p>
                    <p style='color: #000000; font-size: 20px; margin: 0px 0;'>R² Score</p>
                    <p style='color: #000000; font-size: 20px; font-weight: bold; margin: 5px 0;'>
                        0.89-0.90
                    </p>
                    <p style='color: #000000; font-size: 14px; margin: 0px 0;'>
                        Akurasi tinggi!
                    </p>
                </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
                <div style='background: #BDE8F5; padding: 20px; border-radius: 8px; text-align: center;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.08); border:3px solid #4988C4;'>
                    <p style='font-size: 30px; margin: 0;'>📏</p>
                    <p style='color: #000000; font-size: 20px; margin: 0px 0;'>MAE</p>
                    <p style='color: #000000; font-size: 20px; font-weight: bold; margin: 5px 0;'>
                        ~1.25
                    </p>
                    <p style='color: #000000; font-size: 16px; margin: 0px 0;'>
                        Error minimal
                    </p>
                </div>
            """, unsafe_allow_html=True)
        with col_c:
            st.markdown("""
                <div style='background: #BDE8F5; padding: 20px; border-radius: 8px; text-align: center;
                            box-shadow: 0 2px 6px rgba(0,0,0,0.08);border:3px solid #4988C4; margin-bottom: 20px;'>
                    <p style='font-size: 30px; margin: 0;'>📐</p>
                    <p style='color: #000000; font-size: 20px; margin: 0px 0;'>RMSE</p>
                    <p style='color: #000000; font-size: 20px; font-weight: bold; margin: 5px 0;'>
                        ~1.66
                    </p>
                    <p style='color: #000000; font-size: 16px; margin: 0px 0;'>
                        Presisi baik
                    </p>
                </div>
            """, unsafe_allow_html=True)

                # Tech Stack
        st.markdown("""
            <div style='background:#BDE8F5 ;
                        padding: 10px; border-radius: 10px; margin-bottom: 20px; border-left: 4px solid #4988C4'>
                <h3 style='color: #000000; margin: 0 0 5px 0; font-size: 20px;'>
                    🔧 Teknologi
                </h3>
                <p style='color: #000000; margin: 0; font-size: 18px;'>
                    <strong>Model:</strong> Linear Regression dengan StandardScaler<br>
                    <strong>Dataset:</strong> Advertising Dataset dari Kaggle<br>
                    <strong>Framework:</strong> Streamlit, Pandas, Scikit-learn, Matplotlib
                </p>
            </div>
        """, unsafe_allow_html=True)
        #Decorative image placeholder
        st.markdown("""
            <div style='background: #ffff;
                        padding: 30px; border-radius: 10px; text-align: center;
                        box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 20px;'>
                <p style='font-size: 70px; margin: 10px 0;'>📢 🎨 💡</p>
            </div>
        """, unsafe_allow_html=True)
    
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Fun fact section
# Creative Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='background: #FFF6E9;
padding: 25px; border-radius: 10px; text-align: center;
box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-top: 50px;'>

<p style='color: #000000; font-size: 14px; margin: 5px 0;'>
Copyright © 2026 Pengelola MK Praktikum Unggulan (Praktikum DGX), Universitas Gunadarma
</p>

<a href="https://www.praktikum-hpc.gunadarma.ac.id/" target="_blank"
style="display:block; color:#1a73e8; font-size:13px; margin-top:0px;">
https://www.praktikum-hpc.gunadarma.ac.id/
</a>
<a href="https://www.hpc-hub.gunadarma.ac.id/" target="_blank"
style="display:block; color:#1a73e8; font-size:13px; margin-top:0px;">
https://www.hpc-hub.gunadarma.ac.id/
</a>

</div>
""", unsafe_allow_html=True)

