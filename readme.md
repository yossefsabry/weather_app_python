</h2 align="center">weathr app || yossef</h2>



🌦️ The code is a weather app that provides users with the current weather information of any city in the world. It utilizes the OpenWeatherMap API to fetch the weather data.

⚙️ The code starts by importing the necessary requests library for making HTTP requests to the API.

🔑 It defines the API key and base URL required for accessing the weather data from the OpenWeatherMap API.

👋 The code displays a welcome message and instructions for the user.

🔄 Inside a while loop, the code prompts the user to enter a city name. If the user enters "exit" or "q", the loop breaks, and the app terminates.

🌍 The code constructs the complete API request URL using the user-inputted city name and the API key.

📡 It sends an HTTP GET request to the OpenWeatherMap API using the constructed URL.

✅ If the request is successful (status code 200), the code extracts the relevant weather information from the API response JSON.

📊 The code then prints the extracted weather data, including the city name, country, weather description, temperature in Celsius, wind speed, and cloud coverage.

👋 After displaying the weather information, the code thanks the user for using the app.

❌ If the HTTP request fails, the code displays an error message and breaks the loop.

🔚 Once the user decides to exit the app, the code closes the app and the connection to the API.

🔒 Finally, the code closes the HTTP response connection.

👍 The app provides a simple and interactive way for users to check the weather conditions of any city in the world.

### my Email : yossefsabry66@gmail.com
