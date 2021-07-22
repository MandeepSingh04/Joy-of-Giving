# Joy-of-Giving

This is a website for health-care donation purpose. This can be used for health-care donations, educational donations, organizing blood donation camp, etc.
We all know that for a patient suffering from cancer, heart failure, lung disorder, etc., immediate treatment is required. 
This treatment is sometimes very expensive and the families, who are not financially fit pay the bills, become helpless. 
At this time, immediate donations are required. Here, online donation web application plays an important role, since we can reach out a lot of people for help. 
This will make the donation process very fast and we would be able to save life of that patient.
 
Getting funds/donations has a difficult task for the people in need. 
Many a time, people require urgent donation and for that they need to reach out as many people as possible in a very less time in search of donors. 
This donation website will bridge the gap between these needy people and donors. 

## Installation
To run locally, do the usual:
1. Clone the repository::
   ```
   git clone https://github.com/MandeepSingh04/Joy-of-Giving
   ```
2. Move inside the folder
   ```
   cd Joy-of-Giving
   ```
3. Install the requirements::
   ```
   python -m pip install -r requirements.txt
   ```
4. Migrate the tables::
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser::
   ```
   python manage.py createsuperuser
   ```
6. Run
   ```
   python manage.py runserver
   ```
## Software requirements
- Python(3)
- Django
- SQLite

## Technology Used
#### Frontend
- HTML
- CSS
- Bootstrap
#### Backend
- Django
- SQLite database

## How to use
In order to post, you must login in the website. For this, you have to create an account. To create an account, Click on “Signup” button (top-right).
After creating your account, Login using the credentials. <br>
Once you Login, a new tab “Post” will be seen besides the “About Us” tab.<br>
Click on Post to add a new post to the website.<br>

## Note
The images and data used in this website is just for demo purpose.
