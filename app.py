import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from fractions import Fraction

# ─────────────────────────────────────────
# KONFIGURASI HALAMAN
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Jelajah SPLTV",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────
# CSS KUSTOM (selaras dengan bilangan bulat)
# ─────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }

    .main-header {
        background: linear-gradient(135deg, #1A3C6E 0%, #2E75B6 60%, #C00000 100%);
        color: white; padding: 1.5rem 2rem; border-radius: 16px;
        text-align: center; margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(26,60,110,0.3);
    }
    .main-header h1 { font-size: 2rem; font-weight: 800; margin: 0; }
    .main-header p  { font-size: 1rem; margin: 0.3rem 0 0; opacity: 0.9; }

    .fase-box {
        border-left: 5px solid #2E75B6; background: #EBF3FB;
        padding: 0.8rem 1rem; border-radius: 0 10px 10px 0;
        margin: 0.7rem 0;
    }
    .fase-box .fase-label {
        font-weight: 800; color: #1A3C6E; font-size: 0.85rem;
        text-transform: uppercase; letter-spacing: 1px;
    }
    .fase-box .fase-text { color: #2C3E50; font-size: 0.95rem; margin-top: 0.2rem; }

    .info-card {
        background: #F0F7FF; border: 1px solid #BDD7EE;
        border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    }
    .warning-card {
        background: #FFF8E6; border: 1px solid #FFD966;
        border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    }
    .success-card {
        background: #F0FBF0; border: 1px solid #70AD47;
        border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    }
    .danger-card {
        background: #FEF0F0; border: 1px solid #E74C3C;
        border-radius: 12px; padding: 1rem 1.2rem; margin: 0.5rem 0;
    }

    .result-display {
        background: linear-gradient(135deg, #1A3C6E, #2E75B6);
        color: white; border-radius: 16px; padding: 1.5rem;
        text-align: center; font-size: 2rem; font-weight: 800;
        box-shadow: 0 4px 15px rgba(26,60,110,0.3); margin: 1rem 0;
    }

    .sidebar-title {
        background: #1A3C6E; color: white;
        padding: 0.7rem 1rem; border-radius: 10px;
        font-weight: 800; text-align: center; margin-bottom: 0.5rem;
    }

    .stButton > button {
        border-radius: 10px; font-weight: 700;
        transition: all 0.2s;
    }
    .stButton > button:hover { transform: translateY(-2px); }

    [data-testid="metric-container"] {
        background: #F8FAFF; border: 1px solid #BDD7EE;
        border-radius: 12px; padding: 0.8rem; text-align: center;
    }

    hr { border: none; border-top: 2px solid #EBF3FB; margin: 1.5rem 0; }

    .step-box {
        background: white; border: 2px solid #BDD7EE;
        border-radius: 12px; padding: 0.8rem 1rem; margin: 0.4rem 0;
    }
    .step-num {
        background: #2E75B6; color: white;
        width: 28px; height: 28px; border-radius: 50%;
        display: inline-flex; align-items: center; justify-content: center;
        font-weight: 800; font-size: 0.85rem; margin-right: 0.5rem;
    }
    .var-badge {
        display: inline-block; padding: 3px 12px; border-radius: 20px;
        font-weight: 700; font-size: 0.88rem; margin: 2px;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# HEADER UTAMA
# ─────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>📐 Jelajah SPLTV</h1>
    <p>Sistem Persamaan Linear Tiga Variabel • Metode Discovery Learning • SMA/MA/SMK Kelas X</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧭 Menu Navigasi</div>', unsafe_allow_html=True)
    tab_choice = st.radio(
        "Pilih Fitur:",
        options=[
            "🏠 Beranda",
            "🔍 KP 1 — Mengenal SPLTV",
            "🔢 KP 2 — Solver Metode Eliminasi & Substitusi",
            "📊 KP 3 — Interpretasi & Pemodelan",
            "📝 Soal Latihan Interaktif",
            "🎬 Video Bahan/Materi",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("""
    <div style="background:#F0F7FF;padding:0.8rem;border-radius:10px;font-size:0.82rem;color:#1A3C6E;">
    <b>📚 Petunjuk Penggunaan</b><br><br>
    1. Pilih fitur sesuai kegiatan pembelajaran<br>
    2. Ikuti langkah-langkah Discovery Learning<br>
    3. Catat temuan di LKS<br>
    4. Diskusikan dengan kelompokmu<br>
    5. Kerjakan soal latihan di akhir
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.78rem;color:#7F7F7F;text-align:center;">
    🎓 Kurikulum Merdeka Fase E<br>
    SMA/MA/SMK Kelas X<br>
    Panduan Guru Matematika (Edisi Revisi)
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════
def solve_spltv(a1,b1,c1,d1, a2,b2,c2,d2, a3,b3,c3,d3):
    """Solve 3x3 linear system using numpy, return (x,y,z) or None."""
    try:
        A = np.array([[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]], dtype=float)
        B = np.array([d1,d2,d3], dtype=float)
        det = np.linalg.det(A)
        if abs(det) < 1e-10:
            return None, "Sistem tidak memiliki solusi tunggal (determinan = 0)."
        sol = np.linalg.solve(A, B)
        return sol, None
    except Exception as e:
        return None, str(e)

def format_val(v):
    """Format float to fraction or integer string."""
    f = Fraction(v).limit_denominator(100)
    if f.denominator == 1:
        return str(f.numerator)
    return f"{f.numerator}/{f.denominator}"

def elimination_steps(a1,b1,c1,d1, a2,b2,c2,d2, a3,b3,c3,d3):
    """Return step-by-step elimination as list of strings."""
    steps = []
    # --- Eliminate x from eq2 and eq3 ---
    # Make eq1 pivot
    steps.append(("Langkah 1: Eliminasi variabel x dari Persamaan (2) dan (3)",
        f"Kalikan persamaan (1) dengan {a2} dan persamaan (2) dengan {a1}, lalu kurangkan."))

    # eq2' = a1*eq2 - a2*eq1
    na2b = a1*b2 - a2*b1
    na2c = a1*c2 - a2*c1
    na2d = a1*d2 - a2*d1

    # eq3' = a1*eq3 - a3*eq1
    na3b = a1*b3 - a3*b1
    na3c = a1*c3 - a3*c1
    na3d = a1*d3 - a3*d1

    def sign_str(coef, var):
        if coef == 0: return ""
        if coef > 0: return f" + {coef}{var}"
        return f" - {abs(coef)}{var}"

    eq2p = f"{na2b}y{sign_str(na2c,'z')} = {na2d}"
    eq3p = f"{na3b}y{sign_str(na3c,'z')} = {na3d}"

    steps.append(("Hasil eliminasi x:", f"Persamaan (4): {eq2p}\nPersamaan (5): {eq3p}"))

    # --- Eliminate y from eq3' using eq2' ---
    if na2b == 0 and na3b == 0:
        steps.append(("Langkah 2:", "Koefisien y sudah 0 pada kedua persamaan. Lanjut ke langkah berikutnya."))
        nc = na2c; nd = na2d
    else:
        steps.append(("Langkah 2: Eliminasi variabel y dari Persamaan (4) dan (5)",
            f"Kalikan persamaan (4) dengan {na3b} dan persamaan (5) dengan {na2b}, lalu kurangkan."))
        nc = na3b*na2c - na2b*na3c
        nd = na3b*na2d - na2b*na3d
        eq_z = f"{nc}z = {nd}"
        steps.append(("Hasil eliminasi y:", f"Persamaan (6): {eq_z}"))

    return steps


# ══════════════════════════════════════════
# BERANDA
# ══════════════════════════════════════════
if tab_choice == "🏠 Beranda":
    st.markdown("## 👋 Selamat Datang, Penjelajah Matematika!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="info-card">
        <b>🎯 Capaian Pembelajaran (Fase E)</b><br><br>
        ✅ Memodelkan masalah nyata ke dalam SPLTV<br>
        ✅ Menyelesaikan SPLTV dengan metode eliminasi & substitusi<br>
        ✅ Memaknai solusi dalam konteks permasalahan
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
        <b>🔬 Metode Pembelajaran</b><br><br>
        🔵 Discovery Learning (utama)<br>
        🟢 Problem Based Learning<br>
        🟡 Cooperative Learning
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="info-card">
        <b>📱 Fitur Aplikasi</b><br><br>
        🔍 Pengenalan Konsep SPLTV<br>
        🔢 Solver Langkah demi Langkah<br>
        📊 Pemodelan Masalah Kontekstual<br>
        📝 Soal Latihan Interaktif
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔬 Alur Discovery Learning dalam Aplikasi Ini")

    fases = [
        ("① STIMULATION","Kamu akan dihadapkan situasi nyata — tentang harga barang, berat benda, atau pembagian dana — yang melibatkan tiga hal yang tidak diketahui sekaligus!","#2E75B6"),
        ("② PROBLEM STATEMENT","Kamu merumuskan pertanyaan sendiri: variabel apa yang perlu dicari? Persamaan apa yang bisa dibentuk?","#ED7D31"),
        ("③ DATA COLLECTION","Eksplorasi bebas menggunakan solver digital! Masukkan koefisien dan amati langkah-langkah penyelesaiannya.","#70AD47"),
        ("④ DATA PROCESSING","Analisis pola: mengapa eliminasi berhasil? Apa syarat sistem punya solusi tunggal?","#7030A0"),
        ("⑤ VERIFICATION","Substitusi solusi kembali ke ketiga persamaan. Apakah semua persamaan terpenuhi?","#C00000"),
        ("⑥ GENERALIZATION","Rumuskan langkah umum penyelesaian SPLTV dengan kata-katamu sendiri!","#1A3C6E"),
    ]

    cols = st.columns(3)
    for i, (label, text, color) in enumerate(fases):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="border-left:4px solid {color};background:#FAFAFA;
                        padding:0.8rem 1rem;border-radius:0 10px 10px 0;margin-bottom:0.8rem;">
                <div style="font-weight:800;color:{color};font-size:0.9rem;">{label}</div>
                <div style="font-size:0.85rem;color:#444;margin-top:0.3rem;">{text}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="warning-card">
    <b>💡 Prasyarat yang Perlu Kamu Kuasai</b><br>
    Sebelum mempelajari SPLTV, pastikan kamu sudah memahami:
    <b>Sistem Persamaan Linear Dua Variabel (SPLDV)</b> dari SMP —
    khususnya metode eliminasi dan substitusi. SPLTV adalah perluasannya ke 3 variabel!
    </div>
    """, unsafe_allow_html=True)

    # Ringkasan konsep SPLTV
    st.markdown("### 📖 Apa itu SPLTV?")
    col_a, col_b = st.columns([1,1])
    with col_a:
        st.markdown("""
        <div class="info-card">
        <b>Bentuk Umum SPLTV:</b><br><br>
        <code style="font-size:1.05rem;">
        a₁x + b₁y + c₁z = d₁<br>
        a₂x + b₂y + c₂z = d₂<br>
        a₃x + b₃y + c₃z = d₃
        </code><br><br>
        Di mana <b>x, y, z</b> adalah variabel yang dicari,<br>
        dan <b>a, b, c, d</b> adalah konstanta (koefisien).
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="success-card">
        <b>✅ Ciri-ciri Sistem Persamaan Linear:</b><br><br>
        🔵 <b>Linear</b> → semua variabel berpangkat 1<br>
        🔵 <b>Persamaan</b> → menggunakan tanda "="<br>
        🔵 <b>Sistem</b> → semua persamaan berlaku serentak<br>
        🔵 <b>Tiga variabel</b> → ada 3 hal yang dicari<br><br>
        ⚠️ Butuh <b>minimal 3 persamaan</b> untuk solusi tunggal!
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# KP 1 — MENGENAL SPLTV
# ══════════════════════════════════════════
elif tab_choice == "🔍 KP 1 — Mengenal SPLTV":
    st.markdown("## 🔍 Kegiatan Pembelajaran 1: Mengenal SPLTV")

    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">① Stimulation — Pemantik</div>
        <div class="fase-text">
        Seorang pedagang menimbang tiga jenis bola di sekolah.<br><br>
        🏀 <b>2 bola basket + 1 bola kaki + 3 bola voli = 2.500 gram</b><br>
        ⚽ <b>1 bola basket + 2 bola kaki + 2 bola voli = 2.050 gram</b><br>
        🏐 <b>2 bola basket + 1 bola voli = 1.550 gram</b><br><br>
        <b>❓ Berapa gram berat masing-masing bola? Bisakah kita menemukannya?</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">② Problem Statement — Rumusan Masalah</div>
        <div class="fase-text">
        Tuliskan hipotesismu di LKS sebelum bereksplorasi:<br>
        <i>"Menurutku, untuk menemukan berat 3 jenis bola yang berbeda,
        kita memerlukan ... persamaan karena ..."</i><br><br>
        Kemudian tentukan variabel:<br>
        <i>Misalkan x = berat bola basket, y = berat bola kaki, z = berat bola voli</i>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Interaktif: Cek apakah suatu persamaan termasuk SPL atau bukan
    st.markdown("""
    <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
        <div class="fase-label" style="color:#70AD47;">③ Data Collection — Identifikasi SPLTV</div>
        <div class="fase-text">Gunakan alat di bawah untuk mengidentifikasi apakah suatu sistem termasuk SPLTV yang valid!</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🔎 Pemeriksa Bentuk Persamaan Linear")

    contoh_spltv = [
        ("2x + y + 3z = 2500", True, "Semua variabel berpangkat 1 → LINEAR ✅"),
        ("x + 2y + 2z = 2050", True, "Semua variabel berpangkat 1 → LINEAR ✅"),
        ("x² + y + z = 100", False, "Terdapat x² (berpangkat 2) → BUKAN linear ❌"),
        ("xy + z = 50", False, "Terdapat perkalian variabel xy → BUKAN linear ❌"),
        ("3k + 2h + b = 455", True, "Semua variabel berpangkat 1 → LINEAR ✅ (variabel boleh huruf apapun)"),
        ("2a - b + 4c = 0", True, "Semua variabel berpangkat 1 → LINEAR ✅"),
    ]

    for eq, is_lin, alasan in contoh_spltv:
        warna = "#F0FBF0" if is_lin else "#FEF0F0"
        border = "#70AD47" if is_lin else "#E74C3C"
        ikon = "✅" if is_lin else "❌"
        st.markdown(f"""
        <div style="background:{warna};border:1px solid {border};border-radius:10px;
                    padding:0.6rem 1rem;margin:0.3rem 0;display:flex;align-items:center;gap:1rem;">
            <span style="font-size:1.3rem;">{ikon}</span>
            <div>
                <code style="font-size:0.95rem;font-weight:700;">{eq}</code><br>
                <span style="font-size:0.82rem;color:#444;">{alasan}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # DATA PROCESSING
    st.markdown("""
    <div class="fase-box" style="border-color:#7030A0;background:#F5EFFF;">
        <div class="fase-label" style="color:#7030A0;">④ Data Processing — Membuat Model Matematika</div>
        <div class="fase-text">Latihan mengubah permasalahan nyata menjadi sistem persamaan linear! Cocokkan kalimat berikut.</div>
    </div>
    """, unsafe_allow_html=True)

    kasus = [
        {
            "konteks": "🏀 Masalah Bola (dari Eksplorasi 4.1)",
            "narasi": "2 bola basket + 1 bola kaki + 3 bola voli = 2500 g | 1 bola basket + 2 bola kaki + 2 bola voli = 2050 g | 2 bola basket + 1 bola voli = 1550 g",
            "model": "2x + y + 3z = 2500\nx + 2y + 2z = 2050\n2x + z = 1550",
            "var": "x = bola basket, y = bola kaki, z = bola voli",
            "solusi": "x = 650 g, y = 450 g, z = 250 g",
        },
        {
            "konteks": "🖊️ Masalah Toko Alat Tulis (Uji Kompetensi)",
            "narasi": "Buku + Pena + Penghapus dengan harga berbeda di Toko A: b+p+s=12rb | 2b+p+s=14rb | b+p+2s=14rb",
            "model": "b + p + s = 12\n2b + p + s = 14\nb + p + 2s = 14",
            "var": "b = harga buku (ribu Rp), p = harga pena, s = harga penghapus",
            "solusi": "b = 2, p = 8, s = 2 (dalam ribu rupiah)",
        },
    ]

    for k in kasus:
        with st.expander(f"📋 {k['konteks']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                <div class="warning-card">
                <b>Kalimat Cerita:</b><br>
                <span style="font-size:0.88rem;">{k['narasi'].replace(' | ','<br>')}</span>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                <div class="info-card">
                <b>Variabel:</b> {k['var']}
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div style="background:#1A3C6E;color:white;border-radius:12px;padding:1rem;text-align:center;">
                <div style="font-size:0.8rem;opacity:0.8;margin-bottom:0.5rem;">Model Matematika</div>
                <pre style="color:white;font-size:1rem;font-weight:700;text-align:left;margin:0;">{k['model']}</pre>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                <div class="success-card">
                <b>✅ Solusi:</b> {k['solusi']}
                </div>
                """, unsafe_allow_html=True)

    # GENERALIZATION
    st.markdown("---")
    with st.expander("⑥ 💡 Lihat Simpulan Konsep SPLTV"):
        st.markdown("""
        <div class="success-card">
        <b>Simpulan Kegiatan Pembelajaran 1:</b><br><br>
        ✅ SPLTV terdiri dari <b>3 persamaan linear</b> dengan <b>3 variabel</b> yang berlaku secara simultan<br>
        ✅ Ciri persamaan linear: semua variabel berpangkat <b>1</b>, tidak ada perkalian antar variabel<br>
        ✅ Langkah pemodelan: tentukan variabel → buat persamaan → pastikan sistemnya linear<br>
        ✅ SPLTV dapat memiliki: <b>1 solusi</b> (tepat), <b>banyak solusi</b>, atau <b>tidak ada solusi</b>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# KP 2 — SOLVER ELIMINASI & SUBSTITUSI
# ══════════════════════════════════════════
elif tab_choice == "🔢 KP 2 — Solver Metode Eliminasi & Substitusi":
    st.markdown("## 🔢 Kegiatan Pembelajaran 2: Menyelesaikan SPLTV")

    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">① Stimulation — Pemantik</div>
        <div class="fase-text">
        Toko A dan Toko B menjual buku, pena, dan penghapus dengan harga berbeda.<br>
        Dari beberapa transaksi diketahui:<br>
        📚 <b>b + p + s = 12.000</b> | 📚 <b>2b + p + s = 14.000</b> | 📚 <b>b + p + 2s = 14.000</b><br><br>
        <b>❓ Bagaimana menentukan harga satuan buku, pena, dan penghapus secara sistematis?</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">② Problem Statement — Hipotesis</div>
        <div class="fase-text">
        Tuliskan hipotesismu di LKS:<br>
        <i>"Untuk menyelesaikan SPLTV, aku akan mencoba cara ... karena ..."</i><br>
        Ingat cara SPLDV yang sudah dipelajari di SMP: eliminasi dan substitusi!
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
        <div class="fase-label" style="color:#70AD47;">③ Data Collection — Solver SPLTV Interaktif</div>
        <div class="fase-text">Masukkan koefisien sistem persamaan, lalu amati langkah-langkah penyelesaiannya!</div>
    </div>
    """, unsafe_allow_html=True)

    # Preset soal
    st.markdown("#### ⚡ Pilih Contoh Soal atau Masukkan Sendiri")
    preset = st.selectbox("Pilih preset soal:", [
        "Masukkan sendiri",
        "🏀 Bola (Eksplorasi 4.1): 2x+y+3z=2500, x+2y+2z=2050, 2x+z=1550",
        "🖊️ Alat Tulis (Uji Kompetensi): b+p+s=12, 2b+p+s=14, b+p+2s=14",
        "🏑 Tongkat (Latihan 4.1): 3k+2h+b=455, k+3h+2b=545, 2k-b=0",
        "🍎 Buah (kontekstual): j+2p+s=55, 2j+p+2s=65, j+p+s=45",
    ])

    presets = {
        "🏀 Bola (Eksplorasi 4.1): 2x+y+3z=2500, x+2y+2z=2050, 2x+z=1550":
            (2,1,3,2500, 1,2,2,2050, 2,0,1,1550),
        "🖊️ Alat Tulis (Uji Kompetensi): b+p+s=12, 2b+p+s=14, b+p+2s=14":
            (1,1,1,12, 2,1,1,14, 1,1,2,14),
        "🏑 Tongkat (Latihan 4.1): 3k+2h+b=455, k+3h+2b=545, 2k-b=0":
            (3,2,1,455, 1,3,2,545, 2,0,-1,0),
        "🍎 Buah (kontekstual): j+2p+s=55, 2j+p+2s=65, j+p+s=45":
            (1,2,1,55, 2,1,2,65, 1,1,1,45),
    }

    default = presets.get(preset, (2,1,3,2500, 1,2,2,2050, 2,0,1,1550))

    col_lbl, col_input = st.columns([1, 3])
    with col_lbl:
        st.markdown("""
        <div class="info-card" style="margin-top:1.5rem;">
        <b>📋 Form Input:</b><br>
        Masukkan koefisien untuk:<br>
        <b>Pers. (1):</b> a₁x + b₁y + c₁z = d₁<br>
        <b>Pers. (2):</b> a₂x + b₂y + c₂z = d₂<br>
        <b>Pers. (3):</b> a₃x + b₃y + c₃z = d₃
        </div>
        """, unsafe_allow_html=True)

    with col_input:
        col1, col2, col3, col4, col5 = st.columns([1.2,1.2,1.2,1.2,0.5])
        with col1: st.markdown("**a (koef. x)**")
        with col2: st.markdown("**b (koef. y)**")
        with col3: st.markdown("**c (koef. z)**")
        with col4: st.markdown("**d (konst.)**")
        with col5: st.markdown("**#**")

        c1, c2, c3, c4, c5 = st.columns([1.2,1.2,1.2,1.2,0.5])
        a1 = c1.number_input("a1", value=float(default[0]), step=1.0, label_visibility="collapsed")
        b1 = c2.number_input("b1", value=float(default[1]), step=1.0, label_visibility="collapsed")
        c1v = c3.number_input("c1", value=float(default[2]), step=1.0, label_visibility="collapsed")
        d1 = c4.number_input("d1", value=float(default[3]), step=1.0, label_visibility="collapsed")
        c5.markdown("<div style='text-align:center;padding-top:0.6rem;font-weight:800;color:#1A3C6E;'>(1)</div>", unsafe_allow_html=True)

        c1, c2, c3, c4, c5 = st.columns([1.2,1.2,1.2,1.2,0.5])
        a2 = c1.number_input("a2", value=float(default[4]), step=1.0, label_visibility="collapsed")
        b2 = c2.number_input("b2", value=float(default[5]), step=1.0, label_visibility="collapsed")
        c2v = c3.number_input("c2", value=float(default[6]), step=1.0, label_visibility="collapsed")
        d2 = c4.number_input("d2", value=float(default[7]), step=1.0, label_visibility="collapsed")
        c5.markdown("<div style='text-align:center;padding-top:0.6rem;font-weight:800;color:#1A3C6E;'>(2)</div>", unsafe_allow_html=True)

        c1, c2, c3, c4, c5 = st.columns([1.2,1.2,1.2,1.2,0.5])
        a3 = c1.number_input("a3", value=float(default[8]), step=1.0, label_visibility="collapsed")
        b3 = c2.number_input("b3", value=float(default[9]), step=1.0, label_visibility="collapsed")
        c3v = c3.number_input("c3", value=float(default[10]), step=1.0, label_visibility="collapsed")
        d3 = c4.number_input("d3", value=float(default[11]), step=1.0, label_visibility="collapsed")
        c5.markdown("<div style='text-align:center;padding-top:0.6rem;font-weight:800;color:#1A3C6E;'>(3)</div>", unsafe_allow_html=True)

    def fmt(v):
        v = int(v) if v == int(v) else v
        return str(v)

    def persamaan_str(a,b,c,d, vars=("x","y","z")):
        parts = []
        for coef, var in zip([a,b,c], vars):
            coef = int(coef) if coef == int(coef) else coef
            if coef == 0: continue
            if coef == 1: parts.append(f"+{var}")
            elif coef == -1: parts.append(f"-{var}")
            elif coef > 0: parts.append(f"+{coef}{var}")
            else: parts.append(f"{coef}{var}")
        if not parts: return f"0 = {int(d)}"
        s = "".join(parts).lstrip("+")
        return f"{s} = {int(d) if d==int(d) else d}"

    # Display persamaan yang diinput
    d_val = int(d1) if d1==int(d1) else d1
    st.markdown(f"""
    <div style="background:#1A3C6E;color:white;border-radius:14px;padding:1rem 1.5rem;
                margin:1rem 0;font-family:monospace;font-size:1.05rem;">
    <div style="opacity:0.8;font-size:0.8rem;margin-bottom:0.5rem;">Sistem Persamaan yang Diinput:</div>
    <div>(1): {persamaan_str(a1,b1,c1v,d1)}</div>
    <div>(2): {persamaan_str(a2,b2,c2v,d2)}</div>
    <div>(3): {persamaan_str(a3,b3,c3v,d3)}</div>
    </div>
    """, unsafe_allow_html=True)

    # Selesaikan
    sol, err = solve_spltv(a1,b1,c1v,d1, a2,b2,c2v,d2, a3,b3,c3v,d3)

    if err:
        st.markdown(f'<div class="danger-card">⚠️ <b>{err}</b><br>Sistem mungkin memiliki banyak solusi atau tidak ada solusi.</div>', unsafe_allow_html=True)
    else:
        x_sol, y_sol, z_sol = sol
        x_str = format_val(x_sol)
        y_str = format_val(y_sol)
        z_str = format_val(z_sol)

        col_r1, col_r2, col_r3 = st.columns(3)
        for col_r, var, val, color in zip(
            [col_r1, col_r2, col_r3],
            ["x", "y", "z"],
            [x_str, y_str, z_str],
            ["#1A3C6E", "#C00000", "#70AD47"]
        ):
            with col_r:
                st.markdown(f"""
                <div style="background:{color};color:white;border-radius:14px;padding:1.2rem;
                            text-align:center;box-shadow:0 3px 12px rgba(0,0,0,0.2);">
                    <div style="font-size:0.85rem;opacity:0.85;">{var} =</div>
                    <div style="font-size:2.8rem;font-weight:800;">{val}</div>
                </div>
                """, unsafe_allow_html=True)

        # Verifikasi
        st.markdown("---")
        st.markdown("#### ✅ Verifikasi Solusi (Substitusi Balik)")
        persamaan_data = [
            (a1,b1,c1v,d1,1),
            (a2,b2,c2v,d2,2),
            (a3,b3,c3v,d3,3),
        ]
        semua_benar = True
        for a,b,c,d,n in persamaan_data:
            lhs = a*x_sol + b*y_sol + c*z_sol
            selisih = abs(lhs - d)
            benar = selisih < 0.01
            if not benar: semua_benar = False
            warna = "#F0FBF0" if benar else "#FEF0F0"
            border = "#70AD47" if benar else "#E74C3C"
            ikon = "✅" if benar else "❌"
            st.markdown(f"""
            <div style="background:{warna};border:1px solid {border};border-radius:10px;
                        padding:0.6rem 1rem;margin:0.3rem 0;">
            {ikon} <b>Persamaan ({n}):</b>
            {fmt(a)}·{x_str} + {fmt(b)}·{y_str} + {fmt(c)}·{z_str}
            = {lhs:.2f} {"≈" if abs(lhs-round(lhs))>0.001 else "="} {fmt(d)}
            {"✔ Terpenuhi!" if benar else "✖ Tidak terpenuhi!"}
            </div>
            """, unsafe_allow_html=True)

        if semua_benar:
            st.markdown('<div class="success-card">🎉 <b>Semua persamaan terpenuhi!</b> Solusi telah diverifikasi dengan benar.</div>', unsafe_allow_html=True)

    # Langkah-langkah eliminasi
    st.markdown("---")
    st.markdown("""
    <div class="fase-box" style="border-color:#7030A0;background:#F5EFFF;">
        <div class="fase-label" style="color:#7030A0;">④ Data Processing — Langkah Eliminasi & Substitusi</div>
        <div class="fase-text">Amati alur langkah penyelesaian berikut dan catat pola yang kamu temukan di LKS!</div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Lihat Langkah-langkah Penyelesaian Detail"):
        if sol is not None:
            x_sol, y_sol, z_sol = sol

            # Step 1: eliminate x
            st.markdown("**🔵 FASE ELIMINASI — Mengurangi variabel satu per satu**")
            # eq4 = a1*eq2 - a2*eq1
            fa1, fb1, fc1, fd1 = int(a1), int(b1), int(c1v), int(d1)
            fa2, fb2, fc2, fd2 = int(a2), int(b2), int(c2v), int(d2)
            fa3, fb3, fc3, fd3 = int(a3), int(b3), int(c3v), int(d3)

            # Eliminate x between eq1 and eq2
            m12 = fa2
            n12 = fa1
            e4b = n12*fb2 - m12*fb1
            e4c = n12*fc2 - m12*fc1
            e4d = n12*fd2 - m12*fd1

            # Eliminate x between eq1 and eq3
            m13 = fa3
            n13 = fa1
            e5b = n13*fb3 - m13*fb1
            e5c = n13*fc3 - m13*fc1
            e5d = n13*fd3 - m13*fd1

            st.markdown(f"""
            <div class="step-box">
            <b>Langkah 1:</b> Eliminasi x dari Pers.(1) dan Pers.(2)<br>
            <code>({fa1})×Pers.(2) − ({fa2})×Pers.(1)</code><br>
            → Persamaan (4): <b>{e4b}y {'+' if e4c>=0 else ''}{e4c}z = {e4d}</b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="step-box">
            <b>Langkah 2:</b> Eliminasi x dari Pers.(1) dan Pers.(3)<br>
            <code>({fa1})×Pers.(3) − ({fa3})×Pers.(1)</code><br>
            → Persamaan (5): <b>{e5b}y {'+' if e5c>=0 else ''}{e5c}z = {e5d}</b>
            </div>
            """, unsafe_allow_html=True)

            # Eliminate y between eq4 and eq5
            m45 = e5b; n45 = e4b
            e6c = n45*e5c - m45*e4c
            e6d = n45*e5d - m45*e4d

            if e6c != 0:
                z_calc = e6d / e6c
                st.markdown(f"""
                <div class="step-box">
                <b>Langkah 3:</b> Eliminasi y dari Pers.(4) dan Pers.(5)<br>
                <code>({e4b})×Pers.(5) − ({e5b})×Pers.(4)</code><br>
                → Persamaan (6): <b>{e6c}z = {e6d}</b><br>
                → <b style="color:#C00000;">z = {e6d}/{e6c} = {z_sol:.4g}</b>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("**🟢 FASE SUBSTITUSI — Memasukkan nilai yang sudah diketahui**")

            if e4b != 0 and e6c != 0:
                y_from4 = (e4d - e4c*z_sol) / e4b
                st.markdown(f"""
                <div class="step-box">
                <b>Langkah 4:</b> Substitusi z ke Persamaan (4)<br>
                <code>{e4b}y + {e4c}·({z_sol:.4g}) = {e4d}</code><br>
                → <code>{e4b}y = {e4d} - {e4c*z_sol:.4g} = {e4b*y_from4:.4g}</code><br>
                → <b style="color:#C00000;">y = {y_sol:.4g}</b>
                </div>
                """, unsafe_allow_html=True)

            x_from1 = (fd1 - fb1*y_sol - fc1*z_sol) / fa1 if fa1 != 0 else 0
            st.markdown(f"""
            <div class="step-box">
            <b>Langkah 5:</b> Substitusi y dan z ke Persamaan (1)<br>
            <code>{fa1}x + {fb1}·({y_sol:.4g}) + {fc1}·({z_sol:.4g}) = {fd1}</code><br>
            → <code>{fa1}x = {fd1} - {fb1*y_sol:.4g} - {fc1*z_sol:.4g} = {fa1*x_from1:.4g}</code><br>
            → <b style="color:#C00000;">x = {x_sol:.4g}</b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="success-card">
            <b>✅ Solusi SPLTV:</b><br>
            x = <b>{x_str}</b>,  y = <b>{y_str}</b>,  z = <b>{z_str}</b>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Masukkan sistem dengan solusi tunggal untuk melihat langkah-langkah.")

    # GENERALIZATION
    st.markdown("---")
    with st.expander("⑥ 💡 Lihat Simpulan Metode Penyelesaian SPLTV"):
        st.markdown("""
        <div class="success-card">
        <b>✅ Langkah Umum Penyelesaian SPLTV:</b><br><br>
        <b>1.</b> Pilih satu variabel untuk <b>dieliminasi</b> dari dua pasang persamaan → dapat 2 persamaan baru (SPLDV)<br>
        <b>2.</b> Selesaikan SPLDV (eliminasi/substitusi) → dapatkan nilai satu variabel<br>
        <b>3.</b> Substitusi kembali ke persamaan sebelumnya → dapatkan variabel kedua<br>
        <b>4.</b> Substitusi ke persamaan awal → dapatkan variabel ketiga<br>
        <b>5.</b> <b>Verifikasi</b> dengan mensubstitusi semua nilai ke ketiga persamaan awal<br><br>
        💡 <b>Prinsip kunci:</b> Setiap eliminasi mengurangi 1 variabel. Tiga variabel → butuh 2 kali eliminasi utama!
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# KP 3 — INTERPRETASI & PEMODELAN
# ══════════════════════════════════════════
elif tab_choice == "📊 KP 3 — Interpretasi & Pemodelan":
    st.markdown("## 📊 Kegiatan Pembelajaran 3: Interpretasi & Pemodelan Masalah")

    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">① Stimulation — Pemantik Literasi Finansial</div>
        <div class="fase-text">
        UMKM Bu Sari memproduksi sabun cuci tangan dan sabun mandi.<br>
        Modal produksi maksimal <b>Rp500.000</b>, kapasitas maksimal <b>100 liter</b>,
        dan permintaan sabun cuci tangan minimal <b>30 liter</b>.<br><br>
        <b>❓ Berapa liter sabun cuci tangan dan sabun mandi yang harus diproduksi agar
        memperoleh keuntungan maksimal?</b><br>
        <i>(Ini akan menjadi Sistem Pertidaksamaan Linear — perluasan dari SPLTV!)</i>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    tab_a, tab_b, tab_c = st.tabs([
        "🧮 Studio Pemodelan",
        "📈 Visualisasi Solusi",
        "🌍 Konteks Kehidupan Nyata"
    ])

    # ── STUDIO PEMODELAN
    with tab_a:
        st.markdown("""
        <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
            <div class="fase-label" style="color:#70AD47;">③ Data Collection — Ubah Kalimat Cerita ke SPLTV</div>
            <div class="fase-text">Latih kemampuan pemodelanmu! Isi variabel dan sistem persamaannya.</div>
        </div>
        """, unsafe_allow_html=True)

        soal_model = st.selectbox("Pilih soal pemodelan:", [
            "🏑 Tongkat Olahraga — Latihan 4.1 No.1",
            "🧴 Kemasan Minuman — Latihan 4.1 No.2",
            "🍎 Harga Buah — Latihan 4.1 No.3",
            "📚 Harga Alat Tulis — Uji Kompetensi No.1",
        ])

        soal_data = {
            "🏑 Tongkat Olahraga — Latihan 4.1 No.1": {
                "narasi": """Sebuah toko olahraga memiliki 3 jenis tongkat:
                tongkat kasti (k), tongkat hoki (h), dan tongkat bisbol (b).
                Diketahui:
                • 3 tongkat kasti + 2 tongkat hoki + 1 tongkat bisbol panjangnya 455 cm
                • 1 tongkat kasti + 3 tongkat hoki + 2 tongkat bisbol panjangnya 545 cm
                • 2 tongkat kasti panjangnya sama dengan 1 tongkat bisbol""",
                "variabel": "k = panjang tongkat kasti\nh = panjang tongkat hoki\nb = panjang tongkat bisbol",
                "sistem": "3k + 2h + b = 455\nk + 3h + 2b = 545\n2k - b = 0",
                "solusi": "k = 55 cm, h = 90 cm, b = 110 cm",
                "makna": "Tongkat kasti panjang 55 cm, tongkat hoki 90 cm, tongkat bisbol 110 cm.",
                "a": (3,2,1,455, 1,3,2,545, 2,0,-1,0),
            },
            "🧴 Kemasan Minuman — Latihan 4.1 No.2": {
                "narasi": """Sebuah pabrik minuman memiliki kemasan kecil (k), sedang (s), dan besar (b).
                Dari data penjualan:
                • 1k + 2s + 1b = 1.600 ml
                • 2k + 1s + 1b = 1.800 ml
                • 1k + 1s + 2b = 2.200 ml""",
                "variabel": "k = volume kemasan kecil (ml)\ns = volume kemasan sedang (ml)\nb = volume kemasan besar (ml)",
                "sistem": "k + 2s + b = 1600\n2k + s + b = 1800\nk + s + 2b = 2200",
                "solusi": "k = 200 ml, s = 400 ml, b = 600 ml",
                "makna": "Kemasan kecil 200 ml, sedang 400 ml, besar 600 ml.",
                "a": (1,2,1,1600, 2,1,1,1800, 1,1,2,2200),
            },
            "🍎 Harga Buah — Latihan 4.1 No.3": {
                "narasi": """Di pasar, diketahui:
                • 2 kg jeruk + 1 kg pepaya + 1 kg salak = Rp55.000
                • 1 kg jeruk + 2 kg pepaya + 2 kg salak = Rp65.000
                • 1 kg jeruk + 1 kg pepaya + 1 kg salak = Rp45.000""",
                "variabel": "j = harga jeruk per kg (ribu Rp)\np = harga pepaya per kg (ribu Rp)\ns = harga salak per kg (ribu Rp)",
                "sistem": "2j + p + s = 55\nj + 2p + 2s = 65\nj + p + s = 45",
                "solusi": "j = 10, p = 20, s = 15 (ribu Rp)",
                "makna": "Harga jeruk Rp10.000/kg, pepaya Rp20.000/kg, salak Rp15.000/kg.",
                "a": (2,1,1,55, 1,2,2,65, 1,1,1,45),
            },
            "📚 Harga Alat Tulis — Uji Kompetensi No.1": {
                "narasi": """Di toko A:
                • 1 buku + 1 pena + 1 penghapus = Rp12.000
                • 2 buku + 1 pena + 1 penghapus = Rp14.000
                • 1 buku + 1 pena + 2 penghapus = Rp14.000""",
                "variabel": "b = harga buku (ribu Rp)\np = harga pena (ribu Rp)\ns = harga penghapus (ribu Rp)",
                "sistem": "b + p + s = 12\n2b + p + s = 14\nb + p + 2s = 14",
                "solusi": "b = 2, p = 8, s = 2 (ribu Rp)",
                "makna": "Harga buku Rp2.000, pena Rp8.000, penghapus Rp2.000.",
                "a": (1,1,1,12, 2,1,1,14, 1,1,2,14),
            },
        }

        data = soal_data[soal_model]

        col1, col2 = st.columns([1,1])
        with col1:
            st.markdown(f"""
            <div class="warning-card">
            <b>📖 Soal Cerita:</b><br>
            <span style="font-size:0.9rem;">{data['narasi'].replace(chr(10), '<br>')}</span>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="info-card">
            <b>📌 Pemisalan Variabel:</b><br>
            <pre style="font-size:0.9rem;margin:0.3rem 0;">{data['variabel']}</pre>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="background:#1A3C6E;color:white;border-radius:12px;padding:0.8rem 1rem;margin-top:0.5rem;">
            <div style="font-size:0.8rem;opacity:0.8;margin-bottom:0.3rem;">Model Matematika (SPLTV):</div>
            <pre style="color:white;font-size:0.95rem;font-weight:700;margin:0;">{data['sistem']}</pre>
            </div>
            """, unsafe_allow_html=True)

        # Selesaikan otomatis
        a_vals = data["a"]
        sol2, err2 = solve_spltv(*a_vals)
        if sol2 is not None:
            x2,y2,z2 = sol2
            st.markdown(f"""
            <div class="success-card" style="margin-top:0.8rem;">
            <b>✅ Solusi Matematis:</b> {data['solusi']}<br>
            <b>🔍 Makna dalam Konteks:</b> {data['makna']}
            </div>
            """, unsafe_allow_html=True)

    # ── VISUALISASI
    with tab_b:
        st.markdown("### 📈 Visualisasi Nilai Solusi")
        st.markdown("""
        <div class="info-card">
        Grafik batang di bawah menampilkan nilai ketiga variabel dari sistem yang diselesaikan.
        SPLTV dengan 3 variabel membutuhkan ruang 3 dimensi untuk digambarkan grafiknya —
        yang lebih kompleks dari SPLDV. Di sini kita visualisasikan solusinya secara numerik.
        </div>
        """, unsafe_allow_html=True)

        preset_vis = st.selectbox("Pilih sistem untuk divisualisasi:", list(soal_data.keys()), key="vis_sel")
        data_v = soal_data[preset_vis]
        sol_v, _ = solve_spltv(*data_v["a"])

        if sol_v is not None:
            x_v, y_v, z_v = sol_v
            vars_label = [line.split("=")[0].strip() for line in data_v["variabel"].split("\n")][:3]
            vals = [x_v, y_v, z_v]
            colors = ["#1A3C6E", "#C00000", "#70AD47"]

            fig, axes = plt.subplots(1, 2, figsize=(12, 4))
            fig.patch.set_facecolor('#FAFBFF')

            # Bar chart
            ax = axes[0]
            ax.set_facecolor('#FAFBFF')
            bars = ax.bar(vars_label, vals, color=colors, edgecolor='white', linewidth=2, width=0.5)
            for bar, val in zip(bars, vals):
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(vals)*0.01,
                        f'{val:.4g}', ha='center', va='bottom', fontweight='bold', fontsize=11)
            ax.set_title("Nilai Solusi SPLTV", fontweight='bold', color='#1A3C6E', pad=12)
            ax.set_ylabel("Nilai", color='#1A3C6E')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.tick_params(colors='#1A3C6E')

            # Verifikasi bar
            ax2 = axes[1]
            ax2.set_facecolor('#FAFBFF')
            a_v = data_v["a"]
            lhs_vals = [
                a_v[0]*x_v + a_v[1]*y_v + a_v[2]*z_v,
                a_v[4]*x_v + a_v[5]*y_v + a_v[6]*z_v,
                a_v[8]*x_v + a_v[9]*y_v + a_v[10]*z_v,
            ]
            rhs_vals = [a_v[3], a_v[7], a_v[11]]
            labels_eq = ["Pers.(1)", "Pers.(2)", "Pers.(3)"]
            x_pos = np.arange(len(labels_eq))
            ax2.bar(x_pos - 0.2, rhs_vals, 0.35, label="Nilai d (konstan)", color="#BDD7EE", edgecolor='white')
            ax2.bar(x_pos + 0.2, lhs_vals, 0.35, label="Nilai LHS (dari solusi)", color="#2E75B6", edgecolor='white')
            ax2.set_xticks(x_pos)
            ax2.set_xticklabels(labels_eq)
            ax2.set_title("Verifikasi: LHS vs Konstanta", fontweight='bold', color='#1A3C6E', pad=12)
            ax2.legend(fontsize=8)
            ax2.spines['top'].set_visible(False)
            ax2.spines['right'].set_visible(False)
            ax2.tick_params(colors='#1A3C6E')

            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

            st.markdown("""
            <div class="info-card">
            <b>📌 Penjelasan Grafik Kanan (Verifikasi):</b><br>
            Grafik batang kanan membandingkan nilai ruas kiri (LHS) setelah substitusi solusi
            dengan nilai konstanta (d) di ruas kanan. Jika kedua batang sama tinggi →
            solusi terbukti benar!
            </div>
            """, unsafe_allow_html=True)

    # ── KONTEKS KEHIDUPAN NYATA
    with tab_c:
        st.markdown("### 🌍 SPLTV dalam Kehidupan Nyata — Literasi Finansial")

        st.markdown("""
        <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
            <div class="fase-label" style="color:#ED7D31;">Koneksi ke Literasi Finansial</div>
            <div class="fase-text">
            SPLTV sering muncul dalam masalah keuangan nyata. Berikut contoh-contoh
            yang relevan dengan kehidupan sehari-hari.
            </div>
        </div>
        """, unsafe_allow_html=True)

        konteks_list = [
            ("💰 Investasi Portfolio",
             "Seorang investor menanamkan modal di 3 instrumen: deposito (6%/tahun), reksadana (10%/tahun), saham (15%/tahun). Total modal Rp100 juta, total bunga Rp11,5 juta/tahun, dan modal di reksadana = modal di deposito + Rp10 juta.",
             "x + y + z = 100\n0.06x + 0.10y + 0.15z = 11.5\ny = x + 10",
             "x=30, y=40, z=30 (juta Rp)"),
            ("🏪 Produksi UMKM",
             "UMKM Bu Ani memproduksi 3 jenis kue. Total 200 kue/hari. Kue A dua kali lebih banyak dari kue B. Kue C 20 buah lebih banyak dari kue B.",
             "x + y + z = 200\nx = 2y\nz = y + 20",
             "x=120, y=60, z=80 (kue/hari)"),
            ("🎓 Nilai Rapor",
             "Nilai akhir terdiri dari 3 komponen: ulangan harian (UH), PTS, dan PAS. Rata-rata = 85. UH + PTS = 2 × PAS. PTS = UH - 5.",
             "UH + PTS + PAS = 255 (3×85)\nUH + PTS = 2×PAS → UH+PTS-2z=0\nUH - PTS = 5",
             "UH=90, PTS=85, PAS=80"),
        ]

        for judul, narasi, model, solusi in konteks_list:
            with st.expander(f"📋 {judul}"):
                col1, col2 = st.columns([3,2])
                with col1:
                    st.markdown(f"""
                    <div class="warning-card">
                    <b>Situasi:</b><br>{narasi}
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div style="background:#1A3C6E;color:white;border-radius:10px;padding:0.8rem;">
                    <div style="font-size:0.78rem;opacity:0.8;">Model SPLTV:</div>
                    <pre style="color:white;font-size:0.88rem;margin:0.3rem 0;">{model}</pre>
                    </div>
                    <div class="success-card" style="margin-top:0.4rem;font-size:0.88rem;">
                    ✅ <b>Solusi:</b> {solusi}
                    </div>
                    """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# SOAL LATIHAN INTERAKTIF
# ══════════════════════════════════════════
elif tab_choice == "📝 Soal Latihan Interaktif":
    st.markdown("## 📝 Soal Latihan Interaktif")
    st.markdown("""
    <div class="warning-card">
    <b>📌 Petunjuk:</b> Kerjakan soal-soal berikut secara mandiri dan jujur.
    Gunakan solver digital di tab sebelumnya hanya untuk <b>verifikasi</b>, bukan langsung menyalin jawaban!
    Waktu pengerjaan: ±45 menit.
    </div>
    """, unsafe_allow_html=True)

    if 'skor_spltv' not in st.session_state:
        st.session_state.skor_spltv = 0
    if 'jawab_spltv' not in st.session_state:
        st.session_state.jawab_spltv = {}

    soal_list = [
        {
            "no": 1, "tipe": "PG", "kp": "KP 1",
            "soal": "Manakah yang merupakan Sistem Persamaan Linear Tiga Variabel?",
            "konteks": "",
            "pilihan": [
                "A. 2x + y = 5 dan x − y + z = 3",
                "B. 2x + y + z = 5; x − y + 2z = 3; 3x + 2y − z = 7",
                "C. x² + y + z = 10; 2x + y + z = 8; x + y + 2z = 6",
                "D. 2xy + z = 5; x + yz = 3; xy + z = 4"
            ],
            "jawaban": "B",
            "pembahasan": "Pilihan B memiliki 3 persamaan dengan 3 variabel (x, y, z) dan semua variabel berpangkat 1. Pilihan A hanya 2 persamaan, C ada x², D ada perkalian variabel xy."
        },
        {
            "no": 2, "tipe": "PG", "kp": "KP 1",
            "soal": "Jika 3 pensil + 2 buku + 1 penghapus = Rp22.000 dimodelkan sebagai 3p + 2b + q = 22, variabel manakah yang tidak muncul dalam persamaan ini?",
            "konteks": "p = harga pensil, b = harga buku, q = harga penghapus (dalam ribuan)",
            "pilihan": ["A. Tidak ada, semua variabel muncul", "B. Variabel p", "C. Variabel z", "D. Variabel b"],
            "jawaban": "A",
            "pembahasan": "Semua variabel p, b, dan q muncul dalam persamaan 3p + 2b + q = 22. Tidak ada variabel yang hilang."
        },
        {
            "no": 3, "tipe": "PG", "kp": "KP 2",
            "soal": "Diketahui sistem: x + y + z = 6; 2x − y + z = 3; x + 2y − z = 3. Nilai x + y adalah ...",
            "konteks": "💡 Gunakan eliminasi untuk mengurangi variabel secara bertahap!",
            "pilihan": ["A. 3", "B. 4", "C. 5", "D. 6"],
            "jawaban": "B",
            "pembahasan": "Dari sistem: eliminasi z dari Pers(1)&(3): 2x+3y=9. Eliminasi z dari Pers(1)&(2): 3x=9 → x=3. Substitusi: y=1, z=2. Jadi x+y = 3+1 = 4."
        },
        {
            "no": 4, "tipe": "PG", "kp": "KP 2",
            "soal": "Diketahui SPLTV: 2a + b + c = 10; a + 2b + c = 11; a + b + 2c = 12. Nilai a + b + c = ...",
            "konteks": "",
            "pilihan": ["A. 9", "B. 10", "C. 11", "D. 11"],
            "jawaban": "C",
            "pembahasan": "Jumlahkan ketiga persamaan: 4a + 4b + 4c = 33 → tidak bulat. Coba eliminasi: dari pers(1)-(2): a-b=-1; dari pers(2)-(3): b-c=-1. Sehingga a=2,b=3,c=4, total a+b+c=9."
        },
        {
            "no": 5, "tipe": "PG", "kp": "KP 3",
            "soal": "Tongkat kasti (k), hoki (h), bisbol (b): 3k+2h+b=455; k+3h+2b=545; 2k=b. Panjang tongkat hoki adalah ...",
            "konteks": "💡 Ini soal dari Latihan 4.1 buku paket!",
            "pilihan": ["A. 55 cm", "B. 90 cm", "C. 110 cm", "D. 45 cm"],
            "jawaban": "B",
            "pembahasan": "Dari 2k=b → b=2k. Substitusi ke pers(1): 3k+2h+2k=455 → 5k+2h=455. Ke pers(2): k+3h+4k=545 → 5k+3h=545. Kurangkan: h=90 cm. Maka k=55 cm, b=110 cm."
        },
        {
            "no": 6, "tipe": "PG", "kp": "KP 2",
            "soal": "Sebuah SPLTV memiliki determinan matriks koefisien = 0. Artinya ...",
            "konteks": "",
            "pilihan": [
                "A. Sistem memiliki tepat satu solusi",
                "B. Sistem memiliki banyak solusi atau tidak ada solusi",
                "C. Semua variabel bernilai 0",
                "D. Sistem salah karena tidak bisa dibentuk"
            ],
            "jawaban": "B",
            "pembahasan": "Determinan = 0 berarti sistem tidak memiliki solusi tunggal. Kemungkinannya: banyak solusi (persamaan saling bergantung) atau tidak ada solusi (persamaan kontradiktif). Lihat diferensiasi pada buku halaman 143."
        },
        {
            "no": 7, "tipe": "Isian", "kp": "KP 3",
            "soal": "Di pasar, 2 kg jeruk + 1 kg pepaya + 1 kg salak = Rp55.000; 1 kg jeruk + 2 kg pepaya + 2 kg salak = Rp65.000; 1 kg jeruk + 1 kg pepaya + 1 kg salak = Rp45.000. Harga jeruk per kg adalah ...",
            "konteks": "💡 Ini soal Latihan 4.1 No.3 dari buku paket!",
            "pilihan": None,
            "jawaban": "10000",
            "pembahasan": "Misal j, p, s (ribu Rp). Pers(3)-(1): -j = -10 → j = 10. Pers(3)-(2): -p-s = -20 → p+s=20. Dari pers(3): p+s=35 → cek: 10+p+s=45 → p+s=35. Eliminasi antar pers: p=20, s=15. Harga jeruk = Rp10.000."
        },
        {
            "no": 8, "tipe": "Isian", "kp": "KP 3",
            "soal": "Alat tulis: b + p + s = 12; 2b + p + s = 14; b + p + 2s = 14 (dalam ribu rupiah). Harga pena (p) adalah ...",
            "konteks": "💡 Ini soal Uji Kompetensi dari buku paket!",
            "pilihan": None,
            "jawaban": "8000",
            "pembahasan": "Pers(2)-Pers(1): b=2. Pers(3)-Pers(1): s=2. Substitusi ke pers(1): 2+p+2=12 → p=8 (ribu Rp) = Rp8.000."
        },
    ]

    sudah_submit = st.session_state.get('submitted_spltv', False)
    skor_total = 0

    for soal in soal_list:
        kp_color = {"KP 1": "#2E75B6", "KP 2": "#70AD47", "KP 3": "#ED7D31"}[soal["kp"]]
        st.markdown(f"""
        <div style="border:1px solid #E0E0E0;border-radius:12px;padding:1rem 1.2rem;margin:0.8rem 0;
                    border-left:5px solid {kp_color};">
        <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem;">
            <span style="background:{kp_color};color:white;padding:2px 10px;border-radius:20px;
                         font-size:0.78rem;font-weight:700;">{soal['kp']}</span>
            <span style="background:#F0F0F0;padding:2px 10px;border-radius:20px;
                         font-size:0.78rem;font-weight:700;">{soal['tipe']}</span>
            <b>Soal {soal['no']}</b>
        </div>
        <div style="font-size:0.95rem;font-weight:600;">{soal['soal']}</div>
        {f'<div style="background:#FFF8E6;padding:0.5rem 0.8rem;border-radius:8px;margin-top:0.4rem;font-size:0.88rem;color:#8B6914;">{soal["konteks"]}</div>' if soal["konteks"] else ""}
        </div>
        """, unsafe_allow_html=True)

        key = f"soal_spltv_{soal['no']}"
        if soal["tipe"] == "PG":
            jawab = st.radio("Pilih jawaban:", soal["pilihan"],
                            key=key, label_visibility="collapsed",
                            index=None if key not in st.session_state.jawab_spltv else
                            soal["pilihan"].index(st.session_state.jawab_spltv.get(key, soal["pilihan"][0])))
            if jawab:
                st.session_state.jawab_spltv[key] = jawab
        else:
            jawab = st.text_input("Jawaban kamu (angka saja):", key=key, placeholder="Contoh: 10000")
            if jawab:
                st.session_state.jawab_spltv[key] = jawab

        if sudah_submit and key in st.session_state.jawab_spltv:
            j = st.session_state.jawab_spltv[key]
            benar = (soal["tipe"] == "PG" and j and j.startswith(soal["jawaban"])) or \
                    (soal["tipe"] == "Isian" and soal["jawaban"].lower() in j.lower().replace(".","").replace(",",""))
            if benar:
                skor_total += 1
                st.markdown(f'<div class="success-card" style="font-size:0.85rem;">✅ <b>BENAR!</b> {soal["pembahasan"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="danger-card" style="font-size:0.85rem;">❌ <b>Belum tepat.</b> Jawaban: <b>{soal["jawaban"]}</b>. {soal["pembahasan"]}</div>', unsafe_allow_html=True)

        st.markdown("")

    col_btn1, col_btn2 = st.columns([1, 3])
    with col_btn1:
        if st.button("✅ Submit & Lihat Nilai", type="primary", use_container_width=True):
            st.session_state.submitted_spltv = True
            st.rerun()
    with col_btn2:
        if st.button("🔄 Reset Jawaban", use_container_width=True):
            st.session_state.submitted_spltv = False
            st.session_state.jawab_spltv = {}
            st.rerun()

    if sudah_submit:
        persen = skor_total / len(soal_list) * 100
        emoji = "🏆" if persen >= 80 else ("👍" if persen >= 60 else "💪")
        warna_nilai = "#70AD47" if persen >= 80 else ("#ED7D31" if persen >= 60 else "#C00000")
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#1A3C6E,#2E75B6);color:white;
                    border-radius:16px;padding:1.5rem 2rem;text-align:center;margin-top:1rem;">
            <div style="font-size:1.1rem;opacity:0.9;">Nilai Akhir {emoji}</div>
            <div style="font-size:4rem;font-weight:800;color:{warna_nilai};">{persen:.0f}</div>
            <div style="font-size:1rem;opacity:0.8;">{skor_total} dari {len(soal_list)} soal benar</div>
            <div style="margin-top:0.8rem;font-size:0.9rem;">
            {'🏆 Excellent! Kamu sudah sangat memahami SPLTV!' if persen>=80 else ('👍 Bagus! Pelajari lagi bagian yang masih salah.' if persen>=60 else '💪 Semangat! Eksplorasi lebih dalam dengan solver digital!')}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 🔍 Refleksi Penggunaan Kalkulator Digital Streamlit")
        r1 = st.text_area("1. Fitur apa yang paling membantumu memahami SPLTV? Mengapa?",
                          placeholder="Tuliskan refleksimu di sini...", height=80)
        r2 = st.text_area("2. Apa perbedaan yang kamu rasakan saat menyelesaikan SPLTV vs SPLDV?",
                          placeholder="Tuliskan refleksimu di sini...", height=80)
        r3 = st.text_area("3. Bagaimana perasaanmu belajar matematika dengan kalkulator digital ini?",
                          placeholder="Tuliskan refleksimu di sini...", height=80)
        if r1 or r2 or r3:
            st.markdown('<div class="success-card">✅ Terima kasih atas refleksimu! Salin ke LKS-mu.</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════
# VIDEO BAHAN/MATERI
# ══════════════════════════════════════════
elif tab_choice == "🎬 Video Bahan/Materi":
    st.markdown("## 🎬 Video Bahan/Materi")

    st.markdown("""
    <div class="info-card">
    <b>📺 Panduan Menonton Video</b><br><br>
    Sebelum atau sesudah bereksplorasi dengan kalkulator digital, tonton video berikut untuk
    memperkuat pemahamanmu tentang <b>Sistem Persamaan Linear Tiga Variabel (SPLTV)</b>.
    Catat poin-poin penting ke dalam LKS-mu!
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">🎥 Video Pembelajaran — SPLTV (Sistem Persamaan Linear Tiga Variabel)</div>
        <div class="fase-text">
        Simak video berikut dengan seksama. Perhatikan penjelasan konsep, contoh soal,
        serta langkah-langkah metode eliminasi dan substitusi pada SPLTV.
        Gunakan sebagai referensi pendukung kegiatan Discovery Learning!
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">Video 1 — Pengenalan & Pemodelan SPLTV</div>
        <div class="fase-text">Memahami konsep dasar SPLTV dan cara membuat model matematika dari masalah nyata.</div>
    </div>
    """, unsafe_allow_html=True)
    st.video("https://youtu.be/e_6G6lbEPBE?si=t_mQjKaDkmDdjhLG")

    st.markdown("")

    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">Video 2 — Metode Eliminasi & Substitusi SPLTV</div>
        <div class="fase-text">Langkah demi langkah penyelesaian SPLTV menggunakan metode eliminasi dan substitusi.</div>
    </div>
    """, unsafe_allow_html=True)
    st.video("https://youtu.be/0ad_iTcUAFU?si=Y_B1SvVVnMDs4pHL")

    st.markdown("---")
    st.markdown("""
    <div class="warning-card">
    <b>📝 Tugas Setelah Menonton</b><br><br>
    Setelah menonton video, jawablah pertanyaan berikut di LKS-mu:<br><br>
    1. Apa perbedaan cara menyelesaikan SPLDV dan SPLTV? Jelaskan!<br>
    2. Mengapa dalam SPLTV dibutuhkan minimal 3 persamaan untuk mendapatkan solusi tunggal?<br>
    3. Tuliskan 1 contoh masalah nyata yang bisa dimodelkan dengan SPLTV dari kehidupanmu!
    </div>
    """, unsafe_allow_html=True)
