# Article Recommendation Engine

## Project Overview

This project involves building a simple article recommendation engine using word vectors (word2vec). The goal is to create an application that recommends similar articles based on the similarity of their content. The project consists of two main components: `doc2vec.py` and `server.py`, along with accompanying HTML templates.

## Project Files

The project directory includes the following files:

- **doc2vec.py**: This Python script is responsible for processing the GloVe word vector database and generating recommendations for articles. It implements functions for loading GloVe vectors, computing word vector centroids for articles, and generating recommendations based on similarity.

- **server.py**: This Python script contains the Flask web server implementation. It serves as the backend for the article recommendation application, providing routes for accessing the list of articles and viewing individual articles.

- **templates**: This directory contains HTML templates used by the Flask server to generate the user interface. 
    - **article.html**: Template for displaying an individual article along with recommended articles.
    - **articles.html**: Template for displaying a list of articles.

## Project Functionality

The article recommendation engine works as follows:

1. **Data Processing**: The `doc2vec.py` script loads word vectors from the GloVe database and computes word vector centroids for each article in the corpus.

2. **Recommendation Generation**: Based on the similarity of article centroids, the script generates recommendations for similar articles. These recommendations are stored in a dictionary format and used by the web server.

3. **Web Server Implementation**: The `server.py` script implements a Flask web server that provides routes for accessing the list of articles and viewing individual articles. It uses Jinja2 templating to generate HTML pages dynamically.

4. **User Interface**: The user interface consists of two main pages:
    - **List of Articles**: Displays a list of articles with clickable links to view individual articles.
    - **Individual Article**: Displays the text of an individual article along with a list of recommended articles based on similarity.

## Getting Started

To run the application locally:

1. Download the GloVe word vector database and BBC corpus data.

2. Run the `doc2vec.py` script to process the data and generate article recommendations.

3. Run the `server.py` script to start the Flask web server.

4. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Requirements:

- Flask
- NumPy
- Python

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
