
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import tensorflow as tf

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model('model_Main2.h5')
scaler_X = joblib.load('scaler_X2.pkl')
scaler_y = joblib.load('scaler_y2.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        X_input = np.array([data['AC'], data['GR'], data['RT'], data['RXO']]).T
        X_scaled = scaler_X.transform(X_input)
        y_pred = model.predict(X_scaled)
        y_inverse = scaler_y.inverse_transform(y_pred)
        return jsonify({'CNL_predicted': y_inverse.flatten().tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
