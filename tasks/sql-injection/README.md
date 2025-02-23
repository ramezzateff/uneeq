# 🔍 SQL Injection Detection & Exploitation Tool

A Python tool designed to **detect** and **exploit** SQL Injection vulnerabilities in web applications. This project aims to help security professionals and learners understand how SQL Injections work and how to protect against them.

---

## 📖 **Table of Contents**
- [💡 Features](#-features)
- [⚙️ Requirements](#️-requirements)
- [🚀 Usage](#-usage)
- [🧪 How It Works](#-how-it-works)
- [⚠️ Legal Disclaimer](#️-legal-disclaimer)

---

## 💡 **Features**
- ✅ **Error-Based SQL Injection Detection**  
- ✅ **Boolean-Based SQL Injection Detection**  
- ✅ **Automated Payload Injection**  
- ✅ **Exploitation using UNION-based SQLi** (to extract database names)  
- ✅ **Custom Payloads & Error Messages**  
- ✅ **Detailed Response Analysis**

---

## ⚙️ **Requirements**

- Python 3.x  
- **requests** library  

### 📥 Install Dependencies:
```bash
pip install requests
```

---

## 🚀 **Usage**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/sql-injection-tool.git
   cd sql-injection-tool
   ```

2. **Run the Script:**
   ```bash
   python3 sql_injection_tool.py
   ```

3. **Enter the Target URL:**  
   Example format:  
   ```
   http://example.com/page.php?id=
   ```

4. **If Vulnerable:**  
   The tool will offer to attempt exploitation using a **UNION-based SQL Injection**.

---

## 🧪 **How It Works**

1. **Detection Phase:**
   - Sends multiple common SQL injection payloads.
   - Checks for **SQL error messages** and **differences in responses** (Boolean-based detection).

2. **Exploitation Phase (if vulnerable):**
   - Uses **UNION-based SQL Injection** to try extracting **database names**.
   - Checks responses for known database identifiers like `information_schema`.

---

## ⚠️ **Legal Disclaimer**
This tool is intended for **educational purposes** and **authorized penetration testing** only.  
**Do NOT** use it on systems without proper authorization.  
The creator is **not responsible** for any misuse or damages caused by this tool.

---

Happy Hacking! 🚀💻

