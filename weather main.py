import requests # Import the requests library to make HTTP requests

# Function to get weather data from openweathermap.org
def get_weather_data(location):
    # Your API key for authentication.
    api_key = "e52e8eb69e38792ee7ad0f805db74707"

    # Define the base URL for the OpenWeatherMap API.
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Define the parameters for the API request.
    params = {
        'q': location,  # The location (city name or zip code) entered by the user.
        'appid': api_key,  # Your API key for authentication.
        'units': 'imperial'  # Specify imperial units for temperature (°F) and wind speed (mp/h).
    }

    try:
        # Send a GET request to the OpenWeatherMap API with the specified parameters.
        response = requests.get(base_url, params=params)

        # Check the HTTP response status code.
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response into a Python dictionary.
            return data
        elif response.status_code == 404:
            print("Error: City not found. Please check the location name or zip code.")
        else:
            print(f"Error: Unable to fetch weather data. HTTP status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error connecting to the weather service:", e)

    return None

# Function to display weather information
def display_weather(data):
    if data:
        print(f"Weather Forecast for {data['name']}:")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']} °F")
        print(f"Humidity: {data['main']['humidity']} %")
        print(f"Wind Speed: {data['wind']['speed']} mp/h")
    else:
        print("Unable to fetch weather data.")

# Main function
def main():
    print("Welcome to the Weather Forecast App!")

    while True:
        #   Get user input for lookup
        location = input("Please enter a city name or zip code (or 'quit' to exit): ").strip()

        if location.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break

        if location:
            weather_data = get_weather_data(location)  # Get weather data for the user's location.
            display_weather(weather_data)  # Display the weather information.

        else:
            print("Please provide a valid location.")

if __name__ == "__main__":
    main()  # Run the main function when the script is executed.
