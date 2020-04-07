# PizzaHut ordering
This piece of software written in Python allows you to order your favorite pizza from PizzaHut (pizzahutdelivery.ro) just by running a simple command in console.

# How to set up

1. Open your current user profile into a text editor
```
sudo vi ~/.bash_profile
```
2. Add the following environment variables and fill in your PizzaHut credentials
```
export PIZZAHUT_USERNAME="<<ADD YOUR USERNAME>>"
export PIZZAHUT_PASSWORD="<<ADD YOUR PASSWORD>>"
```
3. Save the file
4. Reload your user profile
```
source ~/.bash_profile
```

# How to customize your order
Open the following file and modify the `default_order` section as you like.
```
vi src/config/core.py
```

# How to order
Run the following command in the console.
```
python order.py
```