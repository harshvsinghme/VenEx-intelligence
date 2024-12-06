# VenEx-intelligence

VenEx-intelligence is a Flask-based API for predicting story points in project management. It uses machine learning models and preprocessing pipelines to process input data and return predictions.

## Features

- **Flask**: Lightweight framework for building APIs.
- **Machine Learning Integration**: Preprocessing pipelines and models for prediction.
- **REST API**: Simple and efficient endpoints for data interaction.
- **Modular Design**: Clean separation of concerns with reusable components.
- **Virtual Environment Support**: Encapsulated environment with `.venv`.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/) (v3.8 or above recommended)
- [pip](https://pip.pypa.io/en/stable/installation/) (comes with Python)
- [virtualenv](https://virtualenv.pypa.io/) for virtual environment management

---

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/harshvsinghme/VenEx-intelligence.git
   cd VenEx-intelligence
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv .venv OR python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt OR pip3 install -r requirements.txt
   ```

---

### Running the Application

Start the Flask app:

```bash
python app.py OR python3 app.py
```

By default, the app runs at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

### API Endpoints

#### `/predict` (POST)

- **Description**: Predicts story points based on input data.
- **Request Body** (JSON):

  ```json
  {
    "id": "TASK-001",
    "projectKey": "PROJ",
    "summary": "Add authentication feature",
    "description": "Implement login and registration",
    "assignee": "John",
    "status": "In Progress",
    "issueType": "Story",
    "sprint": "Sprint 1"
  }
  ```

- **Response** (JSON):

  ```json
  {
    "predicted_story_points": 5
  }
  ```

- **Error Response**:

  ```json
  {
    "error": "Missing required features"
  }
  ```

---

### Project Structure

```
VenEx-intelligence/
├── app.py                # Main Flask app
├── model/                # Pretrained ML model and preprocessing steps
│   ├── best_model.pkl    # Serialized ML model
│   └── preprocessing_steps.pkl  # Encoders and scalers
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .venv/                # Virtual environment (optional)
```

---

### Dependencies

Listed in `requirements.txt`:

- Flask
- pandas
- scikit-learn
- numpy

---

### Setting Up the Virtual Environment

To create a virtual environment:

1. Install `virtualenv` if not already installed:

   ```bash
   pip install virtualenv OR pip3 install virtualenv
   ```

2. Create and activate the virtual environment:

   ```bash
   python -m venv .venv OR python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies inside the virtual environment:

   ```bash
   pip install -r requirements.txt OR pip3 install -r requirements.txt
   ```

To deactivate the virtual environment:

```bash
deactivate
```

---

### Technologies Used

- **Flask**: Framework for creating RESTful APIs.
- **scikit-learn**: Machine learning model handling.
- **pandas**: Data manipulation and preprocessing.
- **numpy**: Numerical computations.

---

### Author

Developed and maintained by **Harsh**.
