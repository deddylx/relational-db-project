import pandas as pd
from faker import Faker
import random

# Load city data from an Excel file into a DataFrame
df_city = pd.read_excel('city.xlsx')
df_city  # Display the DataFrame

# Rename columns for consistency and clarity
rename_col = {
    'kota_id': 'city_id',      # Rename 'kota_id' to 'city_id'
    'nama_kota': 'city_name'   # Rename 'nama_kota' to 'city_name'
}
df_city = df_city.rename(columns=rename_col)  # Apply the renaming to the DataFrame
df_city  # Display the updated DataFrame

# Initialize the Faker library to generate fake data
fake = Faker('id_ID')

# Initialize a dictionary to hold user data
users = {}

n_user = 100  # Define the number of users to create

# Generate user data
users['user_id'] = [i + 1 for i in range(n_user)]  # Create a list of user IDs
users['username'] = [fake.user_name() for i in range(n_user)]  # Generate fake usernames
users['name'] = [fake.name() for i in range(n_user)]  # Generate fake names
users['email'] = [fake.email() for i in range(n_user)]  # Generate fake emails
users['phone_number'] = [fake.phone_number() for i in range(n_user)]  # Generate fake phone numbers
users['address'] = [fake.street_address() for i in range(n_user)]  # Generate fake addresses
users['city_id'] = [random.choice(df_city['city_id']) for i in range(n_user)]  # Randomly assign city IDs from the city DataFrame
users['password'] = [fake.password() for i in range(n_user)]  # Generate fake passwords
users['created_at'] = [fake.date_time_between(start_date='-4y', end_date='-2y') for i in range(n_user)]  # Generate random creation dates within the last 4 years

# Convert the user dictionary to a DataFrame
df_users = pd.DataFrame(users)
df_users  # Display the DataFrame containing user data

# Load product details from an Excel file into a DataFrame
df_product_detail = pd.read_excel('car_product.xlsx')
df_product_detail  # Display the DataFrame

# Initialize a dictionary to hold product advertisement data
product_ads = {}

n_ad = 50  # Define the number of advertisements to create

# Generate product advertisement data
product_ads['ad_id'] = [i + 1 for i in range(n_ad)]  # Create a list of advertisement IDs
product_ads['user_id'] = [random.choice(users['user_id']) for i in range(n_ad)]  # Randomly assign user IDs to advertisements
product_ads['title'] = [f'Dijual {df_product_detail["model"][i]}' for i in range(n_ad)]  # Create advertisement titles using car models
product_ads['can_bid'] = [fake.boolean(chance_of_getting_true=70) for i in range(n_ad)]  # Randomly determine if bidding is allowed (70% chance)
product_ads['created_at'] = [fake.date_time_between_dates(datetime_start=users['created_at'][product_ads['user_id'][i]]) for i in range(n_ad)]  # Generate creation dates for ads based on user creation dates

# Convert the product advertisement dictionary to a DataFrame
df_product_ads = pd.DataFrame(product_ads)
df_product_ads  # Display the DataFrame containing product ads

# Prepare to enhance product details with additional information
product_detail_len = len(df_product_detail.axes[0])  # Get the number of product details
transmission = ['Manual', 'Automatic']  # Possible transmission types
description_sample = [  # Sample descriptions for products
    'Kondisi terawat, mesin irit namun tetap bergaya. Cocok untuk pemakaian sehari-hari dengan desain yang atraktif dan performa mesin yang andal.',
    'Performa mesin yang irit bahan bakar namun tetap bertenaga. Desain interior yang luas dan eksterior yang stylish membuat perjalanan semakin menyenangkan. Jaminan kondisi prima dan siap pakai.',
    'Mobil kompak yang sporty dan praktis. Didesain untuk kebutuhan perkotaan namun tetap tangguh di segala medan. Performa mesin yang andal dan ruang kabin yang luas membuatnya cocok untuk segala aktivitas.',
    'Mobil tangguh yang andal di segala medan. Dilengkapi dengan fitur keselamatan terkini dan performa mesin yang bertenaga.',
    'Menggabungkan elegan dan efisiensi dalam satu paket. Desain yang menawan dan performa mesin yang irit membuatnya pilihan ideal untuk gaya hidup aktif Anda.',
    'Interior mewah, kondisi seperti baru, service rutin, harga bersahabat. Jangan lewatkan!'
]

# Generate additional product detail information
ad_id = product_ads['ad_id']  # Get advertisement IDs
transmission_type = [random.choice(transmission) for i in range(product_detail_len)]  # Randomly assign transmission types
is_description = [fake.boolean(chance_of_getting_true=30) for i in range(product_detail_len)]  # Randomly determine if a description should be included (30% chance)
description = [random.choice(description_sample) if desc else None for desc in is_description]  # Assign descriptions based on the random boolean

# Create a new DataFrame with additional columns
new_cols = {
    'ad_id': ad_id,
    'transmission_type': transmission_type,
    'description': description
}
df_product_detail = df_product_detail.assign(**new_cols)  # Assign new columns to the product detail DataFrame

# Reorder the columns of the product detail DataFrame for clarity
df_product_detail = df_product_detail[['product_id', 
                                        'ad_id', 
                                        'brand', 
                                        'model', 
                                        'body_type', 
                                        'transmission_type',
                                        'year',
                                        'description',
                                        'price'
                                        ]]
df_product_detail.head(10)  # Display the first 10 rows of the product detail DataFrame

# Initialize a dictionary to hold bid data
bids = {}

# Create a list of advertisement IDs that allow bidding
can_bid_true = [product_ads['ad_id'][i] for i in range(n_ad) if product_ads['can_bid'][i] == True]

n_bids = 200  # Define the number of bids to create

# Generate bid data
bids['bid_id'] = [i + 1 for i in range(n_bids)]  # Create a list of bid IDs
bids['ad_id'] = [random.choice(can_bid_true) for i in range(n_bids)]  # Randomly assign advertisement IDs for bids
bids['buyer_id'] = [random.choice(users['user_id']) for i in range(n_bids)]  # Randomly assign buyer IDs from the user list
index = [df_product_detail.loc[df_product_detail['ad_id'] == ad_id].index[0] for ad_id in bids['ad_id']]  # Get the index of the product details for the corresponding ad IDs
product_price = [df_product_detail['price'][i] for i in index]  # Get the prices of the products based on the indices
bids['bid_price'] = [int(fake.random_int(70, 95, 5) / 100 * ad_price) for ad_price in product_price]  # Generate bid prices as a percentage of product prices
ad_created_datetime = [df_product_ads['created_at'][i] for i in index]  # Get the creation dates of the ads for the bids
bids['created_at'] = [fake.date_time_between_dates(datetime_start=ad_date) for ad_date in ad_created_datetime]  # Generate creation dates for bids based on ad creation dates

# Convert the bid dictionary to a DataFrame
df_bids = pd.DataFrame(bids)
df_bids  # Display the DataFrame containing bid data

# Save the generated DataFrames to CSV files for further use
df_city.to_csv('dummy_city.csv', index=False)  # Save city data
df_users.to_csv('dummy_users.csv', index=False)  # Save user data
df_product_ads.to_csv('dummy_product_ads.csv', index=False)  # Save product ads data
df_product_detail.to_csv('dummy_product_detail.csv', index=False)  # Save product detail data
df_bids.to_csv('dummy_bids.csv', index=False)  # Save bid data