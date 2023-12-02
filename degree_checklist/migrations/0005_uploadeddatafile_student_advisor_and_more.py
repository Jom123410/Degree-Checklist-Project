# Generated by Django 4.2.5 on 2023-11-16 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('degree_checklist', '0004_semester_remove_course_prerequisites_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedDataFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='advisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.adviser'),
        ),
        migrations.AddField(
            model_name='student',
            name='degree_program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.degreeprogram'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='adviser',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adviser',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='adviser',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='adviser',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='adviser',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester_offered',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='courseenrollment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.course'),
        ),
        migrations.AlterField(
            model_name='courseenrollment',
            name='enrollment_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='courseenrollment',
            name='grade',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='courseenrollment',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.semester'),
        ),
        migrations.AlterField(
            model_name='courseenrollment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.student'),
        ),
        migrations.AlterField(
            model_name='degreeprogram',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='degreeprogram',
            name='duration_in_years',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='degreeprogram',
            name='program_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='degreeprogram',
            name='program_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='degreeprogram',
            name='total_credits_required',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='degreerequirement',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.course'),
        ),
        migrations.AlterField(
            model_name='degreerequirement',
            name='credits_required',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='degreerequirement',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.degreeprogram'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=9, null=True)),
                ('courses', models.ManyToManyField(to='degree_checklist.course')),
                ('semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.semester')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.student')),
            ],
        ),
    ]