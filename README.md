# Preview ✨

![Image](static\images\preview.PNG)

# Guidelines on how to run locally 💻

## Clone this repository

```
https://github.com/Mannuel25/E-Commerce-App.git
```

## Change directory
Change your directory to where you cloned the repository

```
cd E-Commerce-App
```

## Create a virtual environment in the cheqqit directory
Ensure you are in the cheqqit directory, run this command to create a virtual environment:
```
python -m venv .\venv
```
## Activate the virtual environment
Activate the virtual environment using the following command: 
```
venv\scripts\activate
```
Note: Upon running the command **venv\scripts\activate**, if this error shows up:
```
venv\scripts\activate : File C:\Users\Training\Documents\New folder\venv\scripts\Activate.ps1 cannot be loaded because running scripts is 
disabled on this system. For more information, see about_Execution_Policies at http://go.microsoft.com/fwlink/?LinkID=135170.
```
Run this command: 
``` 
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted 
```
Then run the command to activate the virtual environment
## Install all necessary packages 

```
pip install -r requirements.txt
```

## Make migrations
Run the following commands separately to make migrations
```
python manage.py makemigrations
python manage.py migrate
```
## Create a new superuser
Run the following command to create a new superuser
```
python manage.py createsuperuser
```

## Run the project

```
python manage.py runserver
```
<hr>

## Products 🛍️
##### Every product to be added must be grouped into the following categories: `Clothings, Phone and Accessories, Home and Office, Health and Beauty, Gaming`. Each product should have an image which should be added in their respective folder. Add all:
    - Clothing product images to `clothings` folder.
    - Phones & Accessories product images to `phones_accessories` folder.
    - Gaming product images to `gamings_accessories` folder.
    - Health & Beauty product images to `health_beauty` folder.
    - Home & Office product images to `home_office` folder.


# License 🔐
Thsi project is under an [MIT LICENSE](LICENSE)
