from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, unittest

# Path to your form — update if needed
FORM_URL = "file:///" + os.path.abspath("index.html").replace("\\", "/")


class StudentFeedbackFormTest(unittest.TestCase):

    def setUp(self):
        """Launch Chrome browser before each test."""
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")   # Uncomment for headless mode in Jenkins
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        """Close browser after each test."""
        self.driver.quit()

    # ── Test Case 1: Page loads successfully ──────────────────────────────────
    def test_01_page_opens_successfully(self):
        """Check whether the form page opens successfully."""
        self.driver.get(FORM_URL)
        self.assertIn("Student Feedback", self.driver.title,
                      "Page title does not contain 'Student Feedback'")
        self.assertTrue(
            self.driver.find_element(By.ID, "feedbackForm").is_displayed(),
            "Feedback form is not visible on the page."
        )
        print("✅ TC1 PASSED: Page opened successfully.")

    # ── Test Case 2: Submit valid data ────────────────────────────────────────
    def test_02_valid_data_submission(self):
        """Enter valid data and verify successful submission."""
        driver = self.driver
        driver.get(FORM_URL)

        driver.find_element(By.ID, "studentName").send_keys("Devansh Sharma")
        driver.find_element(By.ID, "email").send_keys("devansh@example.com")
        driver.find_element(By.ID, "mobile").send_keys("9876543210")
        Select(driver.find_element(By.ID, "department")).select_by_value("CS")
        driver.find_element(By.ID, "genderMale").click()
        driver.find_element(By.ID, "feedback").send_keys(
            "This is a wonderful course and I learned a lot about DevOps practices this semester."
        )
        driver.find_element(By.ID, "submitBtn").click()

        banner = self.wait.until(
            EC.visibility_of_element_located((By.ID, "successBanner"))
        )
        self.assertTrue(banner.is_displayed(), "Success banner not shown after valid submission.")
        print("✅ TC2 PASSED: Valid data submitted successfully.")

    # ── Test Case 3: Blank mandatory fields show error messages ──────────────
    def test_03_blank_fields_show_errors(self):
        """Leave mandatory fields blank and check error messages appear."""
        driver = self.driver
        driver.get(FORM_URL)

        driver.find_element(By.ID, "submitBtn").click()
        time.sleep(0.5)

        name_error   = driver.find_element(By.ID, "nameError").text
        email_error  = driver.find_element(By.ID, "emailError").text
        mobile_error = driver.find_element(By.ID, "mobileError").text
        dept_error   = driver.find_element(By.ID, "deptError").text
        gender_error = driver.find_element(By.ID, "genderError").text
        fb_error     = driver.find_element(By.ID, "feedbackError").text

        self.assertTrue(len(name_error)   > 0, "Name error not displayed.")
        self.assertTrue(len(email_error)  > 0, "Email error not displayed.")
        self.assertTrue(len(mobile_error) > 0, "Mobile error not displayed.")
        self.assertTrue(len(dept_error)   > 0, "Department error not displayed.")
        self.assertTrue(len(gender_error) > 0, "Gender error not displayed.")
        self.assertTrue(len(fb_error)     > 0, "Feedback error not displayed.")
        print("✅ TC3 PASSED: Error messages shown for all blank fields.")

    # ── Test Case 4: Invalid email format ─────────────────────────────────────
    def test_04_invalid_email_validation(self):
        """Enter invalid email format and verify validation error."""
        driver = self.driver
        driver.get(FORM_URL)

        driver.find_element(By.ID, "studentName").send_keys("Test User")
        driver.find_element(By.ID, "email").send_keys("invalid-email-format")
        driver.find_element(By.ID, "submitBtn").click()
        time.sleep(0.5)

        email_error = driver.find_element(By.ID, "emailError").text
        self.assertIn("valid email", email_error.lower(),
                      f"Expected email validation error, got: '{email_error}'")
        print("✅ TC4 PASSED: Invalid email format correctly detected.")

    # ── Test Case 5: Invalid mobile number ────────────────────────────────────
    def test_05_invalid_mobile_validation(self):
        """Enter invalid mobile number and verify validation error."""
        driver = self.driver
        driver.get(FORM_URL)

        driver.find_element(By.ID, "studentName").send_keys("Test User")
        driver.find_element(By.ID, "email").send_keys("test@example.com")
        driver.find_element(By.ID, "mobile").send_keys("12345")   # Too short
        driver.find_element(By.ID, "submitBtn").click()
        time.sleep(0.5)

        mobile_error = driver.find_element(By.ID, "mobileError").text
        self.assertTrue(len(mobile_error) > 0,
                        "Mobile validation error not shown for short number.")
        print("✅ TC5 PASSED: Invalid mobile number correctly detected.")

    # ── Test Case 6: Dropdown selection ───────────────────────────────────────
    def test_06_dropdown_selection(self):
        """Check whether dropdown selection works properly."""
        driver = self.driver
        driver.get(FORM_URL)

        dept_select = Select(driver.find_element(By.ID, "department"))
        dept_select.select_by_value("IT")

        selected = dept_select.first_selected_option
        self.assertEqual(selected.get_attribute("value"), "IT",
                         "Dropdown did not select 'IT' correctly.")
        print("✅ TC6 PASSED: Dropdown selection works correctly.")

    # ── Test Case 7: Submit and Reset buttons work ────────────────────────────
    def test_07_buttons_work_correctly(self):
        """Check whether Submit and Reset buttons work correctly."""
        driver = self.driver
        driver.get(FORM_URL)

        name_field = driver.find_element(By.ID, "studentName")
        name_field.send_keys("Devansh")

        # Reset clears the field
        driver.find_element(By.ID, "resetBtn").click()
        time.sleep(0.3)
        self.assertEqual(name_field.get_attribute("value"), "",
                         "Reset button did not clear the name field.")

        # Submit button is clickable
        submit_btn = driver.find_element(By.ID, "submitBtn")
        self.assertTrue(submit_btn.is_enabled(), "Submit button is not enabled.")
        print("✅ TC7 PASSED: Submit and Reset buttons work correctly.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
