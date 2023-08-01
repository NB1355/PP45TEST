# Code Institute

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