# Báo cáo cá nhân — Đặng Việt Anh (2A202603685)

## 1. Thông tin thành viên

- Họ tên: Đặng Việt Anh
- MSSV: 2A202603685
- Email: vietanh.dang282@gmail.com
- Vai trong nhóm: Người viết code (giai đoạn 14:00–15:20, nhiệm vụ A). Sau giải lao chuyển sang người kiểm số.

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1): viết ba hàm A1 trong `src/lab13.py`, hàm `mo_hinh` (A2), vòng lặp A3 và phần A4 (chi phí cố định).
- Điền `report/team/bang_chi_phi.md` cho A1–A4.
- Viết báo cáo cá nhân này.

## 3. Đóng góp cụ thể

- Commit `54b87ae`: ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`). Phép thử ĐẠT (1,20 · 1,25 · 1,25).
- Commit `7715c86` (đã merge qua PR #1, `ecc033a`): hàm `mo_hinh`, trả về các khoá token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc, và hỗ trợ `max_lan_chay` cho nhiệm vụ B.
- Nhánh `feat/cp1-a3-a4-bang-chi-phi`: thêm A3 (bảng theo loại) và A4 (chi phí cố định) vào khối `__main__`, điền `bang_chi_phi.md`.
- Đối chiếu số A2, A3, A4 với bảng trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Riêng số lần thử theo `attempt` của `quoc_te` (30,0% / 11,4% / 2,2%) tôi chạy lại trên CSV để kiểm tra.
- Không commit `src/.venv/`, các thư mục rác trong `src/`, hay chỉnh sửa hai file CSV.

## 4. Bằng chứng

- Commit: `54b87ae`, `7715c86`, merge `ecc033a` trên `main`.
- Output của `python lab13.py`: tổng 4.373.585 đ, 978 việc thành công, cps 4.472 đ; A3 và A4 khớp với hướng dẫn trong phạm vi 2%.
- File: `report/team/bang_chi_phi.md` (A1–A4 đã điền, B1–B4 còn trống).

## 5. Công cụ AI đã dùng

- Claude (Claude Code) được dùng để viết phần code `mo_hinh`, A3 và A4 theo yêu cầu của tôi, và để giải thích công thức.
- Cách tự kiểm tra: so từng khoá output với bảng đối chiếu trong hướng dẫn, và chạy lại tỉ lệ thành công theo lần thử từ CSV. Các con số không được lấy từ AI mà từ `lab13.py` chạy trên dữ liệu.

## 6. Tự đánh giá

- Đã làm xong A1–A4 và đối chiếu được đáp án.
- Chưa tự tay giải thích hết các công thức trong code, nên trước khi bảo vệ tôi cần đọc lại `mo_hinh` và giải thích được vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công.
- Chưa làm nhiệm vụ B. Việc này sẽ do người viết code sau giải lao, hoặc tôi làm nếu nhóm phân công.
