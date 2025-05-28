from base import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Tài khoản đã đăng ký sẵn
EXISTING_EMAIL = "trongvup3@gmail.com"
EXISTING_PASSWORD = "12345678"

class TestLogin(BaseTest):
    def test_login_user(self):
        print(f"--- Running: {self._testMethodName} ---")
        print(f"👉 Đăng nhập với: {EXISTING_EMAIL} / {EXISTING_PASSWORD}")

        # Vào trang chủ
        self.navigate_to_home()

        # Nhấn nút "Login"
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
        login_button.click()

        # Đợi trang đăng nhập hiện ra
        self.wait.until(EC.url_contains("/signin"))
        self.wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Điền thông tin đăng nhập
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        email_input.clear()
        password_input.clear()
        email_input.send_keys(EXISTING_EMAIL)
        password_input.send_keys(EXISTING_PASSWORD)

        # Nhấn nút "Sign In"
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign In']")))
        sign_in_button.click()

        # Xác nhận đăng nhập thành công
        self.assert_user_logged_in()
        print("✅ Đăng nhập thành công.")

        # 👉 Quay lại trang chủ sau khi đăng nhập
        self.navigate_to_home()
        print("✅ Đã quay lại trang chủ sau đăng nhập.")

if __name__ == "__main__":
    import unittest
    unittest.main()
