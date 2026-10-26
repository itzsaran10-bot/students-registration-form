# 🎓 Student Registration Form

A desktop GUI application built with **Python** and **Tkinter** that lets users register students, view the submitted details instantly, and browse all registered students in one place.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Overview

Registration forms are used everywhere, from schools to online services. This mini project recreates one as a desktop application using Tkinter, Python's standard GUI library.

## 🎯 Objectives

- Understand how to build a graphical user interface in Python
- Take user input and process it on a button click
- Organize widgets neatly on screen
- Store data and display it back to the user

## ✨ Features

- Enter student **Name**, **Age**, **Gender**, and **Course**
- **Submit** button saves the student and shows their details in a pop-up message box
- **View All** button lists every student registered in the current session
- Friendly message when no students have been registered yet

## 🛠️ Tech Stack & Widgets Used

| Component | Purpose |
|-----------|---------|
| `Label` | Field names |
| `Entry` | Name and age input |
| `Radiobutton` | Gender selection |
| `Combobox` (`ttk`) | Course dropdown (BCA, BSc, BCom, BA) |
| `Button` | Submit and View All actions |
| `pack()` | Arranges widgets vertically |
| `messagebox` | Displays submitted details |

## 🔄 Process Flow

```
Start → Enter details → Click Submit → Save to list → Show message box → View All
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x (Tkinter comes bundled with standard Python installations)

### Run the project

```bash
# Clone the repository
git clone https://github.com/itzsaran10-bot/<your-repo-name>.git

# Move into the project folder
cd <your-repo-name>

# Run the app
python student_registration_form.py
```

## 📁 Project Structure

```
├── student_registration_form.py                         # Main application
├── Student_registration_form__python_mini_project__final.pptx   # Project presentation
└── README.md
```

## 🔮 Future Scope

- Store data permanently in a file or database so it isn't lost when the program closes
- Add input validation (for example, numeric age, required fields)
- Add more fields to the form

## 🙋 Author

**Saran Kumar M**
GitHub: [@itzsaran10-bot](https://github.com/itzsaran10-bot)

---

⭐ If you found this project helpful, consider giving it a star!
