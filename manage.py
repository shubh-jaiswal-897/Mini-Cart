<<<<<<< HEAD
#!/usr/bin/env python
=======
#!/usr/bin/env python3
>>>>>>> b8f2c646db683e3171d896c7c2b8ac63cd943a7c
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minicart.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomerce.settings')
>>>>>>> b8f2c646db683e3171d896c7c2b8ac63cd943a7c
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
