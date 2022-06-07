# Thank you for the challenge!

Hey there.
For your convenience, I will break down how this code works so you know how to run the tests and to run the app itself.

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
```

## Running the app against the dummy data

I included the dummy data from the instructions but I added a bit more to the orders so that we can show off backorders and multiple shipments.
```
python main.py
```
This should get you results like: