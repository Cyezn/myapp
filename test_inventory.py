import inventory

def test_add_and_search_item():
    inventory.add_item("Banana", 15, "Fruit", "5")
    result = inventory.search_item("Banana")
    assert result
    assert result[0]["Item Name"] == "Banana"
