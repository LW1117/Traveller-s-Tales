# Traveller's Tales
 
This repository contains the code for a tourism destinations review website. Users can browse and review various tourism destinations around the world. This README file provides instructions on setting up a virtual environment, installing the necessary dependencies from requirements.txt, and running the server.

## Virtual Environment
To ensure a clean and isolated installation of the project's dependencies, it is recommended to set up a virtual environment. Follow the steps below to create a virtual environment using venv:

#### Open your terminal or command prompt.

#### Navigate to the project's directory: 
`cd <dir/root>.`

#### Create a new virtual environment:

On macOS and Linux:
`python3 -m venv venv`

On Windows:
`python -m venv venv`

#### Activate the virtual environment:

On macOS and Linux:
`source venv/bin/activate`

On Windows:
`venv\Scripts\activate`

## Dependencies
This project utilizes various dependencies, which are listed in the requirements.txt file. To install these dependencies, follow the steps below:
Make sure you have activated the virtual environment as mentioned in the previous section.
Run the following command to install the required dependencies:

`pip install -r requirements.txt`

## Usage
Running the Server
Once you have set up the virtual environment and installed the dependencies, you can run the server. Follow the steps below:

Activate the virtual environment if it is not already activated (refer to the Virtual Environment section for activation instructions).

Run the following command to start the server:

`python manage.py runserver`

Open your web browser and navigate to http://localhost:8000 to access the tourism destinations review website.
