SentryFlow 🛡️📊
Enterprise PII Incident Dashboard

SentryFlow is a web application that analyzes uploaded corporate access logs to detect if sensitive Personally Identifiable Information (PII) has been exposed. Built to bridge the gap between Management Information Systems (MIS) and Cybersecurity, it functions as an automated auditing tool that flags security violations in real-time.

🚀 Features
Real-time Log Scanning: Upload CSV access logs and get instant analysis

Smart Data Filtering: Automatically detects exposed Social Security Numbers and Credit Cards

Interactive Dashboard: View localized security incidents with dynamic metric summary cards

Data Management: Download sample enterprise logs to test, or clear the dashboard instantly

Modern UI: Clean, responsive design powered by Bootstrap 5

Theme Toggling: Seamless switching between Dark Mode and Light Mode

🛠️ Technology Stack
Frontend: HTML5, CSS3, Bootstrap 5

Backend: Python Flask

Data Processing: Python csv and re (Regular Expressions) modules

Deployment: Gunicorn, Render

Analysis: Regex pattern matching for PII data spillage

📋 Prerequisites
Python 3.7+ installed on your system

pip (Python package manager)

A modern web browser

🔧 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/josiahb10/SentryFlow.git
cd SentryFlow
Create a virtual environment and run the application:

Bash
# Set up environment
python -m venv venv
.\venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the app
python app.py
Open your browser and go to:
http://localhost:5000

🎯 How It Works
Upload & Analysis Flow

Generate/Upload Logs: Click "Download Sample Data" to get a generated CSV, or upload your own corporate logs.

PII Detection: The system analyzes the data_payload column for unauthorized sensitive information.

Smart Filtering:

✅ Clean Logs → Ignored to reduce analyst fatigue

❌ Exposed PII → Flagged as a critical security incident

Dashboard Render: Successfully scanned incidents populate the interactive table and update the metric cards.

Detection Methods

SSN Analysis: Checks for standard Social Security Number formatting (XXX-XX-XXXX) using Regex.

Credit Card Signatures: Identifies 16-digit numeric patterns typical of financial data spillage.

📱 User Interface
Main Dashboard (/)

Professional SentryFlow title with dynamic theme-based text

File upload area with inline action buttons

Dynamic metric cards displaying Total Incidents, SSNs Exposed, and Credit Cards Exposed

Data table with timestamp, employee ID, department, and highlighted violation badges

Dark/Light mode toggle switch

📁 Project Structure
Plaintext
SentryFlow/
├── templates/
│   └── index.html          # Main dashboard interface
├── app.py                  # Flask server with Regex detection
├── generate_logs.py        # Dummy enterprise log generator
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore file for venv
└── README.md               # This documentation
🎨 Design Features
Color Scheme: Dark Mode (Linear gradient slate/charcoal + Warning Yellow accents) and Light Mode (Clean white/gray)

Framework: Bootstrap 5 for consistent, enterprise-grade interface elements

Icons: Bootstrap Icons (bi-shield-lock, bi-download, bi-trash)

Responsive: Mobile-friendly table and flexbox forms

🚀 API Endpoints
GET / - Main dashboard interface

POST / - Log file upload and analysis endpoint

GET /download_sample - Serves the enterprise_access_logs.csv test file

🔮 Future Enhancements
SQL Database integration for long-term incident storage

User authentication and role-based access control (RBAC)

Export functionality for compliance reporting (PDF/CSV)

Integration capabilities with enterprise SIEM tools (e.g., Splunk)

🏆 Portfolio Project
Built to address the growing challenge of data privacy compliance in corporate environments. As enterprises handle massive amounts of log data, automated detection systems like SentryFlow are required to catch PII spillage, maintain compliance (GDPR/CCPA), and reduce the manual workload of IT and Security teams.

👥 Developer
Josiah Brown - Full-Stack Developer & Cybersecurity/MIS Student, bjosiah52@gmail.com | LinkedIn

📄 License
MIT License - Built for educational and portfolio purposes.

⚠️ Note: This is a functional prototype demonstrating automated PII detection concepts. For production deployment in a real enterprise environment, implement robust authentication, encrypted databases, and enhanced server security measures.
