from flask import Flask, render_template, request
import pickle

# Load the pre-trained machine learning model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ind.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the 23 input values from the form
    input_data = [float(request.form[f'input{i+1}']) for i in range(24)]

    # Make a prediction using the pre-trained model
    prediction = model.predict([input_data])[0]

    # Render the result template with the prediction value
    #return render_template('result.html', prediction=prediction)
    if prediction==1:
        return "ckd"
    else:
        return "no ckd"

if __name__ == '__main__':
    app.run(port=8000)