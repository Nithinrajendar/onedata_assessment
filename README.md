# FoodItems API

This project is a RESTful API built using Django and Django REST Framework for managing food recipes (FoodItems). It provides endpoints to list, create, and update food recipes with validation for unique names. The data is managed in memory rather than a database.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)


## Features
- List all food items with optional filtering by category.
- Create new food items with validation to ensure unique names.
- Update existing food items.

## Technologies Used
- [Django](https://www.djangoproject.com/) - A high-level Python web framework (version 5.1).
- [Django REST Framework](https://www.django-rest-framework.org/) - A powerful toolkit for building Web APIs (version 3.15.2).
- Python - Version 3.12.2

## Setup and Installation

### Prerequisites
- Python 3.12.2
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/Nithinrajendar/onedata_assesment.git
cd onedata_assesment
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
The API provides the following endpoints:
- `GET /api/fooditems/`: List all food items, optionally filtered by category.
- `POST /api/fooditems/create/`: Create a new food item.
- `PATCH /api/fooditems/<int:id>/update/`: Update an existing food item by ID.

## Running the Application
To run the development server, execute the following command:

```bash
python manage.py runserver
```

You can access the API at `http://127.0.0.1:8000/api/fooditems/`.
