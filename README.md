# to-do-django
To do app rest api with authentication 
This used JWT authentication and have a frontend in react (https://github.com/kaushikaryan04/to-do-react)
I have used a custom user model in which email is used for authentication instead of username as it is better.
The user model is linked with a to-do model that stores users to-dos the api only send those to-do that are related to the user by identifying using the Jwt token send by the react frontend.
All features are mostely in the auth app.
