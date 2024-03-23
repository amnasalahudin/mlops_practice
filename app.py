from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)

# Load the trained logistic regression model
model = load('loan_approval_model.joblib')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the POST request
        data = request.get_json()

        # Create a DataFrame from the JSON data
        features_df = pd.DataFrame([data])

        # Predict the loan status using the model
        prediction = model.predict(features_df)

        # Transform prediction back to original label
        prediction_label = ['Y' if pred == 1 else 'N' for pred in prediction]

        # Return the prediction as a JSON
        return jsonify({'Loan_Status': prediction_label[0]})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
