ADD_ITEMS_TO_BASKET_MUTATION = """
mutation {
    basketItemsAdd(items: [{id: %d, quantity: %d}]) {
        status
        errorMessage
    }
}
"""