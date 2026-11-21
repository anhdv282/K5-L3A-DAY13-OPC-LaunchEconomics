# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại (`duoc_xem_lai` bằng 1) | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Tỉ lệ yêu cầu của nhóm can thiệp được mở bằng trợ lý (nhóm tự đề xuất) | Đếm `request_id` khác nhau có `agent_opened`, chia tổng `request_id` của nhóm can thiệp từ `refund_request_created` với `arm = intervention` | Không tính được từ CSV: thiếu event mở trợ lý và trường phân nhóm `arm` |
| An toàn | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (nhóm tự đề xuất) | Số đơn có `so_tien_da_hoan` khác `so_tien_dung` chia tổng đơn được kiểm tra, từ event `audit_sample_checked` | Không tính được: dữ liệu không có kết quả kiểm tra mẫu. Chỉ số này bắt được lỗi ngầm như ca 5 và 17 |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng.

Kiểm số E1: 994/1.200 = 82,83%; (41 sửa + 7 bỏ)/177 yêu cầu được xem lại = 27,12%; 51/1.200 = 4,25%. Chỉ số mở lại là tín hiệu thay thế để theo dõi lỗi lọt; cần kiểm tra mẫu để phát hiện sai tiền không bị khách mở lại.

## Danh sách event

Đặc tả 11 event cho pilot, chưa phải log đã triển khai. Mọi event có `event_id`, `event_time` kèm múi giờ, `request_id`, `trace_id`; cấp và truyền `trace_id` từ lúc nhận yêu cầu, phân biệt các lần chạy bằng `run_id` và `attempt`. Với CSV hiện tại, nối yêu cầu với trace qua `request_id` trong `logix_runs.csv`; không coi các trace khác nhau của cùng yêu cầu là các yêu cầu mới.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, created_at, loai, so_tien, depot, staff_id, arm, trace_id | Khi khách gửi yêu cầu; ghi phân nhóm khi giao nhân viên |
| agent_opened | Giao diện nhân viên | request_id, staff_id, arm, trace_id | Khi nhân viên mở trợ lý cho yêu cầu |
| agent_run_completed | Agent | request_id, run_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện nhân viên | request_id, suggestion_id, staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| staff_review_decision | Nhân viên | request_id, review_id, quyet_dinh (giu/sua/bo), is_final, phut_xem_lai (đo thật), trace_id | Khi hoàn tất xem lại; một quyết định cuối cho mỗi yêu cầu |
| staff_rework_completed | Nhân viên | request_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | request_id, idempotency_key, so_tien, ket_qua, trace_id | Khi ghi vào sổ cái |
| handoff_to_staff | Agent | request_id, reason, tom_tat, trace_id | Khi chuyển cho nhân viên |
| ticket_closed | Hệ thống ticket | request_id, closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại |
| audit_sample_checked | Kế toán | request_id, sample_id, policy_version, so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, kiểm tra mẫu |

**Kiểm tra chéo:** mỗi chỉ số ở E1 và event dùng để tính:

- Chính: `refund_request_created` cho tổng yêu cầu và `created_at`; `ticket_closed` để kiểm `closed_at - created_at <= 24 giờ`; `ticket_reopened` để loại yêu cầu mở lại trong 7 ngày sau đóng.
- Dùng (bỏ qua gợi ý): số `request_id` có quyết định cuối `sua` hoặc `bo` trong `staff_review_decision`, chia tổng `request_id` có quyết định xem lại cuối; không lấy số gợi ý hiển thị làm mẫu số.
- An toàn (mở lại 7 ngày): số `request_id` có `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia tổng yêu cầu đủ cửa sổ theo dõi từ `refund_request_created`.
- Dùng (nhóm tự đề xuất): số yêu cầu có `agent_opened` trong nhóm can thiệp chia tổng yêu cầu nhóm đó từ `refund_request_created` với `arm`.
- An toàn (nhóm tự đề xuất): số yêu cầu sai tiền chia số yêu cầu kiểm tra trong `audit_sample_checked`.

Khử event gửi trùng bằng `event_id`, đếm theo `request_id`; dùng cùng cohort và chỉ chốt kết quả sau đủ cửa sổ theo dõi 7 ngày theo pilot plan. Không xem thiếu event mở lại ở yêu cầu chưa đủ thời gian theo dõi là bằng chứng an toàn.

Hai chỉ số tự đề xuất đo được khi bật đủ event trên; hiện chưa có dữ liệu để tính thử. `agent_run_completed`, `staff_review_decision`, `staff_rework_completed` cung cấp token, tool và phút đo thật để cập nhật chi phí trong pilot.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Làm lại tăng gấp đôi | Từ 4.472 lên 6.787 đ/việc, +51,8% [simulated], theo B1 | Tỉ lệ làm lại trong phạm vi > 7%/tuần; nền 48/982 = 4,9% | Dừng mở rộng, rà 20 trace làm lại; nếu phải đổi phạm vi/cách xử lý thì dừng đợt đánh giá theo pilot plan | PM trợ lý hoàn phí |
| Xem lại 100% kéo dài | B4: 11.743 đ = 0,98× mức 12.000 đ; nếu làm lại khoảng 15,3 phút thì 12.415 đ = 1,03× [simulated] | Tỉ lệ yêu cầu được xem lại còn > 50% cuối bước rollout 0,25 | Chỉ giảm xem lại theo bậc khi sửa + bỏ < 15% và kiểm tra mẫu không vi phạm luật an toàn; chưa đạt thì giữ kiểm soát, không tăng rollout | Trưởng nhóm CSKH |
| Lương nhân viên tăng | B1: lương tăng 25% thì +23,1%, lên 5.506 đ/việc [simulated]; yếu tố nhạy thứ ba | Đơn giá phút nhân viên trong kỳ điều chỉnh lương > 2.000 đ | Cập nhật `luong_phut` trong mô hình, tính lại tỉ số so với 12.000 đ trước khi mở rộng | Giám đốc vận hành |
| Khối lượng thấp hơn kế hoạch | A4: cố định tăng từ 1.185 lên 2.370 đ/việc khi lượng yêu cầu giảm nửa; tổng tăng 4.599 lên 5.784 đ/việc [simulated] | Số việc thành công/tuần dưới 50% kế hoạch trong 2 tuần liên tiếp | Dừng mở rộng, tính lại phân bổ 40 triệu đ/tháng và lịch đủ mẫu; không kết luận hiệu quả khi thiếu 299 yêu cầu/người | Giám đốc vận hành |
