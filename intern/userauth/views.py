from django.shortcuts import render, redirect
from .forms import PatientSignUpForm, DoctorSignUpForm

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to patient dashboard or display details
            return redirect('patient_dashboard')
    else:
        form = PatientSignUpForm()

    return render(request, 'patient_signup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to doctor dashboard or display details
            return redirect('doctor_dashboard')
    else:
        form = DoctorSignUpForm()

    return render(request, 'doctor_signup.html', {'form': form})
def patient_dashboard(request):
    return render(request,'patient_dashboard.html')

