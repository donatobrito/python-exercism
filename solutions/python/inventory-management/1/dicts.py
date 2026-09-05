"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from 

    Returns:
        dict: The inventory dictionary.
    """
    # Criando o dicionário 'inventory', onde 'key' é o nome do item e 'value' é a quantidade de itens
    inventory = dict()

    # Para cada item:
    for item in items :
        
        # Retorna a quantidade atual deste item no 'inventory'. Se o item não estiver no inventário, retorna quantidade igual a 0
        amount = inventory.get(item, 0)

        # No 'inventario', incrementa a quantidade de itens
        inventory[item] = amount + 1
        
    return inventory
    
    pass


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    # Para cada item:
    for item in items :
        
        # Retorna a quantidade atual deste item no 'inventory'. Se o item não estiver no inventário, retorna quantidade igual a 0
        amount = inventory.get(item, 0)

        # No 'inventario', incrementa a quantidade de itens
        inventory[item] = amount + 1
        
    return inventory
    
    pass


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    # Para cada item:
    for item in items :
        
        # Retorna a quantidade atual deste item no 'inventory'. Se o item não estiver no inventário, retorna quantidade igual a 0
        amount = inventory.get(item, 0)

        # No 'inventario', decrementa a quantidade de itens
        if amount > 0 : inventory[item] = amount - 1
        
    
    return inventory  
    
    pass


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    # Retorna e remove o item do 'inventory'. Se o item não existir, retorna 0.
    inventory.pop(item, 0)

    return inventory
    
    pass


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    output = []
    
    # Para cada item do 'inventory':
    for item in inventory :

        # Somente retorna o item se este tiver 'qtd' maior que 0.
        if inventory[item] > 0 : output.append((item, inventory[item])) 

    return output
    
    pass
