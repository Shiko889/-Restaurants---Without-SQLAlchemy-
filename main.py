import os
import sqlite3
from restaurant import Restaurant
from review import Review
from customer import Customer

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

# Create sample instances
restaurant1 = Restaurant("Restaurant 1", 10)
restaurant2 = Restaurant("Restaurant 2", 20)
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Doe")

# Add reviews
review1 = Review(restaurant1, customer1, 5)
review2 = Review(restaurant2, customer2, 2)

# Test object relationship methods
print("Customer 1's reviews:", customer1.reviews())
print("Customer 2's reviews:", customer2.reviews())
print("Restaurant 1's reviews:", restaurant1.reviews())
print("Restaurant 2's reviews:", restaurant2.reviews())

# Test aggregate and relationship methods
print("Customer 1's full name:", customer1.full_name())
print("Customer 2's full name:", customer2.full_name())

# Check if reviews are good or poor
print("Review 1 is good:", review1.is_good_review())
print("Review 1 is poor:", review1.is_poor_review())
print("Review 2 is good:", review2.is_good_review())
print("Review 2 is poor:", review2.is_poor_review())
# Create or connect to the SQLite database
conn = sqlite3.connect('restaurant_reviews.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                restaurant_id INTEGER,
                customer_id INTEGER,
                star_rating INTEGER,
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )''')

# Create restaurants table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS restaurants (
                id INTEGER PRIMARY KEY,
                name TEXT,
                FOREIGN KEY (id) REFERENCES customers(id)
            )''')

# Prompt customers for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
restaurant_name = input("Enter the name of the restaurant you want to review: ")
star_rating = int(input("Enter your rating (1-5 stars): "))

# Create or retrieve restaurant instance
c.execute("SELECT id FROM restaurants WHERE name=?", (restaurant_name,))
row = c.fetchone()
if row:
    restaurant_id = row[0]
    restaurant = Restaurant(restaurant_name, restaurant_id)
else:
    c.execute("INSERT INTO restaurants (name) VALUES (?)", (restaurant_name,))
    restaurant_id = c.lastrowid
    restaurant = Restaurant(restaurant_name, restaurant_id)

# Create or retrieve customer instance
c.execute("SELECT id FROM customers WHERE first_name=? AND last_name=?", (first_name, last_name))
row = c.fetchone()
if row:
    customer_id = row[0]
    customer = Customer(first_name, last_name)  # Removed customer_id argument
else:
    c.execute("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
    customer_id = c.lastrowid
    customer = Customer(first_name, last_name)  # Removed customer_id argument

# Create review instance
review = Review(restaurant, customer, star_rating)

# Commit changes to the database
conn.commit()

# Close database connection
conn.close()