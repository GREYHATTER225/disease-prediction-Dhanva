from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth.models import User , auth
from main_app.models import patient , doctor
from datetime import datetime

# Create your views here.


def logout(request):
    auth.logout(request)
    request.session.pop('patientid', None)
    request.session.pop('doctorid', None)
    request.session.pop('adminid', None)
    return render(request,'homepage/index.html')


def sign_in_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid username or password for admin account.')
            return redirect('sign_in_admin')
        if user.is_superuser:
            auth.login(request, user)
            return redirect('admin_ui')
        else:
            messages.info(request, 'This account is not a superuser/admin.')
            return redirect('sign_in_admin')
    else:
        return render(request, 'admin/signin/signin.html')


def signup_patient(request):
    if request.method == 'POST':
        if all([request.POST.get('username'), request.POST.get('email'), request.POST.get('name'), request.POST.get('dob'), request.POST.get('gender'), request.POST.get('address'), request.POST.get('mobile_no'), request.POST.get('password'), request.POST.get('password1')]):
            username =  request.POST.get('username')
            email =  request.POST.get('email')
            name =  request.POST.get('name')
            dob =  request.POST.get('dob')
            gender =  request.POST.get('gender')
            address =  request.POST.get('address')
            mobile_no = request.POST.get('mobile_no')
            password =  request.POST.get('password')
            password1 =  request.POST.get('password1')
            if password == password1:
                if User.objects.filter(username = username).exists():
                    messages.info(request,'username already taken')
                    return redirect('signup_patient')
                elif User.objects.filter(email = email).exists():
                    messages.info(request,'email already taken')
                    return redirect('signup_patient')
                else :
                    user = User.objects.create_user(username=username,password=password,email=email)   
                    user.save()
                    patientnew = patient(user=user,name=name,dob=dob,gender=gender,address=address,mobile_no=mobile_no)
                    patientnew.save()
                    messages.info(request,'user created sucessfully')
                    return redirect('sign_in_patient')
            else:
                messages.info(request,'password not matching, please try again')
                return redirect('signup_patient')
        else :
            messages.info(request,'Please make sure all required fields are filled out correctly')
            return redirect('signup_patient') 
    else :
        return render(request,'patient/signup_Form/signup.html')


def sign_in_patient(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid username or password.')
            return redirect('sign_in_patient')
        if not hasattr(user, 'patient') or not user.patient.is_patient:
            messages.info(request, 'This account is not a patient account. Please use doctor login or signup as patient.')
            return redirect('sign_in_patient')
        auth.login(request, user)
        request.session['patientusername'] = user.username
        return redirect('patient_ui')
    else:
        return render(request, 'patient/signin_page/index.html')


def savepdata(request,patientusername):
    if request.method == 'POST':
        name =  request.POST['name']
        dob =  request.POST['dob']
        gender =  request.POST['gender']
        address =  request.POST['address']
        mobile_no = request.POST['mobile_no']
        dobdate = datetime.strptime(dob,'%Y-%m-%d')
        puser = User.objects.get(username=patientusername)
        patient.objects.filter(pk=puser.patient).update(name=name,dob=dobdate,gender=gender,address=address,mobile_no=mobile_no)
        return redirect('pviewprofile',patientusername)


def signup_doctor(request):
    if request.method == 'GET':
        return render(request,'doctor/signup_Form/signup.html')
    if request.method == 'POST':
        if all([request.POST.get('username'), request.POST.get('email'), request.POST.get('name'), request.POST.get('dob'), request.POST.get('gender'), request.POST.get('address'), request.POST.get('mobile_no'), request.POST.get('password'), request.POST.get('password1'), request.POST.get('registration_no'), request.POST.get('year_of_registration'), request.POST.get('qualification'), request.POST.get('state_medical_council'), request.POST.get('specialization')]):
            username =  request.POST.get('username')
            email =  request.POST.get('email')
            name =  request.POST.get('name')
            dob =  request.POST.get('dob')
            gender =  request.POST.get('gender')
            address =  request.POST.get('address')
            mobile_no = request.POST.get('mobile_no')
            registration_no =  request.POST.get('registration_no')
            year_of_registration =  request.POST.get('year_of_registration')
            qualification =  request.POST.get('qualification')
            State_Medical_Council =  request.POST.get('state_medical_council')
            specialization =  request.POST.get('specialization')
            password =  request.POST.get('password')
            password1 =  request.POST.get('password1')
            if password == password1:
                if User.objects.filter(username = username).exists():
                    messages.info(request,'username already taken')
                    return redirect('signup_doctor')
                elif User.objects.filter(email = email).exists():
                    messages.info(request,'email already taken')
                    return redirect('signup_doctor')
                else :
                    user = User.objects.create_user(username=username,password=password,email=email)   
                    user.save()
                    doctornew = doctor( user=user, name=name, dob=dob, gender=gender, address=address, mobile_no=mobile_no, registration_no=registration_no, year_of_registration=year_of_registration, qualification=qualification, State_Medical_Council=State_Medical_Council, specialization=specialization )
                    doctornew.save()
                    messages.info(request,'user created sucessfully')
                    return redirect('sign_in_doctor')
            else:
                messages.info(request,'password not matching, please try again')
                return redirect('signup_doctor')
        else :
            messages.info(request,'Please make sure all required fields are filled out correctly')
            return redirect('signup_doctor') 


def sign_in_doctor(request):
    if request.method == 'GET':
        return render(request, 'doctor/signin_page/index.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid username or password.')
            return redirect('sign_in_doctor')
        if not hasattr(user, 'doctor') or not user.doctor.is_doctor:
            messages.info(request, 'This account is not a doctor account. Please use patient login or signup as doctor.')
            return redirect('sign_in_doctor')
        auth.login(request, user)
        request.session['doctorusername'] = user.username
        return redirect('doctor_ui')


def saveddata(request,doctorusername):
    if request.method == 'POST':
        name =  request.POST['name']
        dob =  request.POST['dob']
        gender =  request.POST['gender']
        address =  request.POST['address']
        mobile_no = request.POST['mobile_no']
        registration_no =  request.POST['registration_no']
        year_of_registration =  request.POST['year_of_registration']
        qualification =  request.POST['qualification']
        State_Medical_Council =  request.POST['State_Medical_Council']
        specialization =  request.POST['specialization']
        dobdate = datetime.strptime(dob,'%Y-%m-%d')
        yor = datetime.strptime(year_of_registration,'%Y-%m-%d')
        duser = User.objects.get(username=doctorusername)
        doctor.objects.filter(pk=duser.doctor).update( name=name, dob=dobdate, gender=gender, address=address, mobile_no=mobile_no, registration_no=registration_no, year_of_registration=yor, qualification=qualification, State_Medical_Council=State_Medical_Council, specialization=specialization )
        return redirect('dviewprofile',doctorusername)
