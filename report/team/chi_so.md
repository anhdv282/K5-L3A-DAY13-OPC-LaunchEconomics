# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại (`duoc_xem_lai` bằng 1) | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Tỉ lệ yêu cầu của nhóm can thiệp được mở bằng trợ lý (nhóm tự đề xuất) | Số yêu cầu mở bằng trợ lý chia tổng yêu cầu của nhóm can thiệp, đếm từ event `agent_suggestion_shown` | Không tính được: chạy thử không có nhóm đối chứng và không có event này trong dữ liệu |
| An toàn | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (nhóm tự đề xuất) | Số đơn có `so_tien_da_hoan` khác `so_tien_dung` chia tổng đơn được kiểm tra, từ event `audit_sample_checked` | Không tính được: dữ liệu không có kết quả kiểm tra mẫu. Chỉ số này bắt được lỗi ngầm như ca 5 và 17 |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent. Dữ liệu `logix_requests.csv` không có cột `trace_id`, nên các event này cần được ghi khi triển khai, không lấy được từ file hiện có.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| staff_review_decision | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| staff_rework_completed | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi vào sổ cái |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển cho nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, kiểm tra mẫu |

**Kiểm tra chéo:** mỗi chỉ số ở E1 và event dùng để tính:

- Chính: `ticket_closed` (đóng trong 24 giờ) và `ticket_reopened` (không mở lại trong 7 ngày).
- Dùng (bỏ qua gợi ý): `staff_review_decision` với quyết định `sua` hoặc `bo`, chia cho số lần `agent_suggestion_shown` được xem.
- An toàn (mở lại 7 ngày): `ticket_reopened` trong 7 ngày sau `ticket_closed`.
- Dùng (nhóm tự đề xuất): `agent_suggestion_shown` và `refund_request_created` với `arm`.
- An toàn (nhóm tự đề xuất): `audit_sample_checked`.

Chỉ số nào không tính được từ danh sách event thì chưa đo được. Hai chỉ số tự đề xuất hiện đều tính được từ event đã liệt kê.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1: +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated]; yếu tố nhạy nhất | Tỉ lệ `staff_rework_completed` / yêu cầu theo tuần > 7% trong phạm vi (đợt chạy thử: 48/982 = 4,9%) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất để tìm nguyên nhân gốc trước khi mở tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | B4: 11.743 đ = 0,98× mức 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca như dữ liệu [simulated]. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (≤ 4,8 phút với 15,3 phút làm lại) [simulated] | % yêu cầu có `staff_review_decision` còn > 50% ở cuối bước rollout 0,25; hoặc phút xem lại đo thật trung bình > 5 phút | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% (đợt chạy thử trong phạm vi: 27/128 = 21,1%) | Trưởng nhóm CSKH |
| Lương nhân viên tăng | B1: lương tăng 25% thì +23,1%, lên 5.506 đ [simulated]; yếu tố nhạy thứ ba | Đơn giá phút nhân viên trong kỳ điều chỉnh lương > 2.000 đ | Cập nhật `luong_phut` trong mô hình và tính lại tỉ số so với 12.000 đ trước khi quyết định mở rộng | Giám đốc vận hành |
| Khối lượng thấp hơn dự kiến | A4: chi phí cố định 40 triệu/tháng là +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa (tổng 5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần < 50% kế hoạch (kế hoạch đầy đủ: 33.750 việc/tháng) | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
