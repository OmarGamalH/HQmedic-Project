from django.shortcuts import render 
from django.contrib.auth import authenticate , logout , login
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import  csrf_exempt
from django import forms
from django.http import HttpResponseRedirect , JsonResponse 
from django.urls import reverse
from .decorators import logedin
import json
from django.db.models import Count
from django.conf import settings
from django.core import serializers
class login_form(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {"class" : "field" , "placeholder" : "Email Address"  , "id" : "patient_login_email"}) , label = False)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {"class" : "field" , "placeholder" : "Password" , "id": "patient_login_password"}) , label = False)
    pass
class doctor_l_form(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {"class" : "field" , "placeholder" : "Email Address"  , "id" : "doctor_login_email"}) , label = False)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {"class" : "field" , "placeholder" : "Password" , "id": "doctor_login_password"}) , label = False)
class register_form(forms.Form):
     email = forms.EmailField(widget = forms.EmailInput(attrs = {"class" : "field" , "placeholder" : "Email Address"  , "id" : "patient_register_email"}) , label = False)
     username = forms.CharField(widget = forms.TextInput(attrs = {"class" : "field" , "placeholder" : "Username" , "id" : "patient_register_username"}) , label = False , max_length = 65 , required = False)
     password = forms.CharField(widget = forms.PasswordInput(attrs = {"class" : "field" , "placeholder" : "Password" , "id": "patient_register_password"}) , label = False)
     phonenumber = forms.CharField(max_length = 20 , required = False , widget = forms.TextInput(attrs = {"placeholder" : "Phone Number" , "class" : "field" , "id" : "patient_register_phonenumber"}) , label = False)
     age = forms.IntegerField(widget = forms.NumberInput(attrs = {"class" : "field" , "placeholder" : "Age" , "id" : "patient_register_age"}) , label = False , min_value = 1 , max_value = 150 , required = False)
     choices = [("male" , "Male") , ("female" , "Female")]
     gender = forms.ChoiceField(widget = forms.RadioSelect(attrs = {"id" : "patient_register_gender"}) , choices = choices , required = False)
class doctor_r_form(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {"class" : "field" , "placeholder" : "Email Address"  , "id" : "doctor_register_email"}) , label = False)
    username = forms.CharField(widget = forms.TextInput(attrs = {"class" : "field" , "placeholder" : "Username" , "id" : "doctor_register_username"}) , label = False , max_length = 65 , required = False)
    password = forms.CharField(widget = forms.PasswordInput(attrs = {"class" : "field" , "placeholder" : "Password" , "id": "doctor_register_password"}) , label = False)
    age = forms.IntegerField(widget = forms.NumberInput(attrs = {"class" : "field" , "placeholder" : "Age" , "id" : "doctor_register_age"}) , label = False , min_value = 1 , max_value = 150, required = False)
    choices = [("male" , "Male") , ("female" , "Female")]
    phonenumber = forms.CharField(max_length = 20 , required = False , widget = forms.TextInput(attrs = {"placeholder" : "Phone Number" , "class" : "field" , "id" : "doctor_register_phonenumber"}) , label = False)
    gender = forms.ChoiceField(widget = forms.RadioSelect(attrs = {"id" : "doctor_register_gender"}) , choices = choices , required = False)
    choices = [("Allergist/Immunologist" , "Allergist/Immunologist") , ("Anesthesiologist" , "Anesthesiologist") , ("Cardiologist" , "Cardiologist") , ("Colon and Rectal Surgeon" , "Colon and Rectal Surgeon") , ("Critical Care Medicine Specialist" , "Critical Care Medicine Specialist") , ("Dermatologist" , "Dermatologist") , ("Endocrinologist" , "Endocrinologist") , ("Family Physician" , "Family Physician")
               , ("Gastroenterologist" , "Gastroenterologist") , ("Geriatric Medicine Specialist" , "Geriatric Medicine Specialist") , ("Hematologist" , "Hematologist") , ("Hospice and Palliative Medicine Specialist" , "Hospice and Palliative Medicine Specialist") , ("Infectious Disease Specialist" , "Infectious Disease Specialist") , ("Internist" , "Internist")
               , ("Medical Geneticist" , "Medical Geneticist") , ("Nephrologist" , "Nephrologist") , ("Neurologist" , "Neurologist") , ("Obstetrician and Gynecologist" , "Obstetrician and Gynecologist") , ("Oncologist" , "Oncologist")
               , ("Ophthalmologist" , "Ophthalmologist") , ("Osteopath" , "Osteopath")  , ("Otolaryngologist" , "Otolaryngologist") , ("Pathologist" , "Pathologist") , ("Pediatrician" , "Pediatrician") , ("Physiatrist" , "Physiatrist") , ("Plastic Surgeon" , "Plastic Surgeon") , ("Podiatrist" , "Podiatrist") , 
               ("Preventive Medicine Specialist" , "Preventive Medicine Specialist") , ("Psychiatrist" , "Psychiatrist") , ("Pulmonologist" , "Pulmonologist") , ("Radiologist" , "Radiologist") , ("Rheumatologist" , "Rheumatologist") , ("Sleep Medicine Specialist" , "Sleep Medicine Specialist") , ("Sports Medicine Specialist" , "Sports Medicine Specialist") , ("General Surgeon" , "General Surgeon") , ("Urologist" , "Urologist")]
    specialist = forms.CharField(widget = forms.Select(choices = choices) , label = False)
class add_image_form(forms.Form):
    image = forms.ImageField(label = False )




# Create your views here.
@login_required
def index(request):
    if request.session["status"] == "patient":
        doctors_specialists = doctor.objects.values("specialist").annotate(sum = Count("specialist"))
        doctors = doctor.objects.all().order_by("-likes")
        return render(request , "first_app/index.html" , {"status" : request.session["status"] , "doctor_specialists" :  doctors_specialists , "doctors" : doctors})
    elif request.session["status"] == "doctor":
        doctor_info = request.user.doctor_info.first()
        patients = doctor_info.my_patients.all()
        print(patients)
        return render(request , "first_app/index.html" , {"status" : request.session["status"] , 
        "doctor_info" : doctor_info,
        "patients" : patients,
                                                      })
@logedin
def login_view(request):
    return render(request , "first_app/login.html" , {
        "login_form" : login_form , "patient_login_error" : "" , "patient_register_error" : "" , "register_form" :register_form , "doctor_l_form" : doctor_l_form , "doctor_r_form" : doctor_r_form
    })

def login_patient(request):
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request , username = email , password = password)
            
            if user:
                if user.is_patient == False:
                    return render(request , "first_app/login.html" , {
                    "patient_login_error" : "Please register as patient" , "login_form" : login_form , "register_form" : register_form , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
                login(request , user)
                request.session["status"] = "patient"
                return  HttpResponseRedirect(reverse("index"))
            else:
                return render(request , "first_app/login.html" , {
                    "patient_login_error" : "Invalid password/email" , "login_form" : login_form , "register_form" : register_form , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
        else:
            return render(request , "first_app/login.html" , {
                 "login_form" : form , "register_form" : register_form , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
    else:
        return HttpResponseRedirect(reverse("login"))
            
def logout_view(request):
    
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def patient_register(request):
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]
            age = form.cleaned_data["age"]
            gender = form.cleaned_data["gender"]
            user = authenticate(request , username = email , password = password)
            if user:
                #  user exist
                is_patient = user.is_patient
                if is_patient:
                    return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : form , "patient_register_error" : "User already exist" , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
                else:
                    user.is_patient = True
                    user.save()
                    patient_file = patient(user = user)
                    patient_file.save()
                    doctor_patient_relation = doctor_patient(patient = patient_file)
                    doctor_patient_relation.save()
                    doctor_patient_like = doctor_patient_liked(patient = patient_file)
                    doctor_patient_like.save()
                    patient_pending_row = patient_pending(patient = patient_file)
                    patient_pending_row.save()
                    login(request , user)
                    request.session["status"] = "patient"
                    return HttpResponseRedirect(reverse("index"))
            else:
                try:
                        if not age or not gender or not username:
                            return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : form , "patient_register_error" : "You must enter all required info" , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
                        user =  User.objects.create_user(username = username , email = email , password = password , is_patient = True , age = age , gender = gender)
                        patient_file = patient(user = user)
                        patient_file.save()
                        doctor_patient_relation = doctor_patient(patient = patient_file)
                        doctor_patient_relation.save()
                        doctor_patient_like = doctor_patient_liked(patient = patient_file)
                        doctor_patient_like.save()
                        patient_pending_row = patient_pending(patient = patient_file)
                        patient_pending_row.save()
                        login(request , user)
                        request.session["status"] = "patient"
                        return HttpResponseRedirect(reverse("index"))
                except:
                    return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : form , "patient_register_error" : "Password is Wrong" , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
            
        else:
               return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : form , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
                
def login_doctor(request):
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request , username = email , password = password)
            if user:
                if user.is_doctor == False:
                    return render(request , "first_app/login.html" , {
                    "doctor_login_error" : "Please register as Doctor" , "login_form" : login_form , "register_form" : register_form , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
                login(request , user)
                request.session["status"] = "doctor"
                return  HttpResponseRedirect(reverse("index"))
            else:
                return render(request , "first_app/login.html" , {
                    "doctor_login_error" : "Invalid password/email" , "login_form" : login_form , "register_form" : register_form , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
        else:
            return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : register_form , "doctor_r_form" : doctor_r_form , "doctor_l_form" : form
                })
    else:
        return HttpResponseRedirect(reverse("login"))
    
def doctor_register(request):
    if request.method == "POST":
        form = doctor_r_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]
            age = form.cleaned_data["age"]
            gender = form.cleaned_data["gender"]
            specialist = form.cleaned_data["specialist"]
            phonenumber = form.cleaned_data["phonenumber"]
            user = authenticate(request , username = email , password = password)
            if user:
                #  user exist
                is_doctor = user.is_doctor
                if is_doctor:
                    return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : register_form , "doctor_register_error" : "User already exist" , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
                else:
                    user.is_doctor = True
                    user.save()
                    doctor_file =  doctor( user = user , specialist = specialist)
                    doctor_file.save()
                    login(request , user)
                    request.session["status"] = "doctor"
                    return HttpResponseRedirect(reverse("index"))
            else:
                try:    
                        if not username or not age or not gender:
                             return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : register_form , "doctor_register_error" : "You must enter all required info" , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
                        user =  User.objects.create_user( username = username , email = email , password = password , is_doctor = True , age = age , gender = gender , phonenumber = phonenumber)
                        doctor_file =  doctor(user = user , specialist = specialist )
                        doctor_file.save()
                        login(request , user)
                        request.session["status"] = "doctor"
                        return HttpResponseRedirect(reverse("index"))
                except :
                    return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : register_form , "doctor_register_error" : "Password is Wrong" , "doctor_r_form" : doctor_r_form , "doctor_l_form" : doctor_l_form
                })
            
        else:
               return render(request , "first_app/login.html" , {
                 "login_form" : login_form , "register_form" : register_form , "doctor_r_form" : form , "doctor_l_form" : doctor_l_form
                })



@csrf_exempt
def liked(request):
    if request.method == "POST":
        body = request.body
        body = json.loads(body)
        id = body["id"]
        doctor_file = doctor.objects.get(pk = id)
        user = User.objects.get(pk = request.user.id)
        patient_file = user.patient_info.all()[0]
        liked_doctors = patient_file.liked_doctors.all()[0]
        liked_doctors = liked_doctors.doctors.all()
        if not doctor_file in liked_doctors:
            return JsonResponse({
                "liked":False
            })
        else:
            return JsonResponse({
                "liked" :True
            })
@csrf_exempt
def like(request):
    if request.method == "POST":
        body = request.body
        body = json.loads(body)
        id = body["id"]
        like = body["like"]
        doctor_file = doctor.objects.get(pk = id)
        user = User.objects.get(pk = request.user.id)
        patient_file = user.patient_info.all()[0]
        liked_doctors = patient_file.liked_doctors.all()[0]
        liked_doctors = liked_doctors.doctors
        #  the doctor will be liked
        if like:
            doctor_file.likes = doctor_file.likes + 1
            doctor_file.save()
            liked_doctors.add(doctor_file)
        else:
            doctor_file.likes = doctor_file.likes - 1
            doctor_file.save()
            liked_doctors.remove(doctor_file)
        return JsonResponse({
            "massage" : "like/dislike done successfully"
        })
@csrf_exempt
def added(request):
    if request.method == "POST":
        body = request.body
        body = json.loads(body)
        id = body["id"]
        doctor_file = doctor.objects.get(pk = id)
        user = request.user
        patient_file = user.patient_info.first()
        patient_doctor = patient_file.my_doctors.first()
        pending_doctors = patient_file.patient_pendings.first().doctors.all()
        doctors = patient_doctor.doctors.all()
        if doctor_file in pending_doctors or doctor_file in doctors:
            return JsonResponse({
                "added" : True
            })
        else:
            return JsonResponse({
                "added" : False
            })

@csrf_exempt 
def add(request):
    if request.method == "POST":
        body = request.body
        body = json.loads(body)
        add = body["add"]
        id = body["id"]
        doctor_file = doctor.objects.get(pk = id)
        user = request.user
        patient_file = user.patient_info.first()
        pending_file = patient_pending.objects.get(patient = patient_file)
        patient_doctor = patient_file.my_doctors.first()
        doctors = patient_doctor.doctors
        pending_doctors = pending_file.doctors
        if add == True:
            pending_doctors.add(doctor_file)
        else:
            if doctor_file in doctors.all():
                doctors.remove(doctor_file)
            elif doctor_file in pending_doctors.all():
               pending_doctors.remove(doctor_file)
        return JsonResponse({
            "massage" : "doctor was added/removed successfully"
        })
@login_required
def profile(request ,status , id):
    profile_person = User.objects.get(pk = id)
    category = status
    if category == "doctor":
        doctor_file = profile_person.doctor_info.first()
    if category == "doctor" and request.session["status"] == "patient":
        try:
            doctor_file = profile_person.doctor_info.first()
            patient_file = request.user.patient_info.first()
            doctors = patient_file.my_doctors.first().doctors.all()
            my_doctor = doctor_file in doctors
            massages = massage.objects.filter(patient = patient_file , doctor = doctor_file)
            advices = doctor_file.doctor_advices.all()
            my_patient = None
        except:
            my_doctor = False
            massages = None
            my_patient = None
            advices = None
    elif category == "patient" and request.session["status"] == "doctor":
        my_doctor = False
        massages = None
        advices = None
        doctor_file = None
        try:
            user = User.objects.get(pk = id)
            patient_info = user.patient_info.first()
            doctor_info = request.user.doctor_info.first()
            massages =  massage.objects.filter(patient = patient_info , doctor = doctor_info)
            doctors = patient_info.my_doctors.first().doctors.all()
            my_patient = True if doctor_info in doctors else False
        except:
            my_patient = None
            massages = None
    else:
        my_patient = None
        my_doctor = None
        massages = None
        if request.session["status"] == "doctor":
            doctor_file = profile_person.doctor_info.first()
            advices = doctor_file.doctor_advices.all()
        else:
            advices = None
            doctor_file = None
    
    return render(request , "first_app/profile.html" , {
        "status" : request.session["status"] , "my_doctor" : my_doctor , "advices" : advices, "doctor_file" : doctor_file,  "my_patient" : my_patient , "massages": massages , "profile_person" : profile_person , "image_form" : add_image_form , "category" : status
    })


def add_photo(request , status):
    if request.method == "POST":
        id = request.POST["id"]
        if int(id) == int(request.user.id):
            profile_person = User.objects.get(pk = id)
            form = add_image_form(request.POST , request.FILES)
            if form.is_valid():
                image = form.cleaned_data["image"]
                profile_person.photo = image
                profile_person.save()
        return HttpResponseRedirect(reverse("profile" , kwargs = {"status" : status , "id" : id}))

@csrf_exempt
def my_doctors(request):
    if request.method == "POST":
        user = request.user
        patient_file = user.patient_info.first()
        patient_doctor = patient_file.my_doctors.first()
        doctors = patient_doctor.doctors
        doctors_specialists = list(doctors.values("specialist").annotate(sum = Count("specialist")))
        doctors = doctors.all()
        doctors = serializers.serialize("json" ,doctors)
        test = json.loads(doctors)

        for doctor_file in test:
            doctor_file["fields"]["user"] = json.loads(serializers.serialize("json" , User.objects.filter(pk = doctor_file["fields"]["user"])))
        return JsonResponse({
            "doctors" : test,
             "doctors_specialists" : doctors_specialists
        })
@csrf_exempt
def add_advice(request):
    if request.method == "POST":
        body = request.body
        body = json.loads(body)
        doctor_id = body["id"]
        advice = body["advice"]
        doctor_id_2 = request.user.doctor_info.first().id
        if int(doctor_id) == int(doctor_id_2):
            try:
                doctor_info = doctor.objects.get(pk = doctor_id)
                advice_info = doctors_advices(doctor = doctor_info , advice = advice)
                advice_info.save()
                return JsonResponse({"message" : "advice was posted"})
            except:
                return JsonResponse({"message" : "advice wasn't Post"})
        else:
            return JsonResponse({"message" : "advice wasn't posted"})

def pending(request):
    if request.session["status"] == "doctor":
        doctor_info = doctor.objects.get(user = request.user)
        pending_patients = doctor_info.doctor_pendings.all()
        print(pending_patients)
        return render(request , "first_app/pending.html" , {
            "status" : request.session["status"] , 
            'pending_patients' : pending_patients
        })
    elif request.session["status"] == "patient":
        patient_info = request.user.patient_info.first()
        pending_doctors = patient_info.patient_pendings.first().doctors.all()
        return render(request , 'first_app/pending.html' , {
            'status' : request.session["status"],
            'pending_doctors' : pending_doctors
        })
    
def confirm(request):
    confirm = request.POST.get("confirm")
    delete =  request.POST.get("delete")
    id = confirm if confirm else delete
    doctor_info = doctor.objects.get(user = request.user)
    patient_info = patient.objects.get(pk = id)
    patient_doctor = patient_info.my_doctors.first()
    pending_patient = patient_info.patient_pendings.first()
    doctors = pending_patient.doctors
    doctors.remove(doctor_info)
    if confirm:
        patient_doctor.doctors.add(doctor_info)
    elif delete:
        pass
    return HttpResponseRedirect(reverse("pending"))

def advices(request):
    advices = doctors_advices.objects.all().order_by("date")
    if request.session["status"] == "doctor":
        doctor_info = request.user.doctor_info.first()
    else:
        doctor_info = None
    return render(request , "first_app/advices.html" , {
        "advices" : advices,
        "status" : request.session["status"],
        "doctor_info" : doctor_info
    })
def massaging(request):
    title = request.POST.get("title")
    massage_data = request.POST.get("massage")
    id = request.POST.get("id")
    print(id)
    print(massage)
    print(title)
    user = User.objects.get(pk = id)
    if request.session["status"] == "patient":
        # patient
        patient_info = patient.objects.get(user = request.user)
        # doctor
        doctor_info = user.doctor_info.first()
        status = "doctor"

    else:
        # doctor
        doctor_info = doctor.objects.get(user = request.user)
        #patient
        patient_info = patient.objects.get(user = user)
        status = "patient"
    if massage != "":
        title = title if title != "" else "No Title"
        massage_info = massage(patient = patient_info , doctor = doctor_info , massage = massage_data , title = title , sender = request.user )
        massage_info.save()
    return HttpResponseRedirect(reverse("profile" , kwargs= {"status" : status,"id" : int(id)}))
        
def remove(request):
    patient_id = request.POST.get("id")
    patient_file = patient.objects.get(pk = patient_id)
    doctors = patient_file.my_doctors.first().doctors
    doctor_file = doctor.objects.get(user = request.user)
    doctors.remove(doctor_file)
    return HttpResponseRedirect(reverse("index"))