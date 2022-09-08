# Generated by Django 4.1 on 2022-09-08 11:40

from django.db import migrations
import streamfieldblocks.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blogpage_body_alter_blogpage_main_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='main_content',
            field=wagtail.fields.StreamField([('richtext', wagtail.blocks.StructBlock([('richtext', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul']))])), ('carousel', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('responsive_image', streamfieldblocks.models.ResponsiveImageBlock()), ('card', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.TextBlock()), ('page_link', wagtail.blocks.PageChooserBlock())]))], blank=True, use_json_field=None),
        ),
    ]
