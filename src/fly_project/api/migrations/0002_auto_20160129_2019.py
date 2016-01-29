# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 20:19
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Goal'), (2, 'Education'), (3, 'Resource')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('level', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('title', models.CharField(blank=True, max_length=63, null=True)),
                ('description', models.CharField(blank=True, max_length=511, null=True)),
                ('has_xp_requirement', models.BooleanField(default=True)),
                ('required_xp', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
            ],
            options={
                'db_table': 'fly_badges',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=63, null=True)),
                ('summary', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=511, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('duration', models.PositiveSmallIntegerField(choices=[(5, '5 Minutes'), (30, '30 Minutes'), (60, '1 Hour')], default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('awarded_xp', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('prerequisites', models.ManyToManyField(blank=True, related_name='_course_prerequisites_+', to='api.Course')),
            ],
            options={
                'db_table': 'fly_courses',
            },
        ),
        migrations.CreateModel(
            name='EnrolledCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('marks', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_enrolled_courses',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('unlocks', models.DateTimeField(blank=True, null=True)),
                ('was_accomplished', models.BooleanField(default=False)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Savings'), (2, 'Credit'), (3, 'Goal')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('times', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('period', models.PositiveSmallIntegerField(choices=[(1, 'Weeks'), (2, 'Months')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('for_want', models.PositiveSmallIntegerField(choices=[(1, 'House'), (2, 'Business'), (3, 'Vacation'), (4, 'Retirement'), (5, 'General Savings'), (6, 'Other')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('for_other_want', models.CharField(blank=True, max_length=63, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_goals',
            },
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('level', models.PositiveSmallIntegerField(db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)])),
                ('xp', models.PositiveSmallIntegerField(db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)])),
                ('badges', models.ManyToManyField(blank=True, related_name='fly_user_awarded_badges', to='api.Badge')),
                ('courses', models.ManyToManyField(blank=True, related_name='fly_user_enrolled_courses', to='api.EnrolledCourse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_mes',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('num', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('title', models.CharField(blank=True, max_length=63, null=True)),
                ('description', models.CharField(blank=True, max_length=511, null=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Multiple Choice'), (2, 'True / False')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('a', models.CharField(blank=True, max_length=255, null=True)),
                ('a_is_correct', models.BooleanField(default=False)),
                ('b', models.CharField(blank=True, max_length=255, null=True)),
                ('b_is_correct', models.BooleanField(default=False)),
                ('c', models.CharField(blank=True, max_length=255, null=True)),
                ('c_is_correct', models.BooleanField(default=False)),
                ('d', models.CharField(blank=True, max_length=255, null=True)),
                ('d_is_correct', models.BooleanField(default=False)),
                ('e', models.CharField(blank=True, max_length=255, null=True)),
                ('e_is_correct', models.BooleanField(default=False)),
                ('f', models.CharField(blank=True, max_length=255, null=True)),
                ('f_is_correct', models.BooleanField(default=False)),
                ('true_choice', models.CharField(blank=True, max_length=127, null=True)),
                ('false_choice', models.CharField(blank=True, max_length=127, null=True)),
                ('answer', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'fly_questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionSubmission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Multiple Choice'), (2, 'True / False')], db_index=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('b', models.BooleanField(default=False)),
                ('c', models.BooleanField(default=False)),
                ('d', models.BooleanField(default=False)),
                ('e', models.BooleanField(default=False)),
                ('f', models.BooleanField(default=False)),
                ('tf_answer', models.BooleanField(default=False)),
                ('marks', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'db_table': 'fly_question_submissions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=63, null=True)),
                ('description', models.CharField(blank=True, max_length=511, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
            options={
                'db_table': 'fly_quizzes',
            },
        ),
        migrations.CreateModel(
            name='QuizSubmission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('marks', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.EnrolledCourse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'fly_quiz_submissions',
            },
        ),
        migrations.CreateModel(
            name='XPLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('level', models.PositiveSmallIntegerField(choices=[(5, '5 Minutes'), (30, '30 Minutes'), (60, '1 Hour')], default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)])),
                ('required_xp', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)])),
            ],
            options={
                'db_table': 'fly_xp_levels',
            },
        ),
        migrations.AddField(
            model_name='questionsubmission',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.QuizSubmission'),
        ),
        migrations.AddField(
            model_name='questionsubmission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Quiz'),
        ),
    ]
