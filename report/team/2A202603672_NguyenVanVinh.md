# Báo cáo cá nhân — Nguyễn Văn Vinh (2A202603672)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Vinh
- MSSV: 2A202603672
- Email: nguyenvanvinh2819@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Giữ hồ sơ `report/team/ho_so_launch_v0.md`: dựng khung bảy mục từ đầu buổi, điền dần con số chính, trạng thái và người phụ trách khi các nhiệm vụ A–E có kết quả.
- Gắn nhãn độc lập 20 ca lỗi ở CP3, so nhãn với người gắn nhãn 1, cùng điền `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

- Dựng khung `ho_so_launch_v0.md`: nhóm OPC, lớp L3A; bảy mục, mỗi mục gán một vai trò phụ trách (PM trợ lý hoàn phí, Giám đốc vận hành, Trưởng nhóm CSKH, Kỹ sư trưởng agent), trạng thái ban đầu "Chưa" và ghi rõ mục đó chờ số từ file nào.
- Sau khi A1–A4 được merge, điền mục 1 (4.472 đ/việc, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu; 4.599 đ khi cộng chi phí cố định ở 45.000 yêu cầu/tháng, 5.784 đ nếu còn một nửa) và mục 3 (0,22× · 0,69× · 0,85× · 1,88× so với 12.000 đ theo loại; 0,38× cho phạm vi noi_dia + hang_nang). Mọi số này đều ghi nhãn `simulated`.
- Chuẩn bị phiếu gắn nhãn 20 ca (tóm tắt từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`) để gắn độc lập ở CP3.

## 4. Bằng chứng

- Commit `77d3078`: dựng khung bảy mục của `ho_so_launch_v0.md`.
- Commit `9edadc3` (nhánh `docs/ho-so-launch-cp1`): điền mục 1, 3 từ kết quả A2–A4 và thêm báo cáo cá nhân này.
- Số trong hồ sơ lấy từ `report/team/bang_chi_phi.md` (A2, A3, A4) do `src/lab13.py` của nhóm tính ra, không tự đặt số.

## 5. Công cụ AI đã dùng

- Công cụ: trợ lý AI (agent lập trình chạy trong repo của nhóm).
- Dùng để tóm tắt repo và đề bài, hướng dẫn các bước cần làm theo vai người gắn nhãn 2 kiêm giữ hồ sơ.
- Theo yêu cầu của tôi, AI soạn và điền nội dung từ số liệu nhóm đã tính: các mục của `ho_so_launch_v0.md` và đề xuất cuối, E2 trong `chi_so.md`, `group_report.md`, `phieu_cham.md`; gộp nhánh và commit, push. Tôi quyết định làm phần nào, đọc lại kết quả trước khi nộp; câu trả lời của đội trình và kết quả duyệt chéo do tôi ghi lại tại buổi.
- Không dùng AI để gắn nhãn: 20 ca ở CP3 tôi tự gắn độc lập (phiếu gốc có lý do từng ca); AI chỉ chép nhãn vào bảng và không so với đáp án trước khi người gắn nhãn 1 gắn xong.
- Tự kiểm tra: đối chiếu mọi số trong hồ sơ với `bang_chi_phi.md` và output của `src/lab13.py`; chạy lại `lab13.py`, kiểm `pilot_plan.yaml` bằng `yaml.safe_load`, tìm từ cấm trong `report/team/`.

## 6. Tự đánh giá

- Đã có khung hồ sơ từ sớm, nên khi A xong thì điền ngay được mục 1 và 3, đúng nhãn `simulated`.
- Hồ sơ đủ bảy mục và đề xuất Go có điều kiện; hội đồng chấm nhóm 30/30, Go có điều kiện.
- Nhãn độc lập của tôi khớp 19/20 ca với nhãn thống nhất (lệch ca 18: tôi gắn Hệ thống, nhãn chốt là Ngữ cảnh); đồng thuận với người gắn nhãn 1 chỉ 55%, nên cần thống nhất định nghĩa trước khi gắn ở lần sau.
- Trước buổi bảo vệ cần tự giải thích được vì sao chi phí mỗi việc thành công (4.472 đ) chưa so trực tiếp được với 12.000 đ khi chưa cộng phần chuyển nhân viên.
