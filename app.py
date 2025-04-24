import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Belajar Turunan", layout="wide")

st.title("📘 Aplikasi Interaktif: Belajar Turunan Kalkulus")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📖 Teori Dasar", "📝 Contoh Soal", "✍️ Penilaian Otomatis" , "🧪 Kuis Pilihan Ganda" ,"🧠 Kalkulator & Grafik", "ℹ️ Tentang Aplikasi"])

with tab1:
    st.header("📖 Teori Dasar Turunan")

    st.markdown("""
    Turunan digunakan untuk menghitung laju perubahan atau kemiringan suatu fungsi terhadap variabelnya. Ini adalah dasar dari banyak konsep di matematika, fisika, dan teknik.

    ### 🔹 Definisi Turunan
    $$
    f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h}
    $$

    ### 🔹 Aturan-aturan Turunan Umum
    | Fungsi | Turunan |
    |--------|---------|
    | \( c \) (konstanta) | 0 |
    | \( x^n \) | \( n \\cdot x^{n-1} \) |
    | \( \sin x \) | \( \cos x \) |
    | \( \cos x \) | \( -\sin x \) |
    | \( e^x \) | \( e^x \) |
    | \( \\ln x \) | \( \\frac{1}{x} \) |

    ### 🔸 Aturan Penjumlahan & Pengurangan
    Jika \( f(x) = u(x) \pm v(x) \), maka:
    $$
    f'(x) = u'(x) \pm v'(x)
    $$

    ### 🔸 Aturan Perkalian
    Jika \( f(x) = u(x) \cdot v(x) \), maka:
    $$
    f'(x) = u'(x)v(x) + u(x)v'(x)
    $$

    ### 🔸 Aturan Pembagian
    Jika \( f(x) = \\frac{u(x)}{v(x)} \), maka:
    $$
    f'(x) = \\frac{u'(x)v(x) - u(x)v'(x)}{[v(x)]^2}
    $$

    ### 🔸 Aturan Rantai (Chain Rule)
    Jika \( f(x) = g(h(x)) \), maka:
    $$
    f'(x) = g'(h(x)) \\cdot h'(x)
    $$
    """)

with tab2:
    st.header("📝 Contoh Soal & Pembahasan")

    st.subheader("🔸 Contoh 1: Fungsi Polinomial")
    st.markdown("""
    **Soal:** Hitung turunan dari fungsi \( f(x) = 3x^2 + 5x - 2 \)

    **Langkah-langkah:**
    1. Gunakan aturan turunan dasar:
        - \( 3x^2 \rightarrow 6x \)
        - \( 5x \rightarrow 5 \)
        - \( -2 \rightarrow 0 \)
    2. Gabungkan hasilnya:
    $$
    f'(x) = 6x + 5
    $$
    """)

    st.subheader("🔸 Contoh 2: Fungsi Trigonometri + Polinomial")
    st.markdown("""
    **Soal:** Turunan dari \( f(x) = \\sin(x) + x^3 \)

    **Langkah-langkah:**
    - Turunan \( \\sin(x) = \\cos(x) \)
    - Turunan \( x^3 = 3x^2 \)
    $$
    f'(x) = \\cos(x) + 3x^2
    $$
    """)

    st.subheader("🔸 Contoh 3: Aturan Perkalian")
    st.markdown("""
    **Soal:** Turunan dari \( f(x) = x^2 \cdot \\sin(x) \)

    **Gunakan aturan perkalian:**
    $$
    f'(x) = (2x) \\cdot \\sin(x) + x^2 \\cdot \\cos(x)
    $$
    """)

    st.subheader("🔸 Contoh 4: Aturan Rantai")
    st.markdown("""
    **Soal:** Turunan dari \( f(x) = (3x^2 + 2)^5 \)

    **Gunakan Aturan Rantai:**
    - Biarkan \( u = 3x^2 + 2 \), maka:
    $$
    f'(x) = 5(3x^2 + 2)^4 \\cdot 6x = 30x(3x^2 + 2)^4
    $$
    """)

    st.subheader("🎯 Latihan Mandiri (Jawaban Disembunyikan)")
    st.markdown("""
    Coba kerjakan dulu, lalu cek jawabanmu di bawahnya (klik expand untuk melihat):

    **Soal 1:** \( f(x) = \\ln(x^2 + 1) \)

    <details>
    <summary>✔️ Lihat Jawaban</summary>

    Aturan rantai:
    $$
    f'(x) = \\frac{1}{x^2 + 1} \\cdot 2x = \\frac{2x}{x^2 + 1}
    $$

    </details>

    **Soal 2:** \( f(x) = \\frac{e^x}{x^2 + 1} \)

    <details>
    <summary>✔️ Lihat Jawaban</summary>

    Aturan pembagian:
    $$
    f'(x) = \\frac{e^x(x^2 + 1) - e^x(2x)}{(x^2 + 1)^2} = \\frac{e^x(x^2 + 1 - 2x)}{(x^2 + 1)^2}
    $$

    </details>
    """)

with tab3:
    st.header("✍️ Cek Jawaban Turunanmu")

    st.markdown("Masukkan fungsi awal dan jawaban turunanmu. Kami akan periksa apakah turunanmu benar.")

    user_fx = st.text_input("Masukkan fungsi f(x):", value="3*x**2 + 5*x - 2")
    user_answer = st.text_input("Masukkan turunan f'(x) versi kamu:", value="6*x + 5")

    if st.button("Cek Jawaban"):
        try:
            x = sp.symbols('x')
            f = sp.sympify(user_fx)
            correct_deriv = sp.diff(f, x)
            user_deriv = sp.sympify(user_answer)

            if sp.simplify(correct_deriv - user_deriv) == 0:
                st.success("✅ Jawaban kamu BENAR!")
            else:
                st.error("❌ Jawaban kamu SALAH!")
                st.markdown(f"Turunan yang benar adalah: $${sp.latex(correct_deriv)}$$")
        except Exception as e:
            st.error(f"Terjadi error: {e}")

with tab4:
    st.header("🧪 Kuis Pilihan Ganda")
    
    soal_kuis = [
        {
            "soal": "Apa turunan dari \( f(x) = x^3 \) ?",
            "opsi": ["x^2", "2x", "3x^2", "x^3"],
            "jawaban": "3x^2"
        },
        {
            "soal": "Apa turunan dari \( f(x) = \\sin(x) \cdot x^2 \) ?",
            "opsi": ["2x + x^2 cos(x)", "x^2 cos(x) + 2x sin(x)", "cos(x)", "x sin(x)"],
            "jawaban": "x^2 cos(x) + 2x sin(x)"
        },
        {
            "soal": "Apa turunan dari \( f(x) = \\ln(x) \) ?",
            "opsi": ["x", "1/x", "ln(x)", "x ln(x)"],
            "jawaban": "1/x"
        }
    ]

    skor = 0
    jawaban_user = []

    for i, item in enumerate(soal_kuis):
        st.subheader(f"Soal {i+1}")
        st.markdown(item["soal"])
        pilihan = st.radio("Pilih jawaban:", item["opsi"], key=i)
        jawaban_user.append(pilihan)

    if st.button("🧾 Lihat Skor"):
        skor = sum([1 for i in range(len(soal_kuis)) if jawaban_user[i] == soal_kuis[i]["jawaban"]])
        st.success(f"Skor kamu: {skor} dari {len(soal_kuis)} soal")

        with st.expander("Lihat Kunci Jawaban"):
            for i, item in enumerate(soal_kuis):
                st.markdown(f"**Soal {i+1}:** {item['jawaban']}")


with tab5:
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

with tab6:
    st.header("ℹ️ Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dibuat menggunakan **Python + Streamlit** untuk membantu pelajar memahami konsep dasar turunan dalam kalkulus secara interaktif.

    **Fitur:**
    - Teori dan aturan dasar turunan
    - Contoh soal dengan pembahasan
    - Kalkulator fungsi + visualisasi grafik

    _Dikembangkan oleh: Ihsan Musyaffa Dwi Yulangga_
    """)
