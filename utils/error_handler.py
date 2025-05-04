from fastapi import FastAPI, Request
# Request là một lớp trong FastAPI để đại diện cho yêu cầu HTTP
# FastAPI là một framework để xây dựng API nhanh chóng và hiệu quả
from fastapi.responses import JSONResponse
# JSONResponse là một lớp trong FastAPI để trả về phản hồi JSON
from fastapi.exceptions import RequestValidationError
# RequestValidationError là một lớp trong FastAPI để xử lý lỗi xác thực yêu cầu

# Định nghĩa một hàm để thêm trình xử lý ngoại lệ tùy chỉnh cho FastAPI
def add_custom_exception_handler(app: FastAPI):
    # Định nghĩa một trình xử lý ngoại lệ cho RequestValidationError
    # Trình xử lý này sẽ được gọi khi có lỗi xác thực trong yêu cầu
    # @app.exception_handler là một decorator để đăng ký trình xử lý ngoại lệ
    # decorator này sẽ tự động gọi hàm validation_exception_handler khi có lỗi xác thực
    # Hàm này nhận vào một yêu cầu và một ngoại lệ
    # và trả về một phản hồi JSON với mã trạng thái 422 (Unprocessable Entity)
    # và một danh sách các lỗi xác thực
    # errors là một danh sách các lỗi xác thực được lấy từ ngoại lệ
    # mỗi lỗi được định dạng thành một từ điển với các trường "field" và "message"
    # "field" là tên trường trong yêu cầu và "message" là thông báo lỗi
    # "loc" là vị trí của lỗi trong yêu cầu
    # "msg" là thông báo lỗi
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        # loc là vị trí của lỗi trong yêu cầu = location
        # msg là thông báo lỗi = message
        errors = [
            {
                "field": ".".join(str(loc) for loc in err["loc"]),
                "message": err["msg"]
            }
            for err in exc.errors()
        ]
        return JSONResponse(status_code=422, content={"errors": errors})