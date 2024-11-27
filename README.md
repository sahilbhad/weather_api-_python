# Running this project


To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

      => pip install virtualenv
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

      => virtualenv env
That will create a new folder env in your project directory. Next activate it with this command on mac/linux:

      => source env/bin/active
Now you can run the project with this command

      => python manage.py runserver

# Key Features:
  This Project fetches and presents weather data, likely obtained from a weather API such as OpenWeatherMap. Key weather details include:

City Name: Displayed in uppercase.
Current Weather: A description of the current atmospheric conditions.
Coordinates: Latitude and longitude of the city.
Weather Details:
ID: Weather condition ID.
Main Weather: General weather type (e.g., "Rain", "Clear").
Temperature: Current temperature.
Main Atmospheric Data:
Pressure: Atmospheric pressure in hPa.
Humidity: Percentage of air moisture.
Visibility: Distance visible in meters.
Wind Speed: Wind velocity.


@ Developed by : Sahil Bhad
