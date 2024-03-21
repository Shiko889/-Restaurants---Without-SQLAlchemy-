class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def reviews(self):
        # Fetch reviews left by this customer from the database
        # Implement SQL query to fetch reviews left by this customer
        pass

    def restaurants(self):
        # Fetch restaurants reviewed by this customer from the database
        # Implement SQL query to fetch restaurants reviewed by this customer
        pass

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Implement logic to find the favorite restaurant of this customer
        pass

    def add_review(self, restaurant, star_rating):
        # Add a new review for the restaurant by this customer to the database
        # Implement SQL query to add a new review
        pass

    def delete_reviews(self, restaurant):
        # Delete all reviews for the given restaurant by this customer from the database
        # Implement SQL query to delete reviews
        pass