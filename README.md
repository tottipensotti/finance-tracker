# Finance Tracker

A Python-based project for tracking monthly expenses, incomes, and savings. Still in progress

## Installation

To set up the project, follow these steps:

### Prerequisites

Ensure you have Python 3.8 or later installed.

### Clone the Repository

```bash
git clone https://github.com/tottipensotti/finance-tracker.git
cd finance-tracker
```

### Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Running the Application

### Starting the Backend
First, run the `database.py` file to create the empty databases:
```
python database.py run
```
To start the backend server:

```
uvicorn main:app --reload
```
This will start the FastAPI server on `http://localhost:8000`

### Testing the Endpoints
First, add an account using `curl`:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/accounts/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Test",
  "description": "Test",
  "type": "Test"
}'
```

Example: Adding an Income
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/incomes/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Test",
  "date": "2024-08-23T00:00:00.001Z",
  "amount": 100,
  "account": 1,
  "category": "Test",
  "currency": "USD"
}'
```

Finally, to see the incomes:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/incomes' \
  -H 'accept: application/json'
```

You can review the API documentation in `http://127.0.0.1:8000/docs` to try out other endpoints.
