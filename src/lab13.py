"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    return 1 / p if k is None else (1 - (1 - p) ** k) / p

def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    token = tien_token.sum()
    tool = tien_tool.sum()
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=token, tool=tool,
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(token + tool) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # Nhiệm vụ A3: tách theo loại yêu cầu.
    print('\nA3 · Theo loại yêu cầu')
    print(f"{'loai':10s} {'yc':>5s} {'tl_thanh_cong':>14s} {'lan/yc':>7s} {'cps':>8s} {'x 12000':>8s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        con = reqs[reqs.loai == loai]
        r = mo_hinh(runs, con)
        so_lan = len(runs[runs.request_id.isin(con.request_id)])
        print(f"{loai:10s} {len(con):5d} {r['thanh_cong'] / len(con):13.1%} "
              f"{so_lan / len(con):7.2f} {r['cps']:8,.0f} {r['cps'] / BASELINE:7.2f}x")

    # Nhiệm vụ A4: cộng chi phí cố định 40 triệu đ/tháng vào phạm vi pilot (noi_dia + hang_nang).
    YC_THANG = 45000        # yêu cầu mỗi tháng ở quy mô đầy đủ
    CHI_PHI_CO_DINH = 40_000_000
    pham_vi = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    r = mo_hinh(runs, pham_vi)
    viec_thang = YC_THANG * r['thanh_cong'] / len(reqs)   # số việc thành công mỗi tháng
    co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_thang
    cps_tong = r['cps'] + co_dinh_moi_viec
    print('\nA4 · Chi phí cố định trong phạm vi noi_dia + hang_nang')
    print(f"Việc thành công mỗi tháng (quy mô đầy đủ): {viec_thang:,.0f}")
    print(f"Chi phí cố định mỗi việc: {co_dinh_moi_viec:,.0f} đ")
    print(f"Chi phí mỗi việc trong phạm vi: {r['cps']:,.0f} đ")
    print(f"Cộng cố định: {cps_tong:,.0f} đ = {cps_tong / BASELINE:.2f}x  [simulated]")

    # Nhiệm vụ B1: đổi từng yếu tố, một lần đổi một yếu tố (simulated).
    print('\nB1 · Đổi từng yếu tố (simulated)')
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    doi = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        doi[ten] = cps / goc - 1
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # Nhiệm vụ B2: đổi một cặp, và xếp hạng theo mức thay đổi tuyệt đối khi đổi một yếu tố.
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Giá token gấp đôi + xem lại gấp đôi: {cap:,.0f} ({(cap / goc - 1) * 100:+.1f}%) [simulated]')
    print('Tổng hai tác động riêng:', f"{(doi['Giá token gấp đôi'] + doi['Xem lại gấp đôi']) * 100:+.1f}%")
    cac_yeu_to = ['Giá token gấp đôi', 'Xem lại gấp đôi', 'Làm lại gấp đôi', 'Lương tăng 25%']
    xep_hang = sorted(((t, doi[t]) for t in cac_yeu_to), key=lambda x: abs(x[1]), reverse=True)
    print('Xếp hạng ba yếu tố mạnh nhất:', ' · '.join(f'{i}. {t}' for i, (t, _) in enumerate(xep_hang[:3], 1)))

    # Nhiệm vụ B3: giới hạn chạy lại, tính cả hệ thống (nhân viên làm 12.000 đ cho mỗi yêu cầu không thành công).
    print('\nB3 · Giới hạn chạy lại (chi phí: simulated)')
    print(f"{'giới hạn':>8s} {'tổng trợ lý':>14s} {'không thành công':>17s} {'cả hệ thống':>14s} {'cps':>8s}")
    for gioi_han in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_tc = len(reqs) - r['thanh_cong']
        he_thong = r['tong'] + BASELINE * khong_tc
        print(f"{gioi_han:8d} {r['tong']:14,.0f} {khong_tc:17d} {he_thong:14,.0f} {r['cps']:8,.0f}")

    # Nhiệm vụ B4: xem lại 100% trong phạm vi noi_dia + hang_nang (theo cách tính trong hướng dẫn).
    pv = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    pv_runs = runs[runs.request_id.isin(pv.request_id)]
    tien_pv = (pv_runs['tokens_in'] / 1000 * GIA_VAO + pv_runs['tokens_out'] / 1000 * GIA_RA
               + pv_runs['tool_calls'] * GIA_TOOL).sum()
    yc_co_ok = pv_runs[pv_runs.status == 'ok'].request_id.nunique()
    ca_lam_lai = (pv['ket_qua'] == 'lam_lai').sum()
    # Trung bình trên toàn bộ ca làm lại (mọi depot, mọi loại), theo hướng dẫn: 15,3 phút.
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    thanh_cong_pv = (pv['ket_qua'] == 'thanh_cong').sum()
    print(f'\nB4 · Phạm vi: {len(pv)} yêu cầu; {yc_co_ok} có lần chạy ok; '
          f'{ca_lam_lai} ca làm lại; {thanh_cong_pv} việc thành công')
    for ten, phut_lam in [('9 phút/ca (đề)', 9), (f'{phut_lam_lai_tb:.1f} phút/ca (dữ liệu)', phut_lam_lai_tb)]:
        tong_pv = tien_pv + yc_co_ok * 5 * LUONG_PHUT + ca_lam_lai * phut_lam * LUONG_PHUT
        cps_pv = tong_pv / thanh_cong_pv
        print(f'\nB4 · Xem lại 100% ({ten}): {cps_pv:,.0f} đ = {cps_pv / BASELINE:.2f}x [simulated]')
        phut_xem_hoa_von = (BASELINE * thanh_cong_pv - tien_pv
                           - ca_lam_lai * phut_lam * LUONG_PHUT) / (yc_co_ok * LUONG_PHUT)
        print(f'Xem lại hòa vốn tối đa: {phut_xem_hoa_von:.1f} phút/yêu cầu '
              '[simulated; chưa cộng chi phí cố định]')

    # Nhiệm vụ D1: cỡ mẫu và giới hạn khi chia theo cụm.
    from statistics import NormalDist
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    def co_mau(p1, p2, alpha=0.05, power=0.8):
        """Cỡ mẫu mỗi nhóm theo công thức hai tỉ lệ trong hướng dẫn."""
        za = NormalDist().inv_cdf(1 - alpha / 2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
                         / (p2 - p1) ** 2)

    icc = 0.02
    n_5_diem = co_mau(0.70, 0.75)
    de_75 = 1 + (75 - 1) * icc
    n_theo_nhan_vien = math.ceil(n_5_diem * de_75)
    nguoi_moi_nhom = math.ceil(n_theo_nhan_vien / 75)
    n_6_diem = co_mau(0.70, 0.76)
    so_cum = 20
    m_6_diem = math.ceil(n_6_diem * (1 - icc) / (so_cum - n_6_diem * icc))
    de_6_diem = 1 + (m_6_diem - 1) * icc
    n_hieu_dung = so_cum * m_6_diem / de_6_diem
    power_5_diem = NormalIndPower().power(
        effect_size=proportion_effectsize(0.75, 0.70), nobs1=n_6_diem,
        alpha=0.05, ratio=1, alternative='two-sided')

    print('\nD1 · Cỡ mẫu (giả định của lab: baseline 0,70; alpha 0,05; power 0,80; ICC 0,02)')
    print(f'a) Theo yêu cầu: {n_5_diem:,} yêu cầu mỗi nhóm')
    print(f'b) Theo nhân viên, m=75: DE={de_75:.2f}; {n_theo_nhan_vien:,} yêu cầu/nhóm; '
          f'{nguoi_moi_nhom} người/nhóm, tổng {2 * nguoi_moi_nhom} > 40: không đủ người')
    print(f'c) 20 người/nhóm: trần tiệm cận {20 / icc:,.0f} mẫu hiệu dụng < {n_5_diem:,}')
    print(f'd) 6 depot/nhóm: trần tiệm cận {6 / icc:,.0f} mẫu hiệu dụng; chỉ 6 cụm < 20')
    print(f'e) MDE 6 điểm: cần {n_6_diem} mẫu hiệu dụng/nhóm; tối thiểu {m_6_diem} yêu cầu/người; '
          f'DE={de_6_diem:.2f}; n hiệu dụng={n_hieu_dung:.2f}')
    print(f'Kế hoạch 20 người/nhóm cần ít nhất {so_cum * m_6_diem:,} yêu cầu thực tế/nhóm; '
          f'nếu tác động thật chỉ 5 điểm, power khoảng {power_5_diem:.2f}')

    mo_lai = int(reqs['mo_lai_trong_7_ngay'].sum())
    mo_lai_pv = int(pv['mo_lai_trong_7_ngay'].sum())
    print(f'\nD3 · Mở lại 7 ngày trong dữ liệu lab: {mo_lai}/{len(reqs)} = '
          f'{mo_lai / len(reqs):.2%}; phạm vi noi_dia + hang_nang: '
          f'{mo_lai_pv}/{len(pv)} = {mo_lai_pv / len(pv):.2%}')

    # Nhiệm vụ E1: chỉ số của đợt chạy thử, chưa có nhóm đối chứng.
    dong_dung_han_khong_mo = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    so_dat_chinh = int(dong_dung_han_khong_mo.sum())
    duoc_xem_lai = reqs[reqs['duoc_xem_lai'] == 1]
    so_bo_qua = int(duoc_xem_lai['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    so_mo_lai = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    print('\nE1 · Chỉ số trong đợt chạy thử (dữ liệu giả lập của lab)')
    print(f'Chính: đóng trong 24 giờ và không mở lại 7 ngày: '
          f'{so_dat_chinh}/{len(reqs)} = {so_dat_chinh / len(reqs):.2%}')
    print(f'Dùng: sửa hoặc bỏ gợi ý trên yêu cầu được xem lại: '
          f'{so_bo_qua}/{len(duoc_xem_lai)} = {so_bo_qua / len(duoc_xem_lai):.2%}')
    print(f'An toàn: mở lại trong 7 ngày: '
          f'{so_mo_lai}/{len(reqs)} = {so_mo_lai / len(reqs):.2%}')
    print('Chưa có đối chứng: không kết luận trợ lý đã nâng chỉ số từ 70%.')
    print('Hai chỉ số đề xuất về mở trợ lý và kiểm tra sai tiền cần event mới; không suy ra từ CSV hiện có.')
    so_lam_lai_pv = int((pv['ket_qua'] == 'lam_lai').sum())
    print(f'E2 · Nền theo dõi làm lại trong phạm vi: '
          f'{so_lam_lai_pv}/{len(pv)} = {so_lam_lai_pv / len(pv):.2%}')
