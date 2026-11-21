# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: OPC
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Đánh giá trợ lý hoàn phí LogiX-VN bằng chi phí mỗi việc thành công, chỉ số sử dụng, an toàn và một pilot có đối chứng. Tính trên 1.200 yêu cầu, 1.624 lần chạy giả lập; đối chiếu công thức và đáp án trong hướng dẫn.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- A–B: code cộng mọi lần chạy, chi phí xem lại/làm lại; phân tích theo loại và độ nhạy trong [bảng chi phí](bang_chi_phi.md).
- C: giữ hai bộ nhãn độc lập; đồng thuận 55%, đã viết lại định nghĩa và chọn 5 ca khắc phục trong [bảng lỗi](bang_loi.md).
- D–E: [pilot plan](pilot_plan.yaml), [chỉ số và event](chi_so.md), [hồ sơ launch v0](ho_so_launch_v0.md) ghi đủ cỡ mẫu, rủi ro, điều kiện và người phụ trách.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

Chi phí 4.472 đ/việc; chi phí cả hệ thống chưa cộng cố định 5.865 đ/yêu cầu [simulated]. Chỉ số chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 4,25%; chưa có đối chứng nên chưa kết luận tác động.

Đề xuất Go có điều kiện cho pilot noi_dia + hang_nang: 20 nhân viên/nhóm, 299 yêu cầu/người, MDE 6 điểm; power chỉ khoảng 0,64 nếu tác động thật 5 điểm. Chưa ghi nhận kết quả duyệt chéo của hội đồng.

## 5. Khó khăn và cách xử lý

Terminal từng lỗi mã hóa tiếng Việt, xử lý bằng `python -X utf8 lab13.py`. Bảng chi phí từng có xung đột merge và số kiểm tay nháp lệch trên 2%; giữ số nháp để đối chiếu, không dùng thay kết quả đã kiểm tra.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

Hà Huy Thái kiểm số CP1–CP2, từ CP3 bổ sung code và rà soát dữ liệu, hoàn thiện CP4 và tính chỉ số CP5; bằng chứng trong [báo cáo cá nhân](2A202603682_HaHuyThai.md). Hai bộ nhãn của Vũ Quang Minh và Nguyễn Văn Vinh được giữ nguyên trong bảng lỗi; các thành viên tự xác nhận đóng góp trong hồ sơ nhóm.

## 7. Hạn chế và hướng cải thiện

Phút xem lại/làm lại còn là simulated; cần thay bằng phút đo thật. Xem lại 100% có thể tốn 12.415 đ/việc [simulated]; cần giảm có kiểm soát. Đồng thuận nhãn 55% còn thấp, đã viết lại định nghĩa; không sửa hai bộ nhãn để nâng tỉ lệ.

Pilot cần ít nhất 5.980 yêu cầu/nhóm và đủ cửa sổ theo dõi 7 ngày; thiếu mẫu thì chưa kết luận hiệu quả. Danh sách event hiện là đặc tả, cần được triển khai và kiểm chứng trước pilot.

## 8. Tài liệu tham khảo

- [Hướng dẫn chi tiết buổi chiều](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), nhiệm vụ A–E.
- [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md); hai CSV trong `src/`; số tính bằng [lab13.py](../../src/lab13.py).
- [Rubric](../../RUBRIC.md), [quy tắc](../../RULES.md), [checkpoints](../../CHECKPOINTS.md).
