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
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; phạm vi noi_dia + hang_nang. Mức 5 điểm cần 1.251 yêu cầu/nhóm nhưng 20 người/nhóm chỉ đạt tối đa 1.000 mẫu hiệu dụng, nên chấp nhận MDE 6 điểm: 859/nhóm, m ≥ 299 yêu cầu/người, DE 6,96. Bất lợi: power chỉ khoảng 0,64 nếu tác động thật là 5 điểm. 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ (mở lại +2 điểm hoặc > 6%, hoàn trùng ≥ 1 ca, chi phí > 8.000 đ/việc, bỏ qua gợi ý > 40%); quyết định 05/01/2027 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | 4 rủi ro trong `chi_so.md`: làm lại gấp đôi +51,8% (6.787 đ) · xem lại 100% 0,98× đến 1,03× · lương +25% thì +23,1% · khối lượng còn một nửa thì cố định +2.370 đ/việc [simulated]; mỗi dòng có dấu hiệu theo dõi, ngưỡng và vai trò phụ trách | Giả lập | PM trợ lý hoàn phí |

**Lý do:** trong phạm vi noi_dia + hang_nang, chi phí mỗi việc thành công cộng cố định là 4.599 đ = 0,38× mức 12.000 đ; tính cả hệ thống trên mọi loại là 0,49× [simulated]. Hai con số bất lợi: xem lại 100% thì lên 0,98× đến 1,03× [simulated], và với 40 nhân viên pilot chỉ đủ mẫu cho mức chênh 6 điểm (power khoảng 0,64 nếu tác động thật là 5 điểm). quoc_te (1,88×) và doi_tac (0,85×, điều khoản riêng) ở ngoài phạm vi [simulated].

**Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang, chia 20 + 20 nhân viên, quyết định ngày 05/01/2027. Chưa đủ điều kiện nào thì không bắt đầu hoặc không chuyển bước rollout.

| Điều kiện | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| Có khoá chống trùng (idempotency_key) và đối soát sổ cái theo trace_id mỗi giờ, chặn lỗi kiểu ca 7 và ca 20; chạy thử 0 ca hoàn trùng | Kỹ sư trưởng agent | 22/11/2026, trước ngày bắt đầu |
| Ký chấp nhận MDE 6 điểm và power 0,64 ở mức 5 điểm; không diễn giải kết quả không có ý nghĩa thống kê là "trợ lý không có tác động" | Giám đốc vận hành | 22/11/2026, trước ngày bắt đầu |
| Bật đủ 10 event có trace_id trong `chi_so.md`; sau tuần 1 thay phút xem lại và làm lại simulated bằng phút đo thật, tính lại chi phí mỗi việc thành công | PM trợ lý hoàn phí | 29/11/2026, cuối bước 0,10 |
| Kế hoạch giảm xem lại theo bậc: chỉ giảm khi tỉ lệ sửa + bỏ < 15% và kiểm tra mẫu không thấy lỗi ngầm; mục tiêu mỗi lần xem lại ≤ 5 phút để không vượt mức hoà vốn (B4) | Trưởng nhóm CSKH | 06/12/2026, cuối bước 0,25 |
