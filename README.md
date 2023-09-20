# Vehicle Registration Number Recognition 🚙

A simple web application to detect the registration number of the vehicle from the uploaded image. The application uses the OpenALPR library to identify the registration number. Users can go to the application, upload any vehicle's image and get the registration number. Currently, the application can detect only US-based vehicle registration numbers. Support for other countries will be added to the application in the near future. 

## Dashboard UI
![Vehicle Registration Number Recognition]()

## Features 🤩

✅ 

## Tech stack 👨‍💻

* Frontend
    * HTML5
    * CSS3
    * MaterializeCSS
    * Javascript
* Backend
    * Python
    * Django
    * PostgreSQL
    * OpenALPR

## Table of contents 📃

1. What is ALPR?
2. How to install ALPR?
3. Project Setup
4. Database Setup
5. Class Diagram
6. ER Diagram
7. Project Demo
8. Anticipated features

## What is ALPR? 🤔
[OpenALPR](https://github.com/openalpr/openalpr) is an open-source Automatic License Plate Recognition library written in C++ with bindings in C#, Java, Node.js, Go, and Python. The library analyzes images and video streams to identify license plates. The output is the text representation of any license plate characters.

## How to install ALPR? 🤔
**For Ubuntu:** Follow the steps mentioned [here](https://gist.github.com/braitsch/ee5434f91744026abb6c099f98e67613) to install the necessary packages and libraries required in order for ALPR to function smoothly

After doing that, go to `/openalpr/src/bindings/python` and run `python setup.py build` followed by `sudo python setup.py install`
This will install the OpenALPR library onto your system.

## Project Setup 🛠
**Note**: Make sure you have Python version 3.8+ and Postgres 14 or above

Environment Setup

`$ git clone https://github.com/Akash1362000/Vehicle-Registration-Number-Recognition.git`

`$ cd plate-detector/`

Create `.env` file (refer `.env.example` file)

Generate `SECRET_KEY` from [here](https://djecrety.ir/)

## Database Setup 💻

Install Postgres Latest version from [here](https://www.postgresql.org/download/)

Install pgAdmin from [here](https://www.pgadmin.org/download/)

Create a Database using pgAdmin by following the steps mentioned [here](https://www.tutorialsteacher.com/postgresql/create-database)

Update your `DATABASE_NAME`, `DATABASE_USER` and `DATABASE_PASSWORD` in `.env` with your DB details

Install requirements

`$ pip install -r requirements.txt`

`$ pre-commit install`

`$ python manage.py migrate`

Create superuser: `$ python manage.py createsuperuser`

That's it. You're all Set!

Run `python manage.py test` to check whether ALPR is properly installed on your system

To run the server: `$ python manage.py runserver`

Open your desired browser and head over to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Class Diagram ✍
![Vehicle Registration Number Recognition Class Diagram](https://github.com/Akash1362000/Vehicle-Registration-Number-Recognition/blob/main/plate_detector/diagrams/class_diagram.png)

## ER Diagram ✍
![Vehicle Registration Number Recognition ER Diagram](https://github.com/Akash1362000/Vehicle-Registration-Number-Recognition/blob/main/plate_detector/diagrams/ER_Diagram.png)

## Project Demo 📽
![Vehicle Registration Number Recognition Project Demo]()

## Anticipated Features 🔥

* Add support to detect registration numbers of Indian Vehicles
* Add support to detect registration numbers from video files
* Add support to store the uploaded images safely on Amazon S3
* Dockerize the application
