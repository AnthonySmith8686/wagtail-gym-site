# Generated by Django 4.2.3 on 2023-07-17 22:08

from django.db import migrations, models
import django.db.models.deletion
import team.models
import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContentPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("body", wagtail.fields.RichTextField(blank=True)),
                (
                    "content",
                    wagtail.fields.StreamField(
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
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
