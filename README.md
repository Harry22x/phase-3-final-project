## Inventory management CLI Application

## Description
This Cli application allows a company to keep track of the current items in its inventory. The inventory manager is 
able to look at all the current items in the company's inventory, add items, delete items, update items and also
search for items with a quantity of less than 10 so they can order more. The user can also look at all the company's
suppliers, add a new supplier and delete a supplier. The user can also makae an order which will increase the item's
quantity remaining by however much the quantity the user ordered the item and will add this order to the orders table which will allow them to keep track of every past order.

## Setup/Installation requirements
* Clone the repository from Github
* Navigate to the folder in your terminal
* Run pipenv install and then run pipenv shell
* Enter the lib/ directory and run  alembic upgrade head to initialize the database
* Run seed.py to seed the database
* Run  python cli.py

## Technologies used

* Sql Alchemy
* Python
* Python faker Library
* Alembic
