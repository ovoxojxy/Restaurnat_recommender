import json

# Define restaurant data
restaurant_data = [
    {
        "name": "16th Avenue Diner",
        "cuisine": "American",
        "address": "207 NE 16th Ave, Gainesville",
        "price": 12.5,
        "diet": [],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.666944, 82.321389]
    },
    {
        "name": "4 Rivers Smokehouse – Gainesville",
        "cuisine": "Barbecue",
        "address": "3262 sw 35th blvd, Gainesville",
        "distance": "",
        "price": 19,
        "diet": ["Vegan","Vegetarian"],
        "dress_code": "Casual Dress",
        "ratings": 4.2,
        "location": [29.623889, 82.3775]
    },
    {
        "name": "43rd St Deli & Breakfast – South",
        "cuisine": "American",
        "address": "3483 SW Williston Rd., Gainesville",
        "distance": "",
        "price": 15,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.600556, 82.374167]
    },
    {
        "name": "43rd St Deli & Breakfast – West",
        "cuisine": "American",
        "address": "4410 NW 25th Pl, Gainesville",
        "distance": "",
        "price": 15,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.676389, 82.390278]
    },
    {
        "name": "4th Ave Food Park",
        "cuisine": "Various",
        "address": "409 SW 4th Ave, Gainesville",
        "distance": "",
        "price": 14,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.7,
        "location": [29.647778, 82.328333]
    },
    {
        "name": "A’xin Mahzu Sushi & Grill",
        "cuisine": "Sushi",
        "address": "5150 SW 34th St, Gainesville",
        "distance": "",
        "price": 21,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.6,
        "location": [29.605556, 82.3725]
    },
    {
        "name": "Adam’s Rib Co. North",
        "cuisine": "Barbecue",
        "address": "2109 NW 13th St, Gainesville",
        "distance": "",
        "price": 18,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.6725, 82.338611]
    },
    {
        "name": "Afternoon",
        "cuisine": "American, Breakfast",
        "address": "231 NW 10th ave, Gainesville",
        "distance": "",
        "price": 18,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.4,
        "location": [29.660833, 82.3275]

    },
    {
        "name": "Airstream – Opus Coffee",
        "cuisine": "Coffee",
        "address": "403 SW4th Ave, Gainesville",
        "distance": "",
        "price": 5,
        "diet": [],
        "dress_code": "Casual",
        "ratings": 4.8,
        "location": [29.648056, 82.329167]
    },
    {
        "name": "Alpin Bistro",
        "cuisine": "French",
        "address": "15 SW 2nd St, Gainesville",
        "distance": "",
        "price": 14.4,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.3,
        "location": [29.651389, 82.326111]
    },
    {
        "name": "Amelia’s Italian Cuisine",
        "cuisine": "Italian",
        "address": "235 S Main St, Suite 107, Gainesville",
        "distance": "",
        "price": 47,
        "diet": ["Vegetarian"],
        "dress_code": "Dressy Casual",
        "ratings": 4.2,
        "location": [29.648889, 82.324167]
    },
    {
        "name": "Bagel Bakery",
        "cuisine": "Bagel",
        "address": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price": 5,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.671944, 82.386667]
    },
    {
        "name": "Bageland Bagels",
        "cuisine": "Bagel",
        "address": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price": 10,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.675833, 82.386667]
    },
    {
        "name": "BagelS & Noodles",
        "cuisine": "Bagel",
        "address": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price": 13,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.652222, 82.337778]
    },
    {
        "name": "Bahama Breeze",
        "cuisine": "Caribbean",
        "address": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price": 20,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.626944, 82.383889]
    },
    {
        "name": "Ballyhoo",
        "cuisine": "Bar & Grill",
        "address": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price": 23,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.652222, 82.379444]
    },
    {
        "name": "Blackadder Brewing",
        "cuisine": "Brewery",
        "address": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price": 0,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.658056, 82.406667]
    },{
        "name": "Blue Gill Quality Foods",
        "cuisine": "Southern",
        "address": "4113 NW 16th Blvd, Gainesville",
        "distance": "",
        "price": 35,
        "diet": ["Vegetarian"],
        "dress_code": "Casual",
        "ratings": 4.5,
        "location": [29.638056, 82.339167]
    },
    
    
]

# Specify the file path where you want to save the JSON file
file_path = 'restaurants.json'

# Write restaurant data to JSON file
with open(file_path, 'w') as json_file:
    json.dump(restaurant_data, json_file, indent=4)

# print(f"JSON data has been saved to {file_path}")
