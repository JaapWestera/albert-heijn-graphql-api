
BASKET_QUERY = """
query {
    basket {
        products {
            id
            quantity
            product {
                id
                price {
                    now {
                        amount
                        formatted
                    }
                }
                id
                brand
                category
                summary
                title
            }
        }
        itemsInOrder {
            id
            quantity
            isClosed
            allocatedQuantity
        }
    }
}
"""


BASKET_WITH_SUMMARY_QUERY = """
query {
    basket {
        summary {
            quantity
            price {
                priceBeforeDiscount {
                    amount
                    formatted
                }
                priceAfterDiscount {
                    amount
                    formatted
                }
                totalPrice {
                    amount
                    formatted
                }
                discount {
                    amount
                    formatted
                }
            }
        }
        itemsInOrder {
            id
            quantity
            product {
                id
                price {
                    now {
                        amount
                        formatted
                    }
                    was {
                        amount
                        formatted
                    }
                }
                smartLabel
                id
                date
                availabilityLabel
                brand
                category
                summary
                title
            }
        }
        products {
            id
            quantity
            product {
                id
                price {
                    now {
                        amount
                        formatted
                    }
                    was {
                        amount
                        formatted
                    }
                }
                smartLabel
                id
                date
                availabilityLabel
                brand
                category
                summary
                title
            }
        }
    }
}
"""

PRODUCT_SEARCH = """
query {
    productSearch(input: {query: "%s", properties: "", taxonomyId: 1, webshopId: 1}) {
        page {
            pageSize
            pageNumber
            totalPages    
            totalElements
        }
        products {
            smartLabel
            id
            brand
            title
            summary
            price {
                now {
                    amount
                    formatted
                }
            }
        }
    }
}
"""
