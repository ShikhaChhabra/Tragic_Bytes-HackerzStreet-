function validateForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var errorMsg = document.getElementById('error-msg');

    function validateForm() {
      var emailField = document.getElementById('email');
      var emailError = document.getElementById('emailError');
      var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

      if (!emailPattern.test(emailField.value)) {
        emailError.textContent = 'Please enter a valid email address.';
        return false;
      } else {
        emailError.textContent = '';
        return true;
      }
    }  
    // Regular expression to check for a minimum of 8 characters,
    // at least one special character, and no spaces
    var passwordPattern = /^(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/;
  
    if (username === '' || password === '') {
      errorMsg.textContent = '\nUsername and password are required.';
      return false;
    } else if (!passwordPattern.test(password)) {
      errorMsg.textContent = '\nPassword must be at least 8 characters long, contain at least one special character, and no spaces.';
      return false;
    }
  
    // If all checks pass, the form is submitted
    return true;
  }
  