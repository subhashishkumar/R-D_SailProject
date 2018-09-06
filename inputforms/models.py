from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator

EMP_TYPE = (
    ('Regular', 'Regular'),
    ('Contract', 'Contract'),
)

ACCD_TYPE = (
    ('Fatal', 'Fatal'),
    ('Reportable', 'Reportable'),
    ('Non-Reportable', 'Non-Reportable'),
    ('First-Aid', 'First-Aid'),
)

SHIFT_TYPE = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('G', 'G'),
)

common_list = [
    ('Fall of material', 'Fall of material'),
    ('Material handling', 'Material handling'),
    ('Road incident', 'Road incident'),
    ('Slip', 'Slip'),
    ('Fall of person', 'Fall of person'),
    ('Burn', 'Burn'),
    ('Electrocution', 'Electrocution'),
    ('Gas exposure', 'Gas exposure'),
    ('Hit/Caught/Pressed', 'Hit/Caught/Pressed'),
]

other_list = [
    ('Violation of SOPs', 'Violation of SOPs'),
    ('Violation of SMPs', 'Violation of SMPs'),
    ('BBS Aspects', 'BBS Aspects'),
    ('Equipment Failure', 'Equipment Failure'),
]

causes_list = (
    ('Common Causes:', tuple(common_list)),
    ('Others:', tuple(other_list)),
)

# Create your models here.
class AllAccident(models.Model):
    unit_name = models.CharField(max_length=50, verbose_name='Unit Name')
    emp_id = models.CharField(max_length=15, verbose_name='Employee ID')
    emp_type = models.CharField(max_length=20, choices=EMP_TYPE, default='Regular', verbose_name='Employee Type')
    emp_name = models.CharField(max_length=30, verbose_name='Employee Name')
    age = models.PositiveSmallIntegerField(default='21', verbose_name='Age', validators=[MinValueValidator(18), MaxValueValidator(65)])
    dept = models.CharField(max_length=50, verbose_name='Department')
    shift = models.CharField(max_length=5, choices=SHIFT_TYPE, default='A', verbose_name='Shift')
    accd_type = models.CharField(max_length=30, choices=ACCD_TYPE, default='Fatal', verbose_name='Accident Type')
    date = models.DateTimeField(verbose_name='Date and Time')
    cause = models.CharField(max_length=100, choices=causes_list, default='Slip', verbose_name='Accident Cause')
    narrative = models.TextField(verbose_name='Narrative')
    learning_point = models.CharField(max_length=100, verbose_name='Learning Point', blank=True)

    class Meta:
        verbose_name_plural = 'Accident Details'

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.emp_id, self.unit_name, self.accd_type, self.emp_type)


class Manhours(models.Model):
    unit_name = models.CharField(max_length=30, verbose_name='Unit Name')
    date = models.DateField(verbose_name='Date')
    manhours_worked_regular = models.PositiveIntegerField(verbose_name='Manhours Worked Regular', default=0)
    manhours_worked_contract = models.PositiveIntegerField(verbose_name='Manhours Worked Contract', default=0)
    mandays_lost = models.PositiveIntegerField(verbose_name='Man-Days Lost', default=0)

    class Meta:
        verbose_name_plural = 'Manhours Details'

    def get_monthly_counts(self):
        month_number = self.date.strftime('%m')
        tc = AllAccident.objects.filter(
            unit_name=self.unit_name, date__month=month_number).defer("emp_name", "narrative", "learning_point")
        fc = tc.filter(accd_type='Fatal').count()
        rc = tc.filter(accd_type='Reportable').count()
        nrc = tc.filter(accd_type='Non-Reportable').count()
        mw = self.manhours_worked_regular + self.manhours_worked_contract
        return fc, rc, nrc, mw

    @property
    def RLTIFR(self):
        fc, rc, nrc, manhours_worked = self.get_monthly_counts()
        self.rltifr = (fc + rc) * 1000000
        self.rltifr = Decimal(self.rltifr) / manhours_worked
        return round(self.rltifr, 4)

    @property
    def LTIFR(self):
        fc, rc, nrc, manhours_worked = self.get_monthly_counts()
        self.ltifr = (fc + rc + nrc) * 1000000
        self.ltifr = Decimal(self.ltifr) / manhours_worked
        return round(self.ltifr, 4)

    @property
    def SEVERITY_RATE(self):
        fc, rc, nrc, manhours_worked = self.get_monthly_counts()
        self.severity_rate = self.mandays_lost * 1000000
        self.severity_rate = Decimal(self.severity_rate) / manhours_worked
        return round(self.severity_rate, 4)

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(
            self.date,
            self.unit_name,
            self.manhours_worked_regular,
            self.manhours_worked_contract,
            self.mandays_lost,
        )
