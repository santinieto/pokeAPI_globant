INTRODUCTION

* The idea of this project is to create a Pokeberries statistics API. The system is feed using an external API named pokeAPI. In the link below you can find the documentation about the API. What we will use from the external API is the berries information.

* pokeAPI link: https://pokeapi.co/docs/v2#berries

* This project was made using:
    1. Python
    2. Django
    3. An external API named pokeAPI
    4. Bootstrap 5
    5. Numpy
    6. Matplotlib

* This project is intended to evaluate the skills of an applicant for a job position of Python Developer.

* What are berries? ---> Berries are small fruits that can provide HP and status condition restoration, stat enhancement, and even damage negation when eaten by Pokémon.

* We will collect the berries information and measure some statistics like mean, median, variance, etc.

FOLDER STRUCTURE

* There are two main forlders:
    1. globantWebsite: In this folder the main project is located. Inside we have both main server files and pokeAPI application for this particular project
    2. ipython_test: In this folder i put the Jupyter notebok that i use to test the data collections from pokeAPI

The most important files are:
* ./.gitignore ---> This file indicates git to ignore specific files/folders o something that accomplish with some conditions
* ./README.md ---> This file
* ./Output.pdf ---> You can see an example that the Berries' information URL shows
* ./globantWebsite/settings.py ---> In this file we indicate the server to find the application
* ./globantWebsite/urls.py ---> Where the URLs of the website are defined
* ./globantWebsite/.env ---> In this file we can find all the environmental variables for the project
* ./globantWebsite/requirements.txt ---> In this file we can find all the needed Python packages used in this project
* ./globantWebsite/pokeAPI/views.py ---> Where what to do for every URLs petition is defined
* ./globantWebsite/pokeAPI/templates/ ---> Where you can find the HTML codes for the website
* ./globantWebsite/pokeAPI/static/ ---> Where you can find all related to the esthetic of the website (i.e., Bootstrap 5 files)
* ./globantWebsite/pokeAPI/pokeAPI_scripts/pokeAPI_scripts.py ---> This is the file where the description of how to get the data from the external API is described
* ./lin-env ---> Folder where the environment for Linux is located
* ./win-env ---> Folder where the environment for Windows is located

DOWNLOADING THE REPOSITORY

First at all, you will need to have the last version of the 'master' branch from the free GitHub repository 'pokeAPI_globant'. You can clone using the command:

$ git clone https://github.com/santinieto/pokeAPI_globant.git

SETTING UP THE ENVIROMENT

Before running the project there are a few steps that you must do. The ones that are marked with (*) need to be done only once.

The next thing that you will need is a command prompt with both Python and Django installed (for this project i used the Python version python3). After cloning the repository, you will need to move inside the project folder:

1. After cloning the repository, go into and switch to master branch:

$ cd pokeAPI_globant
$ git checkout master 

2. Next step is to set up the environment, so go to the server folder

$ cd pokeAPI_globant/globantWebsite

and run:

$ ..\win-env\Scripts\activate.bat (on Windows) 
$ source ../lin-env/bin/activate (on Linux)  

and the command prompt should now have the subscript "(lin-env)" or "(win-env)" according to the Operative System.

3. (*) Check the Python libraries you have, as it is the first time you will see a few packages:

- $ pip list
- Package    Version
- ---------- -------
- pip        22.0.2
- setuptools 59.6.0

4. (*) Install the required packages for the project:

$ python -m pip install -r requirements.txt

The required Python libraries will be installed so if you run once again $pip list you must see more libraries now:

- $ pip list
- Package            Version
- ------------------ ---------
- asgiref            3.5.2
- certifi            2022.9.24
- charset-normalizer 2.1.1
- contourpy          1.0.5
- cycler             0.11.0
- decouple           0.0.7
- Django             4.1.2
- fonttools          4.37.4
- idna               3.4
- kiwisolver         1.4.4
- matplotlib         3.6.0
- numpy              1.23.3
- packaging          21.3
- Pillow             9.2.0
- pip                22.0.2
- pyparsing          3.0.9
- python-dateutil    2.8.2
- python-dotenv      0.21.0
- requests           2.28.1
- setuptools         59.6.0
- six                1.16.0
- sqlparse           0.4.3
- tzdata             2022.4
- urllib3            1.26.12

If so, you are ready to run the project

HOW TO RUN AND USE THE APPLICATION

1. To start the server you will have to run the command

$ python manage.py runserver

If everything is alright you will have now a busy command prompt with the messages:

- Watching for file changes with StatReloader
- Performing system checks...
- 
- System check identified no issues (0 silenced).
- October 05, 2022 - 16:13:40
- Django version 4.1, using settings 'globantWebsite.settings'
- Starting development server at http://127.0.0.1:8000/
- Quit the server with CTRL-BREAK.

Take in note that you must connect to the IP 'http://127.0.0.1:8000/' (or the IP that the command prompt show for every particular case) to access to the server.

2. You will have a few URLs to connect from the server:
* '' ---> This is the default HTML template that you will see when connecting to the server
* 'index' ---> The same as previous case
* 'inicio' ---> The same as previous case
* 'all-berry-stats' ---> In this URL you will see the berries’ information (take in note that the website takes near to 30 seconds to get the data from the external API)
* 'contact' ---> You will have the project's owner information links

3. Whenever you desire to stop the server you can go to the command prompt and press Ctrl + C to terminate the server

BERRIES' INFORMATION

With the server turned on, as said before you will have to connect to <localhost>/all-berry-stats. After getting the data, the server will show you:
* The names of the different berries that were get from pokeAPI
* Statistics about the growing information for the berries (mean, median, variance, frequencies, etc)
* A histogram plot showing the occurrences for each value of "grow_time"
* A plaing JSON information that was used to show the previous information

PYTHON SCRIPTS UNITARY TESTING

In the directory ./ipython_test/ you can find the Jupyter notebook that i used to test the main functions to get the data from the external API. To complement the unitary test i included the 'main' function in the script ./pokeAPI_globant/globantWebsite/pokeAPI/pokeAPI_scripts/pokeAPI_scripts.py that is useful to test the code that was finally implemented for this project. You can run the script unitarily with:

$ python ./pokeAPI_globant/globantWebsite/pokeAPI/pokeAPI_scripts/pokeAPI_scripts.py

If everything is OK, you will see the information for every berry type and the histogram that the website shows.

HOW TO CREATE A NEW ENVIROMENT OR UPDATING PACKAGES

If in the future you need to create a new environment you can create a new one with:

$python -m venv <env_name>

You can install all the required libraries and update the 'requirements' file with:

$ pip freeze > requirements.txt

NOTE: Don't forget to commit and push your changes if you have permissions, if not ask an administrator







