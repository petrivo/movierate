# Movierate

Movierate is a simple Flask web app which gives user ability to compare seen movies and then display them in a way that each consequent movie is liked less than the previous one. The idea is that it is hard to tell right away what movie you like the most of all. By comparing only two movies at a time you can build such a list. Having every movie compared to every other in a user seen list algorithm inserts them in Binary Search Tree and then by traversing postorder one can get most to least liked movie list.

This is a small CRUD web app with complete user login and registration system. It is built using Application Factory pattern.
Movie details such as poster, name and additional info are rendered on a client side using javascript fetch calls to OMDB API. Most of client-server communication is done using AJAX calls.

Frameworks and technologies used in this project: 
* Flask
* Flask-SQLAlchemy
* Flask-login
* WTForms/WTForm-Alchemy
* SQLite
* Gunicorn
* Click
* Bootstrap 4
