from Test_commerce.base import BaseTest
from Test_commerce.dangnhap import EXISTING_EMAIL, EXISTING_PASSWORD


class TestLogin(BaseTest):
    def test_login_user(self):
        print(f"--- Running: {self._testMethodName} ---")
        print(f"👉 Đăng nhập với: {EXISTING_EMAIL} / {EXISTING_PASSWORD}")

        # 1. Vào trang chủ
        self.navigate_to_home()

        # 2. Nhấn nút "Login"
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))) # type: ignore
        login_button.click()

        # 3. Chờ trang đăng nhập
        self.wait.until(EC.url_contains("/signin")) # type: ignore
        self.wait.until(EC.presence_of_element_located((By.NAME, "email"))) # type: ignore

        # 4. Nhập thông tin đăng nhập
        email_input = self.driver.find_element(By.NAME, "email") # type: ignore
        password_input = self.driver.find_element(By.NAME, "password") # type: ignore
        email_input.clear()
        password_input.clear()
        email_input.send_keys(EXISTING_EMAIL)
        password_input.send_keys(EXISTING_PASSWORD)

        # 5. Nhấn "Sign In"
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign In']"))) # type: ignore
        sign_in_button.click()

        # 6. Kiểm tra đăng nhập thành công
        self.assert_user_logged_in()
        print("✅ Đăng nhập thành công.")

        # 7. Quay lại trang chủ
        self.navigate_to_home()
        print("✅ Đã quay lại trang chủ.")

        # --- Phần thêm giỏ hàng ---
        print("🛒 Thêm sản phẩm vào giỏ hàng...")
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]")) # type: ignore
        )
        add_to_cart_button.click()
        print("✅ Đã thêm sản phẩm.")

        # 8. Nhấn vào biểu tượng giỏ hàng (basket)
        basket_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/basket']")) # type: ignore
        )
        basket_button.click()
        self.wait.until(EC.url_contains("/basket")) # type: ignore
        print("🧺 Đã mở trang giỏ hàng.")

        # 9. Nhấn nút "Remove" (Xoá sản phẩm)
        remove_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Remove')]")) # type: ignore
        )
        remove_button.click()
        print("❌ Đã xoá sản phẩm khỏi giỏ hàng.")

        # ✅ Kiểm tra giỏ hàng trống
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Your basket is empty')]")) # type: ignore
        )
        print("✅ Giỏ hàng trống sau khi xoá.")

