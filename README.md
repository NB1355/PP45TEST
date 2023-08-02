
### PPIIV: Full-Stack Toolkit
# The was to explore the possibility of making structural changes in data models and styling of a functioning website.

The business idea has merely the functionality of features in Boutic Ado, but there are requirements to be added or removed, such as:

- contrllling inventory is needed
- disabling products should be possible; the user should not see them
- enableing a product by admin allowd
- good ro have inventory reports ....

##
- The designe not to be limited so here is a try with Tailwind UI for more flecibility.
- This repository is the baseline for the moleds like invententory to be adede.
- cleaning uo the unused objects and code nedd to be done







# Setup
to get it running:

(1-3 will be done automatically in gitpod)

1.
```
pip install -r requirements.txt
```

2.
```
pip install --no-binary :all: psycopg2
```

3. 
run `npm install` to install all the dependencies

4.
remove .env-sample to .env file and add secret keys

5.
run styling with `npm run styling` and run the server with `y`

6.
add your host to the allowed hosts in `/boutique_ado/settings.py`

7.
to load fixtures run `python3 manage.py loaddata categories` and then `python3 manage.py loaddata products`



## test card stripe

4242 4242 4242 4242

date: 12/34