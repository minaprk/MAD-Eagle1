from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render

from appl.forms import LoginForm, UserForm, SelectionForm
from appl.models import Article, Customer, Appointment


def index(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            Customer.objects.create(user=new_user)
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login/edit/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = UserForm()
        args = {'form': form}
        return render(request, 'register.html', args)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'base.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def booking(request):
    if request.user.customer.appointment:
        appointment_id_old = request.user.customer.appointment_id

    if request.method == 'POST':
        form = SelectionForm(request.POST, instance=request.user.customer)
        if form.is_valid():
            if request.user.customer.appointment_id:
                request.user.customer.appointment_allotted = True
                a_id_after = request.user.customer.appointment_id
                appointment = Appointment.objects.get(id=a_id_after)
                appointment.vacant = False
                appointment.save()
                try:
                    appointment = Appointment.objects.get(id=appointment_id_old)
                    appointment.vacant = True
                    appointment.save()
                except BaseException:
                    pass
            else:
                request.user.customer.appointment_allotted = False
                try:
                    appointment = Appointment.objects.get(id=appointment_id_old)
                    appointment.vacant = True
                    appointment.save()
                except BaseException:
                    pass
            form.save()
            return render(request, 'contact.html')
    else:
        form = SelectionForm(instance=request.user.customer)
        appointment_service_type = request.user.customer.appointment.service.service_type
        appointment = Appointment.objects.filter(
            service = appointment_service_type)
        x = Appointment.objects.none()
        if appointment_service_type == 'C':
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=['C'], vacant=True)
                x = x | a
        elif appointment_service_type == 'HC':
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=['HC'], vacant=True)
                x = x | a
        elif appointment_service_type == 'HS':
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=['HS'], vacant=True)
                x = x | a
        elif appointment_service_type == 'MU':
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=['MU'], vacant=True)
                x = x | a
        elif appointment_service_type == 'M':
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=['M'], vacant=True)
                x = x | a
        elif appointment_service_type == 'D':
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=['D'], vacant=True)
                x = x | a
        elif appointment_service_type == 'P':
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=['P'], vacant=True)
                x = x | a
        elif appointment_service_type == 'S':
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=['S'], vacant=True)
                x = x | a
        else:
            for i in range(len(appointment)):
                a_id = appointment[i].id
                a = Appointment.objects.filter(
                    appointment_id=a_id, service_type=appointment_service_type, vacant=True)
                x = x | a
        form.fields["appointment"].queryset = x
        return render(request, 'booking.html', {'form': form})


def blog(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'blog.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Not found!")

    return render(request, 'detail.html', {'article': a})


def contact(request):
    return render(request, 'contact.html')
