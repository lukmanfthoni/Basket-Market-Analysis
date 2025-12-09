import streamlit as st
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Market Basket Analysis - Apriori", layout="wide")
st.title("🧺 Market Basket Analysis dengan Algoritma Apriori")


# ===== LOAD DATA =====
@st.cache_data
def load_dataset(path="bread basket.csv"):
    df = pd.read_csv(path)
    df["Item"] = df["Item"].str.lower().str.strip()
    return df[["Transaction", "Item"]]


# ===== PREPARE BASKET DATA =====
@st.cache_data
def create_basket(df):
    """
    Membuat binary matrix (basket format) untuk Apriori.
    """
    df["Count"] = 1
    basket = (
        df.pivot_table(
            index="Transaction",
            columns="Item",
            values="Count",
            aggfunc="sum"
        )
        .fillna(0)
        .astype(int)
    )

    # Encode menjadi 0/1 (presence)
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    return basket


# ===== APRIORI FUNCTION =====
@st.cache_data
def build_rules(basket_df, min_support=0.01, min_lift=1):
    freq_itemsets = apriori(basket_df, use_colnames=True, min_support=min_support)
    rules = association_rules(freq_itemsets, metric="lift", min_threshold=min_lift)
    return rules


# ===== MAIN PROCESS =====
try:
    df = load_dataset()
    basket = create_basket(df)
    rules = build_rules(basket)

    unique_items = sorted(df["Item"].unique())

    # ===== SIDEBAR FILTERS =====
    st.sidebar.header("🔎 Filters")

    selected_item = st.sidebar.selectbox(
        "Pilih Item Utama",
        unique_items,
        index=unique_items.index("bread") if "bread" in unique_items else 0
    )

    selected_period = st.sidebar.selectbox("Period Day", ["Morning", "Afternoon", "Evening", "Night"])
    selected_daytype = st.sidebar.selectbox("Tipe Hari", ["Weekday", "Weekend"])

    selected_month = st.sidebar.slider("Pilih Bulan", 1, 12, 11)
    selected_day = st.sidebar.slider("Pilih Hari (0-6)", 0, 6, 0)

    # ===== FILTER BY ITEM =====
    filtered_rules = rules[
        rules["antecedents"].apply(lambda x: selected_item in list(x))
    ].copy()

    st.subheader("🔍 Hasil Rekomendasi")

    if not filtered_rules.empty:
        # Ambil rule confidence tertinggi
        top_rule = filtered_rules.sort_values("confidence", ascending=False).iloc[0]
        consequent = list(top_rule["consequents"])[0]

        st.success(
            f"Jika pelanggan membeli **{selected_item.capitalize()}**, "
            f"mereka cenderung juga membeli **{consequent.capitalize()}**."
        )

        # ===== DETAIL METRIK =====
        with st.expander("Lihat Detail Metrik"):
            st.write(f"- **Support:** {top_rule['support']:.4f}")
            st.write(f"- **Confidence:** {top_rule['confidence']:.4f}")
            st.write(f"- **Lift:** {top_rule['lift']:.4f}")

            # tampil 5 rule teratas
            top5 = filtered_rules.nlargest(5, "confidence").copy()
            top5["antecedents"] = top5["antecedents"].apply(lambda x: ", ".join(list(x)))
            top5["consequents"] = top5["consequents"].apply(lambda x: ", ".join(list(x)))
            st.dataframe(top5[["antecedents", "consequents", "support", "confidence", "lift"]])

        # ===== PENJELASAN METRIK =====
        st.markdown("---")
        st.subheader("📘 Penjelasan Metrik")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### Support")
            st.info("Support menunjukkan frekuensi kombinasi item muncul di seluruh transaksi.")
            st.write(f"Nilai: **{top_rule['support']*100:.2f}%**")

        with col2:
            st.markdown("### Confidence")
            st.info("Confidence adalah probabilitas pelanggan membeli item B ketika membeli item A.")
            st.write(f"Nilai: **{top_rule['confidence']*100:.2f}%**")

        with col3:
            st.markdown("### Lift")
            st.info(
                "Lift menunjukkan seberapa besar hubungan antar item dibandingkan jika tidak berhubungan."
            )
            st.write(f"Nilai: **{top_rule['lift']:.3f}**")

        # ===== BUSINESS INSIGHT =====
        st.markdown("---")
        st.subheader("💡 Rekomendasi Bisnis")

        st.success(
            f"""
            Berdasarkan analisis:
            
            1. **Cross-Selling** → Tempatkan **{consequent}** dekat produk **{selected_item}**.
            2. **Bundling Promo** → Buat paket {selected_item} + {consequent}.
            3. **Rekomendasi Produk Otomatis** di kasir / aplikasi.
            4. **Kelola Stok** → Pastikan kedua produk tersedia saat demand meningkat.
            """
        )

    else:
        st.warning(f"Tidak ditemukan rule untuk item **{selected_item}**.")
        st.info("Coba pilih item lain yang lebih sering dibeli bersama.")


except FileNotFoundError:
    st.error("❌ File 'bread basket.csv' tidak ditemukan.")
    st.info("Pastikan file berada di folder yang sama.")

except Exception as e:
    st.error(f"Terjadi error: {e}")
