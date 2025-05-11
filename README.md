# UniApp - GUI Student System (for Group Members)

This is the student-side GUI application developed by Remila Aili.
It includes 4 GUI windows, all fully working and ready to test.

---

## ✅ Included Windows

1. **Login Window** – for entering email + password
2. **Enrolment Window** – shows enrolled subjects and allows adding
3. **Results Window** – shows subject marks, average, pass/fail
4. **Exception Popup Windows** – shown when login fails

---

## 🚀 How to Run (Mac / Windows / VS Code)

### 1. Open terminal or VS Code
### 2. Navigate to the project folder `UniApp`
### 3. Run:

```bash
python3 login_window.py
```

✅ This will open the Login Window.

---

## 🧪 How to Test the 4 Windows

| Window             | How to trigger                                             |
|--------------------|------------------------------------------------------------|
| Login Window       | Opens when you run the program                             |
| Enrolment Window   | Login with correct credentials → automatically opens       |
| Results Window     | Click “View Results” in enrolment window                   |
| Exception Popups   | Try wrong password or unregistered email in login window   |

---

## 🧾 Default Test Accounts (if no data)

If database is empty, you can use CLI to register:

```bash
python3 student_controller.py
```

Choose option `r` to register a new student.

---

If you have any issues running the system, message Remila.Readme
