import pickle
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

with open('model/preprocessing_steps.pkl', 'rb') as file:
    preprocessing_steps = pickle.load(file)

with open('model/best_model.pkl', 'rb') as file:
    model = pickle.load(file)

def preprocess_input(input_data: dict) -> pd.DataFrame:
    input_df = pd.DataFrame([input_data])

    input_df['sprint'] = input_df['sprint'].astype('category')
    input_df['summary_length'] = input_df['summary'].str.len()
    input_df['description_length'] = input_df['description'].str.len()
    input_df['summary_word_count'] = input_df['summary'].str.split().str.len()
    input_df['description_word_count'] = input_df['description'].str.split().str.len()

    input_df['assignee_count'] = input_df['assignee'].map(preprocessing_steps['assignee_count_mapping'])

    input_df['assignee_issueType_interaction'] = input_df['assignee'] + "_" + input_df['issueType']
    input_df['assignee_status_interaction'] = input_df['assignee'] + "_" + input_df['status']
    input_df['issueType_summaryLength_interaction'] = input_df['issueType'] + "_" + input_df['summary_length'].astype(str)
    input_df['assignee_descriptionLength_interaction'] = input_df['assignee'] + "_" + input_df['description_length'].astype(str)
    input_df['assignee_sprint_issueType_interaction'] = input_df['assignee'] + "_" + input_df['sprint'].astype(str) + "_" + input_df['issueType']

    
    ordinal_encoder = preprocessing_steps['ordinal_encoder']

    categorical_columns = [
        'id', 'projectKey', 'summary', 'description', 'assignee', 'status', 'issueType', 'sprint',
        'assignee_issueType_interaction', 'assignee_status_interaction',
        'issueType_summaryLength_interaction', 'assignee_descriptionLength_interaction', 
        'assignee_sprint_issueType_interaction'
    ]
    
    for col in categorical_columns:
        if col in ordinal_encoder:
            encoder = ordinal_encoder[col]
            input_df[col] = encoder.transform(input_df[[col]])

    numerical_columns = ['summary_length', 'description_length', 'summary_word_count', 'description_word_count', 'assignee_count']

    scaler = preprocessing_steps['scaler_min_max']
    input_df[numerical_columns] = scaler.transform(input_df[numerical_columns])

    return input_df

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()

    required_features = ['id', 'projectKey', 'summary', 'description', 'assignee', 'status', 'issueType', 'sprint']
    if not all(feature in input_data for feature in required_features):
        return jsonify({'error': 'Missing required features'}), 400

    processed_input = preprocess_input(input_data)

    predicted_story_points = model.predict(processed_input)

    return jsonify({'predicted_story_points': predicted_story_points[0]}), 200

if __name__ == '__main__':
    app.run(debug=True)
