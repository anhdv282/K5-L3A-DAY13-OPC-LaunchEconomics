# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): OPC · L3A
- Nhóm được chấm: Nhom2Nguoi · L3A · https://github.com/ToyzZone/K5-L3A-DAY13-Nhom2Nguoi-LaunchEconomics (chấm trên commit `9f343cb`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện khớp số của nhóm: cả hệ thống 0,49×, phạm vi có cố định 0,38× [simulated]; so đúng 5.865 đ/yêu cầu, không dùng 0,37×. Nêu đủ hai con số bất lợi kèm cách xử lý: power ~0,64 ở mức 5 điểm (điều kiện ký chấp nhận MDE 6 điểm) và xem lại 100% lên 0,98–1,03× (điều kiện giảm xem lại theo bậc). Điểm yếu nhỏ: điều kiện ký MDE đặt "trước ngày quyết định 05/01/2027" thay vì trước ngày bắt đầu, và các điều kiện chưa có ngày kiểm tra cụ thể. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Nhãn simulated ở mọi số chi phí trong hồ sơ, bảng chi phí và E2 (4.472 đ, 6.787 đ, 0,98–1,03×, +1.185/+2.370 đ). Phạm vi thu hẹp về noi_dia + hang_nang có lý do bằng số: loại quoc_te 1,88×, thành công 27,3%; loại doi_tac 0,85× và điều khoản riêng. Không có từ cấm, không viết "trợ lý đã nâng chỉ số". |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia 20 + 20 nhân viên, ngẫu nhiên phân tầng theo depot, đối chứng chạy cùng tuần; D1 đúng (1.251 · 3.103/42 người · 1.000 · 300 · m ≥ 299, DE 6,96) và ghi rõ đánh đổi MDE 6 điểm. Bước 0,50 kéo dài ≥ 10 ngày, tính theo ~31 yêu cầu trong phạm vi/người/ngày. 3 luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng (+2 điểm/6%, 8.000 đ, 40%), thời hạn và vai trò tắt. Điểm yếu: luật 1 gộp "≥ 1 ca hoàn trùng" với "TRONG 3 ngày liên tiếp", nên ca hoàn trùng không bị tắt ngay; luật lệch +2 điểm không có cỡ mẫu tối thiểu ở bước 4 người. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ đủ bảy mục, mọi số giả lập có nhãn, đề xuất nêu cả hai con số bất lợi (power 0,64; xem lại 100% lên 0,98–1,03× [simulated]) và gắn mỗi điều kiện với một vai trò. Hội đồng thêm hai điều kiện: tách luật hoàn trùng thành luật riêng, tắt ngay trong 30 phút khi có 1 ca; và Giám đốc vận hành ký chấp nhận MDE 6 điểm trước ngày bắt đầu pilot, không phải trước ngày quyết định.

**Một câu hỏi cho đội trình:** Luật dừng 1 ghi "≥ 1 ca hoàn trùng TRONG 3 ngày liênđa tiếp": nếu ngày đầu có 1 ca hoàn trùng, nhóm tắt trợ lý ngay hay đợi đủ 3 ngày? Và ở bước 4 người, mức lệch 2 điểm so với đối chứng có đủ tin để tắt pilot không?

**Câu trả lời của đội trình (ghi lại tại buổi):**

- Hoàn trùng thì tắt ngay, không đợi 3 ngày: hoàn trùng là mất tiền thật, ngưỡng 0 ca. Đối soát sổ cái chạy mỗi giờ; phát hiện thì Giám đốc vận hành tắt trong 30 phút. Đội trình thừa nhận câu chữ "TRONG 3 ngày" đang áp chung cho cả ba vế là viết sai, cần tách hoàn trùng thành luật riêng.
- Ở bước 4 người, chênh 2 điểm chưa đủ tin để tắt: theo mô phỏng của đội trình, dù trợ lý không gây hại, luật vẫn tắt oan khoảng 20% số lần; muốn tắt oan 5% thì ngưỡng phải là 3,5 điểm. Vì vậy ở bước 4 người, chênh 2 điểm chỉ dùng để dừng mở rộng và đọc lại trace các ca mở lại; chỉ tắt hẳn khi chênh ≥ 3,5 điểm hoặc vượt trần 6%. Đến bước 20 người, ngưỡng 2 điểm mới đủ tin (tắt oan khoảng 2%).

**Nhận xét của hội đồng sau câu trả lời:** câu trả lời xử lý đúng cả hai điểm yếu, có số và có người tắt; giữ 30/30 và quyết định Go có điều kiện, với điều kiện đội trình sửa `pilot_plan.yaml` theo đúng hai ý trên (tách luật hoàn trùng; ngưỡng tắt theo bước rollout).
