# Blog Application with User Profiles

## Overview
This is a simple blog application built with Django that allows users to register, log in, create blog posts, and view posts by other users. It includes user authentication, profile management, and post management features.

## Features
### Core Features
- **User Authentication**
  - Users can register, log in, and log out.
 
- **User Profiles**
  - Each user has a profile with a bio and profile picture.
  - Users can edit their profile.
    
- **Blog Posts**
  - Authenticated users can create, edit, and delete their blog posts.
  - Each post has a title, content
  - Clicking on a post title takes the user to a detailed view of the post.
  - 
- **Styling**
  - Uses Bootstrap or another CSS framework for a visually appealing UI.

### Bonus Features (Optional)
- **Pagination**
  - Displays 3 posts per page on the homepage.
- **Search**
  - Users can search for blog posts by title or author.

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- Virtual environment tool (blog)

### Steps to Install
1. **Clone the Repository**
   ```sh
   git clone https://github.com/Swathikk-97/Simple_Blog
   cd blog_app
   ```
2. **Create a Virtual Environment & Activate it**
   ```sh
   python -m venv blog
   source blog/bin/activate  # On Windows use: blog\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```
5. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
6. **Access the Application**
   - Open a browser and go to `http://127.0.0.1:8000/`




