import os
from datetime import datetime
from app.config import settings


def kiem_tra_date_trong_file():
    try:
        file_path = (
            os.path.join(settings.DIR_ROOT, "utils", "shopee") + "fileDateSale.dat"
        )

        date = datetime.now().strftime("%Y-%m-%d")

        with open(file_path, "r") as file:
            lines = str(file.readlines())
            if date in lines:
                print(f"Ngày '{date}' đã tồn tại trong file {file_path}")
                return False
        print(f"Ngày '{date}' không tồn tại trong file {file_path}")
        return True
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return False


def create_directory(path):
    """
    Kiểm tra xem thư mục có tồn tại hay không.
    Nếu không tồn tại, tạo mới thư mục.

    Parameters:
        path (str): Đường dẫn đến thư mục cần kiểm tra/tạo.

    Returns:
        None
    """
    if not os.path.exists(path):
        # Nếu thư mục chưa tồn tại, tạo mới
        os.makedirs(path)
        print(f'Thư mục "{path}" đã được tạo.')
    else:
        print(f'Thư mục "{path}" đã tồn tại.')


def ghi_date_vao_file():
    try:
        file_path = (
            os.path.join(settings.DIR_ROOT, "utils", "shopee") + "fileDateSale.dat"
        )
        # Lấy ngày hiện tại
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Ghi ngày vào file
        with open(file_path, "a") as file:
            file.write(current_date + "\n")

        print(f"Đã ghi '{current_date}' vào file {file_path}")
    except Exception as e:
        print(f"Lỗi khi ghi vào file: {e}")


import requests


def send_mail(api_key, mail_to, mail_title, mail_content):
    url = "http://api.duyvo26.xyz/mail/send-mail/"  # Thay thế bằng URL thực của API
    data = {"mail_to": mail_to, "mail_title": mail_title, "mail_content": mail_content}
    headers = {"API-Key": f"{api_key}"}

    # Gửi request POST tới API
    response = requests.post(url, data=data, headers=headers)

    # Kiểm tra kết quả
    if response.status_code == 200:
        result = response.json()
        print(f"Successfully: {response.text}")
    else:
        print(f"Failed : {response.text}")
