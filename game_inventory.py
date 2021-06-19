
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for item, count in inventory.items():
        print(f"{item}: {count}")


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] == 0:
                del inventory[item]


def print_table(inventory, order=None):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    item_title = "item name"
    count_title = "count"
    separator = " | "
    dash_char = "-"
    max_width_item = max([len(str(item)) for item in inventory.keys()] + [len(item_title)])
    max_width_count = max([len(str(count)) for count in inventory.values()] + [len(count_title)])
    horizontal_line = dash_char * (max_width_item + len(separator) + max_width_count)
    
    # header
    print(horizontal_line)
    print(f"{item_title:>{max_width_item}}{separator}{count_title:>{max_width_count}}")
    print(horizontal_line)
    
    # rows
    inventory_items = []
    if order == "count,asc":
        inventory_items = sorted(inventory.items(), key=lambda tuple: tuple[1], reverse=False)
    elif order == "count,desc":
        inventory_items = sorted(inventory.items(), key=lambda tuple: tuple[1], reverse=True)
    else:
        inventory_items = inventory.items()
    
    for item, count in inventory_items:
        print(f"{item:>{max_width_item}}{separator}{count:>{max_width_count}}")
        
    # footer
    print(horizontal_line)

def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""
    try:
        with open(filename, "rt") as file:
            for line in file:
                items_to_add = line.split(",")
                add_to_inventory(inventory, items_to_add)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
