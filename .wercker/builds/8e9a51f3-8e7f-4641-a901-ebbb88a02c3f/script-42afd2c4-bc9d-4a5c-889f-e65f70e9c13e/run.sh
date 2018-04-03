set -e
echo "from django.contrib.auth.models import User; User.objects.create_superuser('onit', 'weare@init.ws','weare0nit')" | python manage.py shell
