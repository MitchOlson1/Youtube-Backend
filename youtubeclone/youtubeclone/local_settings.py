

SECRET_KEY = 'django-insecure-14ozpb83qa$nzvlk%ty0hq7bh!zr0vjw+_zu-pw^qgb(c(@u+$'


DATABASES = {
    'default':{
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit':True
        }
    }
}