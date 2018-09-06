from inputforms.models import *
import django_tables2 as tables


class WithoutLPTable(tables.Table):
    class Meta:
        model = AllAccident
        exclude = ('id', 'age', 'learning_point')
        sequence = (
            'unit_name', 'accd_type', 'emp_id', 'emp_type', 'emp_name', 'date', 'shift', 'cause',
            'dept', 'narrative',
        )
        attrs = {
            'class': 'paleblue',
            'width': '100%',
            'th': {
                'style': 'text-align: center;'
                'height: 40px;'
                'background-color: white;'
            },
            'td': {
                'style': 'text-align: center;'
                'height: 40px;'
            }
        }


class WithLPTable(tables.Table):
    class Meta:
        model = AllAccident
        exclude = ('id', 'age',)
        sequence = (
            'unit_name', 'accd_type', 'emp_id', 'emp_type', 'emp_name', 'date', 'shift', 'cause',
            'dept', 'narrative', 'learning_point',
        )
        attrs = {
            'class': 'paleblue',
            'width': '100%',
            'th': {
                'style': 'text-align: center;'
                'height: 40px;'
                'background-color: white;'
            },
            'td': {
                'style': 'text-align: center;'
                'height: 40px;'
            }
        }


class ManhoursTable(tables.Table):
    RLTIFR = tables.Column('RLTIFR',)
    LTIFR = tables.Column('LTIFR', )
    SEVERITY_RATE = tables.Column('SEVERITY_RATE',)

    class Meta:
        model = Manhours
        exclude = 'id'
        sequence = (
            'unit_name', 'date', 'manhours_worked_regular', 'manhours_worked_contract', 'mandays_lost',)
        attrs = {
            'class': 'paleblue',
            'width': '100%',
            'th': {
                'style': 'text-align: center;'
                'height: 40px;'
                'background-color: white;'
            },
            'td': {
                'style': 'text-align: center;'
                'height: 40px;'
            }
        }
