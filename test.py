from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Đường dẫn đến chromedriver
CHROMEDRIVER_PATH = r'C:\Users\Tung\Downloads\chromedriver-win64\chromedriver.exe'

# Hàm khởi tạo trình duyệt
def setup_driver():
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    return driver

# Hàm đăng nhập
def login(driver, username_input, password_input):
    # Truy cập trang đăng nhập
    driver.get("http://the-internet.herokuapp.com/login")
    # Tìm và thao tác với các phần tử
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # Xóa và nhập thông tin
    username.clear()
    password.clear()
    username.send_keys(username_input)
    password.send_keys(password_input)
    login_button.click()

# Hàm kiểm tra thông báo hiển thị
def check_message(driver, css_selector, expected_text):
    try:
        element = driver.find_element(By.CSS_SELECTOR, css_selector)
        assert expected_text in element.text, f"Expected '{expected_text}' but got '{element.text}'"
        print(f"PASS: '{expected_text}' xuất hiện chính xác.")
    except Exception as e:
        print(f"FAIL: Lỗi kiểm tra thông báo. {e}")

# Kiểm thử đăng nhập thành công
def test_login_success(driver):
    print("=== Kiểm thử: Đăng nhập thành công ===")
    login(driver, "tomsmith", "SuperSecretPassword!")
    check_message(driver, ".flash.success", "You logged into a secure area!")

# Kiểm thử đăng nhập thất bại
def test_login_failure(driver):
    print("=== Kiểm thử: Đăng nhập thất bại ===")
    login(driver, "wrongusername", "wrongpassword")
    check_message(driver, ".flash.error", "Your username is invalid!")

# Kiểm tra giao diện
def test_check_elements(driver):
    print("=== Kiểm thử: Kiểm tra giao diện ===")
    driver.get("http://the-internet.herokuapp.com/login")
    try:
        assert driver.find_element(By.ID, "username").is_displayed(), "Ô nhập tên đăng nhập không hiển thị"
        assert driver.find_element(By.ID, "password").is_displayed(), "Ô nhập mật khẩu không hiển thị"
        assert driver.find_element(By.CSS_SELECTOR, "button[type='submit']").is_displayed(), "Nút đăng nhập không hiển thị"
        print("PASS: Tất cả các thành phần giao diện hiển thị đúng.")
    except Exception as e:
        print(f"FAIL: Lỗi kiểm tra giao diện. {e}")

# Kiểm tra hiệu năng
def test_login_performance(driver):
    print("=== Kiểm thử: Hiệu năng đăng nhập ===")
    driver.get("http://the-internet.herokuapp.com/login")
    start_time = time.time()
    login(driver, "tomsmith", "SuperSecretPassword!")
    end_time = time.time()
    load_time = end_time - start_time
    print(f"Thời gian tải trang sau đăng nhập: {load_time:.2f} giây")
    assert load_time < 5, "Thời gian tải trang quá lâu!"

# Hàm chính
if __name__ == "__main__":
    # Khởi tạo trình duyệt
    driver = setup_driver()
    try:
        # Chạy các kịch bản kiểm thử
        test_check_elements(driver)
        test_login_success(driver)
        test_login_failure(driver)
        test_login_performance(driver)
    finally:
        # Đóng trình duyệt
        driver.quit()
        print("Đã đóng trình duyệt.")
