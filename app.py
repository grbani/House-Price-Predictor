import streamlit as st
import pandas as pd
import joblib
@st.cache_data
def load_model():
    """Loads the saved machine learning model from disk."""
    model = joblib.load('model.joblib')
    return model
model = load_model()
st.title('House Price Predictor')
st.sidebar.header('Input House Features')

def user_input_features():
    """Creates sidebar widgets for user input and processes them for the model."""
    area = st.sidebar.number_input('Area (in sq. ft.)', min_value=1000, max_value=16000, value=3500, step=100)
    bedrooms = st.sidebar.slider('Bedrooms', min_value=1, max_value=6, value=3, step=1)
    bathrooms = st.sidebar.slider('Bathrooms', min_value=1, max_value=4, value=2, step=1)
    stories = st.sidebar.slider('Stories', min_value=1, max_value=4, value=2, step=1)
    parking = st.sidebar.slider('Parking Spaces', min_value=0, max_value=3, value=1, step=1)
    mainroad = st.sidebar.selectbox('Is it on the main road?', ('yes', 'no'))
    guestroom = st.sidebar.selectbox('Does it have a guest room?', ('yes', 'no'))
    basement = st.sidebar.selectbox('Does it have a basement?', ('yes', 'no'))
    hotwater = st.sidebar.selectbox('Does it have hot water heating?', ('yes', 'no'))
    aircon = st.sidebar.selectbox('Does it have air conditioning?', ('yes', 'no'))
    prefarea = st.sidebar.selectbox('Is it in a preferred area?', ('yes', 'no'))
    
    furnishing = st.sidebar.selectbox('Furnishing Status', ('furnished', 'semi-furnished', 'unfurnished'))

    
    binary_map = {'yes': 1, 'no': 0}    
    data = {
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': stories,
        'mainroad': binary_map[mainroad],
        'guestroom': binary_map[guestroom],
        'basement': binary_map[basement],
        'hotwaterheating': binary_map[hotwater],
        'airconditioning': binary_map[aircon],
        'parking': parking,
        'prefarea': binary_map[prefarea],
        # One-hot encode furnishing status
        'furnishing_semi-furnished': 1 if furnishing == 'semi-furnished' else 0,
        'furnishing_unfurnished': 1 if furnishing == 'unfurnished' else 0,
    }

    bedrooms_for_ratio = bedrooms if bedrooms > 0 else 1
    data['area_per_bedroom'] = area / bedrooms_for_ratio
    data['bath_bed_ratio'] = bathrooms / bedrooms_for_ratio

    feature_order = [
        'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
        'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea',
        'furnishing_semi-furnished', 'furnishing_unfurnished',
        'area_per_bedroom', 'bath_bed_ratio'
    ]
    

    features = pd.DataFrame(data, index=[0])[feature_order]
    return features

input_df = user_input_features()

st.subheader('Your Selections')
st.write(input_df)

prediction = model.predict(input_df)

st.metric(label="Predicted House Price 🔮", value=f"${prediction[0]:,.0f}")