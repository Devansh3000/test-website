// ===== script.js — JavaScript Validation (Sub Task 3) =====

document.getElementById('feedbackForm').addEventListener('submit', function (e) {
  e.preventDefault();
  if (validateForm()) {
    document.getElementById('successBanner').style.display = 'block';
    this.reset();
    clearAllStates();
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(() => {
      document.getElementById('successBanner').style.display = 'none';
    }, 5000);
  }
});

function validateForm() {
  let isValid = true;

  // 1. Student Name — must not be empty
  const name = document.getElementById('studentName').value.trim();
  if (name === '') {
    showError('studentName', 'nameError', 'Student name is required.');
    isValid = false;
  } else {
    clearError('studentName', 'nameError');
  }

  // 2. Email — proper format
  const email = document.getElementById('email').value.trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (email === '') {
    showError('email', 'emailError', 'Email ID is required.');
    isValid = false;
  } else if (!emailRegex.test(email)) {
    showError('email', 'emailError', 'Please enter a valid email (e.g. user@example.com).');
    isValid = false;
  } else {
    clearError('email', 'emailError');
  }

  // 3. Mobile Number — exactly 10 digits
  const mobile = document.getElementById('mobile').value.trim();
  const mobileRegex = /^[0-9]{10}$/;
  if (mobile === '') {
    showError('mobile', 'mobileError', 'Mobile number is required.');
    isValid = false;
  } else if (!mobileRegex.test(mobile)) {
    showError('mobile', 'mobileError', 'Mobile number must contain exactly 10 valid digits.');
    isValid = false;
  } else {
    clearError('mobile', 'mobileError');
  }

  // 4. Department — must be selected
  const dept = document.getElementById('department').value;
  if (dept === '') {
    showError('department', 'deptError', 'Please select your department.');
    isValid = false;
  } else {
    clearError('department', 'deptError');
  }

  // 5. Gender — at least one option must be selected
  const genderSelected = document.querySelector('input[name="gender"]:checked');
  if (!genderSelected) {
    document.getElementById('genderError').textContent = 'Please select your gender.';
    isValid = false;
  } else {
    document.getElementById('genderError').textContent = '';
  }

  // 6. Feedback Comments — not blank, minimum 10 words
  const feedback = document.getElementById('feedback').value.trim();
  const wordCount = feedback.split(/\s+/).filter(w => w.length > 0).length;
  if (feedback === '') {
    showError('feedback', 'feedbackError', 'Feedback comments are required.');
    isValid = false;
  } else if (wordCount < 10) {
    showError('feedback', 'feedbackError',
      `Feedback must be at least 10 words. Currently: ${wordCount} word(s).`);
    isValid = false;
  } else {
    clearError('feedback', 'feedbackError');
  }

  return isValid;
}

function showError(fieldId, errorId, message) {
  const field = document.getElementById(fieldId);
  const error = document.getElementById(errorId);
  if (field) { field.classList.add('invalid'); field.classList.remove('valid'); }
  if (error) error.textContent = message;
}

function clearError(fieldId, errorId) {
  const field = document.getElementById(fieldId);
  const error = document.getElementById(errorId);
  if (field) { field.classList.remove('invalid'); field.classList.add('valid'); }
  if (error) error.textContent = '';
}

function clearAllStates() {
  const fields = ['studentName', 'email', 'mobile', 'department', 'feedback'];
  fields.forEach(id => {
    const el = document.getElementById(id);
    if (el) { el.classList.remove('invalid', 'valid'); }
  });
  ['nameError','emailError','mobileError','deptError','genderError','feedbackError']
    .forEach(id => { document.getElementById(id).textContent = ''; });
}

function resetForm() {
  clearAllStates();
  document.getElementById('successBanner').style.display = 'none';
}

// Live validation on blur
['studentName','email','mobile','department','feedback'].forEach(id => {
  const el = document.getElementById(id);
  if (el) el.addEventListener('blur', validateForm);
});
