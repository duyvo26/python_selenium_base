from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from app.config import settings
from app.utils import *  # noqa: F403
import os
import zipfile

class ChromeDriver:
    def __init__(self) -> None:
        # Đường dẫn đến chromedriver.exe
        self.chromedriver_path = os.path.join(
            settings.DIR_ROOT, "utils", "chromedriver-win64/chromedriver.exe"
        )

        # Đường dẫn đến GoogleChromePortable.exe
        self.chrome_portable_path = os.path.join(
            settings.DIR_ROOT, "utils", "chrome-win64/chrome.exe"
        )
        
        

    def get_driver(self):
        # Cấu hình tùy chọn cho Chrome
        chrome_options = Options()

        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
        )

        path_data_chrome = os.path.join(settings.DIR_ROOT, "utils", settings.DATA_CHROME)
        create_directory(path_data_chrome)  # noqa: F405
        chrome_options.add_argument(f"--user-data-dir={path_data_chrome}")

        chrome_options.binary_location = self.chrome_portable_path

        # Thêm extension proxy
        proxy_extension = self._create_proxy_extension("XX.XX.XX.XX", 000, "XXX", "XXX")
        chrome_options.add_extension(proxy_extension)
        
        
        service = Service(self.chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver



    def _create_proxy_extension(self, proxy_host, proxy_port, proxy_user, proxy_pass):
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            }
        }
        """

        background_js = f"""
        var config = {{
                mode: "fixed_servers",
                rules: {{
                singleProxy: {{
                    scheme: "http",
                    host: "{proxy_host}",
                    port: parseInt({proxy_port})
                }},
                bypassList: ["localhost"]
                }}
            }};
        chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

        chrome.webRequest.onAuthRequired.addListener(
            function(details) {{
                return {{
                    authCredentials: {{
                        username: "{proxy_user}",
                        password: "{proxy_pass}"
                    }}
                }};
            }},
            {{urls: ["<all_urls>"]}},
            ['blocking']
        );
        """

        pluginfile = os.path.join(settings.DIR_ROOT, "utils", "proxy_auth_plugin.zip")
        with zipfile.ZipFile(pluginfile, "w") as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        return pluginfile
