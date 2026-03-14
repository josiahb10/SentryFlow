from flask import Flask, render_template, request, send_file
import csv
import re
import io

app = Flask(__name__)

SSN_PATTERN = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
CC_PATTERN = re.compile(r'\b(?:\d[ -]*?){16}\b')

@app.route('/', methods=['GET', 'POST'])
def index():
    incidents = []
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['file']
        if file.filename != '':
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            reader = csv.DictReader(stream)
            
            for row in reader:
                payload = row.get('data_payload', '')
                timestamp = row.get('timestamp', '')
                employee_id = row.get('employee_id', '')
                department = row.get('department', '')
                
                if SSN_PATTERN.search(payload):
                    incidents.append([timestamp, employee_id, department, 'SSN Exposed'])
                if CC_PATTERN.search(payload):
                    incidents.append([timestamp, employee_id, department, 'Credit Card Exposed'])
                    
            return render_template('index.html', incidents=incidents)

    # For a normal visit (GET request) or when clicking "Clear", return an empty list!
    return render_template('index.html', incidents=[])

@app.route('/download_sample')
def download_sample():
    try:
        return send_file('enterprise_access_logs.csv', as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)