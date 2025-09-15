from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            month = request.form['month']
            entries_json = request.form['entries']

            # Check if entries_json is not empty
            if not entries_json.strip():
                return render_template('index.html', error="Please add at least one entry.")

            entries = json.loads(entries_json)

            data = {}
            total_kg = 0

            for entry in entries:
                day = int(entry['day'])
                kg = float(entry['kg'])
                data[day] = kg
                total_kg += kg

            total_amount = total_kg * amount

            return render_template(
                'index.html',
                summary=data,
                total_kg=total_kg,
                total_amount=total_amount,
                month=month,
                error=None
            )

        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {e}")

    return render_template('index.html', summary=None, error=None)

if __name__ == '__main__':
    app.run(debug=True)
