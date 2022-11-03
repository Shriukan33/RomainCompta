#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('temp_user', '', 'some_random_password')" | python manage.py shell
