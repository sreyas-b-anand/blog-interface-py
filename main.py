#Welcome to Blogo, a simple blog interface that allows users to create, view, edit, and delete blog posts. 
#It includes basic user authentication, ensuring only the author can edit or delete their blogs.

from auth.user import user 
from operations.blogOperations import blogOperations as b
from operations.dbOperations import createTable as c 

 

#creating a table
c.createTable()

#main menu
def mainMenu():
    print("\n")
    print("All Blogs")
    print("**********************")
    blogs = b.fetchData()  # Fetch all blogs
    if blogs:
        b.displayData(blogs)                      # Display the blog title , date , author and ID
    else:
        print("\nNo blogs to show . Please add a blog\n")       
    print("\nOptions:")
    print("1. View a blog")
    print("2. Create a blog")
    print("3. Update a blog")
    print("4. Delete a blog")
    print("5. Logout")
    print("**********************\n")

#blog operations
def blogFunctions():
    while True:
        mainMenu()
        
        option = input("Choose an option (1/2/3/4/5): ").strip()

        if option == '1':
            blogId = input("\nEnter the blog ID to view : ").strip()
            blog = b.fetchOne(blogId)  # Fetch a specific blog by ID
            if blog:
                print("*******************")
                print(f"\nTitle: {blog[0]}")
                print(f"Date: {blog[2]}  |  Author : {blog[3]}")
                print(f"Content: {blog[1]}")
                print("*******************")
            else:
                print(f"No blog found with ID {blogId}.")

        elif option == '2':
            b.createBlog(USERNAME)  #  create a blog

        elif option == '3':
            blogId = input("\nEnter the blog ID to update : ").strip()
            b.editBlog(USERNAME , blogId)  #edit a blog
                
        elif option == '4':
            blogId = input("\nEnter the blog ID to delete : ").strip()
            b.deleteBlog(USERNAME , blogId)  # delete a blog
                
        elif option == '5':
            print("\nExiting the blog application.\n")
            break
        else:
            print("\nInvalid Entry\n")
            
        input("\nPress ENTER to return to main menu....")

#authentication
def authentication():
    global USERNAME
    while True:
        print("1.Register")
        print("2.Login")
        print("3.Close")

        choice = input("Choose an option(1/2/3) : ")
        

        if choice == '1':
            username=input("Enter username : ")  
            password=input("Enter password : ")
            USERNAME = username
            if user.registerUser(username , password):
                print("\nRegisterd successfully\n")
                print(f'\nWELCOME {USERNAME}\n')
                blogFunctions()
        elif choice == '2':
            username=input("Enter username : ")  
            password=input("Enter password : ")
            USERNAME= username
            if user.verifyUser(username , password):
                print("\nLogin successfull\n")
                print(f'\nWELCOME {USERNAME}\n')
                blogFunctions()
            else:
                print("\nInvalid username or password.Please try again\n")
        elif choice == '3':
            print("\nClosing the application\n")
            break
        else:
            print("Invalid Entry . Please try again\n")



def main():
    print("\nWelcome to Blogo\n")
    authentication()
if __name__ :
    main()