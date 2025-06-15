import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

def whatsapp_spam():
    driver = None  # Inisialisasi variabel driver
    try:
        # Setup Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")

        # Inisialisasi WebDriver (versi baru)
        service = webdriver.FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)

        # Buka WhatsApp Web
        print("Membuka WhatsApp Web...")
        driver.get("https://web.whatsapp.com")
        
        # Tunggu scan QR code
        print("Silakan scan QR code di browser biasa...")
        wait = WebDriverWait(driver, 120)
        input_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        ))
        print("Berhasil login!")

        # Pilih chat terakhir
        last_chat = driver.find_element(By.XPATH, '(//div[contains(@class,"_2KKXC")])[last()]')
        last_chat.click()
        time.sleep(2)

        # Mulai mengirim pesan
        print("Memulai pengiriman pesan...")
        while True:
            msg = f"Pesan otomatis {random.randint(1000,9999)}"
            input_box.send_keys(msg + Keys.ENTER)
            print(f"Pesan terkirim: {msg}")
            time.sleep(random.randint(5, 15))

    except Exception as e:
        print(f"Terjadi error: {str(e)}")
    finally:
        if driver is not None:  # Pastikan driver ada sebelum diquit
            driver.quit()
            print("WebDriver ditutup")

if __name__ == "__main__":
    whatsapp_spam()
