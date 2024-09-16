
import datetime
import sqlite3 as db


#connecting to db 
con = db.connect('operations/dbBlog/dbBlog.db')
cur = con.cursor()


#fetch data
def fetchData():
    cur.execute("SELECT id, title, date , author FROM blogs")
    posts = cur.fetchall()
    
    return posts    


#save data
def saveData(title , content , dateString , username):
    cur.execute('''
    INSERT INTO blogs (title, content, date , author)
    VALUES (?, ?, ? , ?)
    ''', (title, content, dateString , username))

    con.commit()
    



#fetch one
def fetchOne(id):
   cur.execute("SELECT title, content, date , author FROM blogs WHERE id = ?", (id,))
   blog = cur.fetchone()
   if not blog:
      return False

   return blog

#display the data
def displayData(blogs):
   for blog in blogs:
      print(f'ID = {blog[0]} | Title = {blog[1]} | Date = {blog[2]} | author = {blog[3]}')    


#create a new blog
def createBlog(username):
    
    title = input("\nEnter the title of your blog : ").strip()
  
    content = input("\nEnter the content of your blog : ").strip()

    dateNow = datetime.date.today()
    dateString = dateNow.strftime("%d-%m-%Y") 
 
    if not title or not content:
        print("\nTitle and content cannot be empty.\n")
        return False


    saveData(title , content , dateString , username)
    con.commit()
    print("\nBlog created successfully!\n")
    return True


#edit blog
def editBlog(username , id):
   cur.execute("SELECT author FROM blogs WHERE id = ?", (id,))#fetch author
   response = cur.fetchone()
   author = response[0]
   if username != author:#verify author is same as username
      print(f"\nCan't edit this blog.\nOnly the blog author ({author}) can edit this blog.\n")
      return False
   print("Previous data")
   cur.execute("SELECT title, content, date FROM blogs WHERE id = ?", (id,))#display previos data
   blog = cur.fetchone()
   if not blog:
      return False
   print(f'Title = {blog[0]}')
   print(f'Content = {blog[1]}')
   print(f'Date = {blog[2]}')
   print("************")
   newTitle = input("Enter new title (Press ENTER to keep the previous title) : ")#entering new data
   newContent = input("Enter new content (Press ENTER to keep the previous content) : ")
   dateNow = datetime.date.today()
   date = dateNow.strftime("%d-%m-%Y")
   title = newTitle if newTitle.strip() else blog[0]
   content = newContent if newContent.strip() else blog[1]
   cur.execute('UPDATE blogs SET title = ?, content = ? , date = ? WHERE id = ?', (title, content,date, id))#saving
   con.commit()
   
   
   print(f"\nPost with ID {id} has been updated.\n")
   return True



#deleting a blog
def deleteBlog(username , id):
   cur.execute('SELECT * FROM blogs WHERE id = ?', (id,))
   blog = cur.fetchone()
   cur.execute('SELECT author FROM blogs WHERE id = ?' , (id,))
   response = cur.fetchone()
   author = response[0]
   if blog:
        author = response[0]

        if author == username:
            cur.execute('DELETE FROM blogs WHERE id = ?', (id,))
            con.commit()
            print(f'\nBlog with ID={id} deleted successfully.\n')
            return True
        else:
            print(f"\nCan't delete blog.\nOnly the blog author ({author}) can delete this blog.\n")
            return False
   else:
       print(f"\nCan't find blog with ID - {id}\n")
       return False
