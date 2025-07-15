# 📋 To-Do List App

![Last Commit](https://img.shields.io/badge/Last%20Commit-Today-brightgreen )  
**Primary Technology:** Python 🐍  

A simple yet dynamic To-Do List app built with **Flask (backend)** and **HTML/CSS/JavaScript (frontend)**. This app allows users to add, view, complete, and delete tasks while storing them in a SQLite database.

---

## 🌟 Features
- Add tasks dynamically. ✏️
- Mark tasks as completed with a single click. 
- Delete tasks when no longer needed. 
- Persistent storage using SQLite. 

---

## 💻 Technology Stack

This project is built using the following technologies:

### **Backend**
- **Python**: The primary programming language.
- **Flask**: A lightweight web framework for building the backend API.
- **SQLite**: A file-based database for storing tasks.

### **Frontend**
- **HTML5**: For structuring the web pages.
- **CSS3**: For styling the user interface.
- **JavaScript (Vanilla JS)**: For adding interactivity and dynamic behavior.

### **Dependencies**
- **Flask-CORS**: To handle Cross-Origin Resource Sharing (CORS) for API requests.
- **sqlite3**: Python's built-in library for interacting with SQLite databases.

### **Development Tools**
- **Git**: For version control and collaboration.
- **Virtualenv**: For creating isolated Python environments.
- **Pip**: For managing Python dependencies.

### **Hosting & Deployment**
- **GitHub**: For hosting the source code.
- **vercel**: Recommended platform for deploying the app.

---

## 📂 Project Structure
The project is organized into the following directories and files:
```
todo-backend/
├── app.py                  # Flask backend code
├── requirements.txt        # List of Python dependencies
├── todo.db                 # SQLite database (optional)
├── templates/              # Folder for HTML templates
│   └── index.html          # Frontend HTML file
├── static/                 # Folder for static files (CSS, JS)
│   └── style.css           # Custom CSS for styling
└── README.md               # Documentation for the project
```

---

## 🚀 Installation

### Prerequisites
- Python 3.x installed on your system. [Download Python](https://www.python.org/downloads/ )
- Git installed for cloning the repository. [Download Git](https://git-scm.com/ )

### Steps to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Seimei95/Jena.git
   cd Jena
   ```
2. **Set Up a Virtual Environment (Optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the App**
    ```bash
    python app.py
    ```
5. **Access the App**
Open your browser and navigate to:
    ```bash
    http://127.0.0.1:5000
    ```

---

## 🛠️ Usage
1. **Add Tasks**
-Enter a task in the input field and click **Add**.
-The task will appear in the list below.
2. **Mark Tasks as Completed**
-Check the checkbox next to a task to mark it as completed.
-Completed tasks will have a strikethrough effect.
3. **Delete Tasks**
-Click the **Delete** button next to a task to remove it from the list.

---

## 🤝 **Wanna Contribute?** 
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## **License**

This project is licensed under a **Custom All Rights Reserved License**.  
See the [LICENSE](./LICENSE) file for details.

## 📞 **Contact**
If you have any questions or suggestions, feel free to reach out:
- **GitHub DM**: [Send me a message on GitHub](https://github.com/Seimei95 )
- **Email**: [yoursvulkan@gmail.com](mailto:yoursvulkan@gmail.com)

## 🎉 **Show Your Support**
If you find this project useful, give it a ⭐️ star on GitHub! It motivates us to keep improving and adding new features.
