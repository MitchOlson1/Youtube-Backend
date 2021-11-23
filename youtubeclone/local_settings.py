SECRET_KEY = 'django-insecure-q#^3irn3k(3=rkirg5ynnmy%1(kq2ue_sr9bsn8w&5btp=-50h'

DATABASES = {
    'default': {
        'ENGINE' : 'mysql.connector.django',
        'NAME' : 'youtubeclone',
        'USER' : 'root',
        'PASSWORD' : 'MyPassword3!',
        'HOST' : '127.0.0.1',
        'OPTIONS' : {
            'autocommit' : True
        }
    }
}
