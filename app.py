from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    incidents = []
    try:
        # Opens the CSV your scanner generated
        with open('incident_report.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skips the header row so it doesn't show up as data
            for row in reader:
                # Assuming the CSV columns are: Timestamp, ID, Dept, Action, Violation
                # We grab the relevant columns to send to the dashboard
                if len(row) >= 4:
                    # You might need to adjust row[x] if your CSV columns are in a different order
                    incidents.append([row[0], row[1], row[2], row[-1]]) 
    except FileNotFoundError:
        print("CSV not found. Make sure scanner.py has been run!")

    return render_template('index.html', incidents=incidents)

if __name__ == '__main__':
    app.run(debug=True)