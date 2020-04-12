# PizzaHut ordering
This piece of software written in Python allows you to order your favorite pizza from PizzaHut (PizzaHutDelivery.ro) just by running a simple command in console.

### How to set up

1. Create an account on PizzaHutDelivery.ro and complete your delivery address

2. Connect to your web server in SSH and open your user profile into a text editor
```
sudo vi ~/.bash_profile
```
3. Add the following environment variables and fill in your PizzaHut credentials and then save the file
```
export PIZZAHUT_USERNAME="<<ADD YOUR USERNAME>>"
export PIZZAHUT_PASSWORD="<<ADD YOUR PASSWORD>>"
```
4. Reload your user profile
```
source ~/.bash_profile
```

### How to customize your order
Open the file bellow and modify the `default_order` section as you like.
```
vi src/config/core.py
```

# How to order
Run the following command in the console.
```
python order.py
```

### Logs
After running the command above, the console will log the order steps. In case of any error, the order will not be send to the store.
```
1. Open pizzahutdelivery.ro
2. Accept cookies
3. Log in
4. Add products to cart
5.  -> Product added to cart [quattro-stagioni / medium / trad]
6.  -> Product added to cart [roma / medium / trad]
7. Checkout order [TOTAL = 67.00 lei]
8. Select delivery time [now]
9. Select payment type [POS]
10. Place order
11. Close browser
```