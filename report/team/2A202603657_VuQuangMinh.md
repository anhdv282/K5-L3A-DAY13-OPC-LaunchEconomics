# Báo cáo cá nhân — Vũ Quang Minh (2A202603657)

## 1. Thông tin thành viên

- Họ tên: Vũ Quang Minh
- MSSV: 2A202603657
- Email: vuquangminh897@gmail.com
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề, theo dõi điều kiện "Xong khi" và mục "Tự kiểm tra" của từng checkpoint, báo nhóm mục nào còn thiếu.
- Gắn nhãn độc lập 20 ca lỗi ở CP3 (nhiệm vụ C), so nhãn với người gắn nhãn 2 và hoàn thiện `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

**Theo dõi checkpoint (CP1, CP2)**

- Đối chiếu CP1 với `CHECKPOINTS.md`: `python lab13.py` in "ĐẠT", số A2 khớp đáp án (4.373.585 đ, 978 việc thành công, 4.472 đ/việc [simulated]). Phát hiện lúc đó còn thiếu A3, A4 trong code, `bang_chi_phi.md` chưa điền và `TEAM.md` chưa chia vai, báo lại nhóm.
- Ghi chú lỗi in tiếng Việt trên terminal Windows (`UnicodeEncodeError`), cách chạy: `python -X utf8 lab13.py`.
- Soát tiến độ sau CP2: B1–B4 đủ, không có từ cấm (quy tắc 5) trong `report/team/`; nhắc người giữ hồ sơ cập nhật mục 2, 3.

**Gắn nhãn CP3**

- Gắn độc lập 20 ca, không trao đổi với người gắn nhãn 2. Bộ nhãn của tôi: Hệ thống 7 · Giới hạn hệ thống 7 · Do người dùng 2 · Ngữ cảnh 2 · Ngầm 2.

| Ca | Nhãn | Ca | Nhãn |
| --: | --- | --: | --- |
| 1 | Ngầm | 11 | Giới hạn hệ thống |
| 2 | Hệ thống | 12 | Hệ thống |
| 3 | Giới hạn hệ thống | 13 | Giới hạn hệ thống |
| 4 | Giới hạn hệ thống | 14 | Do người dùng |
| 5 | Ngầm | 15 | Hệ thống |
| 6 | Do người dùng | 16 | Hệ thống |
| 7 | Hệ thống | 17 | Hệ thống |
| 8 | Ngữ cảnh | 18 | Ngữ cảnh |
| 9 | Giới hạn hệ thống | 19 | Giới hạn hệ thống |
| 10 | Giới hạn hệ thống | 20 | Hệ thống |

- So với người gắn nhãn 2: trùng 11/20 = 55%, dưới ngưỡng 80%. Chín ca không trùng: 1, 3, 8, 9, 10, 12, 16, 17, 18.
- Cùng người gắn nhãn 2 thống nhất nhãn cho 9 ca; ca 1 chốt lại thành Do người dùng vì khách nhập thiếu số tài khoản và ngân hàng đã báo lỗi (sai đã lộ ra, không phải Ngầm).
- Hoàn thiện `bang_loi.md`: định nghĩa viết lại cho bốn cặp loại hay lẫn, một câu quy tắc cho mỗi ca không trùng, bảng khắc phục 5 ca đủ năm loại (ca 9, 7, 18, 13, 12), mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách. Hai cột nhãn độc lập giữ nguyên sau khi so.

## 4. Bằng chứng

- Commit `e70707b` (nhánh `feat/cp3-nhan-nguoi-1`): bộ nhãn độc lập của người gắn nhãn 1, đẩy lên trước khi so nhãn.
- Commit `89520d5` trên `main`: cột trùng, tỉ lệ đồng thuận 11/20 = 55%, nhãn thống nhất, định nghĩa viết lại, quy tắc 9 ca không trùng, bảng khắc phục 5 ca.
- File `report/team/bang_loi.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (trong VS Code).
- **Không dùng AI khi gắn nhãn độc lập:** 20 nhãn ở mục 3 do tôi tự gắn; AI chỉ giải thích năm loại lỗi theo bảng định nghĩa của đề và không gợi ý nhãn cho ca nào.
- **Dùng AI để:** đọc đề và tóm tắt vai trò; chạy `lab13.py` và đối chiếu số với hướng dẫn khi soát CP1, CP2; điền nhãn vào bảng, đếm số ca trùng; soạn nháp định nghĩa viết lại, câu quy tắc cho từng ca không trùng và bảng khắc phục 5 ca; commit và push.
- **Tự kiểm tra:** nhãn thống nhất do hai người gắn nhãn tự chốt, AI chỉ viết câu giải thích cho nhãn đã chốt. Ca 1 được đổi sau khi AI chỉ ra nhãn Ngầm mâu thuẫn với định nghĩa của đề; quyết định đổi là của nhóm. Tôi đọc lại từng câu quy tắc và từng dòng khắc phục với mô tả ca trong đề trước khi commit.

## 6. Tự đánh giá

- Gắn xong 20 ca đúng thời gian và giữ được tính độc lập, nhưng đồng thuận chỉ 55%: tôi hay gắn Giới hạn hệ thống cho ca mà trợ lý vẫn làm được (ca 3, 9, 10) và gắn Hệ thống cho ca chưa ai nhận ra lỗi (ca 12, 17).
- Bài học: gắn theo nguyên nhân gốc; hỏi "đầu vào của khách có sai không" trước, và "đã có ai thấy lỗi chưa" để tách Hệ thống với Ngầm.
- Ở CP1, CP2 tôi chủ yếu theo dõi và báo thiếu, chưa tự tay tính con số nào.
