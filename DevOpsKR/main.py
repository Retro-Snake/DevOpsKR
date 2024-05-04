from datetime import datetime
from flask import render_template, request, jsonify
from DevOpsKR import app
import requests 

@app.route('/weather', methods=['GET'])
def weather_info():
    print("Обработчик для `/weather` вызван.")
    # Получение параметров из запроса
    city = request.args.get('city', 'Moscow')
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')

    # Формирование запроса к API VisualCrossing
    api_key = 'BJ5LCS8UXS2LF3LFPZY9K8JMA'  
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&key={api_key}&unitGroup=metric&contentType=json&aggregateHours=24&location={city}&startDateTime={date_from}&endDateTime={date_to}"
    
    response = requests.get(url)
    weather_data = response.json()

    # Преобразование полученных данных в нужный формат
    temperatures = [entry['temp'] for entry in weather_data['locations'][city]['values']]

    formatted_data = {
        "data": {
            "temperature_c": {
                "average": sum(temperatures) / len(temperatures),
                "median": sorted(temperatures)[len(temperatures) // 2],
                "min": min(temperatures),
                "max": max(temperatures)
            }
        },
        "service": "weather"
    }

    return jsonify(formatted_data)

@app.route('/')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )