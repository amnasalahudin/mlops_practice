import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_predict(client):
    # Example test for predict endpoint with specific fields
    data = {
        "Gender": "Male",
        "Married": "No",
        "Dependents": "0",
        "Education": "Graduate",
        "Self_Employed": "No",
        "ApplicantIncome": 5000,
        "CoapplicantIncome": 0,
        "LoanAmount": 200,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Property_Area": "Urban"
    }
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    assert 'Loan_Status' in response.json
