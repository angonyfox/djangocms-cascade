# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-09 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from cmsplugin_cascade.models import CascadeElement, CascadePage, IconFont


def forwards(apps, schema_editor):
    for cascade_element in CascadeElement.objects.all():
        if cascade_element.plugin_type not in ['FramedIconPlugin', 'TextIconPlugin']:
            continue

        icon_font = cascade_element.glossary.get('icon_font')
        if icon_font:
            try:
                icon_font = IconFont.objects.get(pk=icon_font)
            except IconFont.DoesNotExist:
                pass
            else:
                cms_page = cascade_element.page.get_public_object()
                defaults = {'icon_font': icon_font}
                public_extension, _ = CascadePage.objects.update_or_create(
                    extended_object=cms_page,
                    public_extension=None,
                    defaults=defaults,
                )
                CascadePage.objects.update_or_create(
                    extended_object=cms_page.get_draft_object(),
                    public_extension=public_extension,
                    defaults=defaults,
                )
                # TODO: After implementing a backward migration, remove deprecated `icon_font` from glossary
                # cascade_element.glossary.pop('icon_font')
                # cascade_element.save()


def backwards(apps, schema_editor):
    print("Backward migration not implemented")


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_cascade', '0019_verbose_table_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='cascadepage',
            name='icon_font',
            field=models.ForeignKey(blank=True, help_text='Set Icon Font globally for this page', null=True, on_delete=django.db.models.deletion.CASCADE, to='cmsplugin_cascade.IconFont', verbose_name='Icon Font'),
        ),
        migrations.RunPython(forwards, reverse_code=backwards),
    ]
