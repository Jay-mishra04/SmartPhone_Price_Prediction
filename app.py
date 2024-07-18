import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the prediction function
def predict_price(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]

# Define the Streamlit app
st.title('Smartphone Price Prediction')

# Create input fields for user to input feature values
five_g = st.selectbox('5G', options=[0, 1], index=0)
ram = st.number_input('RAM (GB)', min_value=1, max_value=12, value=4)
rom = st.number_input('ROM (GB)', min_value=16, max_value=512, value=64)
front_camera = st.number_input('Front Camera (MP)', min_value=0, max_value=64, value=8)
back_camera_sum = st.number_input('Back Camera Sum (MP)', min_value=0, max_value=200, value=13)

# Create input fields for brand and processor features
brand_name = st.selectbox('Brand Name', options=[
    'Apple', 'Google', 'Infinix', 'Motorola', 'OPPO', 'OnePlus', 'Others',
    'POCO', 'REDMI', 'Samsung', 'realme', 'vivo'
])

# Define processor options based on brand
if brand_name in ['Apple']:
    processor_options = ['Bionic']
elif brand_name in ['Samsung', 'Google', 'Motorola', 'OPPO', 'OnePlus', 'Infinix', 'POCO', 'REDMI', 'realme', 'vivo']:
    processor_options = ['Mediatek', 'Others', 'Snapdragon']
else:
    processor_options = ['Others']

processor_name = st.selectbox('Processor Name', options=processor_options)

# Create a dictionary for input data
input_data = {
    '5G': five_g,
    'RAM': ram,
    'ROM': rom,
    'Front_camera': front_camera,
    'Back_camera_sum': back_camera_sum,
    'Brand_name_Apple': int(brand_name == 'Apple'),
    'Brand_name_Google': int(brand_name == 'Google'),
    'Brand_name_Infinix': int(brand_name == 'Infinix'),
    'Brand_name_Motorola': int(brand_name == 'Motorola'),
    'Brand_name_OPPO': int(brand_name == 'OPPO'),
    'Brand_name_OnePlus': int(brand_name == 'OnePlus'),
    'Brand_name_Others': int(brand_name == 'Others'),
    'Brand_name_POCO': int(brand_name == 'POCO'),
    'Brand_name_REDMI': int(brand_name == 'REDMI'),
    'Brand_name_Samsung': int(brand_name == 'Samsung'),
    'Brand_name_realme': int(brand_name == 'realme'),
    'Brand_name_vivo': int(brand_name == 'vivo'),
    'Processor_name_Bionic': int(processor_name == 'Bionic'),
    'Processor_name_Mediatek': int(processor_name == 'Mediatek'),
    'Processor_name_Others': int(processor_name == 'Others'),
    'Processor_name_Snapdragon': int(processor_name == 'Snapdragon')
}

# Make prediction
if st.button('Predict Price'):
    predicted_price = predict_price(input_data)
    st.write(f'The predicted price is: {predicted_price}')
