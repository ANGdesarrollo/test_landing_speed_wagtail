from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class FeatureBlock(blocks.StructBlock):
    icon = blocks.CharBlock(max_length=10, help_text="Emoji icon")
    title = blocks.CharBlock(max_length=100)
    description = blocks.TextBlock()
    
    class Meta:
        template = 'blocks/feature_block.html'
        icon = 'edit'
        label = 'Feature'


class TestimonialBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=100)
    role = blocks.CharBlock(max_length=100)
    quote = blocks.TextBlock()
    image = ImageChooserBlock(required=False)
    
    class Meta:
        template = 'blocks/testimonial_block.html'
        icon = 'user'
        label = 'Testimonial'


class StatBlock(blocks.StructBlock):
    number = blocks.CharBlock(max_length=20)
    label = blocks.CharBlock(max_length=100)
    
    class Meta:
        template = 'blocks/stat_block.html'
        icon = 'snippet'
        label = 'Stat'


class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock(max_length=200)
    answer = blocks.TextBlock()
    
    class Meta:
        template = 'blocks/faq_block.html'
        icon = 'help'
        label = 'FAQ'


class GalleryImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(max_length=200, required=False)
    
    class Meta:
        template = 'blocks/gallery_image_block.html'
        icon = 'image'
        label = 'Gallery Image'


class HomePage(Page):
    # Hero Section (usando defaults del modelo para que aparezcan en el template)
    hero_title = models.CharField(max_length=200, default="Revolutionizing Digital Experiences")
    hero_subtitle = models.TextField(default="We create cutting-edge solutions that transform how businesses connect with their customers through innovative technology and design")
    hero_cta_text = models.CharField(max_length=50, default="Get Started Today")
    
    # Newsletter Section
    newsletter_title = models.CharField(max_length=100, default="Stay Updated")
    newsletter_description = models.TextField(default="Subscribe to our newsletter and get the latest updates, tips, and exclusive offers delivered to your inbox.")
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel('hero_cta_text'),
        ], heading="Hero Section"),
        MultiFieldPanel([
            FieldPanel('newsletter_title'),
            FieldPanel('newsletter_description'),
        ], heading="Newsletter Section"),
    ]


class ContactPage(Page):
    header_title = models.CharField(max_length=100, default="Get In Touch")
    header_description = models.TextField(default="Ready to start your next project? We'd love to hear from you. Send us a message and we'll respond as soon as possible.")
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('header_title'),
            FieldPanel('header_description'),
        ], heading="Header Section"),
    ]
