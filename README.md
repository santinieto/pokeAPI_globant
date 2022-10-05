INTRODUCTION

* The idea of this project is to create a Pokeberries statistics API. The system is feed using an external api named pokeAPI. In the link below you can find the documentation about the API. What we will use from the external API is the berries information.

* pokeAPI link: https://pokeapi.co/docs/v2#berries

* This project was made using:
    1. Python
    2. Django
    3. An external API named pokeAPI
    4. Bootstrap 5

* This project is intended to evaluate the skills of an applicant for a job position of Python Developer.


* What are berries? ---> Berries are small fruits that can provide HP and status condition restoration, stat enhancement, and even damage negation when eaten by Pokémon.

* We will collect the berries information and measure some statistics like mean, median, variance, etc.

FOLDER STRUCTURE

* There are two main forlders:
    1. globantWebsite: In this folder the main project is located. Inside we have both main server files and pokeAPI application for this particular project
    2. ipython_test: In this folder i put the Jupyter notebok that i use to test the data collections from pokeAPI

The most important files are:
* ./.gitignore ---> This file indicates git to ignore specific files/folders o something that accomplish with some conditions
* ./README.md ---> This files
* ./Output.pdf ---> You can see an example that the Berries' information URL shows
* ./globantWebsite/settings.py ---> In this file we indicate the server to find the application
* ./globantWebsite/urls.py ---> Where the URLs of the website are defined
* ./globantWebsite/pokeAPI/views.py ---> Where what to do for every URLs petition is defined
* ./globantWebsite/pokeAPI/templates/ ---> Where you can find the HTML codes for the website
* ./globantWebsite/pokeAPI/static/ ---> Where you can find all related to the esthetic of the website (i.e., Bootstrap 5 files)
* ./globantWebsite/pokeAPI/pokeAPI_scripts/pokeAPI_scripts.py ---> This is the file where the description of how to get the data from the external API is described

HOW TO RUN AND USE THE APPLICATION

1. First at all, you will need to have the last version of the 'master' branch from the free GitHub repository 'pokeAPI_globant'. You can clone using the command:

$ git clone https://github.com/santinieto/pokeAPI_globant.git

NOTE: You can switch the branch repository from anyone to master using $ git checkout master 

2. The next thing that you will need is a command prompt with both Python and Django installed (for this project i used the Python version python3). After cloning the repository, you will need to move inside the project folder:

$ cd pokeAPI_globant/globantWebsite

3. Next, to start the server you will have to run the command

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

Take in note that you must connect to the IP 'http://127.0.0.1:8000/' (or the IP that the command promt show for every particular case) to access to the server.

4. You will have a few URLs to connect from the server:
* '' ---> This is the default HTML template that you will see when connecting to the server
* 'index' ---> The same as previous case
* 'inicio' ---> The same as previous case
* 'all-berry-stats' ---> In this URL you will see the berries’ information (take in note that the website takes near to 30 seconds to get the data from the external API)
* 'contact' ---> You will have the project's owner information links

5. Whenever you desire to stop the server you can go to the command prompt and press Ctrl + C to terminate the server

BERRIES' INFORMATION

With the server turned on, as said before you will have to connect to <localhost>/all-berry-stats. After getting the data, the server will show you:
* The names of the different berries that were get from pokeAPI
* Statistics about the growing information for the berries (mean, median, variance, frequencies, etc)
* An histogram plot showing the occurrences for each value of "grow_time"
* A plaing JSON information that was used to show the previous information

PYTHON SCRIPTS UNITARY TESTING

In the directory ./ipython_test/ you can find the Jupyter notebook that i used to test the main functions to get the data from the external API. To complement the unitary test i included the 'main' function in the script ./pokeAPI_globant/globantWebsite/pokeAPI/pokeAPI_scripts/pokeAPI_scripts.py that is useful to test the code that was finally implemented for this project. You can run the script unitarily with:

$ python ./pokeAPI_globant/globantWebsite/pokeAPI/pokeAPI_scripts/pokeAPI_scripts.py

If everything is OK, you will see the information for every berry type and the histogram thtat the website shows.






