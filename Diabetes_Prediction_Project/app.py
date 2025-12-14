from flask import Flask, request, render_template
import pickle
import numpy as np
import datetime

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Get data from form
        name = request.form['name']
        
        # Collect numeric features for the model
        # We exclude 'name' from this list
        feature_values = [
            float(request.form['pregnancies']),
            float(request.form['glucose']),
            float(request.form['bloodpressure']),
            float(request.form['skinthickness']),
            float(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['dpf']),
            float(request.form['age'])
        ]
        
        final_features = [np.array(feature_values)]
        
        # 2. Make prediction
        prediction = model.predict(final_features)
        output = prediction[0]
        
        # 3. Formulate Result
        if output == 1:
            res_text = "High Likelihood of Diabetes"
            res_class = "danger"
            advice = "Please consult a healthcare professional."
        else:
            res_text = "Low Likelihood of Diabetes"
            res_class = "success"
            advice = "Great! Maintain your healthy lifestyle."

        # 4. Get Current Date for the Report
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # 5. Return template with ALL data (so inputs don't vanish)
        return render_template('index.html', 
                               result=res_text, 
                               result_class=res_class,
                               advice=advice,
                               date=current_date,
                               name=name,
                               # Pass back the original form data to repopulate fields
                               form_data=request.form)

    except Exception as e:
        return render_template('index.html', result="Error", advice="Please check your inputs.", result_class="danger", form_data=request.form)

if __name__ == "__main__":
    app.run(debug=True)