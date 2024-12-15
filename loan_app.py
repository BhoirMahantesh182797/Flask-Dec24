from flask import Flask, request
app = Flask(__name__)
import pickle
import sklearn

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return '<h1> Loan Approval Application </h1>'

@app.route('/Predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return "I will make the Predictions "
    else:
        # post request along with data
        # then i will make predictions

        loan_req = request.get_json()
        if loan_req['Gender'] == "Male":
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == "No":
            Married = 0
        else:
            Married = 1
        
        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History= loan_req['Credit_History']           

        input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
        result = model.predict([input_data])
        
        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"


        return {"loan_approval_status":pred}