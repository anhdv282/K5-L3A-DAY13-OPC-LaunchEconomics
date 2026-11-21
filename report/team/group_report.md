# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: OPC
- Lớp: L3A
- Thành viên: xem `TEAM.md` (Đặng Việt Anh, Hà Huy Thái, Nguyễn Văn Vinh, Vũ Quang Minh)

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a duyệt kế hoạch pilot, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.

Cách tiếp cận: mọi con số do `src/lab13.py` của nhóm tính từ hai file CSV, người kiểm số tính tay lại một con số ở mỗi phần, rồi đối chiếu với slide chữa (lệch không quá 2%). Mỗi số tính từ cột `_simulated` ghi nhãn `simulated`. Người giữ hồ sơ điền `ho_so_launch_v0.md` dần theo từng checkpoint thay vì đợi đến cuối buổi.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí | Ba hàm A1 qua phép thử (1,20 · 1,25 · 1,25); `mo_hinh` cộng token, tool của mọi lần chạy kể cả lỗi, cộng phút xem lại và làm lại, chia cho số việc thành công; tách theo loại (A3); cộng chi phí cố định 40 triệu/tháng (A4) | `src/lab13.py`, [bang_chi_phi.md](bang_chi_phi.md) |
| B · Độ nhạy | Gọi lại `mo_hinh` cho 9 kịch bản, một cặp, giới hạn 1–3 lần chạy tính cả phần nhân viên làm thay, và kịch bản xem lại 100% | [bang_chi_phi.md](bang_chi_phi.md) |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca, so nhãn, viết lại định nghĩa, thống nhất nhãn, chọn 5 ca cho bảng khắc phục | [bang_loi.md](bang_loi.md) |
| D · Pilot | Tính năm câu D1 trước, chọn chia theo nhân viên 20 + 20, viết D2 và 4 luật dừng; kiểm bằng `yaml.safe_load` | [pilot_plan.yaml](pilot_plan.yaml) |
| E · Chỉ số, hồ sơ | Tính thử ba chỉ số, đặc tả 11 event có `trace_id`, 4 dòng rủi ro kinh tế; ghép A–E thành hồ sơ một trang | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

- Chi phí mỗi việc thành công: 4.472 đ, gấp 16,3 lần hoá đơn token chia số yêu cầu; giờ nhân viên chiếm 92,5% tổng chi phí [simulated].
- So với nhân viên tự làm (12.000 đ): cả hệ thống 0,49×; phạm vi noi_dia + hang_nang có cộng cố định 0,38×; quoc_te 1,88× nên loại khỏi pilot [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại +51,8% · tỉ lệ xem lại +40,7% · lương +23,1%; giá token chỉ +5,6% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ) [simulated].
- Bảng lỗi: đồng thuận độc lập 11/20 = 55%; sau khi viết lại định nghĩa, nhãn thống nhất phủ đủ năm loại; bảng khắc phục 5 ca.
- Pilot: chia 20 + 20 nhân viên, MDE 6 điểm (859/nhóm, m ≥ 299, DE 6,96), power khoảng 0,64 nếu tác động thật là 5 điểm; quyết định 05/01/2027.
- Chỉ số trong đợt chạy thử: chính 82,83% · dùng 27,12% · an toàn 4,25%.
- **Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang, bốn điều kiện có vai trò phụ trách và ngày kiểm tra.
- Kết quả duyệt chéo từ hội đồng: **30/30**, quyết định **Go có điều kiện**, khớp với đề xuất của nhóm.

## 5. Khó khăn và cách xử lý

- **Cài đặt:** có máy chưa có `pandas`, chạy `python lab13.py` báo `ModuleNotFoundError`; xử lý bằng venv và `pip install -r requirements.txt`. Terminal Windows lỗi khi in tiếng Việt; chạy `python -X utf8 lab13.py`.
- **Xung đột khi gộp bài:** `bang_chi_phi.md` từng xung đột merge và có số kiểm tay nháp lệch trên 2%; giữ số đã kiểm bằng `lab13.py`, số nháp chỉ để đối chiếu.
- **So sánh với 12.000 đ:** 4.472 / 12.000 = 0,37× là so sai vì chưa tính 222 yêu cầu nhân viên làm thay; nhóm dùng chi phí cả hệ thống (0,49×).
- **Đồng thuận gắn nhãn thấp (55% < 80%):** hai người lẫn ở bốn cặp loại (Hệ thống/Ngữ cảnh, Hệ thống/Ngầm, Giới hạn/Ngữ cảnh, Do người dùng/Giới hạn). Nhóm viết lại định nghĩa thành bốn câu hỏi theo thứ tự và ghi quy tắc cho từng ca không trùng; không sửa bộ nhãn độc lập.
- **Không cách chia nào đủ mẫu cho 5 điểm:** với 40 nhân viên, chia theo nhân viên tối đa 1.000 mẫu hiệu dụng < 1.251. Nhóm chấp nhận MDE 6 điểm và ghi rõ power 0,64 thay vì chia theo depot (chỉ 6 cụm).
- **Ngưỡng an toàn:** tỉ lệ mở lại hiện tại 4,25% (3,97% trong phạm vi), nên không đặt ngưỡng tuyệt đối 3%; dùng chênh so với đối chứng +2 điểm kèm trần 6%.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

| Thành viên | Vai | Phần chính |
| --- | --- | --- |
| Đặng Việt Anh | Người viết code (trước giải lao), sau đó kiểm số | A1–A4, B1–B4 trong `lab13.py`, `bang_chi_phi.md`, E1 trong `chi_so.md` |
| Hà Huy Thái | Người kiểm số, sau đó viết code | Kiểm tay A, B; D1 và E1 trong `lab13.py`; `pilot_plan.yaml`; đặc tả 11 event trong `chi_so.md` |
| Nguyễn Văn Vinh | Người gắn nhãn 2, kiêm giữ hồ sơ | Nhãn người 2; `ho_so_launch_v0.md` bảy mục và đề xuất; E2 rủi ro kinh tế |
| Vũ Quang Minh | Người gắn nhãn 1 | Nhãn người 1; so nhãn, định nghĩa viết lại, bảng khắc phục trong `bang_loi.md` |

## 7. Hạn chế và hướng cải thiện

- Hơn 90% chi phí dựa trên phút xem lại và làm lại giả lập; cần event `staff_review_decision` và `staff_rework_completed` đo phút thật ngay tuần đầu pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chỉ nói "chỉ số trong đợt chạy thử là 82,83%", chưa kết luận được tác động của trợ lý.
- Pilot chỉ đủ mẫu cho mức chênh 6 điểm; nếu tác động thật là 5 điểm, khả năng bỏ sót khoảng 36%. Cải thiện bằng cách kéo dài bước 0,50 hoặc mở rộng số nhân viên.
- Đồng thuận gắn nhãn lần đầu thấp; lần sau nên thống nhất bốn câu hỏi phân biệt trước khi gắn.
- Hai chỉ số tự đề xuất (mở bằng trợ lý, hoàn sai tiền qua kiểm tra mẫu) chưa tính được vì dữ liệu chưa có event tương ứng.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu statsmodels, `statsmodels.stats.power.NormalIndPower`.
- Đề bài và hướng dẫn Lab 13: `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`.
