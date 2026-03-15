# SentryFlow 🛡️📊

**Enterprise PII Incident Dashboard**

SentryFlow is a web application that analyzes uploaded corporate access logs to detect if sensitive Personally Identifiable Information (PII) has been exposed. Built to bridge the gap between Management Information Systems (MIS) and Cybersecurity, it functions as an automated auditing tool that flags security violations in real-time.

### 🚀 Features

* **Real-time Log Scanning:** Upload CSV access logs and get instant analysis.
* **Smart Data Filtering:** Automatically detects exposed Social Security Numbers and Credit Cards.
* **Interactive Dashboard:** View localized security incidents with dynamic metric summary cards.
* **Data Management:** Download sample enterprise logs to test, or clear the dashboard instantly.
* **Modern UI:** Clean, responsive design powered by Bootstrap 5.
* **Theme Toggling:** Seamless switching between Dark Mode and Light Mode.

### 🛠️ Technology Stack

* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Backend:** Python Flask
* **Data Processing:** Python `csv` and `re` (Regular Expressions) modules
* **Deployment:** Gunicorn, Render
* **Analysis:** Regex pattern matching for PII data spillage

### 📋 Prerequisites

* Python 3.7+ installed on your system
* `pip` (Python package manager)
* A modern web browser

### 🔧 Installation & Setup

Clone the repository:
```bash
git clone [https://github.com/josiahb10/SentryFlow.git](https://github.com/josiahb10/SentryFlow.git)
cd SentryFlow
