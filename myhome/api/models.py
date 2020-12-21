from django.db import models
from django import forms
from django.contrib.auth.models import User


class Account(models.Model):
    GENDER_CHOICES = [
        ('남성', '남성'),
        ('여성', '여성'),
    ]

    ROLE_CHOICES = [
        ('집주인', '집주인'),
        ('세입자', '세입자'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest_rooms = models.ManyToManyField('Room', related_name='users', verbose_name='관심 매물', blank=True)
    name = models.CharField('이름', max_length=20)
    contact = models.CharField('휴대폰 번호', max_length=20)
    birth = models.DateField('생년월일')
    gender = models.CharField('성별', max_length=5, choices=GENDER_CHOICES)
    role = models.CharField('역할', max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name, self.role


class Appointment(models.Model):
    user = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='appointments', verbose_name='집주인')
    time = models.DateTimeField('방문 시간')
    reserved = models.BooleanField('예약 완료 여부', default=False)


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('원룸', '원룸'),
        ('투룸', '투룸'),
        ('쓰리룸', '쓰리룸'),
    ]

    HEATING_CHOICES = [
        ('중앙난방', '중앙난방'),
        ('개별난방', '개별난방'),
    ]

    user = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='rooms', verbose_name='집주인')
    address = models.CharField('주소', max_length=100)
    zip_code = models.CharField('우편번호', max_length=10)
    room_type = models.CharField('방 종류', max_length=10, choices=ROOM_TYPE_CHOICES)
    deposit = models.IntegerField('보증금')
    monthly_rent = models.IntegerField('월세')
    management_fee = models.IntegerField('관리비')
    total_floor = models.IntegerField('전체 층수')
    floor = models.IntegerField('층수')
    structure = models.CharField('구조', max_length=20)
    space = models.IntegerField('전용 면적')
    completion_year = models.IntegerField('준공연도')
    elevator = models.BooleanField('엘레베이터')
    bed = models.BooleanField('침대')
    desk = models.BooleanField('책상')
    refrigerator = models.BooleanField('냉장고')
    induction = models.BooleanField('인덕션')
    air_conditioner = models.BooleanField('에어컨')
    washer = models.BooleanField('세탁기')
    short_term = models.BooleanField('단기 임대')
    heating = models.CharField('난방', max_length=10, choices=HEATING_CHOICES)
    occupancy_date = models.DateField('입주 가능일')
    introduction = models.CharField('한 줄 소개', max_length=30)
    detail = models.TextField('상세 설명')
    distance = models.CharField('거리', max_length=40, null=True, blank=True)
    landlord_name = models.CharField('집주인 이름', max_length=10)
    landlord_contact = models.CharField('집주인 번호', max_length=20)
    sold_out = models.BooleanField('활성화', default=True)

    def __str__(self):
        return self.address


def rate_validator(value):
    if value < 0 or value > 5:
        raise forms.ValidationError('0 ~ 5 사이의 숫자를 입력해주세요.')


class Review(models.Model):
    user = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='reviews', verbose_name='세입자')
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='reviews', verbose_name='매물')
    pros = models.CharField('장점', max_length=40)
    cons = models.CharField('단점', max_length=40)
    comment = models.CharField('하고 싶은 말', max_length=40)
    rate = models.FloatField('평점', validators=[rate_validator])


class Photo(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='photos', verbose_name='매물')
    photo_file = models.ImageField('사진', upload_to='photo/%Y/%m/%d')  # request.FIELS['image_files'] -> MEDIA_ROOT
    # path: image.image_file.path  MEDIA_ROOT/photo/~/~/~/~.jpg (절대 경로) - 경로에 저장
    # url: image.image_file.url  MEDIA_URL/photo/~/~/~/~.jpg (상대 경로) - DB에 문자열로 저장
