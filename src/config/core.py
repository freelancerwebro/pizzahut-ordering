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