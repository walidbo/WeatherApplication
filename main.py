import streamlit as st
import requests
import speech_recognition as sr
###########from sklearn.svm import SVC
###########from sklearn.preprocessing import StandardScaler


# Weather information retrieval
def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    api_key = "e44b093d9186c95a9e142492c85c308c"  # Replace with your OpenWeatherMap API key
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change the units if desired
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] == 200:
            return data
        else:
            st.write("Error retrieving weather data.")
            return None
    except requests.exceptions.RequestException as e:
        st.write(f"Error: {e}")
        return None


# Process the weather data and display the forecast
def process_weather_data(data):
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    st.write(f"Temperature: {temperature}°C")
    st.write(f"Description: {description}")
    st.write(f"Humidity: {humidity}%")
    st.write(f"Wind Speed: {wind_speed} m/s")


# Train your SVM model
# def train_svm_model():
#     # Load your training data and labels
#     X_train = load_training_data()  # Replace with your actual training data
#     y_train = load_training_labels()  # Replace with your actual training labels
#
#     # Preprocess the data
#     scaler = StandardScaler()
#     X_train = scaler.fit_transform(X_train)
#
#     # Train the SVM model
#     svm_model = SVC()
#     svm_model.fit(X_train, y_train)
#
#     return svm_model


# Voice input and weather update
def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please speak...")
        audio = r.listen(source)
        st.write("Recognizing...")
    try:
        query = r.recognize_google(audio)
        st.write(f"You said: {query}")
        data = get_weather_data(query)
        process_weather_data(data)
    except sr.UnknownValueError:
        st.write("Sorry, I couldn't understand your voice.")
    except sr.RequestError as e:
        st.write(f"Speech recognition service error: {e}")


# Chatbot interaction
def chatbot_interaction():
    city = st.text_input("Enter a city name")
    if city:
        if st.button("Get Weather"):
            data = get_weather_data(city)
            process_weather_data(data)
    else:
        st.write("Please enter a city name.")


# SVM weather prediction
# def svm_prediction():
#     user_input = st.text_input("Enter the location for weather prediction")
#     num_hours = st.number_input("Enter the number of hours for prediction", min_value=1, max_value=24, step=1)
#     num_days = st.number_input("Enter the number of days for prediction", min_value=1, max_value=7, step=1)
#
#     # Retrieve weather data for the specified location
#     data = get_weather_data(user_input)
#
#     # Process the weather data and extract features
#     temperature = data["main"]["temp"]
#     humidity = data["main"]["humidity"]
#     wind_speed = data["wind"]["speed"]
#
#     # Prepare the feature vector
#     features = [[temperature, humidity, wind_speed]]  # Modify based on your feature representation
#
#     # Scale the features using the same scaler used during training
#     features = scaler.transform(features)
#
#     # Make predictions using the SVM model
#     predictions = svm_model.predict(features)
#
#     # Display the predictions
#     st.write("Weather Predictions:")
#
#     # Iterate over the predicted labels and display the corresponding weather conditions
#     for i in range(len(predictions)):
#         st.write(f"{i + 1} hour(s)/day(s) ahead:")
#
#         # Display the predicted weather condition based on the predicted labels
#         if predictions[i] == 0:
#             st.write("Sunny")
#         elif predictions[i] == 1:
#             st.write("Rainy")
#         elif predictions[i] == 2:
#             st.write("Cloudy")
#         else:
#             st.write("Unknown")


# Train the SVM model
##########################svm_model = train_svm_model()


# Streamlit application
def main():
    st.title("Weather Prediction System")
    st.write("Welcome to the Weather Prediction System!")

    option = st.sidebar.selectbox("Select an option", ("Voice Input", "Chatbot Interaction", "SVM Weather Prediction"))

    if option == "Voice Input":
        voice_input()
    elif option == "Chatbot Interaction":
        chatbot_interaction()
    #######elif option == "SVM Weather Prediction":
        ######svm_prediction()


if __name__ == "__main__":
    main()
