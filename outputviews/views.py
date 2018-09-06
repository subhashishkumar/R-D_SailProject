import json
import datetime
import collections
from login.models import *
from inputforms.models import *
from outputviews.tables import *
from outputviews.filters import *
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
units_list = Profile.objects.values_list('unit', flat=True).order_by("unit")
accd = AllAccident.objects.defer("age", "emp_name", "narrative", "learning_point")

accd_r = accd.filter(emp_type='Regular')
accd_c = accd.filter(emp_type='Contract')

accd_fa_r = accd_r.filter(accd_type='First-Aid')
accd_fa_c = accd_c.filter(accd_type='First-Aid')

accd_nr_r = accd_r.filter(accd_type='Non-Reportable')
accd_nr_c = accd_c.filter(accd_type='Non-Reportable')

accd_r_r = accd_r.filter(accd_type='Reportable')
accd_r_c = accd_c.filter(accd_type='Reportable')

accd_f_r = accd_r.filter(accd_type='Fatal')
accd_f_c = accd_c.filter(accd_type='Fatal')


def calculate_data_view(accd_reg, accd_contr):
    dt_reg = collections.OrderedDict()
    dt_contr = collections.OrderedDict()
    sum_type = collections.OrderedDict()
    for x in units_list:
        dt_reg[x] = accd_reg.filter(unit_name=x,).count()
        dt_contr[x] = accd_contr.filter(unit_name=x,).count()

    sum_reg = sum(dt_reg.values())
    sum_contr = sum(dt_contr.values())

    for x in units_list:
        sum_type[x] = dt_reg[x] + dt_contr[x]
    sum_total = sum(sum_type.values())
    type_list = zip(units_list, dt_reg.values(), dt_contr.values(), sum_type.values())

    return type_list, sum_reg, sum_contr, sum_total


def parseDate(request):
    date_today = datetime.datetime.now().date().strftime('%Y-%m-%d')
    date_tomorrow = (datetime.datetime.now().date() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    date1 = request.GET.get('start_date', date_today)
    date2 = request.GET.get('end_date', date_tomorrow)
    start_date = datetime.datetime.strptime(date1, '%Y-%m-%d').strftime('%Y-%m-%d')
    end_date = datetime.datetime.strptime(date2, '%Y-%m-%d').strftime('%Y-%m-%d')

    return (start_date, end_date)


@login_required(login_url='/users/login_user/')
def showtables(request):
    return render(request, 'showtables.html',)


@login_required(login_url='/users/login_user/')
def get_data_view(request, accdType):
    type_accd = accdType
    ar = []
    ac = []
    use_name = ""
    time_filter_type = ""
    sum_reg = ""
    sum_contr = ""
    sum_total = ""
    type_list = []

    if type_accd == "fatal":
        ar = accd_f_r
        ac = accd_f_c
        use_name = "Fatal"

    elif type_accd == "first-aid":
        ar = accd_fa_r
        ac = accd_fa_c
        use_name = "First-Aid"

    elif type_accd == "reportable":
        ar = accd_r_r
        ac = accd_r_c
        use_name = "Reportable"

    elif type_accd == "non-reportable":
        ar = accd_nr_r
        ac = accd_nr_c
        use_name = "Non-Reportable"

    start_date, end_date = parseDate(request)
    accd_reg = ar.filter(date__range=(start_date, end_date))
    accd_contr = ac.filter(date__range=(start_date, end_date))
    type_list, sum_reg, sum_contr, sum_total = calculate_data_view(accd_reg, accd_contr)
    time_filter_type = "Records between" + " " + start_date + " to " + end_date

    context = {
        # Genral Default Contexts
        'Header': use_name, 'pagetitle': use_name, 'time': time_filter_type,
        # Query Context
        'list': type_list, 'sum_reg': sum_reg, 'sum_contr': sum_contr, 'sum': sum_total,
    }

    return render(request, 'filter_category_table.html', context)


@login_required(login_url='/users/login_user/')
def year_wise_detailed(request):
    """ get the year total from all the units """
    # fa_year_r, fa_year_reg, fa_year_c, fa_year_contr = first-aid accidents(regular, contracts)
    # f_year_r, f_year_reg, f_year_c, f_year_contr = fatal accidents(regular, contracts)
    # nr_year_r, nr_year_reg, nr_year_c, nr_year_contr = Non-Reportable accidents(regular, contracts)
    # r_year_r, r_year_reg, r_year_c, r_year_contr = Reportable accidents(regular, contracts)

    if request.method == 'GET':
        start_date, end_date = parseDate(request)
        records = "Records between" + " " + start_date + " to " + end_date

        # a list of all accidents type for regular and on contract employee
        accd_type_list = [accd_fa_r, accd_f_r, accd_nr_r, accd_r_r, accd_fa_c, accd_f_c, accd_nr_c, accd_r_c, ]

        # iterating through the accd_type_list and storing the output to their respective variable name
        # for the requested year
        fa_year_r, f_year_r, nr_year_r, r_year_r, fa_year_c, f_year_c, nr_year_c, r_year_c \
            = (accd_type.filter(date__range=(start_date, end_date)) for accd_type in accd_type_list)

        # ordered dictionaries to store the values in a particular order
        fa_year_reg, f_year_reg, nr_year_reg, r_year_reg, \
            fa_year_contr, f_year_contr, nr_year_contr, r_year_contr, \
            sum_fa_year, sum_f_year, sum_nr_year, sum_r_year \
            = (collections.OrderedDict() for x in range(12))

        # a list of type_year_category items
        category_year_type_list = [fa_year_r, f_year_r, nr_year_r, r_year_r, fa_year_c, f_year_c, nr_year_c, r_year_c]

        # iterating through the units_list and storing the accidents count for each accident category for each units
        for unit in units_list:
            fa_year_reg[unit], f_year_reg[unit], nr_year_reg[unit], r_year_reg[unit], \
                fa_year_contr[unit], f_year_contr[unit], nr_year_contr[unit], r_year_contr[unit] \
                = (category_year_type.filter(unit_name=unit,).count() for category_year_type in category_year_type_list)

        # a list of accd_year_type dictionaries
        accd_year_type_list = [fa_year_reg, f_year_reg, nr_year_reg, r_year_reg,
                               fa_year_contr, f_year_contr, nr_year_contr, r_year_contr]

        # calculate the sum of the values of each dictionary in accd_year_type_list
        sum_fa_year_reg, sum_f_year_reg, sum_nr_year_reg, sum_r_year_reg, \
            sum_fa_year_c, sum_f_year_c, sum_nr_year_c, sum_r_year_c \
            = (sum(accd_year_type.values()) for accd_year_type in accd_year_type_list)

        # calculating the sum of each category of accidents from all units
        for x in units_list:
            sum_fa_year[x] = fa_year_reg[x] + fa_year_contr[x]
            sum_f_year[x] = f_year_reg[x] + f_year_contr[x]
            sum_nr_year[x] = nr_year_reg[x] + nr_year_contr[x]
            sum_r_year[x] = r_year_reg[x] + r_year_contr[x]

        # a list of individual sum values of accd_type_year dictionaries
        sum_type_year_list = [sum_fa_year, sum_f_year, sum_nr_year, sum_r_year]

        # calculating the total sum of each accident type
        total_fa_year, total_f_year, total_nr_year, total_r_year \
            = (sum(sum_type_year.values()) for sum_type_year in sum_type_year_list)

        # a list of units_lists and corresponding records of each units
        year_list = zip(
            units_list,
            f_year_reg.values(), f_year_contr.values(), sum_f_year.values(),
            r_year_reg.values(), r_year_contr.values(), sum_r_year.values(),
            nr_year_reg.values(), nr_year_contr.values(), sum_nr_year.values(),
            fa_year_reg.values(), fa_year_contr.values(), sum_fa_year.values(),
        )

        # a list containing sum total values of different accident types items
        total_list = [
            sum_f_year_reg, sum_f_year_c, total_f_year,
            sum_r_year_reg, sum_r_year_c, total_r_year,
            sum_nr_year_reg, sum_nr_year_c, total_nr_year,
            sum_fa_year_reg, sum_fa_year_c, total_fa_year,
        ]

        context = {
            'list': year_list, 'total': total_list, 'records': records,
        }

    return render(request, 'accd_table_detailed.html', context)


class ManhoursFilteredView(LoginRequiredMixin, TemplateView):
    template_name = 'manhours.html'
    login_url = '/users/login_user/'

    def get_queryset(self, **kwargs):
        return Manhours.objects.all().order_by("unit_name")

    def get_context_data(self, **kwargs):
        context = super(ManhoursFilteredView, self).get_context_data(**kwargs)
        filter = ManhoursFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        table = ManhoursTable(filter.qs)
        RequestConfig(self.request, paginate={'per_page': 20}).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context


class AllFilteredView(LoginRequiredMixin, TemplateView):
    template_name = 'filter_accd_table.html'
    login_url = '/users/login_user/'

    def get_queryset(self, **kwargs):
        return AllAccident.objects.all().defer("age", "learning_point").order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(AllFilteredView, self).get_context_data(**kwargs)
        filter = AllAccdFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        table = WithoutLPTable(filter.qs)
        RequestConfig(self.request, paginate={'per_page': 20}).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context


def get_unitname(request):
    if request.is_ajax():
        unit_get = request.GET.get('term', '')
        unitres = Profile.objects.filter(unit__icontains=unit_get)

        unit_results = []

        for x in unitres:
            units_json = {}
            units_json['label'] = x.unit
            units_json['value'] = x.unit

            if units_json not in unit_results:
                unit_results.append(units_json)

        data = json.dumps(unit_results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get_department(request):
    if request.is_ajax():
        dept_get = request.GET.get('term', '')
        deptres = AllAccident.objects.filter(dept__icontains=dept_get)

        dept_results = []

        for x in deptres:
            dept_json = {}
            dept_json['label'] = x.dept
            dept_json['value'] = x.dept

            if dept_json not in dept_results:
                dept_results.append(dept_json)

        data = json.dumps(dept_results)
    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
