# Generated by Django 3.1 on 2020-08-11 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200811_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='company_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='github_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='institution_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='live_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='play_store_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='website_link',
        ),
        migrations.CreateModel(
            name='WebsiteProjectLink',
            fields=[
                ('projectlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.projectlink')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            bases=('projects.projectlink',),
        ),
        migrations.CreateModel(
            name='PlayStoreProjectLink',
            fields=[
                ('projectlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.projectlink')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            bases=('projects.projectlink',),
        ),
        migrations.CreateModel(
            name='LiveProjectLink',
            fields=[
                ('projectlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.projectlink')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            bases=('projects.projectlink',),
        ),
        migrations.CreateModel(
            name='InstitutionProjectLink',
            fields=[
                ('projectlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.projectlink')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            bases=('projects.projectlink',),
        ),
        migrations.CreateModel(
            name='GitHubProjectLink',
            fields=[
                ('projectlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.projectlink')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            bases=('projects.projectlink',),
        ),
        migrations.CreateModel(
            name='CompanyProjectLink',
            fields=[
                ('projectlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projects.projectlink')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            bases=('projects.projectlink',),
        ),
    ]