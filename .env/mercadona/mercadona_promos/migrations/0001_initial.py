# Generated by Django 4.2 on 2023-04-24 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercadona_promos.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.DateField()),
                ('fin', models.DateField()),
                ('pourcentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercadona_promos.produit')),
            ],
        ),
    ]