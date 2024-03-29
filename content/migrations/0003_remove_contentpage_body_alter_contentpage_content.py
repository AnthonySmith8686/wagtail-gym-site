# Generated by Django 4.2.3 on 2023-07-18 16:02

from django.db import migrations
import team.models
import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_alter_contentpage_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contentpage",
            name="body",
        ),
        migrations.AlterField(
            model_name="contentpage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "team_members",
                        wagtail.blocks.ListBlock(
                            wagtail.snippets.blocks.SnippetChooserBlock(
                                team.models.TeamMember
                            ),
                            icon="user",
                        ),
                    )
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
    ]
