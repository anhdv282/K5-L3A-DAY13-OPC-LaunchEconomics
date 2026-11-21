# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: OPC · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc trên 1.200 yêu cầu, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ) [simulated]; phạm vi noi_dia + hang_nang cộng cố định 40 triệu/tháng: 4.599 đ ở 45.000 yc/tháng, 5.784 đ nếu còn một nửa [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. số ca làm lại gấp đôi +51,8% (6.787 đ) · 2. tỉ lệ xem lại gấp đôi +40,7% (6.292 đ) · 3. lương tăng 25% +23,1% (5.506 đ) [simulated]; giá token gấp đôi chỉ +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88× (thành công 27,3%) [simulated]. Cả hệ thống, cộng 222 ca nhân viên làm thay: 7.037.585 ÷ 1.200 = 5.865 đ/yêu cầu = 0,49× [simulated]; giới hạn 2 lần chạy rẻ nhất (6.901.220 đ) [simulated]. Bất lợi: xem lại 100% noi_dia + hang_nang thì 11.743 đ = 0,98×, hoặc 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (không có đối chứng): chính 82,83% (994/1.200) đóng trong 24 giờ và không mở lại 7 ngày · dùng 27,12% (48/177) bỏ qua gợi ý · an toàn 4,25% (51/1.200) mở lại trong 7 ngày; 10 event có `trace_id` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn 4 · Ngầm 3; đồng thuận độc lập 11/20 = 55% (< 80%), đã viết lại định nghĩa theo bốn câu hỏi thứ tự và ghi quy tắc cho 9 ca không trùng; bảng khắc phục 5 ca (9, 7, 18, 13, 12), mỗi ca có event, ngưỡng và một vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | (chờ D1, D2 trong `pilot_plan.yaml`) | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | 4 rủi ro trong `chi_so.md`: làm lại gấp đôi +51,8% (6.787 đ) · xem lại 100% 0,98× đến 1,03× · lương +25% thì +23,1% · khối lượng còn một nửa thì cố định +2.370 đ/việc [simulated]; mỗi dòng có dấu hiệu theo dõi, ngưỡng và vai trò phụ trách | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
