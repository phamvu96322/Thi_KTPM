from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_success():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Mở trang đăng nhập
        driver.get("https://e-commerce-for-testing.onrender.com/")

        # Đợi form xuất hiện
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )

        # Nhập thông tin
        email = driver.find_element(By.NAME, 'email')
        password = driver.find_element(By.NAME, 'password')
        email.send_keys('user@example.com')
        password.send_keys('12345678')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Đợi phản hồi và kiểm tra alert lỗi hoặc token
        WebDriverWait(driver, 5).until(lambda d: d.current_url != "https://e-commerce-for-testing.onrender.com/signin" or d.find_elements(By.CLASS_NAME, 'chakra-alert'))
        if '/profile' in driver.current_url:
            print("✅ Đăng nhập thành công. Đã chuyển hướng tới trang profile.")
            assert True
        else:
            try:
                alert = driver.find_element(By.CLASS_NAME, 'chakra-alert')
                print("Thông báo lỗi trên giao diện:", alert.text)
            except Exception:
                print("Không tìm thấy alert lỗi trên giao diện.")
            token = driver.execute_script("return window.localStorage.getItem('token');")
            print("Token từ localStorage:", token)
            print("Current URL:", driver.current_url)
            print("Page title:", driver.title)
            page_source = driver.page_source
            print("Page source (rút gọn):", page_source[:1000], "...\n---END---")
            assert False, "Đăng nhập thất bại hoặc không chuyển hướng sang /profile"
    finally:
        driver.quit()