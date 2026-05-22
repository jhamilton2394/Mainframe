# Mainframe

Mainframe was created to modernize aviation maintenance project tracking. It aims to do away with the old book-and-pen passdown and the microsoft word passdown.
It eliminates data loss and cuts down time spent flipping pages. Mainframe can easily be adapted to any organizations' style of collaboration.

Mainframe allows teams to:
- quickly and easily get up to date with current projects
- add further progress to existing projects
- retrieve and review every step taken on previous projects
- analyze and identify recurring issues with individual aircraft

Installation:

1. Download code or clone repo, then ensure python 3.11 is installed.

2. Install python packages from requirements.txt
```Python
pip install -r requirements.txt
```
3. Install PostreSQL and create a user with sufficient permisions, and a database. Note the port and the host name.

4. Inside the passdown_project2 folder create a file called ".env". Copy and paste the contents of .template.env into the .env file.
   Set your django secret key to anything you like, then fill in the database info from step 3.

5. Make migrations for the new database:
```Python
python manage.py makemigrations

python manage.py migrate
```
6. Install node.js version 14 or later, and npm

7. Open two terminal windows inside your project directory. In both enter the following:

```Bash
export READ_DOT_ENV_FILE=True
```
This will set your environment variables for the session. This will need to be done any time you open the project.

8. In terminal 1 type the following:
```Python
python manage.py runserver
```
and in terminal 2 type the following:

```Python
python manage.py tailwind install
python manage.py tailwind start
```
