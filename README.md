# SentryFlow 🛡️📊

**Enterprise PII Incident Detection Dashboard**

SentryFlow is a web application that analyzes uploaded corporate access logs to detect if sensitive **Personally Identifiable Information (PII)** has been exposed. Built to bridge the gap between **Management Information Systems (MIS)** and **Cybersecurity**, it functions as an automated auditing tool that flags security violations in real time.

---

## 🚀 Features

- **Real-time Log Scanning**: Upload CSV access logs and get instant analysis
- **Smart PII Detection**: Automatically detects exposed Social Security Numbers and Credit Card numbers
- **Interactive Security Dashboard**: View detected security incidents with dynamic metric summary cards
- **Data Management**: Download sample enterprise logs to test or clear the dashboard instantly
- **Modern UI**: Clean, responsive interface built with Bootstrap 5
- **Theme Toggling**: Seamless switching between Dark Mode and Light Mode

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Python Flask
- **Data Processing**: Python `csv` and `re` (Regular Expressions) modules
- **Deployment**: Gunicorn, Render
- **Analysis**: Regex pattern detection for PII data exposure

---

## 📋 Prerequisites

- **Python 3.7+** installed on your system
- **pip** (Python package manager)
- A modern web browser

---

## 🔧 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/josiahb10/SentryFlow.git
cd SentryFlow
```

### 2. Set up the environment and run the application

```bash
# Create virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### 3. Open your browser and go to

```
http://localhost:5000
```

---

## 🎯 How It Works

### Upload & Analysis Flow

1. **Upload Logs**
   - Upload your own corporate CSV log file
   - Or download generated sample logs

2. **PII Detection**
   - The system analyzes the `data_payload` column for sensitive information exposure

3. **Smart Filtering**

- ✅ **Clean logs** → Ignored to reduce analyst fatigue  
- ❌ **PII detected** → Flagged as a critical security incident

4. **Dashboard Update**
   - Flagged incidents populate the dashboard table and update the metric cards

### Detection Methods

- **SSN Analysis**
  - Detects Social Security Numbers using the pattern:

```
XXX-XX-XXXX
```

- **Credit Card Detection**
  - Identifies 16-digit numeric sequences typical of financial data exposure

---

## 📱 User Interface

### Main Dashboard (`/`)

- Professional **SentryFlow** dashboard header
- CSV file upload interface with action buttons

**Dynamic metric cards displaying:**

- Total Incidents
- SSNs Exposed
- Credit Cards Exposed

**Security incident table showing:**

- Timestamp
- Employee ID
- Department
- Violation badges

- Dark Mode / Light Mode toggle

---

## 📁 Project Structure

```
SentryFlow/
├── templates/
│   └── index.html          # Main dashboard interface
├── app.py                  # Flask server with PII detection logic
├── generate_logs.py        # Enterprise log generator for testing
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignore virtual environment files
└── README.md               # Project documentation
```

---

## 🎨 Design Features

### Color Scheme

- **Dark Mode**: Slate/Charcoal + Warning Yellow
- **Light Mode**: Clean white and gray

### Framework

- Bootstrap 5 for consistent enterprise UI components

### Icons

- Bootstrap Icons
- `bi-shield-lock`
- `bi-download`
- `bi-trash`

### Responsive Design

- Mobile-friendly tables
- Flexible form layouts

---

## 🚀 API Endpoints

- `GET /` – Main dashboard interface
- `POST /` – Log file upload and analysis
- `GET /download_sample` – Download generated enterprise access logs

---

## 🔮 Future Enhancements

- SQL database integration for persistent incident storage
- User authentication and role-based access control (RBAC)
- Compliance reporting exports (PDF / CSV)
- Integration with enterprise SIEM tools (e.g., Splunk)
- Advanced PII detection using machine learning

---

## 🏆 Portfolio Project

SentryFlow was built to demonstrate how automated log analysis can improve **enterprise security monitoring and data privacy compliance**. As organizations handle massive volumes of system logs, automated tools like SentryFlow help detect **PII data exposure**, maintain **GDPR/CCPA compliance**, and reduce manual security workloads.

---

## 👨‍💻 Developer 

- **Josiah Brown** – Full-Stack Developer & Cybersecurity/MIS Student  
- Email: bjosiah52@gmail.com  
- GitHub: https://github.com/josiahb10

---

## 📄 License

MIT License – Built for educational and portfolio purposes.

---

⚠️ **Note:** This project is a prototype demonstrating automated PII detection concepts. A production-ready system would require secure authentication, encrypted databases, advanced detection models, and hardened server security.
