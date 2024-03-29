# Generated by Django 3.2.7 on 2023-03-03 18:00

import blog.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title', template='blog/blocks/blog_heading.html')), ('paragraph', blog.models.ParagraphBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(template='blog/blocks/blog_image.html'))]),
        ),
    ]
