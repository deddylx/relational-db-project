# SQL Portfolio: Creating a Database for a Used Car E-Commerce Platform
## Overview
This project focuses on building a relational database for a used car sales website. The database will allow users to post advertisements for their used cars and enable potential buyers to search for vehicles based on specific criteria such as brand, model, year, price, and mileage. The primary objective is to create a structured and efficient system for managing user data, advertisements, and search functionalities, ensuring a seamless experience for both sellers and buyers. This project demonstrates the application of SQL in designing and managing a database for a real-world e-commerce platform.

## Project Features and Scope

This project involves designing a relational database for a used car sales platform with the following features and constraints:
1. User Management:
   - Each user can list more than one used car for sale.
   - Before selling a car, users must complete their profile by providing personal information such as their name, contact details, and location.
2. Advertisement Listings:
   - Users can post advertisements to showcase their cars on the website.
   - Each advertisement includes:
     - A title.
     - Detailed product information.
     - Seller contact details.
   - The product information in the advertisement must include:
     - Car brand (e.g., Toyota, Daihatsu, Honda, etc.).
     - Model (e.g., Toyota Camry, Toyota Corolla Altis, Toyota Vios, Toyota Camry Hybrid, etc.).
     - Body type (e.g., MPV, SUV, Van, Sedan, Hatchback, etc.).
     - Transmission type (e.g., manual or automatic).
     - Year of manufacture (e.g., 2005, 2010, 2011, 2020).
     - Additional details such as color, mileage, and other specifications can be included as needed.
3. Search Functionality:
   - Users can search for cars based on:
     - Seller location.
     - Car brand.
     - Body type.
4. Bidding Feature:
   - If a potential buyer is interested in a car, they can place a bid (if the seller allows bidding).
5. Transaction Handling:
   - The actual purchase transaction occurs outside the application and is not within the scope of this project.

## Database Design: SQL Code and Schema Details
The database schema for the used car sales platform includes tables like Users and Advertisements, designed to manage user data, car listings, and search functionality. The SQL code defines the structure with primary keys, foreign keys, and constraints to ensure data integrity. This schema supports scalability, performance, and efficient data retrieval, forming the backbone of the platform's backend.

The SQL code for designing the database can be found [here](https://github.com/deddylx/relational-db-project/blob/main/database_design.sql)
<img width="729" alt="Screenshot 2025-02-14 at 13 33 52" src="https://github.com/user-attachments/assets/1ba98131-b981-421d-89f7-a6d851d53b09" />

<div align="center">
Entity Relationship Diagram
</div>

## Generating a Dummy Dataset Using Python Faker
To simulate real-world data for testing and development purposes, I used the Python Faker library to generate a dummy dataset. This dataset includes realistic but fictional information for users, advertisements, and other relevant entities in the used car sales platform. The Faker library provides a wide range of data types, such as names, addresses, phone numbers, and more, making it an ideal tool for creating mock data.

The Python code for generating dataset can be found [here](https://github.com/deddylx/relational-db-project/blob/main/dummy_dataset.py)

## Transactional and Analytical Queries
I performed transactional queries to handle real-time data operations for the used car sales platform and also conducted analytical queries to derive insights and trends from the dataset.

### Transactional Queries: Core Operations
Focus on daily data management, listing, bidding, and searching.
- Find cars manufactured in 2015 or later.
- Add a new product bid.
- View all cars sold by an account (newest first).
- Find the cheapest used cars by keyword.
- Find the nearest used cars by city ID (Euclidean distance calculation).

### Analytical Queries: Insights & Trends
Designed to extract insights from the data - popularity, pricing, bidding patterns, and trends.
- Rank car model popularity by bid count.
- Compare car prices by average price per city.
- Analyze bid date differences and prices for a car model.
- Compare the percentage difference between average car model price and average bid price (last 6 months).
- Calculate a 6-month rolling average bid price for a car make/model using a window function.

## Contact me
I appreciate you being here! If you have any questions, suggestions, or just want to say hi, please feel free to reach out to [Deddy Laudryansyah Putra](mailto:ldeddy@gmail.com). I'm excited to connect with you!
