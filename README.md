# Selenium Automated Testing for Web Login Functionality

This project demonstrates how to automate the testing of login functionality in a web application using **Selenium WebDriver**, covering both positive and negative scenarios, UI checks, and performance testing.

---

## 📜 **Project Overview**

The project includes the following test cases:

1. **Positive Login Test**: Valid username and password.
2. **Negative Login Test**: Invalid username or password.
3. **UI Verification**: Ensures that all essential elements (username field, password field, login button) are displayed.
4. **Performance Check**: Measures the time taken to load the secure page after login.

This project uses **Python** with **Selenium WebDriver** for browser automation.

---

## 📂 **Project Structure**

The project structure is as follows:

```
.
├── selenium_login_test
│   ├── test.py                 # Main script containing the test cases
│   ├── requirements.txt        # Python dependencies (e.g., selenium==4.x.x)
│   ├── chromedriver.exe        # Chrome WebDriver (ensure it's compatible with your browser version)
└── README.md                   # Project documentation
```

---

## 🚀 **Features**

### 1. **Positive Login Test**

Tests successful login with valid credentials.

```python
login(driver, "tomsmith", "SuperSecretPassword!")
check_message(driver, ".flash.success", "You logged into a secure area!")
```

### 2. **Negative Login Test**

Tests unsuccessful login with invalid credentials.

```python
login(driver, "wrongusername", "wrongpassword")
check_message(driver, ".flash.error", "Your username is invalid!")
```

### 3. **UI Verification**

Ensures that all essential elements are displayed on the login page.

```python
assert driver.find_element(By.ID, "username").is_displayed()
assert driver.find_element(By.ID, "password").is_displayed()
assert driver.find_element(By.CSS_SELECTOR, "button[type='submit']").is_displayed()
```

### 4. **Performance Check**

Measures the time taken to load the secure page after login.

```python
start_time = time.time()
login(driver, "tomsmith", "SuperSecretPassword!")
end_time = time.time()
assert (end_time - start_time) < 5, "Page load took too long!"
```

---

## ✅ **Test Implementation**

All tests are modularized and organized into reusable functions for clarity and maintainability.

### Sample Test Function

```python
def test_login_success(driver):
    login(driver, "tomsmith", "SuperSecretPassword!")
    check_message(driver, ".flash.success", "You logged into a secure area!")
```

---

## 📊 **Test Results**

### Expected Outcomes:
- **Positive login**: A success message is displayed, and the user is navigated to the secure area.
- **Negative login**: An error message is shown for invalid credentials.
- **UI components**: All essential elements (username field, password field, and login button) are displayed correctly.
- **Performance**: The page loads within 5 seconds.

### Example Output

```bash
=== Test: UI Verification ===
PASS: All UI elements are displayed correctly.

=== Test: Positive Login ===
PASS: Successfully logged into the secure area.

=== Test: Negative Login ===
PASS: Error message displayed for invalid credentials.

=== Test: Login Performance ===
PASS: Page loaded within acceptable time (2.5 seconds).
```

---

## 🛠 **Setup and Execution**

### Prerequisites
- **Python 3.8+**
- **Selenium** library
- **Chrome WebDriver** compatible with your browser version

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/selenium-login-test.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update the path to `chromedriver.exe` in the script:
   ```python
   CHROMEDRIVER_PATH = r'path\to\your\chromedriver.exe'
   ```
4. Run the tests:
   ```bash
   python test.py
   ```

---

## ⚙️ **Testing Scenarios**

### Test Cases

| Test Case             | Input                                 | Expected Result                             |
|-----------------------|---------------------------------------|---------------------------------------------|
| **Positive Login**    | Username: `tomsmith`, Password: `SuperSecretPassword!` | Success message and secure page load.       |
| **Negative Login**    | Invalid username or password         | Error message for invalid credentials.      |
| **UI Verification**   | -                                     | All elements (username, password, button) are displayed correctly. |
| **Performance Test**  | Valid credentials                     | Page load completes in under 5 seconds.     |

---

## 📈 **Enhancements**

### Future Improvements
- **Cross-Browser Testing**: Extend support for Firefox, Edge.
- **Data-Driven Testing**: Use a data file for multiple test scenarios.
- **Integration with CI/CD**: Automate test execution in Jenkins or GitHub Actions.
- **Generate HTML Reports**: Use `pytest-html` or `Allure` for detailed reports.

---

## 🔗 **Resources**

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
- [Python Selenium API](https://selenium-python.readthedocs.io/)

---

## 🖋 **Author**

- **Name**: Nguyen Son Tung  
- **GitHub**: [Son-Tung](https://github.com/Son-Tung)  
- **Email**: [sontung18072004@gmail.com](mailto:sontung18072004@gmail.com)  

Feel free to contribute or suggest improvements!

---

## 🤝 **Contributing**

Feel free to open an issue or submit a pull request if you have improvements or bug fixes.

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
