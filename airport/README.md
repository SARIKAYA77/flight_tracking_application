# Flight-Tracking-Application

This is a simple application with you can add, delete, update your flights and view the number of flights. .

## How to run the project via Docker

- Make sure docker engine is running and resource is given as project directory

    ```
    $ start-engine docker
    $ docker run" from terminal
    $ "docker-compose up" 
    
    ```

## How to run the project locally

- Clone the repository.

git clone https://github.com/SARIKAYA77/flight_tracking_application.git

Open your terminal and follow the below steps :

- Change Directory 

  ```change directory
  $ cd airport
  ```
- Next create a virtual environment and install the dependencies.

    ``` source venv/bin/activate
    pip install -r requirements.txt ```

- Get the server running

  ```runserver
  $ python manage.py runserver
  ```