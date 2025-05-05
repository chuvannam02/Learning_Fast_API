Cài đặt môi trường ảo (Virtual Environment):
Trước khi cài đặt các thư viện, tạo một môi trường ảo để không gây xung đột với các thư viện hệ thống.

## Tạo môi trường ảo cho back-end

#

python -m venv venv

Kích hoạt môi trường ảo:

# Kích hoạt môi trường ảo (macOS/Linux)

Trên macOS/Linux:
venv/bin/activate
source venv/bin/activate

Trên Windows:

# Kích hoạt môi trường ảo (Windows)

.\venv\Scripts\activate

Cài đặt các thư viện trong requirements.txt:
Sau khi kích hoạt môi trường ảo, sử dụng pip để cài đặt các thư viện.

# Cài đặt các thư viện Python trong tệp tin requirements.txt

pip install -r requirements.txt

Chạy dự án:
Tùy thuộc vào dự án của bạn, bạn sẽ cần chạy một tệp Python cụ thể. Ví dụ:

# Nếu là ứng dụng FastAPI, bạn có thể chạy bằng cách:

uvicorn main:app --reload
python -m uvicorn main:app --reload
# Nếu là một dự án khác, có thể chạy bằng:

python app.py

# Uvicorn là một ASGI server (Asynchronous Server Gateway Interface) cho Python, được thiết kế để chạy các ứng dụng web bất đồng bộ (asynchronous) như FastAPI, Starlette, hoặc bất kỳ framework Python nào hỗ trợ ASGI.

# Điểm mạnh của Uvicorn là:

# Hiệu suất cao: Uvicorn rất nhanh vì nó sử dụng asyncio, một thư viện bất đồng bộ trong Python, giúp xử lý nhiều yêu cầu đồng thời mà không bị chặn.

# Hỗ trợ WebSocket: Uvicorn hỗ trợ WebSocket và các giao thức bất đồng bộ khác, làm cho nó phù hợp cho các ứng dụng thời gian thực như chat hoặc ứng dụng yêu cầu dữ liệu liên tục.

# Tính đơn giản: Cài đặt và sử dụng rất dễ dàng, chỉ cần một lệnh đơn giản.

# Trong đó:

# main là tên của tệp Python chứa ứng dụng FastAPI (ví dụ: main.py).

# app là đối tượng FastAPI (hoặc đối tượng ASGI khác) được khai báo trong tệp main.py.

# --reload cho phép tự động tải lại khi bạn thay đổi mã nguồn (thường dùng trong môi trường phát triển).
