import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Belajar Turunan", layout="wide")

st.title("📘 Aplikasi Interaktif: Belajar Turunan Kalkulus")

tab1, tab2, tab3, tab4 = st.tabs(["📖 Teori Dasar", "📝 Contoh Soal", "🧠 Kalkulator & Grafik", "ℹ️ Tentang Aplikasi"])

with tab1:
    st.header("📖 Teori Dasar Turunan")
    st.markdown("""
    Turunan adalah salah satu konsep dasar dalam kalkulus yang digunakan untuk mengetahui **laju perubahan** suatu fungsi terhadap variabelnya.

    ### 🔹 Definisi
    Jika f(x) adalah fungsi kontinu, maka turunannya didefinisikan sebagai:
    $$
    f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h}
    $$

    ### 🔹 Aplikasi Turunan
    - Menentukan kecepatan suatu benda (turunan posisi).
    - Menentukan kemiringan garis singgung grafik.
    - Menemukan nilai maksimum atau minimum fungsi (dalam optimasi).
    """)

    st.subheader("📚 Aturan-aturan Turunan Umum")
    st.markdown("""
    | Fungsi | Turunan |
    |--------|---------|
    | \( c \) (konstanta) | 0 |
    | \( x^n \) | \( n \\cdot x^{n-1} \) |
    | \( \sin x \) | \( \cos x \) |
    | \( \cos x \) | \( -\sin x \) |
    | \( e^x \) | \( e^x \) |
    | \( \\ln x \) | \( \\frac{1}{x} \) |
    """)

with tab2:
    st.header("📝 Contoh Soal & Pembahasan")

    st.subheader("🔸 Contoh 1:")
    st.markdown("""
    **Soal:** Hitung turunan dari fungsi \( f(x) = 3x^2 + 5x - 2 \)

    **Langkah-langkah:**
    1. Identifikasi setiap suku:
       - \( 3x^2 \rightarrow \) turunan = \( 6x \)
       - \( 5x \rightarrow \) turunan = \( 5 \)
       - \( -2 \rightarrow \) turunan = \( 0 \)
    2. Jumlahkan hasil turunan tiap suku:
    $$
    f'(x) = 6x + 5
    $$
    """)

    st.subheader("🔸 Contoh 2:")
    st.markdown("""
    **Soal:** Hitung turunan dari \( f(x) = \\sin(x) + x^3 \)

    **Langkah-langkah:**
    - Turunan \( \\sin(x) = \\cos(x) \)
    - Turunan \( x^3 = 3x^2 \)

    Maka:
    $$
    f'(x) = \\cos(x) + 3x^2
    $$
    """)

with tab3:
    st.header("🧠 Kalkulator Turunan + Visualisasi Grafik")

    fungsi_input = st.text_input("Masukkan fungsi (misal: x**2 + 3*x)", value="x**2 + 3*x")
    x = sp.Symbol('x')
    if fungsi_input:
        try:
            fungsi = sp.sympify(fungsi_input)
            turunan = sp.diff(fungsi, x)

            st.latex(f"f(x) = {sp.latex(fungsi)}")
            st.latex(f"f'(x) = {sp.latex(turunan)}")

            # Plot grafik
            st.subheader("📊 Grafik Fungsi dan Turunannya")
            fig, ax = plt.subplots()
            f_lambd = sp.lambdify(x, fungsi, "numpy")
            df_lambd = sp.lambdify(x, turunan, "numpy")

            X_vals = np.linspace(-10, 10, 400)
            Y_vals = f_lambd(X_vals)
            dY_vals = df_lambd(X_vals)

            ax.plot(X_vals, Y_vals, label="f(x)", color='blue')
            ax.plot(X_vals, dY_vals, label="f'(x)", color='red')
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

with tab4:
    st.header("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dibuat menggunakan **Python + Streamlit** untuk membantu pelajar memahami konsep dasar turunan dalam kalkulus secara interaktif.

    **Fitur:**
    - Teori dan aturan dasar turunan
    - Contoh soal dengan pembahasan
    - Kalkulator fungsi + visualisasi grafik

    _Dikembangkan oleh: Ihsan Musyaffa Dwi Yulangga_
    """)

