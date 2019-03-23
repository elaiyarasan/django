# Generated by Django 2.1.7 on 2019-03-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dailytask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('workingproject', models.TextField()),
                ('company', models.TextField()),
                ('workinghour', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('stage', models.TextField()),
            ],
        ),
    ]
