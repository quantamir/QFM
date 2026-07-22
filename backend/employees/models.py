from django.db import models


UNIT_CHOICES = [
    ('floor1', 'خدمات طبقه اول'),
    ('floor2', 'خدمات طبقه دوم'),
    ('thalassemia', 'خدمات تالاسمی'),
    ('laboratory', 'خدمات آزمایشگاه'),
    ('pharmacy', 'خدمات داروخانه'),
    ('linen', 'لنژری'),
    ('csr', 'CSR'),
    ('waste', 'پسماند'),
    ('patient_transport', 'بیماربر'),
    ('pantry_floor1', 'آبدارخانه طبقه اول'),
    ('pantry_floor3', 'آبدارخانه و سالن غذاخوری طبقه سوم'),
    ('security', 'حراست'),
    ('driver_official', 'راننده استخدامی'),
    ('driver_private', 'راننده خصوصی'),
    ('warehouse', 'انبار خدمات'),
    ('wheelchair', 'مدیریت ویلچر'),
]


EMPLOYMENT_TYPE_CHOICES = [
    ('shift', 'شیفتی'),
    ('fixed', 'ثابت'),
]


class Employee(models.Model):

    first_name = models.CharField(
        max_length=100,
        verbose_name="نام"
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="نام خانوادگی"
    )

    personnel_code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="کد پرسنلی"
    )

    national_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="کد ملی"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="شماره تماس"
    )

    unit = models.CharField(
        max_length=30,
        choices=UNIT_CHOICES,
        verbose_name="واحد"
    )

    employment_type = models.CharField(
        max_length=10,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default="fixed",
        verbose_name="نوع فعالیت"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "پرسنل"
        verbose_name_plural = "پرسنل"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"