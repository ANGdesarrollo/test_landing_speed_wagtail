# simple_create.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.dev')
django.setup()

from wagtail.models import Site, Page
from home.models import HomePage, ContactPage

# Eliminar todo y empezar de cero
Page.objects.all().delete()
Site.objects.all().delete()

# Crear root page
root = Page.add_root(title="Root")

# Crear site
site = Site.objects.create(
    hostname='localhost',
    port=8001,
    root_page=root,
    is_default_site=True
)

# Crear HomePage como root
home = HomePage(title="Home", slug="")
root.add_child(instance=home)
home.save_revision().publish()

# Crear ContactPage
contact = ContactPage(title="Contact", slug="contact") 
home.add_child(instance=contact)
contact.save_revision().publish()

# Actualizar site root
site.root_page = home
site.save()

print("✅ Páginas creadas!")
print("Home: http://localhost:8001/")
print("Contact: http://localhost:8001/contact/")