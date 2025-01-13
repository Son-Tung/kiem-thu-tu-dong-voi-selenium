https://chatgpt.com/share/678515b9-ec34-8002-8f52-7807b8775d14
# Selenium Automated Testing: Login Functionality

This project demonstrates automated testing using **Selenium** for a login functionality on a web application. It includes both positive and negative test cases, checks for UI components, and measures login performance.

---

## 📜 **Project Overview**

The project covers the following test cases:

1. **Positive Login**: Valid username and password.
2. **Negative Login**: Invalid username or password.
3. **UI Verification**: Ensures all key elements (username field, password field, login button) are displayed.
4. **Performance Check**: Measures the time taken for login and page load.

Each test is implemented with **Python** using **Selenium WebDriver** for browser automation.

---

## 📂 **Project Structure**

```
.
├── selenium_login_test
│   ├── test.py                 # Main script containing the test cases
│   ├── requirements.txt        # Python dependencies
│   ├── chromedriver.exe        # Chrome WebDriver (update for your system)
└── README.md                   # Documentation
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
Ensures the presence of all essential elements on the login page.

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

### Expected Outcomes
- Positive login: Displays a success message and navigates to the secure area.
- Negative login: Displays an error message for invalid credentials.
- UI components: All essential elements (username, password, login button) are present.
- Performance: Page load completes within 5 seconds.

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
   python login_test.py
   ```

---

## ⚙️ **Testing Scenarios**

### Test Cases

| Test Case             | Input                     | Expected Result                             |
|-----------------------|---------------------------|---------------------------------------------|
| **Positive Login**    | Valid credentials         | Success message and secure page load.       |
| **Negative Login**    | Invalid credentials       | Error message for invalid credentials.      |
| **UI Verification**   | -                         | All elements (username, password, button).  |
| **Performance Test**  | Valid credentials         | Page load completes in under 5 seconds.     |

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
- **Email**: sontung18072004@gmail.com  

Feel free to contribute or suggest improvements!


This `README.md` file provides a complete overview of the project, ensuring clarity for anyone who wants to understand or contribute to the repository.
