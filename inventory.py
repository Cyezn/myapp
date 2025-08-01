import csv
import os

CSV_FILE = 'store_inventory.csv'

def load_inventory():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_inventory(inventory):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['Item Name', 'Quantity', 'Comment', 'Low Stock Threshold']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)

def add_item(name, quantity, comment, threshold):
    inventory = load_inventory()
    for item in inventory:
        if item['Item Name'].lower() == name.lower():
            item['Quantity'] = str(int(item['Quantity']) + int(quantity))
            item['Low Stock Threshold'] = threshold
            if comment:
                item['Comment'] = comment
            break
    else:
        inventory.append({
            'Item Name': name,
            'Quantity': quantity,
            'Comment': comment,
            'Low Stock Threshold': threshold
        })
    save_inventory(inventory)

def remove_item(name, quantity):
    inventory = load_inventory()
    for item in inventory:
        if item['Item Name'].lower() == name.lower():
            current_qty = int(item['Quantity'])
            remove_qty = int(quantity)
            if remove_qty >= current_qty:
                inventory.remove(item)
            else:
                item['Quantity'] = str(current_qty - remove_qty)
            break
    save_inventory(inventory)

def search_item(keyword):
    inventory = load_inventory()
    return [item for item in inventory if keyword.lower() in item['Item Name'].lower()]
