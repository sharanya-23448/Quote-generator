# Quote Generator with History

A Flask-based web application that fetches random quotes from an external API and stores quote history in an SQLite database.

## Features

* Generate random quotes
* Fetch quotes from external API
* Store quote history in database
* Display previously generated quotes
* Flask backend integration

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS
* Requests Library

## Project Structure

quote-generator/

│

├── app.py

├── quotes.db

│

├── templates/

│ └── index.html

│

└── static/

└── style.css

## API Used

https://zenquotes.io/api/random

## How to Run

1. Install required libraries

pip install flask requests

2. Run the application

python app.py

3. Open browser

http://127.0.0.1:5000

## Functionality

* Fetches a random quote from API
* Saves quote and author into SQLite database
* Displays quote history dynamically
* Generates a new quote every refresh/button click

## Author

Sharanya Akula
