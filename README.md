# Neighbourhood

##### By Florence Wambui.


![Homepage](/static/images/homepage.png)



### Description
This is a web application that keeps users informed about what's going on in their neighborhood.A user logs in and establishes a profile, decides the kind of information to get based on their location. Users may list their enterprises and view the entries of other businesses in the region and all through the app. Users may also identify local amenities.


### Technology Used

The following languages have been used on this project:

- HTML
- CSS
- Bootstrap
- Python
- Django
- PostgreSQL



- Live link to view the project <a target="_blank" href="https://neighbourhoodconnect.herokuapp.com">Neighbourhood</a>


### User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all projects submitted by any user.
* Click on links to visit a live site.
* Search for Project by title.
* Must be signed up to vote.
* See averages of projects as voted by other users.
* Rate Projects.


### Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete Neighbourhoods, Businesses, Announcements and Amenities.
* Manage the application.


### Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all Businesses| **Home page** | View all businesses posted from all neighbourhoods|
| To add a business  | **Through Admin dashboard and Authenticated Users Homeview** | Click on add and upload respectively|
| To add an amenitiy  | **Through Admin dashboard and Authenticated Users Homeview** | Redirected to the add amenities form details |
| To add an announcement | **Through Admin dashboard and Authenticated Users Homeview** | Redirected to the add announcements form details |
| To search businesses by name | **Enter text in search bar** | Users can search by Business Name|


### Setup Installation

- Copy the github repository url
- Clone to your computer
- Open terminal and navigate to the directory of the project you just cloned to your computer
- Run the following command to start the server using virtual environment

```
python3 -m venv --without-pip virtual
```

- To activate the virtual environment

```
source virtual/bin/activate
```

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

```
pip install -r requirements.txt
```

- Edit the .env file and replace the values with your own Cloudinary credentials and database credentials

- To run the server

```
python manage.py runserver

```

- Open the browser and navigate to http://127.0.0.1:8000/ to see the application in action


### Authors Info
Email Address- gflorencewambui@gmail.com.

Copyright (c) [2022] Florence Wambui.