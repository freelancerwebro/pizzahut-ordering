import os

url = {
    "base" : "https://www.pizzahutdelivery.ro",
    "my_account" : "/contul-meu",
    "checkout" : "/checkout",
    "payment" : "/checkout/plata"
}
credentials = {
    "username" : os.environ['PIZZAHUT_USERNAME'],
    "password" : os.environ['PIZZAHUT_PASSWORD']
}
pizzas = {
    "types": {
        "margherita",
        "quattro-stagioni",
        "rodeo",
        "roma",
        "california",
        "europeana"
    },
    "sizes": {
        "small",
        "medium",
        "large"
    },
    "bases" : {
        "trad",
        "italian",
        "pan",
        "crust",
        "chbit"
    }
}
default_order = {
    "items": [
        {
            "quantity": 1,
            "product": "quattro-stagioni",
            "size": "medium",
            "base": "trad"
        },
        {
            "quantity": 1,
            "product": "roma",
            "size": "medium",
            "base": "trad"
        }
    ]
}
ordering = {
    "delivery_time" : "now",
    "payment_type"  : 3 ## POS
}
payment_methods = {
    9999 : "Card",
    2    : "Cash",
    3    : "POS",
    4    : "Meal tickets"
}