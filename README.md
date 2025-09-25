
# Unit Converter

A Django-based web application for converting units of measurement, including length, temperature, and weight. The app provides both a user-friendly web interface and an API for programmatic access.

## Features

- **Unit Conversions Supported:**
  - Length: Millimeter, Centimeter, Meter, Kilometer, Inch, Foot, Yard, Mile
  - Temperature: Celsius, Fahrenheit, Kelvin
  - Weight: Milligram, Gram, Kilogram, Ounce, Pound

- **Web Interface:** Interactive form-based UI built with Bootstrap for easy conversions.
- **API Endpoint:** RESTful API for integrating conversions into other applications.
- **Real-time Updates:** Dynamic dropdowns that update based on selected measurement type.

## Installation

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd UnitConverter
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```
   python manage.py migrate
   ```

4. **Start the development server:**
   ```
   python manage.py runserver
   ```

5. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

### Web Interface
- Select the type of measurement (Length, Temperature, or Weight).
- Enter the value to convert.
- Choose the source unit ("From") and target unit ("To").
- Click "Convert" to see the result.

### API Usage
Send a POST request to `/api/convert/` with the following JSON payload:

```json
{
  "measurement": "length",
  "value": 100,
  "from": "m",
  "to": "km"
}
```

**Example using curl:**
```bash
curl -X POST http://127.0.0.1:8000/convert/ \
  -H "Content-Type: application/json" \
  -d '{"measurement": "length", "value": 100, "from": "m", "to": "km"}'
```

**Response:**
```json
{
  "result": 0.1
}
```

## Technologies Used

- **Backend:** Django 5.1.7, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5.3.8
- **Database:** SQLite (default Django setup)
- **Deployment:** WSGI/ASGI ready

## Project Structure

- `UnitConverter/`: Main Django project settings
- `mainApp/`: Application logic, including views and conversion modules
- `templates/`: HTML templates


## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## [Inspiration](https://roadmap.sh/projects/unit-converter)
