import pandas as pd

def load_raw_data():
    orders = pd.read_csv('../data/raw/orders.csv')
    customers = pd.read_csv('../data/raw/customers.csv')
    print("Orders and Customers loaded successfully.")
    return orders, customers

if __name__ == "__main__":
    load_raw_data()
