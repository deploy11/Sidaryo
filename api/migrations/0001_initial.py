# Generated by Django 4.2.5 on 2024-10-14 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orinbosar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sorov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish', models.CharField(max_length=500, verbose_name='To`liq ismingizni kiriting?')),
                ('idpassport', models.CharField(max_length=500, verbose_name='pasport seriasini kiriting')),
                ('Yashashmanzili', models.CharField(max_length=500)),
                ('mfynomi', models.CharField(max_length=500)),
                ('kochanomi', models.CharField(max_length=500)),
                ('telefonraqami', models.CharField(max_length=500)),
                ('rasmvavidio', models.CharField(max_length=500)),
                ('ariza_mazmuni', models.CharField(max_length=500)),
                ('matn', models.TextField()),
                ('korish', models.BooleanField(default=False)),
                ('muddat', models.DateField(auto_now=True, null=True)),
                ('user', models.CharField(default='1', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tashkilotlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Hokimiyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muddat', models.DateField(auto_now=True)),
                ('bajarildi', models.BooleanField(default=False, null=True)),
                ('muddat_holati', models.BooleanField(default=False, null=True)),
                ('orinbosar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.orinbosar')),
                ('tashkilot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.tashkilotlar')),
                ('tel_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sorov')),
            ],
        ),
    ]