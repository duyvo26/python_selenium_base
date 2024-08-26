# File cấu hình chung cho ứng dụng

import os
from dotenv import load_dotenv

# Load các biến môi trường từ file .env
load_dotenv()


class Settings:
    # SETTING
    DIR_ROOT = os.path.dirname(os.path.abspath(".env"))

    DATA_CHROME = os.environ["DATA_CHROME"]
    
    # api
    API_KEY = os.environ["API_KEY"]


settings = Settings()
