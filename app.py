import streamlit as st
import joblib
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder

# Constants
DEFAULT_CLASSES = ['apple', 'mandarin', 'orange', 'lemon']  # Update with your actual class order
MODEL_FILES = ['best_model.pkl', 'scaler.pkl', 'label_encoder.pkl']

def load_model_artifacts():
    """Load and validate all model artifacts"""
    if not all(os.path.exists(f) for f in MODEL_FILES):
        raise FileNotFoundError("Model files not found. Please run train_models.py first.")
    
    artifacts = {
        'model': joblib.load('best_model.pkl'),
        'scaler': joblib.load('scaler.pkl'),
        'encoder': joblib.load('label_encoder.pkl')
    }
    
    # Validate LabelEncoder
    if not hasattr(artifacts['encoder'], 'classes_'):
        st.warning("LabelEncoder not properly fitted. Using default classes.")
        artifacts['encoder'] = LabelEncoder()
        artifacts['encoder'].classes_ = np.array(DEFAULT_CLASSES)
    
    return artifacts

def create_input_features():
    """Create input feature UI and collect values"""
    col1, col2 = st.columns(2)
    with col1:
        mass = st.slider('Mass (g)', min_value=50, max_value=300, value=150, step=1)
        width = st.slider('Width (cm)', min_value=5.0, max_value=15.0, value=8.0, 
                         step=0.1, format="%.1f")
    with col2:
        height = st.slider('Height (cm)', min_value=5.0, max_value=15.0, value=8.0, 
                         step=0.1, format="%.1f")
        color_score = st.slider('Color Score (0-1)', min_value=0.0, max_value=1.0, 
                              value=0.5, step=0.01, format="%.2f")
    return np.array([[mass, width, height, color_score]], dtype=np.float64)

def make_prediction(model, scaler, encoder, input_data):
    """Make prediction with proper error handling"""
    try:
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        return encoder.inverse_transform(prediction.reshape(-1))[0]
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
        return None

def main():
    # Page configuration
    st.set_page_config(page_title="Fruit Classifier", page_icon="🍎")
    st.title('🍎 Fruit Classification App')
    st.write("Predict the type of fruit based on its characteristics")
    
    try:
        # Load models
        artifacts = load_model_artifacts()
        
        # Get user input
        input_data = create_input_features()
        
        # Make prediction
        if st.button('Predict Fruit Type'):
            fruit_name = make_prediction(
                artifacts['model'],
                artifacts['scaler'],
                artifacts['encoder'],
                input_data
            )
            if fruit_name:
                st.success(f'The predicted fruit is: **{fruit_name}**')
                
    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.stop()

if __name__ == "__main__":
    main()
