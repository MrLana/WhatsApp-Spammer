import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_dependencies():
    try:
        import urllib3
        import six
        import selenium
        return True
    except ImportError as e:
        print(f"Error: {e}")
        print("Silakan jalankan perintah berikut di Termux:")
        print("pip install urllib3==1.26.15 six==1.16.0 selenium==4.10.0")
        return False

def whatsapp_spam():
    if not check_dependencies():
        sys.exit(1)
        
    try:
        # Setup Firefox
        from webdriver_manager.firefox import GeckoDriverManager
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        
        print("Buka WhatsApp Web di browser biasa dan scan QR code...")
        driver.get("https://web.whatsapp.com")
        
        # Tunggu hingga loading selesai
        wait = WebDriverWait(driver, 120)
        input_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        ))
        print("Login berhasil!")
        
        # Pilih chat terakhir
        last_chat = driver.find_element(By.XPATH, '(//div[contains(@class,"_2KKXC")])[last()]')
        last_chat.click()
        time.sleep(2)
        
        # Kirim pesan
        while True:
            msg = f"Pesan {random.randint(1000,9999)}"
            input_box.send_keys(msg + Keys.ENTER)
            print(f"Terkirim: {msg}")
            time.sleep(random.randint(5, 15))
            
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    whatsapp_spam()
