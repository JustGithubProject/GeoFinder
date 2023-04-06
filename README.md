# GeoFinder Microservice

This microservice is built using FastAPI and provides the latitude and longitude coordinates of a city based on user input.

## Installation

1. Clone the repository: `git clone https://github.com/username/city-to-coords-microservice.git`
2. Navigate to the project directory: `cd city-to-coords-microservice`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Run the application: `uvicorn main:app --reload`

## Usage

1. Open your web browser and navigate to `http://localhost:8000/`.
2. Enter the name of a city in the input field and click "Get Location".
3. The latitude and longitude coordinates of the city will be displayed.

## API Documentation

The API documentation can be found at `http://localhost:8000/docs`.

## Contributing

Contributions are always welcome. If you have any ideas, bug reports, or feature requests, please create an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
