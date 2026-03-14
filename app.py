from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    rows = []
    with open('incident_report.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        for row in reader:
            rows.append(row)
    return render_template('index.html', headers=headers, rows=rows)

if __name__ == '__main__':
    app.run(debug=True)