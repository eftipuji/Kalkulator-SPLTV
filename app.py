
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        import numpy as np

        st.markdown("""
        <div class="fase-box" style="border-color:#C00000;background:#FEF5F5;">
            <div class="fase-label" style="color:#C00000;">🖊️ Studio Mandiri — Input Model & Visualisasi Langsung</div>
            <div class="fase-text">
            Masukkan sendiri model matematika SPLTV dari soal yang kamu kerjakan,
            lalu lihat <b>visualisasi solusi, verifikasi grafik, dan analisis sensitivitas</b> secara langsung!
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── STEP 1: Nama variabel ────────────────────────────────────────────
        st.markdown("### 📌 Langkah 1 — Beri Nama Variabelmu")
        st.markdown("""
        <div class="info-card" style="font-size:0.88rem;">
        💡 Penamaan variabel membantu kamu memahami <b>makna</b> dari nilai x, y, z
        dalam konteks soal. Contoh: x = harga buku, y = harga pena, z = harga penghapus.
        </div>
        """, unsafe_allow_html=True)

        col_v1, col_v2, col_v3 = st.columns(3)
        with col_v1:
            nama_x = st.text_input("Nama variabel x:", value="variabel x",
                                   placeholder="contoh: harga buku",
                                   key="studio_nama_x")
        with col_v2:
            nama_y = st.text_input("Nama variabel y:", value="variabel y",
                                   placeholder="contoh: harga pena",
                                   key="studio_nama_y")
        with col_v3:
            nama_z = st.text_input("Nama variabel z:", value="variabel z",
                                   placeholder="contoh: harga penghapus",
                                   key="studio_nama_z")

        satuan = st.text_input("Satuan nilai (opsional):",
                               value="",
                               placeholder="contoh: ribu Rp, gram, cm, ml ...",
                               key="studio_satuan")
        satuan_str = f" {satuan}" if satuan else ""

        st.markdown("---")

        # ── STEP 2: Input Konteks Soal ───────────────────────────────────────
        st.markdown("### 📖 Langkah 2 — Tuliskan Konteks Soal (Opsional)")
        konteks_soal = st.text_area(
            "Tulis narasi/kalimat soal di sini:",
            placeholder="Contoh: Di toko Bu Devi, terdapat 3 jenis roti. Diketahui bahwa...",
            height=80,
            key="studio_konteks"
        )

        if konteks_soal.strip():
            st.markdown(f"""
            <div class="warning-card" style="font-size:0.88rem;">
            <b>📖 Konteks Soal:</b><br>
            {konteks_soal}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # ── STEP 3: Input Koefisien ──────────────────────────────────────────
        st.markdown("### 🔢 Langkah 3 — Masukkan Model SPLTV-mu")
        st.markdown("""
        <div class="info-card" style="font-size:0.88rem;">
        Isi koefisien setiap persamaan. Bentuk: <code>a·x + b·y + c·z = d</code><br>
        Jika suatu variabel tidak ada dalam persamaan, isikan <b>0</b> pada kolomnya.
        </div>
        """, unsafe_allow_html=True)

        # Header tabel
        hcol0, hcol1, hcol2, hcol3, hcol4, hcol5 = st.columns([0.6, 1.4, 1.4, 1.4, 1.4, 0.6])
        hcol0.markdown("**Pers.**")
        hcol1.markdown(f"**a** (koef. x)")
        hcol2.markdown(f"**b** (koef. y)")
        hcol3.markdown(f"**c** (koef. z)")
        hcol4.markdown(f"**d** (konst.)")
        hcol5.markdown("**No.**")

        # Persamaan 1
        r1c0, r1c1, r1c2, r1c3, r1c4, r1c5 = st.columns([0.6,1.4,1.4,1.4,1.4,0.6])
        with r1c0:
            st.markdown("<div style='padding-top:0.55rem;font-weight:700;color:#1A3C6E;'>(1)</div>",
                        unsafe_allow_html=True)
        sa1 = r1c1.number_input("a1_s", value=1.0, step=1.0, label_visibility="collapsed", key="sa1")
        sb1 = r1c2.number_input("b1_s", value=1.0, step=1.0, label_visibility="collapsed", key="sb1")
        sc1 = r1c3.number_input("c1_s", value=1.0, step=1.0, label_visibility="collapsed", key="sc1")
        sd1 = r1c4.number_input("d1_s", value=0.0, step=1.0, label_visibility="collapsed", key="sd1")
        with r1c5:
            st.markdown("<div style='padding-top:0.55rem;text-align:center;'>①</div>",
                        unsafe_allow_html=True)

        # Persamaan 2
        r2c0, r2c1, r2c2, r2c3, r2c4, r2c5 = st.columns([0.6,1.4,1.4,1.4,1.4,0.6])
        with r2c0:
            st.markdown("<div style='padding-top:0.55rem;font-weight:700;color:#C00000;'>(2)</div>",
                        unsafe_allow_html=True)
        sa2 = r2c1.number_input("a2_s", value=1.0, step=1.0, label_visibility="collapsed", key="sa2")
        sb2 = r2c2.number_input("b2_s", value=1.0, step=1.0, label_visibility="collapsed", key="sb2")
        sc2 = r2c3.number_input("c2_s", value=1.0, step=1.0, label_visibility="collapsed", key="sc2")
        sd2 = r2c4.number_input("d2_s", value=0.0, step=1.0, label_visibility="collapsed", key="sd2")
        with r2c5:
            st.markdown("<div style='padding-top:0.55rem;text-align:center;'>②</div>",
                        unsafe_allow_html=True)

        # Persamaan 3
        r3c0, r3c1, r3c2, r3c3, r3c4, r3c5 = st.columns([0.6,1.4,1.4,1.4,1.4,0.6])
        with r3c0:
            st.markdown("<div style='padding-top:0.55rem;font-weight:700;color:#70AD47;'>(3)</div>",
                        unsafe_allow_html=True)
        sa3 = r3c1.number_input("a3_s", value=1.0, step=1.0, label_visibility="collapsed", key="sa3")
        sb3 = r3c2.number_input("b3_s", value=1.0, step=1.0, label_visibility="collapsed", key="sb3")
        sc3 = r3c3.number_input("c3_s", value=1.0, step=1.0, label_visibility="collapsed", key="sc3")
        sd3 = r3c4.number_input("d3_s", value=0.0, step=1.0, label_visibility="collapsed", key="sd3")
        with r3c5:
            st.markdown("<div style='padding-top:0.55rem;text-align:center;'>③</div>",
                        unsafe_allow_html=True)

        # ── Helper: format koefisien jadi string rapi ────────────────────────
        def _fmt_eq(a, b, c, d, nx, ny, nz):
            """Bentuk string persamaan dari koefisien dan nama variabel."""
            parts = []
            for coef, var in [(a, nx), (b, ny), (c, nz)]:
                coef_i = int(coef) if coef == int(coef) else coef
                if coef_i == 0:
                    continue
                if coef_i == 1:
                    parts.append(f"+ {var}")
                elif coef_i == -1:
                    parts.append(f"- {var}")
                elif coef_i > 0:
                    parts.append(f"+ {coef_i}{var}")
                else:
                    parts.append(f"- {abs(coef_i)}{var}")
            if not parts:
                expr = "0"
            else:
                expr = " ".join(parts).lstrip("+ ").replace("+ -", "- ")
            d_i = int(d) if d == int(d) else d
            return f"{expr} = {d_i}"

        # Preview model
        eq_strs = [
            _fmt_eq(sa1, sb1, sc1, sd1, nama_x, nama_y, nama_z),
            _fmt_eq(sa2, sb2, sc2, sd2, nama_x, nama_y, nama_z),
            _fmt_eq(sa3, sb3, sc3, sd3, nama_x, nama_y, nama_z),
        ]
        colors_eq = ["#1A3C6E", "#C00000", "#70AD47"]

        st.markdown(f"""
        <div style="background:#1A3C6E;color:white;border-radius:14px;
                    padding:1rem 1.5rem;margin:0.8rem 0;">
            <div style="font-size:0.78rem;opacity:0.75;margin-bottom:0.6rem;
                        letter-spacing:1px;text-transform:uppercase;">
                Preview Model SPLTV kamu:
            </div>
            <div style="font-family:monospace;font-size:1rem;line-height:2;">
                <span style="color:#BDD7EE;">(1)</span>&nbsp;&nbsp;{eq_strs[0]}<br>
                <span style="color:#FFACAC;">(2)</span>&nbsp;&nbsp;{eq_strs[1]}<br>
                <span style="color:#B7E1A1;">(3)</span>&nbsp;&nbsp;{eq_strs[2]}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── TOMBOL SELESAIKAN ────────────────────────────────────────────────
        col_btn_s, col_btn_r = st.columns([1, 3])
        with col_btn_s:
            tombol_hitung = st.button("🔍 Selesaikan & Visualisasikan",
                                      type="primary",
                                      use_container_width=True,
                                      key="studio_hitung")
        with col_btn_r:
            tombol_reset = st.button("🔄 Reset Input",
                                     use_container_width=True,
                                     key="studio_reset")

        if tombol_reset:
            for k in ["sa1","sb1","sc1","sd1","sa2","sb2","sc2","sd2",
                       "sa3","sb3","sc3","sd3","studio_nama_x","studio_nama_y",
                       "studio_nama_z","studio_satuan","studio_konteks"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()

        # ── HASIL & VISUALISASI ──────────────────────────────────────────────
        if tombol_hitung:
            st.markdown("---")

            # Selesaikan sistem
            sol_s, err_s = solve_spltv(
                sa1, sb1, sc1, sd1,
                sa2, sb2, sc2, sd2,
                sa3, sb3, sc3, sd3,
            )

            if err_s:
                st.markdown(f"""
                <div class="danger-card">
                ⚠️ <b>Sistem tidak dapat diselesaikan.</b><br>
                {err_s}<br><br>
                <b>Kemungkinan penyebab:</b><br>
                • Dua persamaan identik (duplikat)<br>
                • Persamaan-persamaan tidak konsisten (kontradiktif)<br>
                • Koefisien semua 0 pada satu baris<br><br>
                Coba periksa kembali koefisien yang kamu masukkan!
                </div>
                """, unsafe_allow_html=True)

            else:
                xs, ys, zs = sol_s
                xf, yf, zf = format_val(xs), format_val(ys), format_val(zs)

                # ── KARTU HASIL ──────────────────────────────────────────────
                st.markdown("### 🎯 Hasil Penyelesaian")
                r1, r2, r3 = st.columns(3)
                for col_r, var_name, val_str, raw_val, col_hex in zip(
                    [r1, r2, r3],
                    [nama_x, nama_y, nama_z],
                    [xf, yf, zf],
                    [xs, ys, zs],
                    ["#1A3C6E", "#C00000", "#70AD47"]
                ):
                    with col_r:
                        st.markdown(f"""
                        <div style="background:{col_hex};color:white;border-radius:14px;
                                    padding:1.2rem 0.8rem;text-align:center;
                                    box-shadow:0 4px 14px rgba(0,0,0,0.18);">
                            <div style="font-size:0.78rem;opacity:0.8;margin-bottom:0.2rem;">
                                {var_name}
                            </div>
                            <div style="font-size:2.4rem;font-weight:800;line-height:1.1;">
                                {val_str}{satuan_str}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                # ── VERIFIKASI SUBSTITUSI ────────────────────────────────────
                st.markdown("#### ✅ Verifikasi Substitusi Balik")
                pers_data = [
                    (sa1, sb1, sc1, sd1, 1),
                    (sa2, sb2, sc2, sd2, 2),
                    (sa3, sb3, sc3, sd3, 3),
                ]
                semua_ok = True
                for a_, b_, c_, d_, n_ in pers_data:
                    lhs_ = a_ * xs + b_ * ys + c_ * zs
                    ok_ = abs(lhs_ - d_) < 0.01
                    if not ok_:
                        semua_ok = False
                    bg_ = "#F0FBF0" if ok_ else "#FEF0F0"
                    bd_ = "#70AD47" if ok_ else "#E74C3C"
                    ic_ = "✅" if ok_ else "❌"
                    lhs_disp = f"{lhs_:.4g}"
                    d_disp = f"{int(d_) if d_==int(d_) else d_}"
                    st.markdown(f"""
                    <div style="background:{bg_};border:1px solid {bd_};border-radius:10px;
                                padding:0.55rem 1rem;margin:0.25rem 0;font-size:0.88rem;">
                    {ic_} <b>Persamaan ({n_}):</b>&nbsp;
                    Ruas kiri = <b>{lhs_disp}</b> &nbsp;|&nbsp; Konstanta = <b>{d_disp}</b>
                    &nbsp;→ {"<b style='color:#1D7A1D;'>Terpenuhi ✔</b>" if ok_
                           else "<b style='color:#C00000;'>Tidak terpenuhi ✖</b>"}
                    </div>
                    """, unsafe_allow_html=True)

                if semua_ok:
                    st.markdown("""
                    <div class="success-card">
                    🎉 <b>Verifikasi berhasil!</b>
                    Semua persamaan terpenuhi — model SPLTV-mu sudah benar!
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("---")

                # ══════════════════════════════════════════════════════════════
                #  VISUALISASI — 4 PANEL
                # ══════════════════════════════════════════════════════════════
                st.markdown("### 📊 Visualisasi Solusi")

                vis_tab1, vis_tab2, vis_tab3, vis_tab4 = st.tabs([
                    "📊 Nilai Solusi",
                    "✅ Verifikasi Grafik",
                    "🔥 Peta Panas Koefisien",
                    "📐 Analisis Sensitivitas",
                ])

                var_labels = [nama_x, nama_y, nama_z]
                val_nums   = [xs, ys, zs]
                COLORS_3   = ["#1A3C6E", "#C00000", "#70AD47"]
                LIGHT_3    = ["#BDD7EE", "#FFACAC", "#B7E1A1"]

                # ── Panel 1: Nilai Solusi ─────────────────────────────────────
                with vis_tab1:
                    st.markdown("""
                    <div class="info-card" style="font-size:0.85rem;">
                    Grafik ini menampilkan nilai <b>x, y, z</b> yang merupakan solusi dari
                    SPLTV yang kamu masukkan. Baca nilai di atas tiap batang.
                    </div>
                    """, unsafe_allow_html=True)

                    fig1, axes1 = plt.subplots(1, 2, figsize=(13, 4.5))
                    fig1.patch.set_facecolor("#FAFBFF")

                    # Bar chart nilai solusi
                    ax_bar = axes1[0]
                    ax_bar.set_facecolor("#FAFBFF")
                    bars_ = ax_bar.bar(
                        var_labels, val_nums,
                        color=COLORS_3, edgecolor="white",
                        linewidth=2.5, width=0.5,
                        zorder=3
                    )
                    ax_bar.grid(axis="y", color="#E8EDF5", linewidth=1, zorder=0)
                    for bar_, val_ in zip(bars_, val_nums):
                        label_ = f"{val_:.4g}{satuan_str}"
                        ax_bar.text(
                            bar_.get_x() + bar_.get_width() / 2,
                            bar_.get_height() + max(abs(v) for v in val_nums) * 0.02,
                            label_, ha="center", va="bottom",
                            fontweight="bold", fontsize=11, color="#1A3C6E"
                        )
                    ax_bar.set_title("Nilai Solusi SPLTV", fontweight="bold",
                                     color="#1A3C6E", pad=12, fontsize=13)
                    ax_bar.set_ylabel(f"Nilai{satuan_str}", color="#1A3C6E", fontsize=10)
                    ax_bar.tick_params(colors="#1A3C6E")
                    for spine in ["top", "right"]:
                        ax_bar.spines[spine].set_visible(False)

                    # Radar / spider chart (normalisasi terhadap nilai terbesar)
                    ax_rad = axes1[1]
                    ax_rad.set_facecolor("#FAFBFF")
                    max_abs = max(abs(v) for v in val_nums) or 1
                    norm_vals = [abs(v) / max_abs for v in val_nums]
                    categories = var_labels + [var_labels[0]]  # tutup poligon
                    norm_plot  = norm_vals + [norm_vals[0]]
                    angles = [n / float(len(var_labels)) * 2 * np.pi
                              for n in range(len(var_labels))]
                    angles += angles[:1]

                    ax_rad = plt.subplot(1, 2, 2, polar=True, facecolor="#FAFBFF")
                    ax_rad.plot(angles, norm_plot, color="#2E75B6", linewidth=2)
                    ax_rad.fill(angles, norm_plot, color="#2E75B6", alpha=0.2)
                    ax_rad.set_xticks(angles[:-1])
                    ax_rad.set_xticklabels(var_labels, fontsize=10,
                                           fontweight="bold", color="#1A3C6E")
                    ax_rad.set_yticklabels([])
                    ax_rad.set_title("Proporsi Nilai (Radar)", fontweight="bold",
                                     color="#1A3C6E", pad=20, fontsize=13)
                    ax_rad.grid(color="#BDD7EE", linewidth=0.8)

                    plt.tight_layout()
                    st.pyplot(fig1)
                    plt.close()

                    # Tabel ringkasan
                    st.markdown("**📋 Tabel Ringkasan Solusi:**")
                    rows_html = ""
                    for vname, vval, vfmt in zip(var_labels, val_nums, [xf, yf, zf]):
                        rows_html += f"""
                        <tr>
                            <td style='padding:0.4rem 0.8rem;font-weight:700;color:#1A3C6E;'>{vname}</td>
                            <td style='padding:0.4rem 0.8rem;font-family:monospace;font-size:1rem;
                                       font-weight:800;color:#C00000;'>{vfmt}{satuan_str}</td>
                            <td style='padding:0.4rem 0.8rem;font-size:0.85rem;color:#555;'>
                                ≈ {vval:.6g}</td>
                        </tr>"""
                    st.markdown(f"""
                    <table style="width:100%;border-collapse:collapse;margin-top:0.4rem;">
                        <thead>
                            <tr style="background:#1A3C6E;color:white;">
                                <th style="padding:0.5rem 0.8rem;text-align:left;">Variabel</th>
                                <th style="padding:0.5rem 0.8rem;text-align:left;">Nilai</th>
                                <th style="padding:0.5rem 0.8rem;text-align:left;">Nilai Desimal</th>
                            </tr>
                        </thead>
                        <tbody style="background:#FAFBFF;">{rows_html}</tbody>
                    </table>
                    """, unsafe_allow_html=True)

                # ── Panel 2: Verifikasi Grafik ────────────────────────────────
                with vis_tab2:
                    st.markdown("""
                    <div class="info-card" style="font-size:0.85rem;">
                    Grafik ini membandingkan nilai <b>ruas kiri (LHS)</b> setelah substitusi solusi
                    dengan nilai <b>konstanta (d)</b> di ruas kanan.
                    Jika batang LHS dan batang d sama tinggi → solusi terbukti benar!
                    </div>
                    """, unsafe_allow_html=True)

                    fig2, ax2 = plt.subplots(figsize=(10, 4.5))
                    fig2.patch.set_facecolor("#FAFBFF")
                    ax2.set_facecolor("#FAFBFF")

                    lhs_list = [
                        sa1 * xs + sb1 * ys + sc1 * zs,
                        sa2 * xs + sb2 * ys + sc2 * zs,
                        sa3 * xs + sb3 * ys + sc3 * zs,
                    ]
                    rhs_list = [sd1, sd2, sd3]
                    eq_labels = ["Persamaan (1)", "Persamaan (2)", "Persamaan (3)"]
                    x_pos = np.arange(len(eq_labels))
                    w = 0.32

                    bars_rhs = ax2.bar(x_pos - w / 2, rhs_list, w,
                                       label="Nilai d (konstan)",
                                       color="#BDD7EE", edgecolor="white",
                                       linewidth=1.5, zorder=3)
                    bars_lhs = ax2.bar(x_pos + w / 2, lhs_list, w,
                                       label="Ruas Kiri setelah substitusi",
                                       color="#2E75B6", edgecolor="white",
                                       linewidth=1.5, zorder=3)

                    for bar_, val_ in zip(bars_rhs, rhs_list):
                        ax2.text(bar_.get_x() + bar_.get_width() / 2,
                                 bar_.get_height() + max(abs(v) for v in rhs_list + lhs_list) * 0.01,
                                 f"{val_:.4g}", ha="center", va="bottom",
                                 fontsize=9, color="#555")
                    for bar_, val_ in zip(bars_lhs, lhs_list):
                        ax2.text(bar_.get_x() + bar_.get_width() / 2,
                                 bar_.get_height() + max(abs(v) for v in rhs_list + lhs_list) * 0.01,
                                 f"{val_:.4g}", ha="center", va="bottom",
                                 fontsize=9, fontweight="bold", color="#1A3C6E")

                    ax2.set_xticks(x_pos)
                    ax2.set_xticklabels(eq_labels, fontsize=10, color="#1A3C6E")
                    ax2.set_title("Verifikasi: Ruas Kiri vs Konstanta (d)",
                                  fontweight="bold", color="#1A3C6E", pad=12, fontsize=13)
                    ax2.legend(fontsize=9, framealpha=0.7)
                    ax2.grid(axis="y", color="#E8EDF5", linewidth=1, zorder=0)
                    for spine in ["top", "right"]:
                        ax2.spines[spine].set_visible(False)
                    ax2.tick_params(colors="#1A3C6E")

                    plt.tight_layout()
                    st.pyplot(fig2)
                    plt.close()

                    # Selisih error
                    st.markdown("**📋 Tabel Selisih (Error) Verifikasi:**")
                    err_rows = ""
                    for i, (lhs_v, rhs_v, eq_l) in enumerate(
                            zip(lhs_list, rhs_list, eq_labels), 1):
                        err_v = abs(lhs_v - rhs_v)
                        status = "✅ Tepat" if err_v < 0.01 else f"⚠️ Selisih {err_v:.4g}"
                        err_rows += f"""
                        <tr>
                            <td style='padding:0.4rem 0.8rem;font-weight:700;'>{eq_l}</td>
                            <td style='padding:0.4rem 0.8rem;font-family:monospace;'>{lhs_v:.6g}</td>
                            <td style='padding:0.4rem 0.8rem;font-family:monospace;'>{rhs_v:.6g}</td>
                            <td style='padding:0.4rem 0.8rem;'>{status}</td>
                        </tr>"""
                    st.markdown(f"""
                    <table style="width:100%;border-collapse:collapse;margin-top:0.4rem;">
                        <thead>
                            <tr style="background:#1A3C6E;color:white;">
                                <th style="padding:0.5rem 0.8rem;text-align:left;">Persamaan</th>
                                <th style="padding:0.5rem 0.8rem;text-align:left;">LHS (kiri)</th>
                                <th style="padding:0.5rem 0.8rem;text-align:left;">d (kanan)</th>
                                <th style="padding:0.5rem 0.8rem;text-align:left;">Status</th>
                            </tr>
                        </thead>
                        <tbody style="background:#FAFBFF;">{err_rows}</tbody>
                    </table>
                    """, unsafe_allow_html=True)

                # ── Panel 3: Peta Panas Koefisien ────────────────────────────
                with vis_tab3:
                    st.markdown("""
                    <div class="info-card" style="font-size:0.85rem;">
                    <b>Peta Panas (Heatmap)</b> menampilkan matriks koefisien sistem persamaanmu.
                    Warna lebih gelap = nilai absolut koefisien lebih besar.
                    Ini membantu melihat variabel mana yang paling "dominan" di tiap persamaan.
                    </div>
                    """, unsafe_allow_html=True)

                    coef_matrix = np.array([
                        [sa1, sb1, sc1],
                        [sa2, sb2, sc2],
                        [sa3, sb3, sc3],
                    ])
                    const_vec = np.array([sd1, sd2, sd3])

                    fig3, axes3 = plt.subplots(1, 2, figsize=(13, 4.5),
                                               gridspec_kw={"width_ratios": [3, 1]})
                    fig3.patch.set_facecolor("#FAFBFF")

                    # Heatmap matriks koefisien
                    ax_hm = axes3[0]
                    ax_hm.set_facecolor("#FAFBFF")
                    im = ax_hm.imshow(coef_matrix, cmap="Blues", aspect="auto")
                    ax_hm.set_xticks([0, 1, 2])
                    ax_hm.set_xticklabels(var_labels, fontsize=11,
                                          fontweight="bold", color="#1A3C6E")
                    ax_hm.set_yticks([0, 1, 2])
                    ax_hm.set_yticklabels(["Pers.(1)", "Pers.(2)", "Pers.(3)"],
                                          fontsize=11, color="#1A3C6E")
                    for i in range(3):
                        for j in range(3):
                            val_ij = coef_matrix[i, j]
                            disp_ij = int(val_ij) if val_ij == int(val_ij) else f"{val_ij:.2g}"
                            text_color = "white" if abs(val_ij) > (
                                np.max(np.abs(coef_matrix)) * 0.6) else "#1A3C6E"
                            ax_hm.text(j, i, str(disp_ij), ha="center", va="center",
                                       fontweight="bold", fontsize=13, color=text_color)
                    ax_hm.set_title("Matriks Koefisien [A]",
                                    fontweight="bold", color="#1A3C6E", pad=12, fontsize=13)
                    plt.colorbar(im, ax=ax_hm, shrink=0.8, label="Nilai koefisien")

                    # Vektor konstanta
                    ax_cv = axes3[1]
                    ax_cv.set_facecolor("#FAFBFF")
                    im2 = ax_cv.imshow(const_vec.reshape(3, 1), cmap="Oranges", aspect="auto")
                    ax_cv.set_xticks([0])
                    ax_cv.set_xticklabels(["d"], fontsize=11,
                                          fontweight="bold", color="#C00000")
                    ax_cv.set_yticks([0, 1, 2])
                    ax_cv.set_yticklabels(["(1)", "(2)", "(3)"],
                                          fontsize=11, color="#1A3C6E")
                    for i in range(3):
                        val_ci = const_vec[i]
                        disp_ci = int(val_ci) if val_ci == int(val_ci) else f"{val_ci:.2g}"
                        text_col = "white" if abs(val_ci) > (
                            np.max(np.abs(const_vec)) * 0.6) else "#7B3000"
                        ax_cv.text(0, i, str(disp_ci), ha="center", va="center",
                                   fontweight="bold", fontsize=13, color=text_col)
                    ax_cv.set_title("Vektor\nKonstanta [d]",
                                    fontweight="bold", color="#C00000", pad=12, fontsize=11)
                    plt.colorbar(im2, ax=ax_cv, shrink=0.8)

                    plt.tight_layout()
                    st.pyplot(fig3)
                    plt.close()

                    # Determinan
                    A_mat = np.array([
                        [sa1, sb1, sc1],
                        [sa2, sb2, sc2],
                        [sa3, sb3, sc3],
                    ], dtype=float)
                    det_val = np.linalg.det(A_mat)
                    st.markdown(f"""
                    <div class="{'success-card' if abs(det_val)>1e-10 else 'danger-card'}"
                         style="font-size:0.88rem;margin-top:0.8rem;">
                    <b>Det(A) = {det_val:.6g}</b>&nbsp;&nbsp;→&nbsp;&nbsp;
                    {"✅ Determinan ≠ 0 → Sistem memiliki <b>tepat satu solusi</b>."
                     if abs(det_val) > 1e-10
                     else "⚠️ Determinan = 0 → Sistem <b>tidak memiliki solusi tunggal</b> (banyak/tidak ada)."}
                    </div>
                    """, unsafe_allow_html=True)

                # ── Panel 4: Analisis Sensitivitas ───────────────────────────
                with vis_tab4:
                    st.markdown("""
                    <div class="info-card" style="font-size:0.85rem;">
                    <b>Analisis Sensitivitas</b> menunjukkan bagaimana nilai solusi berubah
                    jika <b>salah satu konstanta (d)</b> diubah sedikit-sedikit
                    sementara koefisien tetap. Ini membantu kamu memahami "kepekaan" solusi
                    terhadap perubahan data soal.
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("#### ⚙️ Pilih Konstanta yang Diubah")
                    sens_col1, sens_col2 = st.columns([1, 2])
                    with sens_col1:
                        sens_which = st.selectbox(
                            "Ubah konstanta:",
                            options=["d₁ (Persamaan 1)",
                                     "d₂ (Persamaan 2)",
                                     "d₃ (Persamaan 3)"],
                            key="studio_sens_which"
                        )
                        base_d = [sd1, sd2, sd3][["d₁ (Persamaan 1)",
                                                   "d₂ (Persamaan 2)",
                                                   "d₃ (Persamaan 3)"].index(sens_which)]
                        sens_range_pct = st.slider(
                            "Rentang perubahan (%):",
                            min_value=5, max_value=50, value=20, step=5,
                            key="studio_sens_range"
                        )
                        sens_steps = st.slider(
                            "Jumlah titik sampel:",
                            min_value=5, max_value=30, value=15, step=1,
                            key="studio_sens_steps"
                        )

                    with sens_col2:
                        # Hitung rentang d
                        delta = abs(base_d) * sens_range_pct / 100 if base_d != 0 else sens_range_pct
                        d_range = np.linspace(base_d - delta, base_d + delta, sens_steps)

                        xs_arr, ys_arr, zs_arr = [], [], []
                        for d_val_s in d_range:
                            if sens_which == "d₁ (Persamaan 1)":
                                sol_s2, err_s2 = solve_spltv(
                                    sa1, sb1, sc1, d_val_s,
                                    sa2, sb2, sc2, sd2,
                                    sa3, sb3, sc3, sd3)
                            elif sens_which == "d₂ (Persamaan 2)":
                                sol_s2, err_s2 = solve_spltv(
                                    sa1, sb1, sc1, sd1,
                                    sa2, sb2, sc2, d_val_s,
                                    sa3, sb3, sc3, sd3)
                            else:
                                sol_s2, err_s2 = solve_spltv(
                                    sa1, sb1, sc1, sd1,
                                    sa2, sb2, sc2, sd2,
                                    sa3, sb3, sc3, d_val_s)
                            if sol_s2 is not None:
                                xs_arr.append(sol_s2[0])
                                ys_arr.append(sol_s2[1])
                                zs_arr.append(sol_s2[2])
                            else:
                                xs_arr.append(np.nan)
                                ys_arr.append(np.nan)
                                zs_arr.append(np.nan)

                        fig4, ax4 = plt.subplots(figsize=(9, 4.5))
                        fig4.patch.set_facecolor("#FAFBFF")
                        ax4.set_facecolor("#FAFBFF")

                        for arr_, lbl_, col_ in zip(
                            [xs_arr, ys_arr, zs_arr],
                            var_labels,
                            COLORS_3
                        ):
                            ax4.plot(d_range, arr_, color=col_, linewidth=2.5,
                                     label=lbl_, marker="o", markersize=4)

                        # Tandai nilai asli (base)
                        ax4.axvline(x=base_d, color="#ED7D31", linewidth=1.8,
                                    linestyle="--", label=f"Nilai asli ({base_d:.4g})")
                        ax4.axhline(y=xs, color=COLORS_3[0], linewidth=0.8,
                                    linestyle=":", alpha=0.5)
                        ax4.axhline(y=ys, color=COLORS_3[1], linewidth=0.8,
                                    linestyle=":", alpha=0.5)
                        ax4.axhline(y=zs, color=COLORS_3[2], linewidth=0.8,
                                    linestyle=":", alpha=0.5)

                        ax4.set_xlabel(f"Nilai {sens_which}", color="#1A3C6E", fontsize=10)
                        ax4.set_ylabel(f"Nilai Solusi{satuan_str}", color="#1A3C6E", fontsize=10)
                        ax4.set_title(f"Sensitivitas Solusi terhadap Perubahan {sens_which}",
                                      fontweight="bold", color="#1A3C6E", pad=12, fontsize=12)
                        ax4.legend(fontsize=9, framealpha=0.7)
                        ax4.grid(color="#E8EDF5", linewidth=1)
                        for spine in ["top", "right"]:
                            ax4.spines[spine].set_visible(False)
                        ax4.tick_params(colors="#1A3C6E")

                        plt.tight_layout()
                        st.pyplot(fig4)
                        plt.close()

                    # Interpretasi sensitivitas
                    st.markdown("""
                    <div class="warning-card" style="font-size:0.85rem;margin-top:0.6rem;">
                    <b>📌 Cara Membaca Grafik Sensitivitas:</b><br>
                    • Garis <b>curam</b> → variabel sangat sensitif terhadap perubahan konstanta
                      (sedikit perubahan data = perubahan solusi besar)<br>
                    • Garis <b>mendatar</b> → variabel tidak terlalu terpengaruh<br>
                    • Titik <b>perpotongan garis putus-putus oranye</b> = nilai solusi aslimu<br>
                    • Berguna dalam analisis: <i>"bagaimana jika harga totalnya berubah?"</i>
                    </div>
                    """, unsafe_allow_html=True)

                # ── REFLEKSI ──────────────────────────────────────────────────
                st.markdown("---")
                st.markdown("### 📝 Catat Temuanmu (Refleksi Discovery Learning)")
                st.markdown("""
                <div class="fase-box" style="border-color:#7030A0;background:#F5EFFF;">
                    <div class="fase-label" style="color:#7030A0;">⑥ Generalization — Simpulkan Temuanmu</div>
                    <div class="fase-text">Setelah bereksplorasi dengan model sendiri, catat simpulanmu di LKS!</div>
                </div>
                """, unsafe_allow_html=True)

                col_ref1, col_ref2 = st.columns(2)
                with col_ref1:
                    ref_a = st.text_area(
                        "1. Apakah model SPLTV-mu sudah benar? Bagaimana kamu memastikannya?",
                        placeholder="Tulis di sini...", height=90,
                        key="studio_ref_a"
                    )
                    ref_b = st.text_area(
                        "2. Apa makna dari nilai x, y, z dalam konteks soal?",
                        placeholder="Tulis di sini...", height=90,
                        key="studio_ref_b"
                    )
                with col_ref2:
                    ref_c = st.text_area(
                        "3. Dari grafik sensitivitas, variabel mana yang paling berubah?",
                        placeholder="Tulis di sini...", height=90,
                        key="studio_ref_c"
                    )
                    ref_d = st.text_area(
                        "4. Bagaimana SPLTV ini bisa diterapkan dalam kehidupan nyata?",
                        placeholder="Tulis di sini...", height=90,
                        key="studio_ref_d"
                    )

                if any([ref_a, ref_b, ref_c, ref_d]):
                    st.markdown("""
                    <div class="success-card">
                    ✅ <b>Refleksimu sudah tercatat!</b>
                    Salin ke LKS-mu dan diskusikan dengan kelompokmu.
                    </div>
                    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  PANDUAN INTEGRASI LENGKAP
# ══════════════════════════════════════════════════════════════════════════════
#
#  LANGKAH 1 — Ubah definisi tabs di KP 3:
#  ─────────────────────────────────────────
#  Cari:
#      tab_a, tab_b, tab_c = st.tabs([
#          "🧮 Studio Pemodelan",
#          "📈 Visualisasi Solusi",
#          "🌍 Konteks Kehidupan Nyata"
#      ])
#
#  Ganti dengan:
#      tab_a, tab_b, tab_c, tab_d = st.tabs([
#          "🧮 Studio Pemodelan",
#          "📈 Visualisasi Solusi",
#          "🌍 Konteks Kehidupan Nyata",
#          "🖊️ Studio Mandiri",
#      ])
#
#
#  LANGKAH 2 — Tempel blok "with tab_d:" (dari atas) SETELAH:
#  ─────────────────────────────────────────────────────────────
#      # ── KONTEKS KEHIDUPAN NYATA
#      with tab_c:
#          ...  (seluruh isi tab_c tetap tidak diubah)
#
#  Artinya: tempel persis setelah baris penutup blok with tab_c:,
#  sebelum baris "elif tab_choice ==" berikutnya.
#
#
#  LANGKAH 3 — Import (sudah ada di file utama, tidak perlu tambah):
#  ─────────────────────────────────────────────────────────────────
#  matplotlib, numpy sudah diimpor di atas kode utama.
#  solve_spltv() dan format_val() sudah didefinisikan sebagai helper.
#
#
#  TIDAK ADA perubahan lain. Semua kode lama tetap persis seperti semula.
# ══════════════════════════════════════════════════════════════════════════════
