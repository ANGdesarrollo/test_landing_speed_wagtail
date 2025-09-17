from django.core.management.base import BaseCommand
from wagtail.models import Site
from home.models import HomePage, ContactPage
import json


class Command(BaseCommand):
    help = 'Populate the site with demo content'

    def handle(self, *args, **options):
        # Get or create the root page and site
        site = Site.objects.get(is_default_site=True)
        root_page = site.root_page
        
        # Delete existing pages if they exist
        HomePage.objects.all().delete()
        ContactPage.objects.all().delete()
        
        # Create HomePage
        home_page = HomePage(
            title="Home",
            slug="home",
            hero_title="Revolutionizing Digital Experiences",
            hero_subtitle="We create cutting-edge solutions that transform how businesses connect with their customers through innovative technology and design",
            hero_cta_text="Get Started Today",
            hero_cta_link="/contact",
            newsletter_title="Stay Updated",
            newsletter_description="Subscribe to our newsletter and get the latest updates, tips, and exclusive offers delivered to your inbox.",
        )
        
        # Add features
        features_data = [
            {
                "type": "feature",
                "value": {
                    "icon": "⚡",
                    "title": "Fast Performance",
                    "description": "Lightning-fast loading times with optimized code and advanced caching techniques"
                }
            },
            {
                "type": "feature", 
                "value": {
                    "icon": "📱",
                    "title": "Responsive Design",
                    "description": "Perfect experience on all devices from mobile phones to desktop computers"
                }
            },
            {
                "type": "feature",
                "value": {
                    "icon": "🔍",
                    "title": "SEO Optimized", 
                    "description": "Built for search engines with proper meta tags, structured data, and performance"
                }
            },
            {
                "type": "feature",
                "value": {
                    "icon": "🔒",
                    "title": "Secure",
                    "description": "Enterprise-level security with encryption, authentication, and data protection"
                }
            },
            {
                "type": "feature",
                "value": {
                    "icon": "📈",
                    "title": "Scalable",
                    "description": "Grows with your business from startup to enterprise with flexible architecture"
                }
            },
            {
                "type": "feature",
                "value": {
                    "icon": "🎧",
                    "title": "24/7 Support",
                    "description": "Always here to help with dedicated support team available around the clock"
                }
            }
        ]
        home_page.features = json.dumps(features_data)
        
        # Add stats
        stats_data = [
            {
                "type": "stat",
                "value": {
                    "number": "50,000+",
                    "label": "Happy Customers"
                }
            },
            {
                "type": "stat", 
                "value": {
                    "number": "99.9%",
                    "label": "Uptime Guarantee"
                }
            },
            {
                "type": "stat",
                "value": {
                    "number": "24/7",
                    "label": "Support Available"
                }
            },
            {
                "type": "stat",
                "value": {
                    "number": "15",
                    "label": "Years Experience"
                }
            }
        ]
        home_page.stats = json.dumps(stats_data)
        
        # Add testimonials
        testimonials_data = [
            {
                "type": "testimonial",
                "value": {
                    "name": "Sarah Johnson",
                    "role": "CEO TechCorp",
                    "quote": "Amazing results, exceeded expectations in every way. The team delivered exactly what we needed."
                }
            },
            {
                "type": "testimonial",
                "value": {
                    "name": "Mike Chen", 
                    "role": "CTO StartupX",
                    "quote": "Best investment we've made for our digital transformation. Highly recommended."
                }
            },
            {
                "type": "testimonial",
                "value": {
                    "name": "Lisa Rodriguez",
                    "role": "Marketing Director", 
                    "quote": "Incredible team and service. They understood our vision and brought it to life perfectly."
                }
            },
            {
                "type": "testimonial",
                "value": {
                    "name": "David Kim",
                    "role": "Founder",
                    "quote": "They delivered exactly what we needed on time and within budget. Exceptional quality."
                }
            },
            {
                "type": "testimonial", 
                "value": {
                    "name": "Emma Wilson",
                    "role": "Product Manager",
                    "quote": "Professional and reliable. The results speak for themselves. Will work with them again."
                }
            }
        ]
        home_page.testimonials = json.dumps(testimonials_data)
        
        # Add gallery images
        gallery_data = []
        for i in range(12):
            gallery_data.append({
                "type": "image",
                "value": {
                    "caption": f"Gallery image {i+1}"
                }
            })
        home_page.gallery_images = json.dumps(gallery_data)
        
        # Add FAQs
        faqs_data = [
            {
                "type": "faq",
                "value": {
                    "question": "How long does implementation take?",
                    "answer": "Implementation time varies depending on project scope, but typically ranges from 2-8 weeks. We provide detailed timelines during our initial consultation."
                }
            },
            {
                "type": "faq",
                "value": {
                    "question": "What's included in the basic plan?",
                    "answer": "Our basic plan includes responsive design, SEO optimization, basic analytics setup, and 3 months of support. Additional features can be added as needed."
                }
            },
            {
                "type": "faq", 
                "value": {
                    "question": "Do you offer custom solutions?",
                    "answer": "Yes, we specialize in custom solutions tailored to your specific business needs. Every project is unique and we adapt our approach accordingly."
                }
            },
            {
                "type": "faq",
                "value": {
                    "question": "Is there a money-back guarantee?",
                    "answer": "We offer a 30-day satisfaction guarantee. If you're not completely satisfied with our work, we'll refund your investment or work until you are."
                }
            },
            {
                "type": "faq",
                "value": {
                    "question": "How do you handle data security?",
                    "answer": "We implement enterprise-level security measures including SSL encryption, secure hosting, regular backups, and compliance with industry standards."
                }
            },
            {
                "type": "faq",
                "value": {
                    "question": "Can I upgrade my plan later?", 
                    "answer": "Absolutely! Our solutions are designed to scale with your business. You can upgrade your plan or add features at any time."
                }
            },
            {
                "type": "faq",
                "value": {
                    "question": "Do you provide training?",
                    "answer": "Yes, we provide comprehensive training for your team to ensure they can effectively manage and maintain the solution we deliver."
                }
            },
            {
                "type": "faq",
                "value": {
                    "question": "What's your support response time?",
                    "answer": "We guarantee response within 24 hours for standard support and within 2 hours for urgent issues. Premium plans include priority support."
                }
            }
        ]
        home_page.faqs = json.dumps(faqs_data)
        
        # Add home page to root
        root_page.add_child(instance=home_page)
        home_page.save_revision().publish()
        
        # Set as homepage
        site.root_page = home_page
        site.save()
        
        # Create Contact Page
        contact_page = ContactPage(
            title="Contact",
            slug="contact",
            header_title="Get In Touch", 
            header_description="Ready to start your next project? We'd love to hear from you. Send us a message and we'll respond as soon as possible.",
            address="123 Broadway Street\nNew York, NY 10001",
            phone="+1 (555) 123-4567",
            email="hello@digitalexp.com",
            hours="Mon - Fri: 9:00 AM - 6:00 PM\nSat - Sun: 10:00 AM - 4:00 PM"
        )
        
        # Add contact page to root
        root_page.add_child(instance=contact_page)
        contact_page.save_revision().publish()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated content!')
        )