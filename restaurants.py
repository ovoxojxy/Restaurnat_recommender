import json

# Define restaurant data
restaurant_data = [
    {
        "name": "16th Avenue Diner",
        "cuisine": "American",
        "location": "207 NE 16th Ave, Gainesville",
        "price_range": "$",
        "dietary_options": ["Vegetarian", "Vegan"],
        "dress_code": "Casual",
        "ratings": 4.2
        'menu': '''1. Classic
        2. 2-2 Combo
        3. Big Boy
        4. Corned Beef Hash
        5. Country Fried Steak
        6. Grilled Pork Chops
        7. Steak &amp; Eggs
        8. 2 Pancakes
        9. Bill's Special
        10. Biscuit &amp; Homemade Sausage Gravy
        11. BLT
        12. Breakfast Croissant Sandwich
        13. Breakfast Burrito
        14. Breakfast Sandwich
        15. French Toast
        16. Sausage Biscuit
        17. Grits Bowl
        18. Bill’s Saturday Omelet
        19. Cheese Omelet
        20. Hot-Mex Omelet
        21. Meat Lovers Omelet
        22. Philly Cheese Steak Omelet
        23. Veggie Scramble
        24. Western Omelet
        25. 8 oz Angus Burger
        26. Chicken &amp; Cheese Philly
        27. Fried Chicken Wrap
        28. Chicken Burger
        29. Double Burger
        30. Grilled Cheese
        31. Grilled Chicken Sandwich
        32. Grilled Ham and Cheese
        33. Hawaiian Burger
        34. Patty Melt
        35. Philly Cheese Steak
        36. Ribeye Burger
        37. The Cajun
        38. The New Melt
        39. 6 oz Ribeye &amp; two Sides, Texas Toast 
        40. 2 Grilled Pork Chops &amp; two Sides, Texas Toast    $11.99
        41. Smothered Chicken Breast with two Sides
        42. Country Fried Steak
        43. Chicken Tender &amp; Fries Basket
        44. Salad
        45. Fried Fish
        46. Classic Club
        47. Coffee
        48. Hot Tea
        49. Cocoa
        50. Milk
        51. Jumex
        52. Pink Lemonade
        53. Iced Tea
        54. Soft Drink
        55. Malta
        56. Arnold Palmer
        57. Red Bull
        58. Monster
        59. Apple juice
        60. Orange juice
        61. Water
        62. Café Cubano
        63. Cortadito
        64. 3 Tacos
        65. Burritos
        66. Giant Quesadilla
        67. Nachos
        68. Hamburger with Fries
        69. Chicken Tenders with Fries
        70. 2 Quesadillas
        71. 1 hotcake, 1 egg, 2 bacon
        72. 3 hotcakes w/ choco chips
        73. Neapolitan Flan
        74. Pudin Cubano
        75. Choco Flan'''
    },
    {
        "name": "4 Rivers Smokehouse – Gainesville",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "43rd St Deli & Breakfast – South",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "43rd St Deli & Breakfast – West",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "4 Rivers Smokehouse – Gainesville",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "4th Ave Food Park",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "A’xin Mahzu Sushi & Grill",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Adam’s Rib Co. North",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "afternoon",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Airstream – Opus Coffee",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Alpin Bistro",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Amelia’s Italian Cuisine",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
    {
        "name": "Bagel Bakery",
        "cuisine": "Mexican",
        "location": "456 Oak Ave",
        "distance": "2 miles",
        "price_range": "$",
        "dietary_options": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5
    },
]

# Specify the file path where you want to save the JSON file
file_path = 'restaurants.json'

# Write restaurant data to JSON file
with open(file_path, 'w') as json_file:
    json.dump(restaurant_data, json_file, indent=4)

print(f"JSON data has been saved to {file_path}")
