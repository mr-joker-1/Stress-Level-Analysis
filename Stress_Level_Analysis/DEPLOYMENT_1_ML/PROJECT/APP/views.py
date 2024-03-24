from django.shortcuts import render, redirect
from . models import UserPredictModel
from . forms import UserPredictForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    
Model = joblib.load('E:/Projects/ITPML12 - STRESS/DEPLOYMENT_1_ML/PROJECT/APP/MODEL1.pkl')
    
def Deploy_8(request): 
    if request.method == 'POST':
        fieldss = ['sr','rr','t','lm','bo','rem','srh','hr']
        form = UserPredictForm(request.POST)
        features = []
        for i in fieldss:
            info = request.POST[i]
            features.append(info)
        Final_features = [np.array(features)]
        prediction = Model.predict(Final_features)
        actual_output = prediction[0]
        if actual_output == 0:
            actual_output = "VERY LESS STRESS LEVEL AFFECTED"
        elif actual_output == 1:
            actual_output = "LESS STRESS LEVEL AFFECTED"
        elif actual_output == 2:
            actual_output = "MODERATE STRESS LEVEL AFFECTED"
        elif actual_output == 3:
            actual_output = "HIGH STRESS LEVEL AFFECTED"
        elif actual_output == 4:
            actual_output = "VERY HIGH STRESS LEVEL AFFECTED"


        print(features)
        print(actual_output)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        
        data = UserPredictModel.objects.latest('id')
        data.label = actual_output
        data.save()
        
        return render(request, '8_Deploy.html', {'form':form, 'prediction_text':actual_output})
    else:
        print('Else working')
        form = UserPredictForm(request.POST)    
    return render(request, '8_Deploy.html', {'form':form})

def Out_Database_9(request):
    models = UserPredictModel.objects.all()
    return render(request, '9_Out_Database.html', {'models':models})

def Logout(request):
    logout(request)
    return redirect('Landing_1')
