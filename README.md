# Gas Billing System

## Project Overview

The **Gas Billing System** is a Python-based project developed to manage gas company billing. Users can create accounts, generate bills, mark bills as paid, and manage customer details. The project uses a **MySQL** database to store user and customer information.

## Features

1.  **User Account Creation**: Users can create an account with a unique username and password.
2.  **Login System**: Separate access for users and management.
3.  **Customer Management**: Add customers with details such as name, address, phone number, and email.
4.  **Bill Generation**: Generate bills based on meter readings.
5.  **Bill Payment**: Mark bills as paid.
6.  **Management Features**: View details of all customers and specific customers, and access all generated bills.

## Project Structure

The project consists of three main Python files:

1.  **Main File**: Controls the main program flow.
2.  **Functions Files**: Contains functions for interacting with the database (e.g., adding customers, generating bills).

## Built-in Modules and Libraries Used

-   **mysql.connector**: For connecting and interacting with the MySQL database.

## User-defined Functions

-   `connectDatabase()`
-   `create_table_customers()`
-   `create_table_bills()`
-   `create_table_users()`
-   `login()`
-   `add_user()`
-   `add_customer()`
-   `generate_bill()`
-   `display_customers()`
-   `display_customer()`
-   `display_bills()`
-   `mark_bill_as_paid()`

## Database Schema

-   **Database Name**: `gas`
-   **Tables**:
    -   `users` (User management)
    -   `customers` (Customer information)
    -   `bills` (Billing information)

## Prerequisites

-   **Python 3.9.6**
-   **MySQL 8.0.31**
