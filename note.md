python -m venv venv -> Create virtual environment folder

source venv/Scripts/activate -> Windows
source venv/bin/activate -> Mac/*Unix

pip3 install -r requirements.txt -> Install requirements to virtual environment


git pull origin main -> Pulls latest changes from remote repository

After creating a new model in models.py and check that this application is added to settings.py.INSTALLED_APPS:
1. Create migration files:
    ```bash
    python -m manage makemigrations
    ```
2. Apply migration files to database:
    ```bash
    python -m manage migrate
    ```
