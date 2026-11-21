# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: OPC · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc, gấp 16,3× hoá đơn/yêu cầu [simulated]. Phạm vi noi_dia + hang_nang cộng cố định 40 triệu/tháng: 4.599 đ ở 45.000 yêu cầu/tháng; 5.784 đ nếu giảm nửa [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi: +51,8%, 6.787 đ; xem lại gấp đôi: +40,7%, 6.292 đ; lương tăng 25%: +23,1%, 5.506 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống chưa cộng cố định: 5.865 đ/yêu cầu = 0,49× mức 12.000 đ [simulated]. Loại quoc_te vì 22.515 đ/việc = 1,88×; loại doi_tac vì điều khoản riêng, chi phí 0,85× [simulated]. Bất lợi: xem lại 100% trong phạm vi tốn 11.743–12.415 đ/việc = 0,98–1,03× [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Lần lượt 994/1.200 = 82,83%; 48/177 = 27,12%; 51/1.200 = 4,25%. Đặc tả 11 event có trace_id trong `chi_so.md`; chưa có đối chứng để kết luận tác động | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca; hai bộ nhãn trùng 11/20 = 55%, dưới 80%; đã viết lại định nghĩa, giải thích 9 ca khác nhau và có bảng khắc phục đủ 5 loại lỗi | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | 20 người/nhóm, 299 yêu cầu/người = 5.980 mẫu quan sát/nhóm; DE 6,96, mẫu hiệu dụng 859; MDE 6 điểm, power khoảng 0,64 nếu tác động thật 5 điểm. Có 4 luật dừng; quyết định 05/01/2027 khi đủ mẫu và theo dõi | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | 3 rủi ro trong `chi_so.md`: làm lại +51,8%; xem lại 100% lên 1,03× nhân viên; khối lượng giảm nửa làm cố định/việc tăng từ 1.185 lên 2.370 đ [simulated] | Giả lập | PM trợ lý hoàn phí |

- Kỹ sư trưởng agent: trước 22/11/2026 có bằng chứng kiểm thử ca 7 và 20, không báo đã hoàn khi ghi sổ lỗi và không hoàn trùng.
- Giám đốc vận hành: trước 22/11/2026 ký chấp nhận MDE 6 điểm và power khoảng 0,64 ở mức 5 điểm; chỉ duyệt pilot noi_dia + hang_nang.
- Kỹ sư trưởng agent: trước 22/11/2026 bật đủ 11 event, 100% event có trace_id và request_id; kiểm tra cách tính đủ 5 chỉ số đã đặc tả.
- Trưởng nhóm CSKH: trước 22/11/2026 thống nhất định nghĩa lỗi đã sửa; tuần đầu xem lại 100%, đo phút thật và kiểm ngày 29/11/2026; ngày 06/12/2026 chỉ giảm xem lại khi sửa + bỏ < 15% và không vi phạm luật an toàn.

**Đề xuất:** Go có điều kiện cho kế hoạch pilot; chỉ bắt đầu khi các điều kiện trước pilot ở trên đã có bằng chứng, tuân thủ các mốc kiểm tra và luật dừng trong `pilot_plan.yaml`.
