# Banking Transaction Web App

![Last Commit](https://img.shields.io/github/last-commit/onahte/final_flask_auth?)
![Pull Requests](https://img.shields.io/github/issues-pr/onahte/final_flask_auth?)
![Contributors](https://img.shields.io/github/contributors/onahte/final_flask_auth?)
![Languages](https://img.shields.io/github/languages/count/onahte/final_flask_auth?) 
![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=onahte.final_flask_auth?style=plastic)

This app uses containerization and SQLAlchemy to convert a CSV of financial transactions to SQL, 
which can then be viewed by logging into the webapp. SQL is implemented to store the transactional 
data as well as user login information. Logging has also been enabled using Python's built-in 
Logging library.

# Deployment Status & Links

[![Production Workflow](https://img.shields.io/github/workflow/status/onahte/final_flask_auth/Production?label=Producation&logo=Github)](https://github.com/onahte/final_flask_auth/actions/workflows/prod.yml)

* [Production Deployment](https://onahtefinal-prod.herokuapp.com/)


[![Development Workflow](https://img.shields.io/github/workflow/status/onahte/final_flask_auth/Development?label=Development&logo=Github)](https://github.com/onahte/final_flask_auth/actions/workflows/dev.yml)

* [Developmental Deployment](https://onahtefinal-dev.herokuapp.com/)

# Added Features

As per project requirement, a CSV file can be uploaded and viewed. A balance is calculated and is also viewable on both the main page and the dashboard. Additionally...
* The web app also has a profile pic feature, where an uploaded image will be resized automatically.
* The logs menu item will display all logging to the general.logs file.
* Navigation has been reorganized so that the nav bar displays links for accessing app related actions and the My Account pull down only contains links for account related pages.
