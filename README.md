# 📂 PDF Management Tool (Python)

A powerful Python-based tool to **organize, search, and manage PDF files** efficiently across your system.

---

## 🚀 Features

✅ Scan entire system for PDF files  
✅ Automatically organize PDFs into A–Z folders  
✅ Fast search by filename (recursive)  
✅ Detect duplicate files using SHA-256 hashing  
✅ Safely move duplicates to Recycle Bin (no permanent loss)  

---

## 🛠️ Tech Stack

- Python 3
- OS module (file handling)
- shutil (file operations)
- hashlib (duplicate detection)
- send2trash (safe deletion)

---

## 📁 Folder Structure

After organizing:
All_PDFs/
A/
B/
C/
...
Others/


---

## ⚙️ Installation

### 1. Clone the repository

'''bash
git clone https://github.com/your-username/pdf-management-tool.git
cd pdf-management-tool

### 2. Install dependencies
pip install send2trash

### 3. Run
python pdf_manager.py

Menu Options:
-Scan and organize PDFs
-Search PDFs by name
-Show duplicate PDFs
-Move duplicates to Recycle Bin
-Exit

🔐 Duplicate Handling
Uses SHA-256 hashing (accurate detection)
Keeps one original file
Moves duplicates to Recycle Bin (safe)

💡 Future Improvements
GUI desktop application (Tkinter / PyQt)
Search inside PDF content
Auto-categorization (Invoices, Notes, Books)
File preview feature

🤝 Contributing
Contributions are welcome!
Feel free to fork this repo and improve it.

📌 Author

VijayShankar6170

⭐ Support
If you found this project helpful, consider giving it a ⭐ on GitHub!
