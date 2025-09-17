#!/usr/bin/env python
import os
import django
import sys

# Add the project directory to the Python path
sys.path.append('/home/alexis/Documents/Alexis/proof_of_concept/wagtail_vs_astro/wagtail_page')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.dev')

# Setup Django
django.setup()

from wagtail.models import Site, Page
from home.models import HomePage, ContactPage

def create_pages():
    try:
        # Get the default site and root page
        site = Site.objects.get(is_default_site=True)
        root_page = site.root_page
        
        print(f"Root page: {root_page}")
        print(f"Root page children: {root_page.get_children()}")
        
        # Delete existing pages if they exist
        HomePage.objects.all().delete()
        ContactPage.objects.all().delete()
        
        # Create a simple HomePage
        home_page = HomePage(
            title="Home",
            slug="",  # Empty slug for root
            hero_title="Revolutionizing Digital Experiences",
            hero_subtitle="We create cutting-edge solutions that transform how businesses connect with their customers through innovative technology and design",
            hero_cta_text="Get Started Today",
            hero_cta_link="/contact/",
        )
        
        # Add to the current root page
        existing_home = None
        for child in root_page.get_children():
            if child.title == "Welcome to your new Wagtail site!":
                existing_home = child
                break
        
        if existing_home:
            # Replace the existing welcome page
            existing_home.delete()
        
        root_page.add_child(instance=home_page)
        home_page.save_revision().publish()
        
        # Set as the site root
        site.root_page = home_page
        site.save()
        
        print(f"Created HomePage: {home_page}")
        
        # Create ContactPage
        contact_page = ContactPage(
            title="Contact",
            slug="contact",
            header_title="Get In Touch",
            header_description="Ready to start your next project? We'd love to hear from you. Send us a message and we'll respond as soon as possible.",
        )
        
        home_page.add_child(instance=contact_page)
        contact_page.save_revision().publish()
        
        print(f"Created ContactPage: {contact_page}")
        print("Pages created successfully!")
        
    except Exception as e:
        print(f"Error creating pages: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_pages()