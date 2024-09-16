Blog Interface

- This is a Python-based blog management interface that allows users to create, edit, view, and delete blog posts. The project includes user authentication and 
 ensures that only the author of a blog post can modify or delete their content. It uses SQLite for data storage and basic command-line interaction.

Features

- User Registration & Login: Secure user registration and login with password hashing.
- Create Blog : Users can create new blog posts with a title, content, and automatic date tracking.
- View Blog: View all blogs or a single blog post by its ID.
- Edit Blog: Only the author of a blog post can edit its content.
- Delete Blog: Only the author can delete their blog post.
- Command-line Interface: Easy interaction with blog management through the terminal.

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
