# Generated by Django 2.2.4 on 2019-10-30 23:10

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmedia.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))])), ('full_richtext', streams.blocks.RichTextBlock()), ('card', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('trackno', wagtail.core.blocks.FloatBlock(help_text='Track Number', required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Episode Title', max_length=40, required=True)), ('track', wagtailmedia.blocks.AbstractMediaChooserBlock(help_text='Upload/Choose audio file', required=True)), ('trackdate', wagtail.core.blocks.DateBlock(help_text='Upload date', required=True)), ('shownotespage', wagtail.core.blocks.PageChooserBlock(help_text='Choose Shownotespage', required=False))])))]))], blank=True, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Flex Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
