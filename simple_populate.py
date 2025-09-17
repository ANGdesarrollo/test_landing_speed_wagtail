import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.dev')
django.setup()

from wagtail.models import Site, Page
from home.models import HomePage, ContactPage

def create_pages():
    # Get or create default site
    try:
        site = Site.objects.get(is_default_site=True)
        root = site.root_page
    except Site.DoesNotExist:
        # Create root page if it doesn't exist
        from wagtail.models import Page
        if not Page.objects.filter(depth=1).exists():
            root = Page.add_root(title="Root", slug="root")
        else:
            root = Page.objects.filter(depth=1).first()
        
        # Create site
        site = Site.objects.create(
            hostname='localhost',
            port=8001,
            root_page=root,
            is_default_site=True,
            site_name="Demo Site"
        )
    
    # Delete existing pages (but not root)
    HomePage.objects.all().delete()
    ContactPage.objects.all().delete()
    
    # Create HomePage as direct child of root
    home = HomePage(
        title="Home",
        slug="",  # Empty slug makes it the homepage
    )
    root.add_child(instance=home)
    home.save_revision().publish()
    
    # Create ContactPage as child of home
    contact = ContactPage(
        title="Contact", 
        slug="contact",
    )
    home.add_child(instance=contact)
    contact.save_revision().publish()
    
    # Update site root to point to home
    site.root_page = home
    site.save()
    
    print("✅ Páginas creadas!")
    print(f"Site: http://localhost:8001/")
    print(f"Contact: http://localhost:8001/contact/")

if __name__ == "__main__":
    create_pages()