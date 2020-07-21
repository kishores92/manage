# Generated by Django 3.0.7 on 2020-07-20 09:43

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'Admin'), (2, 'Instructor'), (3, 'Students')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attendance_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('batch_name', models.CharField(max_length=255)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('days', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('test_date', models.DateField(auto_now_add=True)),
                ('batch_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='account.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('batch_array', models.CharField(max_length=255)),
                ('faceTaken', models.BooleanField(default=False)),
                ('batch_id', models.ManyToManyField(related_name='studentss', to='account.Batch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('msg_content', models.TextField()),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('recieveN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recievers', to=settings.AUTH_USER_MODEL)),
                ('sendN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senders', to='account.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='MarkReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.IntegerField(default=0)),
                ('mark_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Mark')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='markrep', to='account.Students')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Course'),
        ),
        migrations.AddField(
            model_name='batch',
            name='instructor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Instructor'),
        ),
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Attendance')),
                ('student_id', models.ManyToManyField(related_name='attendancereports', to='account.Students')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.Batch'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
