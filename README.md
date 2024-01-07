# The Great Encyclopedia Web App

## Overview

The Great Encyclopedia web app is a Flask application that allows users to search for entries on Wikipedia and display relevant information, including the entry title, image and text content. Users can submit search queries, and the app fetches and parses data from Wikipedia using the BeautifulSoup library. The parsed information is then displayed to the user through a clean and user-friendly interface.

## Features

### 1. Search Functionality
- Users can enter search queries in the provided input field.
- The app fetches data from Wikipedia based on the user's input.

### 2. Display Entry Information
- The retrieved entry title is prominently displayed at the top of the page.
- Text content of the entry is displayed paragraph by paragraph, providing a comprehensive view of the information.
- An optional image associated with the entry is displayed on the right side of the page.

### 3. Responsive Design
- The application uses Bootstrap for styling, ensuring a responsive and visually appealing design.

## Technologies Used

### 1. Flask
- The web app is built using the Flask framework, a lightweight and efficient web framework for Python.

### 2. BeautifulSoup
- BeautifulSoup is employed for web scraping, enabling the app to extract data from the Wikipedia page's HTML content.

### 3. Requests
- The Requests library is utilised to send HTTP requests to Wikipedia and retrieve the HTML content of the pages.

### 4. HTML/CSS
- The front-end of the application is designed using HTML for structure and CSS (via Bootstrap) for styling.

### 5. Jinja2 Templating
- Jinja2 is used for templating in Flask, allowing dynamic content rendering in the HTML templates.

## How to Run the App

1. Ensure you have Python installed on your system.
2. Install the required Python packages by running:
3. Run the Flask app by executing 'python app.py' in the terminal

4. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the Great Encyclopedia web app.

## Acknowledgments

- The app uses Wikipedia as a data source, and credit goes to Wikipedia for providing open access to their content.

Feel free to explore the Great Encyclopedia web app, search for interesting entries, and discover a wealth of information!
