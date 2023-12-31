# Generated by Django 4.2.3 on 2023-07-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galary', '0003_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='defoult', upload_to='profile_images'),
        ),
    ]
