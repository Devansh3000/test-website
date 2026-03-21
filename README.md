# Student Feedback Registration Form — DevOps CA2

A full-stack student feedback form built with **HTML, CSS, JavaScript, Selenium, and Jenkins** as part of the DevOps (Semester VI) CA2 assignment.

---

## 📁 Project Structure

```
student-feedback-form/
├── index.html          # Main form (Sub Task 1)
├── style.css           # External CSS styling (Sub Task 2)
├── script.js           # JavaScript validation (Sub Task 3)
├── tests/
│   └── test_form.py    # Selenium test cases (Sub Task 4)
├── Jenkinsfile         # Jenkins CI pipeline (Sub Task 5)
└── README.md
```

---

## ✅ Sub Task Breakdown

### Sub Task 1 — HTML Form
- Fields: Student Name, Email ID, Mobile Number, Department, Gender, Feedback Comments
- Submit and Reset buttons

### Sub Task 2 — CSS Styling
- **External CSS** → `style.css` (glassmorphism dark theme, gradient, animations)
- **Internal CSS** → `<style>` block inside `index.html` (form title, subtitle, success banner)

### Sub Task 3 — JavaScript Validation
All validations in `script.js`:
- Student Name → not empty
- Email → valid format (`user@domain.com`)
- Mobile → exactly 10 digits
- Department → must be selected from dropdown
- Gender → at least one option selected
- Feedback → not blank, minimum 10 words

### Sub Task 4 — Selenium Test Cases
File: `tests/test_form.py`

| TC | Description |
|----|-------------|
| TC1 | Page opens successfully |
| TC2 | Valid data → successful submission |
| TC3 | Blank fields → error messages shown |
| TC4 | Invalid email format → error shown |
| TC5 | Invalid mobile number → error shown |
| TC6 | Dropdown selection works |
| TC7 | Submit & Reset buttons work |

### Sub Task 5 — Jenkins Pipeline
- `Jenkinsfile` automates checkout → pip install → run Selenium tests
- Create a **Pipeline** job in Jenkins and point it to this repo

---

## 🚀 How to Run

### Open the Form
Simply open `index.html` in any browser.

### Run Selenium Tests
```bash
pip install selenium
python tests/test_form.py
```
> Make sure **ChromeDriver** is installed and matches your Chrome version.

### Jenkins Setup
1. Install Jenkins
2. Create a new **Pipeline** job
3. Set SCM to this GitHub repo
4. Script Path: `student-feedback-form/Jenkinsfile`
5. Click **Build Now**

---

## 🔧 Requirements
- Python 3.x
- `selenium` pip package
- Google Chrome + ChromeDriver
- Jenkins (for Sub Task 5)
