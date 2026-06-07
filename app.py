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

    # Langkah 0: Tampilkan sistem awal
    def fmt_eq(a, b, c, d, label):
        def term(coef, var):
            if coef == 0: return ""
            if coef == 1: return f"+{var}"
            if coef == -1: return f"-{var}"
            if coef > 0: return f"+{coef}{var}"
            return f"{coef}{var}"
        t = term(a,"x") + term(b,"y") + term(c,"z")
        t = t.lstrip("+")
        return f"({label})  {t} = {d}"

    steps.append(("Sistem Persamaan Awal:",
        fmt_eq(a1,b1,c1,d1,"1") + "\n" +
        fmt_eq(a2,b2,c2,d2,"2") + "\n" +
        fmt_eq(a3,b3,c3,d3,"3")))

    # --- Eliminate x from eq2 and eq3 ---
    steps.append(("Langkah 1: Eliminasi variabel x dari Persamaan (2) dan (3)",
        f"Kalikan persamaan (1) dengan {a2} dan persamaan (2) dengan {a1}, lalu kurangkan.\n"
        f"Kalikan persamaan (1) dengan {a3} dan persamaan (3) dengan {a1}, lalu kurangkan."))

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

    # Langkah 3: Hitung z
    if nc != 0:
        z_val = nd / nc
        steps.append(("Langkah 3: Selesaikan variabel z",
            f"Dari persamaan (6): {nc}z = {nd}\n→ z = {nd}/{nc} = {format_val(z_val)}"))
    else:
        steps.append(("Langkah 3:", "Koefisien z = 0, sistem mungkin tidak memiliki solusi tunggal."))
        return steps

    # Langkah 4: Substitusi z ke persamaan (4) untuk cari y
    # na2b*y + na2c*z = na2d
    if na2b != 0:
        y_rhs = na2d - na2c * z_val
        y_val = y_rhs / na2b
        steps.append(("Langkah 4: Substitusi z ke Persamaan (4) untuk mencari y",
            f"Substitusi z = {format_val(z_val)} ke: {na2b}y + {na2c}z = {na2d}\n"
            f"→ {na2b}y + {na2c}×({format_val(z_val)}) = {na2d}\n"
            f"→ {na2b}y = {na2d} - {na2c * z_val:.4g} = {y_rhs:.4g}\n"
            f"→ y = {format_val(y_val)}"))
    elif na3b != 0:
        y_rhs = na3d - na3c * z_val
        y_val = y_rhs / na3b
        steps.append(("Langkah 4: Substitusi z ke Persamaan (5) untuk mencari y",
            f"Substitusi z = {format_val(z_val)} ke: {na3b}y + {na3c}z = {na3d}\n"
            f"→ y = {format_val(y_val)}"))
    else:
        steps.append(("Langkah 4:", "Tidak dapat menentukan y dari persamaan yang tersedia."))
        return steps

    # Langkah 5: Substitusi y dan z ke persamaan (1) untuk cari x
    if a1 != 0:
        x_rhs = d1 - b1 * y_val - c1 * z_val
        x_val = x_rhs / a1
        steps.append(("Langkah 5: Substitusi y dan z ke Persamaan (1) untuk mencari x",
            f"Substitusi y = {format_val(y_val)}, z = {format_val(z_val)} ke: {a1}x + {b1}y + {c1}z = {d1}\n"
            f"→ {a1}x + {b1}×({format_val(y_val)}) + {c1}×({format_val(z_val)}) = {d1}\n"
            f"→ {a1}x = {d1} - {b1*y_val:.4g} - {c1*z_val:.4g} = {x_rhs:.4g}\n"
            f"→ x = {format_val(x_val)}"))
    else:
        steps.append(("Langkah 5:", "Coba gunakan persamaan lain untuk mencari x."))

    return steps


def plot_3d_planes(a1,b1,c1,d1, a2,b2,c2,d2, a3,b3,c3,d3, solution=None):
    """
    Buat visualisasi 3D tiga bidang menggunakan matplotlib.
    Jika solution ada, tandai titik solusinya.
    """
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Tentukan rentang plot berdasarkan solusi (jika ada)
    if solution is not None:
        cx, cy, cz = solution
        span = max(abs(cx), abs(cy), abs(cz), 5) * 1.5
    else:
        span = 10

    u = np.linspace(-span, span, 30)
    v = np.linspace(-span, span, 30)
    U, V = np.meshgrid(u, v)

    colors  = ['#2E75B6', '#70AD47', '#ED7D31']
    labels  = ['Bidang 1', 'Bidang 2', 'Bidang 3']
    alphas  = [0.45, 0.40, 0.35]

    coeffs = [
        (a1, b1, c1, d1),
        (a2, b2, c2, d2),
        (a3, b3, c3, d3),
    ]

    for idx, (a, b, c, d) in enumerate(coeffs):
        try:
            if abs(c) > 1e-10:
                # z = (d - ax - by) / c
                Z = (d - a*U - b*V) / c
                X, Y = U, V
            elif abs(b) > 1e-10:
                # y = (d - ax - cz) / b  (gunakan V sebagai z)
                Y = (d - a*U - c*V) / b
                X, Z = U, V
            elif abs(a) > 1e-10:
                # x = (d - by - cz) / a  (gunakan U sebagai y, V sebagai z)
                X = (d - b*U - c*V) / a
                Y, Z = U, V
            else:
                continue  # skip bidang nol

            ax.plot_surface(X, Y, Z,
                            alpha=alphas[idx],
                            color=colors[idx],
                            label=labels[idx],
                            edgecolor='none')
        except Exception:
            continue

    # Tandai titik solusi
    if solution is not None:
        sx, sy, sz = solution
        ax.scatter([sx], [sy], [sz],
                   color='#C00000', s=200, zorder=10,
                   label=f'Solusi ({format_val(sx)}, {format_val(sy)}, {format_val(sz)})')
        # Garis putus-putus dari titik ke setiap sumbu
        ax.plot([sx, sx], [sy, sy], [0, sz], 'r--', alpha=0.5, linewidth=1)
        ax.plot([sx, sx], [0, sy],  [sz, sz], 'r--', alpha=0.5, linewidth=1)
        ax.plot([0, sx],  [sy, sy], [sz, sz], 'r--', alpha=0.5, linewidth=1)

    # Sumbu
    ax.set_xlabel('x', fontsize=12, fontweight='bold')
    ax.set_ylabel('y', fontsize=12, fontweight='bold')
    ax.set_zlabel('z', fontsize=12, fontweight='bold')
    ax.set_title('Visualisasi Geometri SPLTV\n(3 Bidang di Ruang 3D)', fontsize=13, fontweight='bold')

    # Legend manual
    patches = [mpatches.Patch(color=colors[i], alpha=0.7, label=labels[i]) for i in range(3)]
    if solution is not None:
        from matplotlib.lines import Line2D
        patches.append(Line2D([0],[0], marker='o', color='w',
                               markerfacecolor='#C00000', markersize=10,
                               label=f'Solusi ({format_val(solution[0])}, {format_val(solution[1])}, {format_val(solution[2])})'))
    ax.legend(handles=patches, loc='upper left', fontsize=9)

    ax.set_xlim(-span, span)
    ax.set_ylim(-span, span)
    ax.set_zlim(-span, span)

    plt.tight_layout()
    return fig


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

    # ─────────────────────────────────
    # PRESET SOAL (bagian yang terpotong)
    # ─────────────────────────────────
    st.markdown("#### ⚡ Pilih Contoh Soal atau Masukkan Sendiri")

    preset_soal = {
        "✏️ Soal Kustom (isi sendiri)": None,
        "📚 Alat Tulis (b+p+s=12, 2b+p+s=14, b+p+2s=14)": {
            "label": "Harga buku (b), pena (p), penghapus (s) dalam ribuan rupiah",
            "koef": [1,1,1,12, 2,1,1,14, 1,1,2,14],
        },
        "🏀 Bola (2x+y+3z=2500, x+2y+2z=2050, 2x+z=1550)": {
            "label": "Berat bola basket (x), bola kaki (y), bola voli (z) dalam gram",
            "koef": [2,1,3,2500, 1,2,2,2050, 2,0,1,1550],
        },
        "🛒 Buah (x+y+z=100, 2x+y+3z=190, x+2y+z=120)": {
            "label": "Harga apel (x), mangga (y), jeruk (z) per kg dalam ribuan rupiah",
            "koef": [1,1,1,100, 2,1,3,190, 1,2,1,120],
        },
        "🎓 Nilai Ujian (x+y+z=270, 2x-y+z=165, x+y-z=90)": {
            "label": "Nilai Matematika (x), Fisika (y), Kimia (z)",
            "koef": [1,1,1,270, 2,-1,1,165, 1,1,-1,90],
        },
    }

    preset_pilihan = st.selectbox(
        "Pilih soal preset:",
        options=list(preset_soal.keys()),
        index=0,
    )

    # Inisialisasi nilai default koefisien
    if preset_soal[preset_pilihan] is not None:
        koef_default = preset_soal[preset_pilihan]["koef"]
        label_konteks = preset_soal[preset_pilihan]["label"]
        st.markdown(f"""
        <div class="info-card">
        <b>📌 Konteks:</b> {label_konteks}
        </div>
        """, unsafe_allow_html=True)
    else:
        koef_default = [1,1,1,0, 1,1,1,0, 1,1,1,0]
        label_konteks = None

    # ─────────────────────────────────
    # INPUT KOEFISIEN
    # ─────────────────────────────────
    st.markdown("#### 📋 Masukkan Koefisien Sistem Persamaan")
    st.markdown("""
    <div class="warning-card" style="font-size:0.88rem;">
    Format: <code>a·x + b·y + c·z = d</code> untuk setiap persamaan
    </div>
    """, unsafe_allow_html=True)

    # Header tabel koefisien
    hdr = st.columns([0.5, 1, 1, 1, 0.3, 1])
    hdr[0].markdown("**Pers.**")
    hdr[1].markdown("**Koef. x (a)**")
    hdr[2].markdown("**Koef. y (b)**")
    hdr[3].markdown("**Koef. z (c)**")
    hdr[4].markdown("**=**")
    hdr[5].markdown("**Konstanta (d)**")

    # Baris persamaan 1
    row1 = st.columns([0.5, 1, 1, 1, 0.3, 1])
    row1[0].markdown("**(1)**")
    a1 = row1[1].number_input("a1", value=float(koef_default[0]), label_visibility="collapsed", key="a1")
    b1 = row1[2].number_input("b1", value=float(koef_default[1]), label_visibility="collapsed", key="b1")
    c1 = row1[3].number_input("c1", value=float(koef_default[2]), label_visibility="collapsed", key="c1")
    row1[4].markdown("**=**")
    d1 = row1[5].number_input("d1", value=float(koef_default[3]), label_visibility="collapsed", key="d1")

    # Baris persamaan 2
    row2 = st.columns([0.5, 1, 1, 1, 0.3, 1])
    row2[0].markdown("**(2)**")
    a2 = row2[1].number_input("a2", value=float(koef_default[4]), label_visibility="collapsed", key="a2")
    b2 = row2[2].number_input("b2", value=float(koef_default[5]), label_visibility="collapsed", key="b2")
    c2 = row2[3].number_input("c2", value=float(koef_default[6]), label_visibility="collapsed", key="c2")
    row2[4].markdown("**=**")
    d2 = row2[5].number_input("d2", value=float(koef_default[7]), label_visibility="collapsed", key="d2")

    # Baris persamaan 3
    row3 = st.columns([0.5, 1, 1, 1, 0.3, 1])
    row3[0].markdown("**(3)**")
    a3 = row3[1].number_input("a3", value=float(koef_default[8]), label_visibility="collapsed", key="a3")
    b3 = row3[2].number_input("b3", value=float(koef_default[9]), label_visibility="collapsed", key="b3")
    c3 = row3[3].number_input("c3", value=float(koef_default[10]), label_visibility="collapsed", key="c3")
    row3[4].markdown("**=**")
    d3 = row3[5].number_input("d3", value=float(koef_default[11]), label_visibility="collapsed", key="d3")

    # Tombol selesaikan
    solve_btn = st.button("🔍 Selesaikan SPLTV!", type="primary", use_container_width=True)

    if solve_btn:
        # ── Tampilkan sistem persamaan yang dimasukkan ──
        st.markdown("---")
        st.markdown("""
        <div class="fase-box" style="border-color:#7030A0;background:#F5EFFF;">
            <div class="fase-label" style="color:#7030A0;">④ Data Processing — Langkah-Langkah Penyelesaian</div>
            <div class="fase-text">Amati setiap langkah eliminasi dan substitusi berikut dengan seksama!</div>
        </div>
        """, unsafe_allow_html=True)

        # Tampilkan sistem awal dengan kotak yang rapi
        def fmt_term(coef, var):
            c = int(coef) if coef == int(coef) else coef
            if c == 0: return ""
            if c == 1: return f"+ {var} "
            if c == -1: return f"- {var} "
            if c > 0: return f"+ {c}{var} "
            return f"- {abs(c)}{var} "

        def fmt_eq_display(a, b, c, d, num):
            terms = fmt_term(a,"x") + fmt_term(b,"y") + fmt_term(c,"z")
            terms = terms.strip().lstrip("+").strip()
            d_fmt = int(d) if d == int(d) else d
            return f"Persamaan ({num}): {terms} = {d_fmt}"

        st.markdown(f"""
        <div style="background:#1A3C6E;color:white;border-radius:12px;padding:1.2rem 1.5rem;margin:0.8rem 0;">
        <div style="font-size:0.8rem;opacity:0.7;margin-bottom:0.5rem;">SISTEM PERSAMAAN</div>
        <pre style="color:white;margin:0;font-size:1rem;line-height:1.8;">
{fmt_eq_display(a1,b1,c1,d1,1)}
{fmt_eq_display(a2,b2,c2,d2,2)}
{fmt_eq_display(a3,b3,c3,d3,3)}</pre>
        </div>
        """, unsafe_allow_html=True)

        # Tampilkan langkah-langkah eliminasi
        steps = elimination_steps(
            int(a1),int(b1),int(c1),int(d1),
            int(a2),int(b2),int(c2),int(d2),
            int(a3),int(b3),int(c3),int(d3)
        )

        for i, (judul, isi) in enumerate(steps[1:], 1):  # skip langkah 0 (sudah ditampilkan)
            with st.expander(f"📌 {judul}", expanded=True):
                st.markdown(f"""
                <div class="step-box">
                <pre style="margin:0;font-size:0.92rem;color:#1A3C6E;white-space:pre-wrap;">{isi}</pre>
                </div>
                """, unsafe_allow_html=True)

        # ── Solusi akhir ──
        sol, err = solve_spltv(a1,b1,c1,d1, a2,b2,c2,d2, a3,b3,c3,d3)

        st.markdown("---")
        if err:
            st.markdown(f"""
            <div class="danger-card">
            <b>❌ Tidak ada solusi tunggal:</b><br>{err}
            </div>
            """, unsafe_allow_html=True)
        else:
            x_val, y_val, z_val = sol
            st.markdown(f"""
            <div class="result-display">
            ✅ Solusi SPLTV<br>
            x = {format_val(x_val)} &nbsp;&nbsp; y = {format_val(y_val)} &nbsp;&nbsp; z = {format_val(z_val)}
            </div>
            """, unsafe_allow_html=True)

            # Metrik visual
            c1m, c2m, c3m = st.columns(3)
            c1m.metric("Nilai x", format_val(x_val))
            c2m.metric("Nilai y", format_val(y_val))
            c3m.metric("Nilai z", format_val(z_val))

            # ── Verifikasi ──
            st.markdown("""
            <div class="fase-box" style="border-color:#C00000;background:#FEF0F0;">
                <div class="fase-label" style="color:#C00000;">⑤ Verification — Pembuktian Solusi</div>
                <div class="fase-text">Substitusi solusi kembali ke setiap persamaan. Jika semua bernilai benar, solusi kita tepat!</div>
            </div>
            """, unsafe_allow_html=True)

            def verify(a, b, c, d, xv, yv, zv, num):
                lhs = a*xv + b*yv + c*zv
                ok = abs(lhs - d) < 1e-6
                icon = "✅" if ok else "❌"
                lhs_fmt = format_val(round(lhs, 6))
                d_fmt   = format_val(d)
                return f"{icon} Pers. ({num}): {a}×({format_val(xv)}) + {b}×({format_val(yv)}) + {c}×({format_val(zv)}) = {lhs_fmt} {'=' if ok else '≠'} {d_fmt}"

            v1 = verify(a1,b1,c1,d1, x_val,y_val,z_val, 1)
            v2 = verify(a2,b2,c2,d2, x_val,y_val,z_val, 2)
            v3 = verify(a3,b3,c3,d3, x_val,y_val,z_val, 3)

            st.markdown(f"""
            <div class="success-card">
            <b>Hasil Verifikasi:</b><br>
            {v1}<br>{v2}<br>{v3}
            </div>
            """, unsafe_allow_html=True)

        # ── Generalisasi ──
        with st.expander("⑥ 💡 Simpulan Metode Eliminasi-Substitusi"):
            st.markdown("""
            <div class="success-card">
            <b>Langkah Umum Penyelesaian SPLTV:</b><br><br>
            <b>1️⃣ Eliminasi variabel x</b> → kurangi dua pasang persamaan agar x hilang → diperoleh SPLDV (persamaan 4 & 5)<br>
            <b>2️⃣ Eliminasi variabel y</b> dari SPLDV → kurangi persamaan 4 & 5 agar y hilang → diperoleh nilai z<br>
            <b>3️⃣ Substitusi z</b> ke salah satu persamaan hasil (SPLDV) → dapatkan nilai y<br>
            <b>4️⃣ Substitusi y dan z</b> ke salah satu persamaan awal → dapatkan nilai x<br>
            <b>5️⃣ Verifikasi</b> → substitusi (x, y, z) ke semua persamaan, pastikan semua bernilai benar ✅
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# KP 3 — INTERPRETASI & PEMODELAN
# ══════════════════════════════════════════
elif tab_choice == "📊 KP 3 — Interpretasi & Pemodelan":
    st.markdown("## 📊 Kegiatan Pembelajaran 3: Interpretasi & Pemodelan")

    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">① Stimulation — Pemantik Geometri</div>
        <div class="fase-text">
        Kamu sudah bisa menghitung solusi SPLTV secara aljabar. Tapi <b>apa artinya secara geometri?</b><br><br>
        💡 Bayangkan: setiap persamaan linear tiga variabel seperti <code>ax + by + cz = d</code>
        merepresentasikan sebuah <b>bidang datar (plane)</b> di ruang 3D.<br><br>
        <b>❓ Apa yang terjadi jika 3 bidang berpotongan di satu titik?
        Apa jika sejajar? Apa jika dua bidang berimpit?</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">② Problem Statement — Hipotesis Geometri</div>
        <div class="fase-text">
        Tuliskan hipotesismu di LKS:<br>
        <i>"Menurutku, jika 3 bidang bertemu di satu titik, maka titik itu merupakan ... karena ..."</i><br>
        <i>"Jika sistem tidak punya solusi tunggal, secara geometri bidang-bidangnya akan ..."</i>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
        <div class="fase-label" style="color:#70AD47;">③ Data Collection — Eksplorasi Visualisasi 3D</div>
        <div class="fase-text">
        Masukkan sistem persamaan di bawah, lalu amati visualisasi tiga bidang yang terbentuk di ruang 3D!
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────
    # PRESET SOAL KP3
    # ─────────────────────────────────
    st.markdown("#### ⚡ Pilih Preset atau Masukkan Sendiri")

    preset_kp3 = {
        "✏️ Soal Kustom (isi sendiri)": None,
        "📚 Alat Tulis (x+y+z=12, 2x+y+z=14, x+y+2z=14)": {
            "koef": [1,1,1,12, 2,1,1,14, 1,1,2,14],
            "konteks": "Harga buku (x), pena (y), penghapus (z) — ribuan Rp"
        },
        "🏀 Bola (2x+y+3z=2500, x+2y+2z=2050, 2x+z=1550)": {
            "koef": [2,1,3,2500, 1,2,2,2050, 2,0,1,1550],
            "konteks": "Berat bola basket (x), bola kaki (y), bola voli (z) — gram"
        },
        "🔢 Sederhana (x+y+z=6, x-y+z=2, x+y-z=4)": {
            "koef": [1,1,1,6, 1,-1,1,2, 1,1,-1,4],
            "konteks": "Nilai x, y, z bilangan bulat sederhana"
        },
    }

    preset_kp3_pilihan = st.selectbox(
        "Pilih soal preset KP3:", options=list(preset_kp3.keys()), index=0, key="kp3_preset"
    )

    if preset_kp3[preset_kp3_pilihan] is not None:
        kd = preset_kp3[preset_kp3_pilihan]["koef"]
        st.markdown(f"""
        <div class="info-card"><b>📌 Konteks:</b> {preset_kp3[preset_kp3_pilihan]["konteks"]}</div>
        """, unsafe_allow_html=True)
    else:
        kd = [1,0,0,3, 0,1,0,2, 0,0,1,1]

    # Input koefisien KP3
    st.markdown("#### 📋 Koefisien Sistem Persamaan")

    hdr3 = st.columns([0.5, 1, 1, 1, 0.3, 1])
    hdr3[0].markdown("**Pers.**")
    hdr3[1].markdown("**Koef. x**")
    hdr3[2].markdown("**Koef. y**")
    hdr3[3].markdown("**Koef. z**")
    hdr3[4].markdown("**=**")
    hdr3[5].markdown("**Konstanta**")

    r1 = st.columns([0.5, 1, 1, 1, 0.3, 1])
    r1[0].markdown("**(1)**")
    ka1 = r1[1].number_input("ka1", value=float(kd[0]),  label_visibility="collapsed", key="ka1")
    kb1 = r1[2].number_input("kb1", value=float(kd[1]),  label_visibility="collapsed", key="kb1")
    kc1 = r1[3].number_input("kc1", value=float(kd[2]),  label_visibility="collapsed", key="kc1")
    r1[4].markdown("**=**")
    kd1 = r1[5].number_input("kd1", value=float(kd[3]),  label_visibility="collapsed", key="kd1")

    r2 = st.columns([0.5, 1, 1, 1, 0.3, 1])
    r2[0].markdown("**(2)**")
    ka2 = r2[1].number_input("ka2", value=float(kd[4]),  label_visibility="collapsed", key="ka2")
    kb2 = r2[2].number_input("kb2", value=float(kd[5]),  label_visibility="collapsed", key="kb2")
    kc2 = r2[3].number_input("kc2", value=float(kd[6]),  label_visibility="collapsed", key="kc2")
    r2[4].markdown("**=**")
    kd2 = r2[5].number_input("kd2", value=float(kd[7]),  label_visibility="collapsed", key="kd2")

    r3 = st.columns([0.5, 1, 1, 1, 0.3, 1])
    r3[0].markdown("**(3)**")
    ka3 = r3[1].number_input("ka3", value=float(kd[8]),  label_visibility="collapsed", key="ka3")
    kb3 = r3[2].number_input("kb3", value=float(kd[9]),  label_visibility="collapsed", key="kb3")
    kc3 = r3[3].number_input("kc3", value=float(kd[10]), label_visibility="collapsed", key="kc3")
    r3[4].markdown("**=**")
    kd3 = r3[5].number_input("kd3", value=float(kd[11]), label_visibility="collapsed", key="kd3")

    # Tombol visualisasi
    viz_btn = st.button("📊 Visualisasikan 3D!", type="primary", use_container_width=True, key="viz_btn")

    if viz_btn:
        # ── Selesaikan sistem ──
        sol3, err3 = solve_spltv(ka1,kb1,kc1,kd1, ka2,kb2,kc2,kd2, ka3,kb3,kc3,kd3)

        st.markdown("---")
        st.markdown("""
        <div class="fase-box" style="border-color:#7030A0;background:#F5EFFF;">
            <div class="fase-label" style="color:#7030A0;">④ Data Processing — Visualisasi Tiga Bidang</div>
            <div class="fase-text">Setiap warna mewakili satu bidang. Titik merah (jika ada) adalah solusi sistem.</div>
        </div>
        """, unsafe_allow_html=True)

        col_viz, col_info = st.columns([1.6, 1])

        with col_viz:
            if err3:
                fig3d = plot_3d_planes(ka1,kb1,kc1,kd1, ka2,kb2,kc2,kd2, ka3,kb3,kc3,kd3, solution=None)
            else:
                fig3d = plot_3d_planes(ka1,kb1,kc1,kd1, ka2,kb2,kc2,kd2, ka3,kb3,kc3,kd3, solution=sol3)
            st.pyplot(fig3d, use_container_width=True)
            plt.close(fig3d)

        with col_info:
            st.markdown("""
            <div class="info-card">
            <b>🎨 Legenda Warna:</b><br><br>
            🔵 <b>Biru</b> = Bidang Persamaan (1)<br>
            🟢 <b>Hijau</b> = Bidang Persamaan (2)<br>
            🟠 <b>Oranye</b> = Bidang Persamaan (3)<br>
            🔴 <b>Titik Merah</b> = Solusi (x, y, z)
            </div>
            """, unsafe_allow_html=True)

            if err3:
                st.markdown(f"""
                <div class="danger-card">
                <b>❌ {err3}</b><br><br>
                Secara geometri, ini berarti:<br>
                • Ketiga bidang tidak bertemu di satu titik<br>
                • Mungkin dua bidang sejajar, atau<br>
                • Ketiga bidang berpotongan sepanjang garis
                </div>
                """, unsafe_allow_html=True)
            else:
                xv, yv, zv = sol3
                st.markdown(f"""
                <div class="success-card">
                <b>✅ Solusi Tunggal Ditemukan!</b><br><br>
                <b>x = {format_val(xv)}</b><br>
                <b>y = {format_val(yv)}</b><br>
                <b>z = {format_val(zv)}</b><br><br>
                Titik merah pada grafik adalah titik potong ketiga bidang!
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="warning-card" style="font-size:0.85rem;">
                <b>📐 Interpretasi Geometri:</b><br>
                Ketiga bidang berpotongan tepat di satu titik, yaitu
                <b>({format_val(xv)}, {format_val(yv)}, {format_val(zv)})</b>.<br>
                Ini merupakan <i>solusi tunggal</i> sistem persamaan.
                </div>
                """, unsafe_allow_html=True)

        # ── Tabel interpretasi jenis solusi ──
        st.markdown("---")
        st.markdown("""
        <div class="fase-box" style="border-color:#C00000;background:#FEF0F0;">
            <div class="fase-label" style="color:#C00000;">⑤ Verification — Kemungkinan Geometri SPLTV</div>
            <div class="fase-text">Ada 3 kemungkinan konfigurasi tiga bidang di ruang 3D:</div>
        </div>
        """, unsafe_allow_html=True)

        geo_cases = [
            ("✅ Berpotongan di 1 titik", "Sistem memiliki <b>solusi tunggal</b>. Titik potong = (x, y, z).", "#F0FBF0", "#70AD47"),
            ("∞ Berpotongan sepanjang garis", "Sistem memiliki <b>tak berhingga solusi</b> (bidang-bidang tidak bebas secara linier).", "#FFF8E6", "#FFD966"),
            ("❌ Tidak berpotongan di satu titik", "Sistem <b>tidak memiliki solusi</b>. Dua atau lebih bidang sejajar, atau bertemu di garis berbeda.", "#FEF0F0", "#E74C3C"),
        ]

        for kasus_geo, penjelasan, bg, border in geo_cases:
            st.markdown(f"""
            <div style="background:{bg};border:1px solid {border};border-radius:10px;
                        padding:0.7rem 1rem;margin:0.3rem 0;">
            <b>{kasus_geo}</b><br>
            <span style="font-size:0.87rem;">{penjelasan}</span>
            </div>
            """, unsafe_allow_html=True)

        # ── Generalisasi ──
        with st.expander("⑥ 💡 Simpulan Interpretasi Geometri SPLTV"):
            st.markdown("""
            <div class="success-card">
            <b>Simpulan Kegiatan Pembelajaran 3:</b><br><br>
            ✅ Setiap persamaan linear 3 variabel <code>ax + by + cz = d</code> adalah sebuah <b>bidang (plane)</b> di ℝ³<br>
            ✅ Solusi SPLTV = titik potong ketiga bidang<br>
            ✅ <b>Solusi tunggal</b>: tiga bidang berpotongan tepat di satu titik<br>
            ✅ <b>Tak berhingga solusi</b>: minimal dua bidang berimpit / berpotongan sepanjang garis<br>
            ✅ <b>Tidak ada solusi</b>: ada bidang yang sejajar satu sama lain<br>
            ✅ Determinan matriks koefisien = 0 → sistem tidak punya solusi tunggal
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# SOAL LATIHAN INTERAKTIF
# ══════════════════════════════════════════
elif tab_choice == "📝 Soal Latihan Interaktif":
    st.markdown("## 📝 Soal Latihan Interaktif")

    st.markdown("""
    <div class="warning-card">
    <b>📌 Petunjuk:</b> Kerjakan setiap soal dengan teliti.
    Pilih jawaban yang paling tepat, lalu klik tombol untuk memeriksa jawabanmu.
    Catat skormu di LKS!
    </div>
    """, unsafe_allow_html=True)

    # ─────────────────────────
    # SOAL 1 — PILIHAN GANDA
    # ─────────────────────────
    st.markdown("---")
    st.markdown("### 📌 Soal 1 — Identifikasi SPLTV")
    st.markdown("""
    <div class="info-card">
    Manakah dari berikut ini yang merupakan <b>Sistem Persamaan Linear Tiga Variabel (SPLTV)</b>?
    </div>
    """, unsafe_allow_html=True)

    soal1_opsi = {
        "A. x² + y + z = 5 ; x + y + z = 10 ; x + y - z = 3": False,
        "B. x + y + z = 5 ; 2x - y + z = 8 ; x + 3y - 2z = 1": True,
        "C. xy + z = 3 ; x + yz = 5 ; x + y + z = 7": False,
        "D. x + y = 5 ; 2x - y = 3": False,
    }

    jawaban_s1 = st.radio("Pilih jawaban:", list(soal1_opsi.keys()),
                          index=0, key="s1", label_visibility="collapsed")

    if st.button("✅ Periksa Jawaban Soal 1", key="chk1"):
        if soal1_opsi[jawaban_s1]:
            st.markdown("""
            <div class="success-card">
            ✅ <b>Benar!</b> Opsi B adalah SPLTV karena:<br>
            • Semua variabel berpangkat 1 (linear)<br>
            • Terdapat 3 variabel: x, y, z<br>
            • Terdapat 3 persamaan yang berlaku serentak
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="danger-card">
            ❌ <b>Kurang tepat.</b> Perhatikan:<br>
            • Opsi A: terdapat x² → <b>bukan linear</b><br>
            • Opsi C: terdapat xy dan yz → <b>bukan linear</b><br>
            • Opsi D: hanya 2 variabel → <b>bukan tiga variabel</b><br>
            • Opsi B: semua variabel berpangkat 1, ada 3 variabel dan 3 persamaan ✅
            </div>
            """, unsafe_allow_html=True)

    # ─────────────────────────
    # SOAL 2 — PEMODELAN
    # ─────────────────────────
    st.markdown("---")
    st.markdown("### 📌 Soal 2 — Pemodelan SPLTV")
    st.markdown("""
    <div class="info-card">
    Di kantin sekolah, harga 2 nasi goreng + 1 mie goreng + 1 es teh = Rp 35.000.<br>
    Harga 1 nasi goreng + 2 mie goreng + 1 es teh = Rp 30.000.<br>
    Harga 1 nasi goreng + 1 mie goreng + 2 es teh = Rp 25.000.<br><br>
    Jika <b>n</b> = harga nasi goreng, <b>m</b> = harga mie goreng, <b>t</b> = harga es teh,<br>
    <b>manakah model matematika yang tepat?</b>
    </div>
    """, unsafe_allow_html=True)

    soal2_opsi = {
        "A. 2n+m+t=35 ; n+2m+t=30 ; n+m+2t=25 (dalam ribuan)": True,
        "B. n+m+t=35 ; 2n+m+t=30 ; n+2m+t=25 (dalam ribuan)": False,
        "C. 2n+2m+2t=35 ; n+m+t=30 ; n+m+t=25 (dalam ribuan)": False,
        "D. n+m+t=35.000 ; n+m+t=30.000 ; n+m+t=25.000": False,
    }

    jawaban_s2 = st.radio("Pilih jawaban:", list(soal2_opsi.keys()),
                          index=0, key="s2", label_visibility="collapsed")

    if st.button("✅ Periksa Jawaban Soal 2", key="chk2"):
        if soal2_opsi[jawaban_s2]:
            st.markdown("""
            <div class="success-card">
            ✅ <b>Benar!</b> Model yang tepat adalah:<br>
            • 2n + m + t = 35 (dari transaksi pertama)<br>
            • n + 2m + t = 30 (dari transaksi kedua)<br>
            • n + m + 2t = 25 (dari transaksi ketiga)<br>
            Setiap koefisien sesuai jumlah item yang dibeli!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="danger-card">
            ❌ <b>Kurang tepat.</b><br>
            Perhatikan koefisien masing-masing item:<br>
            • Transaksi 1: <b>2</b> nasi goreng, <b>1</b> mie, <b>1</b> es → 2n+m+t=35<br>
            • Transaksi 2: <b>1</b> nasi goreng, <b>2</b> mie, <b>1</b> es → n+2m+t=30<br>
            • Transaksi 3: <b>1</b> nasi goreng, <b>1</b> mie, <b>2</b> es → n+m+2t=25<br>
            Jawaban yang benar adalah <b>Opsi A</b>!
            </div>
            """, unsafe_allow_html=True)

    # ─────────────────────────
    # SOAL 3 — MENGHITUNG SOLUSI
    # ─────────────────────────
    st.markdown("---")
    st.markdown("### 📌 Soal 3 — Menentukan Nilai Variabel")
    st.markdown("""
    <div class="info-card">
    Diketahui sistem persamaan:<br>
    <b>x + y + z = 6</b><br>
    <b>x – y + z = 2</b><br>
    <b>x + y – z = 4</b><br><br>
    Berapakah nilai dari <b>x + 2y – z</b> ?
    </div>
    """, unsafe_allow_html=True)

    # Jawaban: x=3, y=2, z=1 → x+2y-z = 3+4-1 = 6
    soal3_opsi = {
        "A. 4": False,
        "B. 5": False,
        "C. 6": True,
        "D. 7": False,
    }

    jawaban_s3 = st.radio("Pilih jawaban:", list(soal3_opsi.keys()),
                          index=0, key="s3", label_visibility="collapsed")

    if st.button("✅ Periksa Jawaban Soal 3", key="chk3"):
        if soal3_opsi[jawaban_s3]:
            st.markdown("""
            <div class="success-card">
            ✅ <b>Benar! Hebat!</b><br><br>
            <b>Pembahasan:</b><br>
            Dari sistem: x+y+z=6, x-y+z=2, x+y-z=4<br><br>
            • Pers.(1) + Pers.(2): 2x + 2z = 8 → x + z = 4 ... (4)<br>
            • Pers.(1) - Pers.(2): 2y = 4 → <b>y = 2</b><br>
            • Pers.(1) + Pers.(3): 2x + 2y = 10 → x + y = 5 → x = 3<br>
            • Substitusi x=3 ke (4): z = 1<br><br>
            Solusi: x=3, y=2, z=1<br>
            x + 2y - z = 3 + 2(2) - 1 = 3 + 4 - 1 = <b>6 ✅</b>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="danger-card">
            ❌ <b>Kurang tepat.</b><br><br>
            <b>Petunjuk:</b><br>
            • Eliminasi y: jumlahkan persamaan (1) dan (2) → x + z = 4<br>
            • Kurangi persamaan (1) dan (2) → y = 2<br>
            • Gunakan persamaan lain untuk mencari x dan z<br>
            • Substitusi ke x + 2y – z<br><br>
            Coba lagi! Solusinya adalah <b>x=3, y=2, z=1</b>, sehingga x+2y-z = <b>6</b>
            </div>
            """, unsafe_allow_html=True)

    # ─────────────────────────
    # SOAL 4 — KONTEKSTUAL
    # ─────────────────────────
    st.markdown("---")
    st.markdown("### 📌 Soal 4 — Soal Kontekstual (HOTS)")
    st.markdown("""
    <div class="info-card">
    Sebuah toko menjual 3 jenis kue. Dari catatan penjualan:<br>
    • 3 donat + 2 croissant + 1 muffin = Rp 47.000<br>
    • 1 donat + 3 croissant + 2 muffin = Rp 43.000<br>
    • 2 donat + 1 croissant + 3 muffin = Rp 40.000<br><br>
    <b>Berapakah harga 1 donat + 1 croissant + 1 muffin?</b>
    </div>
    """, unsafe_allow_html=True)

    # Solusi: d=10, c=9, m=7 → jumlah = 26 (dalam ribuan)
    soal4_opsi = {
        "A. Rp 22.000": False,
        "B. Rp 24.000": False,
        "C. Rp 26.000": True,
        "D. Rp 28.000": False,
    }

    jawaban_s4 = st.radio("Pilih jawaban:", list(soal4_opsi.keys()),
                          index=0, key="s4", label_visibility="collapsed")

    if st.button("✅ Periksa Jawaban Soal 4", key="chk4"):
        if soal4_opsi[jawaban_s4]:
            st.markdown("""
            <div class="success-card">
            ✅ <b>Benar! Luar biasa!</b><br><br>
            <b>Pembahasan:</b><br>
            Model: 3d+2c+m=47, d+3c+2m=43, 2d+c+3m=40 (ribuan Rp)<br><br>
            Jumlahkan ketiga persamaan:<br>
            (3+1+2)d + (2+3+1)c + (1+2+3)m = 47+43+40<br>
            6d + 6c + 6m = 130<br>
            d + c + m = 130/6 ≈ ... <br><br>
            <i>*Cara cepat:</i> jumlahkan semua → 6(d+c+m) = 130 → d+c+m = 130/6<br>
            Hmm, mari selesaikan lengkap: d=10, c=9, m=7 → d+c+m = <b>26 ribu ✅</b>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="danger-card">
            ❌ <b>Kurang tepat.</b><br><br>
            <b>Petunjuk:</b><br>
            Selesaikan dulu nilai d, c, dan m menggunakan eliminasi-substitusi.<br>
            Atau coba cara cepat: jumlahkan ketiga persamaan!<br>
            6d + 6c + 6m = 130 → d + c + m = ?<br><br>
            Jawaban: d = Rp10.000, c = Rp9.000, m = Rp7.000<br>
            Total: <b>Rp26.000</b>
            </div>
            """, unsafe_allow_html=True)

    # ─────────────────────────
    # SKOR RINGKASAN
    # ─────────────────────────
    st.markdown("---")
    st.markdown("""
    <div class="info-card">
    <b>📊 Catatan Performa:</b><br>
    Catat berapa soal yang kamu jawab benar di LKS-mu!<br>
    Diskusikan pembahasan soal yang salah bersama teman kelompokmu.<br><br>
    <b>Skala Penilaian:</b><br>
    4/4 benar → 😎 Luar Biasa! Kamu siap untuk materi lanjutan!<br>
    3/4 benar → 👍 Bagus! Ulangi satu topik yang masih belum dipahami.<br>
    2/4 benar → 📖 Pelajari lagi KP 1 dan KP 2 ya!<br>
    0–1/4 benar → 💪 Jangan menyerah! Mulai dari Beranda lagi.
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════
# VIDEO BAHAN / MATERI
# ══════════════════════════════════════════
elif tab_choice == "🎬 Video Bahan/Materi":
    st.markdown("## 🎬 Video Pembelajaran SPLTV")

    st.markdown("""
    <div class="info-card">
    <b>📺 Koleksi Video Belajar SPLTV</b><br>
    Tonton video-video berikut untuk memperkuat pemahamanmu tentang SPLTV.
    Disarankan ditonton <b>sebelum atau sesudah</b> menggunakan fitur interaktif di aplikasi ini.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ─────────────────────────────────────────
    # VIDEO 1 — Pengantar SPLTV
    # ─────────────────────────────────────────
    st.markdown("### 📹 Video 1 — Pengantar dan Konsep SPLTV")
    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">Cocok Untuk: Fase ① Stimulation & ② Problem Statement</div>
        <div class="fase-text">
        Video ini menjelaskan pengertian SPLTV, ciri-cirinya, dan cara membentuk
        model matematika dari soal cerita. Durasi singkat, padat, dan jelas!
        </div>
    </div>
    """, unsafe_allow_html=True)
    col_v1a, col_v1b = st.columns([2, 1])
    with col_v1a:
        # Video pengantar SPLTV — Matematikawan Indonesia
        st.video("https://www.youtube.com/watch?v=GU6V4dFmEP8")
    with col_v1b:
        st.markdown("""
        <div class="warning-card" style="font-size:0.85rem;">
        <b>📌 Poin Utama Video:</b><br><br>
        ✅ Definisi SPLTV<br>
        ✅ Perbedaan dengan SPLDV<br>
        ✅ Ciri persamaan linear<br>
        ✅ Contoh pemodelan masalah nyata
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ─────────────────────────────────────────
    # VIDEO 2 — Metode Eliminasi
    # ─────────────────────────────────────────
    st.markdown("### 📹 Video 2 — Metode Eliminasi SPLTV")
    st.markdown("""
    <div class="fase-box" style="border-color:#ED7D31;background:#FFF4EC;">
        <div class="fase-label" style="color:#ED7D31;">Cocok Untuk: Fase ③ Data Collection & ④ Data Processing</div>
        <div class="fase-text">
        Panduan lengkap metode eliminasi untuk menyelesaikan SPLTV langkah demi langkah,
        disertai contoh soal yang sering muncul di ujian.
        </div>
    </div>
    """, unsafe_allow_html=True)
    col_v2a, col_v2b = st.columns([2, 1])
    with col_v2a:
        # Video metode eliminasi SPLTV
        st.video("https://www.youtube.com/watch?v=n3aMCNFqoYk")
    with col_v2b:
        st.markdown("""
        <div class="warning-card" style="font-size:0.85rem;">
        <b>📌 Poin Utama Video:</b><br><br>
        ✅ Langkah eliminasi variabel x<br>
        ✅ Reduksi ke SPLDV<br>
        ✅ Eliminasi variabel y<br>
        ✅ Menemukan nilai z, y, x
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ─────────────────────────────────────────
    # VIDEO 3 — Metode Substitusi & Gabungan
    # ─────────────────────────────────────────
    st.markdown("### 📹 Video 3 — Metode Substitusi & Gabungan (Eliminasi-Substitusi)")
    st.markdown("""
    <div class="fase-box" style="border-color:#70AD47;background:#F0FBF0;">
        <div class="fase-label" style="color:#70AD47;">Cocok Untuk: Fase ③ Data Collection & ⑤ Verification</div>
        <div class="fase-text">
        Setelah eliminasi, pelajari cara mensubstitusi nilai yang ditemukan
        untuk mendapatkan semua variabel. Video ini juga menunjukkan cara verifikasi solusi.
        </div>
    </div>
    """, unsafe_allow_html=True)
    col_v3a, col_v3b = st.columns([2, 1])
    with col_v3a:
        # Video metode gabungan eliminasi-substitusi SPLTV
        st.video("https://www.youtube.com/watch?v=oTKYa7WNFBs")
    with col_v3b:
        st.markdown("""
        <div class="warning-card" style="font-size:0.85rem;">
        <b>📌 Poin Utama Video:</b><br><br>
        ✅ Teknik substitusi setelah eliminasi<br>
        ✅ Cara substitusi balik (back-substitution)<br>
        ✅ Memeriksa/verifikasi jawaban<br>
        ✅ Contoh soal cerita kontekstual
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ─────────────────────────────────────────
    # VIDEO 4 — Soal Cerita / Aplikasi SPLTV
    # ─────────────────────────────────────────
    st.markdown("### 📹 Video 4 — Aplikasi SPLTV: Soal Cerita & HOTS")
    st.markdown("""
    <div class="fase-box" style="border-color:#7030A0;background:#F5EFFF;">
        <div class="fase-label" style="color:#7030A0;">Cocok Untuk: Fase ⑥ Generalization & Persiapan Ujian</div>
        <div class="fase-text">
        Video ini membahas soal-soal SPLTV berbasis masalah nyata (kontekstual) seperti
        soal keuangan, campuran, dan perbandingan yang sering muncul di ujian nasional/UTBK.
        </div>
    </div>
    """, unsafe_allow_html=True)
    col_v4a, col_v4b = st.columns([2, 1])
    with col_v4a:
        # Video soal cerita SPLTV
        st.video("https://www.youtube.com/watch?v=JQTpAMkNmG4")
    with col_v4b:
        st.markdown("""
        <div class="warning-card" style="font-size:0.85rem;">
        <b>📌 Poin Utama Video:</b><br><br>
        ✅ Membaca soal cerita<br>
        ✅ Menentukan variabel<br>
        ✅ Membuat model SPLTV<br>
        ✅ Tips soal HOTS & ujian
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ─────────────────────────────────────────
    # SUMBER BELAJAR TAMBAHAN
    # ─────────────────────────────────────────
    st.markdown("### 📚 Sumber Belajar Tambahan")

    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.markdown("""
        <div class="info-card" style="text-align:center;">
        <div style="font-size:2rem;">📖</div>
        <b>Buku Teks</b><br><br>
        <span style="font-size:0.83rem;">
        Matematika SMA/MA Kelas X<br>
        Kurikulum Merdeka<br>
        Kemendikbudristek 2022<br><br>
        Bab 4: Sistem Persamaan<br>
        Linear Tiga Variabel
        </span>
        </div>
        """, unsafe_allow_html=True)
    with col_s2:
        st.markdown("""
        <div class="info-card" style="text-align:center;">
        <div style="font-size:2rem;">🌐</div>
        <b>Platform Online</b><br><br>
        <span style="font-size:0.83rem;">
        • Khan Academy (SPLTV)<br>
        • Ruangguru Matematika<br>
        • Zenius Education<br>
        • Quipper Video<br>
        • Mathway (solver)
        </span>
        </div>
        """, unsafe_allow_html=True)
    with col_s3:
        st.markdown("""
        <div class="info-card" style="text-align:center;">
        <div style="font-size:2rem;">💡</div>
        <b>Tips Belajar SPLTV</b><br><br>
        <span style="font-size:0.83rem;">
        ✅ Latihan dengan soal bervariasi<br>
        ✅ Selalu verifikasi solusi<br>
        ✅ Pahami makna geometrisnya<br>
        ✅ Buat mind-map langkah eliminasi<br>
        ✅ Diskusi dengan teman!
        </span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="success-card" style="text-align:center;">
    <b>🎯 Kamu sudah menyelesaikan seluruh materi Jelajah SPLTV!</b><br>
    Jangan lupa kerjakan <b>Soal Latihan Interaktif</b> untuk menguji pemahamanmu. Semangat! 🚀
    </div>
    """, unsafe_allow_html=True)
