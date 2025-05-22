def authenticate_user(password_input):
    correct_password = "admin123"  # Replace with env var or database check
    return password_input == correct_password

