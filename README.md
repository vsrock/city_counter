# City Counter

This Django project allows users to enter a letter and see how many cities from a sample OpenWeatherMap API start with that letter.

## Features

- Simple HTML/JS frontend
- Django backend
- Fetches live data from OpenWeatherMap sample API

## Setup Instructions

### Prerequisites

- Python 3.x
- pip
- virtualenv (optional but recommended)

### Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/vsrock/city_counter.git
  cd citycounter

2. Create a virtual environment and activate it:

  python -m venv env
  source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install dependencies:

  pip install django requests

4. Run the server:
  python manage.py runserver
