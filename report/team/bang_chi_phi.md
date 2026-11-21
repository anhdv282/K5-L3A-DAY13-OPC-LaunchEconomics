# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

`python -X utf8 lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` (bật UTF-8 nếu terminal lỗi khi in tiếng Việt).

Kiểm tay với p = 0,8: (1 − 0,2²) / 0,8 = 1,20; 1 / 0,8 = 1,25; [(1 − 0,2³) / 0,8] / (1 − 0,2³) = 1,25.

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp 16,3 lần "hoá đơn chia số yêu cầu" (4.472 ÷ 274,7) [simulated].
- Khoản lớn nhất là làm lại, 51,8% tổng chi phí [simulated]; tiếp theo là xem lại, 40,7% [simulated]. Giờ nhân viên chiếm 92,5% tổng chi phí [simulated].
- Khi so với nhân viên tự làm, cộng 1.200 − 978 = 222 yêu cầu không thành công: (4.373.585,132 + 222 × 12.000) / 1.200 ≈ 5.865 đ/yêu cầu, bằng 0,49× mức 12.000 đ [simulated], chưa cộng cố định. Không dùng riêng 4.472 / 12.000 = 0,37× để kết luận mức tiết kiệm của cả hệ thống.

Kiểm tay từ CSV: xem lại 890 phút × 2.000 = 1.780.000 đ; làm lại 1.132 phút × 2.000 = 2.264.000 đ [simulated]. Tổng (245.585,132 + 84.000 + 1.780.000 + 2.264.000) / 978 ≈ 4.472 đ/việc [simulated]. Cộng mọi lần chạy kể cả lỗi; 93.804 đ chạy lại đã nằm trong token + tool, không cộng thêm; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 [simulated] | 0,85× [simulated] |

- Loại không đáng để trợ lý xử lý: `quoc_te` (22.515 đ/việc = 1,88× mức 12.000 đ [simulated], thành công 27,3%). Chạy lại giúp ít: tỉ lệ `status == 'ok'` là 45/150 = 30,0% (lần 1), 12/105 = 11,4% (lần 2), 2/93 = 2,2% (lần 3); trung bình 2,32 lần chạy/yêu cầu vẫn chỉ đạt 27,3% thành công.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Chi phí cố định không đổi kết luận tại 45.000 và 22.500 yêu cầu/tháng: lần lượt 4.599 đ (0,38×) và 5.784 đ (0,48×) [simulated]. Giả định cơ cấu và tỉ lệ thành công giữ nguyên; đây là chi phí mỗi việc trợ lý làm thành công, chưa gồm phần nhân viên làm thay.

Kiểm tay A4: phạm vi có 900 việc thành công; quy mô đầy đủ 45.000 × 900 / 1.200 = 33.750 việc/tháng. Một nửa khối lượng: 22.500 × 900 / 1.200 = 16.875; cố định 40.000.000 / 16.875 ≈ 2.370 đ/việc; cộng chi phí biến đổi 3.072.513,274 / 900 ≈ 3.414 đ/việc, được 5.784 đ/việc [simulated].

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 [simulated] | −8,1% |

Kiểm tra trên số chưa làm tròn: "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi"; phần trăm hiển thị làm tròn một chữ số (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9) [simulated]. Ví dụ xem lại gấp đôi: (4.373.585,132 + 1.780.000) / 978 ≈ 6.292 đ/việc, tăng 40,7% [simulated].

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: (4.373.585,132 + 245.585,132 + 1.780.000) / 978 ≈ 6.543 đ, tăng 46,3% [simulated]; bằng tổng hai tác động riêng (5,6% + 40,7%) [simulated] vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%) [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 [simulated] | 319 | 7.449.781 [simulated] | 4.111 [simulated] |
| 2 lần | 4.093.220 [simulated] | 234 | 6.901.220 [simulated] | 4.237 [simulated] |
| 3 lần | 4.373.585 [simulated] | 222 | 7.037.585 [simulated] | 4.472 [simulated] |

- Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 × số yêu cầu không thành công. Giới hạn 2 lần rẻ nhất: 4.093.220 + 234 × 12.000 = 6.901.220 đ [simulated]; giới hạn 1 lần có chi phí mỗi việc thấp nhất (4.111 đ [simulated]) nhưng chuyển thêm 319 − 234 = 85 việc sang nhân viên so với 2 lần.

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% (`noi_dia` + `hang_nang`): (224.513,274 + 948 × 5 × 2.000 + 48 × 9 × 2.000) / 900 ≈ 11.743 đ = 0,98× mức 12.000 đ [simulated]. Thay 9 bằng trung bình chính xác 15,2973 phút/ca từ cột `_simulated` trên toàn bộ ca làm lại: 12.414,50 đ, làm tròn 12.415 đ = 1,03× [simulated]; hướng dẫn ghi xấp xỉ 12.414 đ, lệch dưới 0,01%.
- Tiền xem lại chiếm khoảng 90% chi phí trong kịch bản 9 phút làm lại [simulated]; pilot cần tìm tỉ lệ xem lại thấp nhất vẫn an toàn. Thời gian xem lại hoà vốn tối đa khoảng 5,1 phút với 9 phút làm lại hoặc 4,8 phút với 15,3 phút làm lại [simulated]; chưa cộng chi phí cố định.

## Kiểm số tính tay

Phần dưới là bản nháp từ nhánh gộp, giữ để đối chiếu; chưa có xác nhận người tính và cách tính. Cả 5 dòng lệch trên 2% so với code, không dùng thay kết quả A2 đã kiểm tra.

- Người tính: [họ tên], ngày [dd/mm]
- Cách lập bản nháp: cần người tính xác nhận có dùng bảng tính và thời điểm tính.
- Công thức: [dán các công thức ở bảng trên, hoặc mô tả ngắn]

| Khoản | Tính tay (đ), bản nháp | Từ code (đ) | Lệch so với code |
| --- | ---: | ---: | ---: |
| Token | 240.000 | 245.585 | 2,27% |
| Tool | 82.000 | 84.000 | 2,38% |
| Làm lại [simulated] | 2.200.000 | 2.264.000 | 2,83% [simulated] |
| Tổng [simulated] | 4.250.000 | 4.373.585 | 2,83% [simulated] |
| Chi phí mỗi việc thành công [simulated] | 4.350 | 4.472 | 2,73% [simulated] |

Lệch = trị tuyệt đối (bản nháp − số từ code) / số từ code × 100%; chưa có công thức của bản nháp để xác định nguyên nhân sai.
