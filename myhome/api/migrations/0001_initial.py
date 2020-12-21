# Generated by Django 3.0.8 on 2020-12-20 22:53

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('contact', models.CharField(max_length=20, verbose_name='휴대폰 번호')),
                ('birth', models.DateField(verbose_name='생년월일')),
                ('gender', models.CharField(choices=[('남성', '남성'), ('여성', '여성')], max_length=5, verbose_name='성별')),
                ('role', models.CharField(choices=[('집주인', '집주인'), ('세입자', '세입자')], max_length=10, verbose_name='역할')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('zip_code', models.CharField(max_length=10, verbose_name='우편번호')),
                ('room_type', models.CharField(choices=[('원룸', '원룸'), ('투룸', '투룸'), ('쓰리룸', '쓰리룸')], max_length=10, verbose_name='방 종류')),
                ('deposit', models.IntegerField(verbose_name='보증금')),
                ('monthly_rent', models.IntegerField(verbose_name='월세')),
                ('management_fee', models.IntegerField(verbose_name='관리비')),
                ('total_floor', models.IntegerField(verbose_name='전체 층수')),
                ('floor', models.IntegerField(verbose_name='층수')),
                ('structure', models.CharField(max_length=20, verbose_name='구조')),
                ('space', models.IntegerField(verbose_name='전용 면적')),
                ('completion_year', models.IntegerField(verbose_name='준공연도')),
                ('elevator', models.BooleanField(verbose_name='엘레베이터')),
                ('bed', models.BooleanField(verbose_name='침대')),
                ('desk', models.BooleanField(verbose_name='책상')),
                ('refrigerator', models.BooleanField(verbose_name='냉장고')),
                ('induction', models.BooleanField(verbose_name='인덕션')),
                ('air_conditioner', models.BooleanField(verbose_name='에어컨')),
                ('washer', models.BooleanField(verbose_name='세탁기')),
                ('short_term', models.BooleanField(verbose_name='단기 임대')),
                ('heating', models.CharField(choices=[('중앙난방', '중앙난방'), ('개별난방', '개별난방')], max_length=10, verbose_name='난방')),
                ('occupancy_date', models.DateField(verbose_name='입주 가능일')),
                ('introduction', models.CharField(max_length=30, verbose_name='한 줄 소개')),
                ('detail', models.TextField(verbose_name='상세 설명')),
                ('distance', models.CharField(blank=True, max_length=40, null=True, verbose_name='거리')),
                ('landlord_name', models.CharField(max_length=10, verbose_name='집주인 이름')),
                ('landlord_contact', models.CharField(max_length=20, verbose_name='집주인 번호')),
                ('sold_out', models.BooleanField(default=True, verbose_name='활성화')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='api.Account', verbose_name='집주인')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pros', models.CharField(max_length=40, verbose_name='장점')),
                ('cons', models.CharField(max_length=40, verbose_name='단점')),
                ('comment', models.CharField(max_length=40, verbose_name='하고 싶은 말')),
                ('rate', models.FloatField(validators=[api.models.rate_validator], verbose_name='평점')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Room', verbose_name='매물')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Account', verbose_name='세입자')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_file', models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='사진')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='api.Room', verbose_name='매물')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='방문 시간')),
                ('reserved', models.BooleanField(default=False, verbose_name='예약 완료 여부')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='api.Account', verbose_name='집주인')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='interest_rooms',
            field=models.ManyToManyField(blank=True, related_name='users', to='api.Room', verbose_name='관심 매물'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
