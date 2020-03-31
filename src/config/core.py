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
            "size": "large",
            "base": "trad"
        }
    ]
}