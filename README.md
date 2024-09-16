Blogo - Blog Interface
=
Welcome to Blogo, a simple blog interface that allows users to create, view, edit, and delete blog posts. It includes basic user authentication, ensuring only the author can edit or delete their blogs.

Features
=
 - User Authentication:
 - Register a new user
 - Login with an existing user
 - Blog Management:
    - View all blog posts
    - View details of individual blog posts
    - Create a new blog post
    - Edit existing blog posts (only the author)
    - Delete blog posts (only the author)


Tech Stack
=
 - Backend: Python, SQLite for database management.
 - Frontend: CLI-based interface.
 - Dependencies:
    - sqlite3 for database operations.
    - Python's built-in libraries for creating the CLI interface.

Installation
=
  - Clone the repository:
     - git clone https://github.com/sreyas-b-anand/blog-interface-py.git
     - cd blog-interface-py
  - Install the required Python modules:
     - pip install -r requirements.txt
  - Create the SQLite database:
     - The required tables will be automatically created when you first run the application.

Usage
=
 - Run the application:
     - python main.py
 -  Register:
     - New users can register with a username and password.
 -  Login:
     - Existing users can log in using their credentials.
 - Blog Management:
     - After logging in, users can create a new blog, view a blog, edit an existing blog, or delete a blog.
  

Application Flow
=
 - Authentication:
   * Users must either register or log in to access blog operations.
   * Username and password are stored in the database after registration.
 - Main Menu:
   * The main menu provides options to view all blogs, view a specific blog by ID, create a new blog, update or delete a blog, or log out.
  
 License
 =
  - This project is licensed under the MIT License. See the LICENSE file for details
