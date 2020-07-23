# Cinematic  
  
A movie rental system created as a school project for CSC 445 Software Engineering.  
This project is powered by python and the Flask framework.  

The backend of Cinematic is written in Python. The Python Flask package is utilized to initialize the app and run an instance on a local web server. Python’s SQLalchemy package is utilized to initialize an instance of a database in order to store the information of users,  payment information, and create a cart.
Movies are stored as JSON objects and displayed on the movies page.
The front end of Cinematic is written in Javascript and HTML. The front end creates the graphical interface a user can interact with as well as communicating to the backend.

  
Contributors:  
**John Funk**  
**Jon Linton**  
**Wes Thompson**  
**Jesvian Villarroel**  
  
# Installation guide  

### 1.) Download this project by clicking the big green button in the top right, then clicking Download ZIP. Then unzip the file.

If you do not have python 3 installed on your machine, click the following link and follow the instructions to download python for your operating system:
[Download Python](https://realpython.com/installing-python/)

### 2.) After this project has been downloaded, navigate to the downloads folder in your terminal or console.  
Ex:
`cd Downloads`

### 3.) Then, navigate into the project directory:
`cd Cinematic-master`  
  
### 4.) Next, create a virtual environment in that directory: 

**On Mac**     
`python3 -m venv venv`  

**On Windows**      
`virtualenv venv`
  
### 5.) Activate your virtual environment.  

**On a Mac**       
`source venv/bin/activate`  
  
**On Windows**        
`venv\Scripts\activate`  

### 6.) Next, download all of the project dependencies:  
`pip install -r requirements.txt`  
  
### 7.) Finally, run the application: 
 
**On a Mac**  
`python3 movie-rental-system.py`  

**On Windows**  
`movie-rental-system.py`
  
### 8.) In your favorite browser, navigate to this URL:  
`http://127.0.0.1:3001/`

To stop the application press `ctrl + C`
