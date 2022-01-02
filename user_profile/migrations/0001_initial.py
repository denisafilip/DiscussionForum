# Generated by Django 4.0 on 2021-12-28 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_count', models.IntegerField(blank=True, default=0)),
                ('post_count', models.IntegerField(blank=True, default=0)),
                ('reply_count', models.IntegerField(blank=True, default=0)),
                ('accepted_answer_count', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default/user.png', upload_to='images')),
                ('birth_date', models.DateField(blank=True, default='2000-07-02', help_text='Format: YYYY-MM-DD')),
                ('age', models.IntegerField(blank=True, default='21', help_text='Your current age.')),
                ('country', models.CharField(blank=True, default='Romania', help_text='Your country of origin.', max_length=30)),
                ('city', models.CharField(blank=True, default='Oradea', help_text='Your city of origin.', max_length=30)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]