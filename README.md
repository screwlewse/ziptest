# Thank you for the challenge!

For your convenience, I have broken down how the code works so you can run the tests and the app itself.

## Running tests

Create a virtual environment and install the requirements.
```
# using pyenv
# in the directory of the code,
# install using whatever 3.10 python version you have
pyenv virtualenv 3.10.x davidgzip
pyenv local davidgzip

# install requirements
pip install -r test-requirements.txt

# or simply
pip install pytest

# and then run
pytest tests/
```

## Explanation of files and their purpose: 

- `main.py`: This file simply runs the API's.   This is like the client who makes the orders.
- `order_actions.py`: The view layer in MVC.  This hanldes the calls, and calls the correct objects.  

## Running the app against the dummy data

I included the dummy data from the instructions but I added a bit more to the orders so that we can show off backorders and multiple shipments.
```
python main.py
```
This should get you results like:
```
/opt/src/ziptest$ python main.py
Adding new products
Products created
{0: {'mass_g': 700, 'product_id': 0, 'product_name': 'RBC A+ Adult'},
 1: {'mass_g': 700, 'product_id': 1, 'product_name': 'RBC B+ Adult'},
 2: {'mass_g': 750, 'product_id': 2, 'product_name': 'RBC AB+ Adult'},
 3: {'mass_g': 680, 'product_id': 3, 'product_name': 'RBC O- Adult'},
 4: {'mass_g': 350, 'product_id': 4, 'product_name': 'RBC A+ Child'},
 5: {'mass_g': 200, 'product_id': 5, 'product_name': 'RBC AB+ Child'},
 6: {'mass_g': 120, 'product_id': 6, 'product_name': 'PLT AB+'},
 7: {'mass_g': 80, 'product_id': 7, 'product_name': 'PLT O+'},
 8: {'mass_g': 40, 'product_id': 8, 'product_name': 'CRYO A+'},
 9: {'mass_g': 80, 'product_id': 9, 'product_name': 'CRYO AB+'},
 10: {'mass_g': 300, 'product_id': 10, 'product_name': 'FFP A+'},
 11: {'mass_g': 300, 'product_id': 11, 'product_name': 'FFP B+'},
 12: {'mass_g': 300, 'product_id': 12, 'product_name': 'FFP AB+'}}
Stocking items into the inventory
Inventory items stocked
{0: {'product_id': 0, 'quantity': 30},
 1: {'product_id': 1, 'quantity': 25},
 2: {'product_id': 2, 'quantity': 25},
 3: {'product_id': 3, 'quantity': 12},
 4: {'product_id': 4, 'quantity': 15},
 5: {'product_id': 5, 'quantity': 10},
 6: {'product_id': 6, 'quantity': 8},
 7: {'product_id': 7, 'quantity': 8},
 8: {'product_id': 8, 'quantity': 20},
 9: {'product_id': 9, 'quantity': 10},
 10: {'product_id': 10, 'quantity': 5},
 11: {'product_id': 11, 'quantity': 5},
 12: {'product_id': 12, 'quantity': 5}}
shipping: {'order_id': 123, 'shipped': [{'product_id': 0, 'quantity': 2}, {'product_id': 10, 'quantity': 5}, {'product_id': 2, 'quantity': 5}]}
ORDERS:
[{'order_id': 123,
  'requested': [{'product_id': 0, 'quantity': 2},
                {'product_id': 10, 'quantity': 5},
                {'product_id': 2, 'quantity': 5}]}]
SHIPMENTS:
[[{'order_id': 123,
   'shipped': [{'product_id': 0, 'quantity': 2},
               {'product_id': 10, 'quantity': 5},
               {'product_id': 2, 'quantity': 5}]}]]
BACKORDERS:
[[{'product_id': <built-in function id>, 'quantity': 2}]]
```

## Problem area

You can likely see that there is a problem here.
The ordering code doesn't take into account, the weight of each product, multiplied by its quantity.  I left it as is because I went over my personal time limit on this project.

