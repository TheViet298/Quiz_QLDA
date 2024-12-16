

# Quiz_QLDA
---
**Quiz_QLDA** là web đơn giản nhằm giúp sinh viên luyện trắc nghiệm môn quản lý dự án  PTIT.Có thể truy cập tại:

- **Đường dẫn đã deploy**: [https://clinquant-cheesecake-4df723.netlify.app/](https://clinquant-cheesecake-4df723.netlify.app/)
- 
## Hướng dẫn sử dụng

1. **Thiết lập server**:
   - Đảm bảo server của bạn đã cài đặt Git, Nginx (hoặc Apache) và các yêu cầu cần thiết khác.
   - Clone repository vào server của bạn:
     ```bash
     git clone https://github.com/TheViet298/Quiz_QLDA.git /path/to/your/repository
     cd /path/to/your/repository
     ```

2. **Cấu hình server web (Nginx hoặc Apache)**:
   - Cấu hình file cấu hình Nginx (hoặc Apache) để phục vụ ứng dụng của bạn:
     ```nginx
     server {
         listen 80;
         server_name your_domain_or_IP;

         location / {
             root /path/to/your/repository;
             index index.html;
         }
     }
     ```
   - Sau đó, reload Nginx hoặc restart Apache để áp dụng thay đổi:
     ```bash
     sudo systemctl reload nginx
     ```

3. **Khởi động lại ứng dụng**:
   - Nếu ứng dụng của bạn cần khởi động lại sau khi cập nhật:
     ```bash
     sudo systemctl restart your_application_service
     ```

4. **Kiểm tra**:
   - Truy cập ứng dụng từ trình duyệt với đường dẫn của server:
     ```
     http://your_domain_or_IP
     ```
   - Đảm bảo mọi tính năng của ứng dụng hoạt động bình thường.

## Tài liệu tham khảo và liên hệ
- **Repository**: [GitHub - Quiz_QLDA](https://github.com/TheViet298/Quiz_QLDA)
- **Liên hệ**: Ngô Thế Việt (Email: ngotheviet2003@gmail.com, LinkedIn: [LinkedIn - Ngô Thế Việt](https://www.linkedin.com/in/th%E1%BA%BF-vi%E1%BB%87t-a35776307/?trk=opento_sprofile_details))

---
