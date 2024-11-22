# BlogNest

BlogNest is a Django-based blog application that allows users to create, edit, and delete blog posts. It supports rich text content and image uploads for each blog post, offering an intuitive and attractive interface for users.

---

## Features
- **User Authentication**: Secure login and logout functionality.
- **Blog Management**: Authenticated users can create, edit, and delete blog posts.
- **Image Upload**: Blog posts support image attachments.
- **Responsive Design**: Fully responsive and visually appealing user interface.

---

## Prerequisites
Before setting up the project, ensure the following dependencies are installed:
- Python 3.10 or higher
- Django 5.1.3
- A virtual environment tool (e.g., `venv` or `virtualenv`)
- pip (Python package manager)

---

## Setup Instructions

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/BlogNest.git
   cd BlogNest
   ```
   
2. **Set Up a Virtual Environment**
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # For macOS/Linux
venv\Scripts\activate       # For Windows
```

3. **Install Dependencies**
4. Install the required Python packages:
```bash
pip install -r requirements.txt
```

4. **Apply Migrations**
Set up the database by running migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a Superuser**
Create an admin user for accessing the admin panel:
```bash
python manage.py createsuperuser
```

6. **Run the Development Server**
Start the local development server:
```bash
python manage.py runserver
```

7. **Access the Application**
 i)   Open a browser and navigate to http://127.0.0.1:8000 to view the application.
 ii)  To access the admin panel, go to http://127.0.0.1:8000/admin.


***Application Functionality***
  i) **Homepage**: Displays all published blog posts with their images, titles, and excerpts.
  
  ii) **Post Detail**: View the full content of a specific blog post.
  
  iii) **Create/Edit Posts**: Authenticated users can add or modify blog posts with title, content, and an optional image.
  
  iv) **Delete Posts**: Users can delete their posts.
  
  v) **User Authentication**: Secure login/logout system with signup functionality.

***Additional Notes***
    i) Static Files: Ensure the STATIC_ROOT is configured properly in the deployment settings.
    ii) Media Files: Uploaded images are stored in the MEDIA_ROOT directory. Ensure the appropriate configuration for serving media files in production.




