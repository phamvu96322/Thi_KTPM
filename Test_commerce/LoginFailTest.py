from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginFailTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # đợi tối đa 10s

    def test_login_with_wrong_password(self):
        driver = self.driver
        driver.get("https://e-commerce-for-testing.onrender.com/")

        # Đợi nút Login dạng button có text 'Login' xuất hiện rồi bấm
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
        )
        login_button.click()

        # Đợi form login hiện ra
        email_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys("trongvup3@gmail.com")

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("12345654")

        password_input.send_keys(Keys.RETURN)

        # Đợi thông báo lỗi xuất hiện
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Email hoặc mật khẩu không đúng')]"))
        )

        self.assertIn("Email hoặc mật khẩu không đúng", error_element.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
