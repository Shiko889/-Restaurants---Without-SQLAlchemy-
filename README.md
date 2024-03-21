
## Restaurant
**Introduction**
In this code challenge, we'll be working with a restaurant review domain. We have three models: Restaurant, Review, and Customer.

## Instructions
Implement methods in the classes according to the deliverables listed below.
Use SQLite3 to set up the database and create necessary tables.
Test your code in the console as you write it.
First, focus on getting the functionality working. You can refactor your code later for best practices if time allows.
Deliverables
Object Relationship Methods

## Review

customer(): Returns the Customer instance for this review.
restaurant(): Returns the Restaurant instance for this review.
Restaurant

reviews(): Returns all the reviews for the Restaurant.
customers(): Returns all the customers who reviewed the Restaurant.
Customer

reviews(): Returns all the reviews left by the Customer.
restaurants(): Returns all the restaurants reviewed by the Customer.
Aggregate and Relationship Methods
Customer

full_name(): Returns the full name of the customer.
favorite_restaurant(): Returns the restaurant with the highest star rating from this customer.
add_review(restaurant, rating): Adds a new review for the given restaurant with the provided rating.
delete_reviews(restaurant): Deletes all reviews for the specified restaurant.
Review

full_review(): Returns a formatted string representing the review.

## Restaurant

fanciest(): Returns the restaurant with the highest price.
all_reviews(): Returns a list of formatted strings representing all reviews for the restaurant.