# Django HTMX Student List

A basic Django project demonstrating how to use HTMX with Django to fetch data from the backend. This project retrieves a list of students and displays them in the frontend.

## Features
- Fetches student names from the Django backend
- Demonstrates how to integrate HTMX with Django views
- Simple and easy to understand, ideal for beginners

## Requirements

- Python 3.x
- Django 3.x or 4.x
- HTMX (loaded via CDN in the HTML templates)
- tzdata

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Benedict086005/Htmx-And-Django-Simple-Project.git 
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Make migrations and Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

6. **Visit the project in your browser**:
   Go to `http://127.0.0.1:8000/admin` to add student data of your choice {Dont forget to create superuser }.

## Project Structure

- **models.py**: Defines a `Student` model with fields like `name`.
- **views.py**: Contains views to fetch and return student data.
- **templates**: HTML templates using HTMX to display student names dynamically.

## Usage

When you visit the main page, HTMX will automatically fetch the list of students from the backend after the page loads and display them.

## Example Code Snippets

### HTML Template

```html




{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>HTMX TRIAL WITH BOOTSTRAP</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link href="{% static 'css/index.css' %}" rel="stylesheet">     # Y O U    C A N   U S E    B O O T S T R A P   C D N    H E R E
 <script src="https://unpkg.com/htmx.org@1.9.2"></script>
  
  </head>
  <body>

  {% block content %}
  
  {% endblock content %}
  </body>
</html>
```

### Django View

```python
from django.shortcuts import render
from . models import Students


def home(request):
    return render(request,'app/home.html')



def students(request):
    students = Students.objects.all()
    context = {
        "students" : students
    }
    return render(request, 'extra/students.html', context)


```

## Contributing

Feel free to fork the repository and make improvements. Pull requests are welcome!

## License

This project is open source and available under the [MIT License](LICENSE).
