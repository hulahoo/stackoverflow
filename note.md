python -m venv venv -> Create virtual environment folder

source venv/Scripts/activate -> Windows
source venv/bin/activate -> Mac/*Unix

pip3 install -r requirements.txt -> Install requirements to virtual environment

Pull the latest changes from Git:
1. Pull changes:
    ```bash
    git pull origin main
    ```

After creating a new model in models.py and check that this application is added to settings.py.INSTALLED_APPS:
1. Create migration files:
    ```bash
    python -m manage makemigrations
    ```
2. Apply migration files to database:
    ```bash
    python -m manage migrate
    ```
3. Run Django application:
    ```bash
    python -m manage runserver <port number>(default :8000)
    ```
4. Create Django custom app:
    ```bash
    django-admin startapp <app name>
    ```


MVC -> Model View Controller

Authentication verifies the identity of a user, who is user
Authorization show to which resources user have access

Simple url address of some resource: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses
                                     https://developer.mozilla.org/fr/docs/Web/HTTP/Status
                                     https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status
                                     https://developer.mozilla.org/en-US/docs/Web/HTTP
http://<ip-address>/<domain name>:<port address>
      34.111.97.67/developer.mozilla.org
      127.0.0.1(0.0.0.0):8000/localhost


### DNS(Domain Name System)
34.111.97.67 -> google.com
IPv4/IPv6
34.111.97.67 - IPv4
2400:cb00:2048:1::c629:d7a2 - IPv6

### Phonebook example
898412343125 -> Tom

http://127.0.0.1:8000/
http://127.0.0.1:5432


## Django Email configurations

1. Declare EMAIL_BACKEND:
    1.1. If we want to send real email message to existing email address:
    ```python
        EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    ```
    1.2. If we want to send a test email to console(terminal/cli):
    ```python
        EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    ```


## Django Queryset methods

1. To add filtering by column values, use .filter():
    ```python
        user = CustomUser.objects.filter(email=self.email, activation_code=self.code).all()
    ```
2. To retrieve all values from column, use .all():
    ```python
        users = CustomUser.objects.all() # List[CustomUser] -> Returns a list of CustomUser objects
    ```
3. To retrieve only first record from a list of records, use .first():
    ```python
        users = CustomUser.objects.first() # CustomUser | None -> Returns object of CustomUser or None if no records exists in table
    ```


ON DELETE CLAUSES

1. CASCADE - delete all related objects
2. DO_NOTHING - do nothing
3. PROTECT - not allow to delete


Authentications:
1. BasicAuthentication -> https://www.django-rest-framework.org/api-guide/authentication/#basicauthentication