import random
from base import BaseTest

class TestLogin(BaseTest):
    def test_login_user(self):
        email = f"longdaubui{random.randint(1000,9999)}@gmail.com"
        password = "123213213"
        print(f"--- Running: {self._testMethodName} ---")
        print(f"👉 Đăng ký tài khoản trước khi login: {email} / {password}")

        # Đăng ký trước
        self.register_new_user(email, password)

        # Đăng nhập
        self.login_user(email, password)
        print("✅ Đăng nhập thành công.")

        # Đăng xuất
        self.logout_user()
        print("✅ Đăng xuất thành công.")

if __name__ == "__main__":
    import unittest
    unittest.main()
