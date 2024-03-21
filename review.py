class Review:
    def __init__(self, restaurant, customer, star_rating):
        self.restaurant = restaurant
        self.customer = customer
        self.star_rating = star_rating

    def is_good_review(self):
        return self.star_rating >= 4

    def is_poor_review(self):
        return self.star_rating < 4

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."