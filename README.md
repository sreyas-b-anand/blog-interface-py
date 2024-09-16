Blogo - Blog Interface
Welcome to Blogo, a simple blog interface that allows users to create, view, edit, and delete blog posts. It includes basic user authentication, ensuring only the author can edit or delete their blogs.

Features
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
Backend: Python, SQLite for database management.
Frontend: CLI-based interface.
Dependencies:
sqlite3 for database operations.
Python's built-in libraries for creating the CLI interface.ommand-line Interface: Easy interaction with blog management through the terminal.

blogo/
├── auth/
│   └── user.py          # Handles user registration and login
├── operations/
│   ├── blogOperations/  # Handles blog operations (CRUD)
│   └── dbOperations.py  # Database table creation and setup
├── main.py              # Main entry point of the application
├── README.md            # Project documentation
└── requirements.txt     # Python package dependencies


Setup Instructions

- Clone the repository : git clone https://github.com/sreyas-b-anand/blog-interface-py.git

- Install dependencies :  Set up a virtual environment and install the required Python packages:

- python3 -m venv env
   - On macOS/Linux : source env/bin/activate
   - On Windows: env\Scripts\activate
   - 
- pip install -r requirements.txt
- 
- Database Setup: The SQLite database will be automatically created when you run the project. However, you can modify the database schema in 
  operations/dbBlog/dbBlog.db.

- Run the Project: Start the blog interface from the terminal:

- python main.py


Usage

- Register a user: The system prompts for a username and password to create an account.

- Login: Enter your username and password to log in.

- Create, edit, view, and delete blogs: Once logged in, you can manage blogs based on the provided options.


Future Enhancements

- Add user roles and permissions.
- Implement a web interface with Flask or Django.
- Improve security with session management








#   b l o g o - p y t h o n 
 
 #   b l o g - i n t e r f a c e - p y 
 
 #   b l o g - i n t e r f a c e - p y 
 
 #   b l o g - i n t e r f a c e - p y 
 
 #   b l o g - i n t e r f a c e - p y 
 
 
