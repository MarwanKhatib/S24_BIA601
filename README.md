# Vehicle Routing Problem (VRP) Solver

Welcome to the Vehicle Routing Problem (VRP) Solver project! This web application is designed to tackle the VRP using a Genetic Algorithm, providing a practical solution for optimizing delivery routes. Built with Django, it offers an intuitive interface for users to input locations and visualize the optimal route.

## Project Overview

The Vehicle Routing Problem (VRP) is a well-known challenge in logistics and operations research. It involves finding the most efficient routes for a fleet of vehicles to deliver goods to a set of locations. This project implements a Genetic Algorithm to approximate a solution, allowing users to input locations and visualize the computed route on an interactive map.

### Key Features

- **Location Input**: Users can input locations with coordinates through a straightforward form, making it easy to set up the problem.
- **Algorithm Execution**: The application uses a Genetic Algorithm, a method inspired by natural selection, to compute the optimal route.
- **Result Visualization**: The computed route is displayed on an interactive map using Leaflet.js, providing a clear and engaging visual representation.
- **Responsive Design**: The application is designed to be accessible and user-friendly across a range of devices, ensuring a seamless experience.

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.13**: The latest version of Python, ensuring compatibility with modern libraries and features.
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs, used for creating the API endpoints for locations and vehicles.
- **Numpy**: A fundamental package for scientific computing with Python, used in the Genetic Algorithm for numerical operations.
- **Leaflet.js**: A JavaScript library for interactive maps, included via CDN in the HTML for visualizing routes.
- **Docker**: A platform to develop, ship, and run applications in containers.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.

### Installation Steps

#### Method 1: Traditional Setup

1. **Clone the Repository**:
   Begin by cloning the repository to your local machine:
   ```bash
   git clone https://github.com/MarwanKhatib/BIA601.git
   cd BIA601
   ```

2. **Install Dependencies**:
   Install the necessary Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   Set up the database by running migrations:
   ```bash
   python manage.py migrate
   ```

4. **Start the Django Server**:
   Launch the server to start the application:
   ```bash
   python manage.py runserver
   ```

#### Method 2: Using Docker

1. **Clone the Repository**:
   Begin by cloning the repository to your local machine:
   ```bash
   git clone https://github.com/MarwanKhatib/BIA601.git
   cd BIA601
   ```

2. **Run with Docker**:
   Build and start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**:
   Open your web browser and navigate to `http://localhost:8000/` to start using the application.

## Usage Guide

1. **Add Locations**: Use the form on the homepage to add locations by entering a name and coordinates. This step is crucial for setting up the problem.
2. **Execute Algorithm**: Click the "Run VRP Algorithm" button to compute the optimal route. The algorithm will process the input data and provide a solution.
3. **View Results**: The best route and total distance will be displayed, and the route will be drawn on the map, allowing you to visualize the solution.

## Developer Information

This project was developed by [Your Name] as part of a senior project. It demonstrates the application of genetic algorithms in solving complex optimization problems like the VRP. The project reflects a deep interest in logistics and algorithmic problem-solving.

## Acknowledgments

- The project utilizes Leaflet.js for map visualization, chosen for its simplicity and effectiveness.
- The Genetic Algorithm implementation is inspired by various academic resources and online tutorials, reflecting a blend of theoretical knowledge and practical application.
