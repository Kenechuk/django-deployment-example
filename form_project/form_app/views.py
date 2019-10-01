from django.shortcuts import render
from form_app import forms

# Create your views here.
def index(request):
    return render(request, 'form_app/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Valied Form")
            print('Name: '+form.cleaned_data['name'])
            print('email: '+form.cleaned_data['email'])
            print('Text: '+form.cleaned_data['text'])


    return render(request,'form_app/froms_app.html',{'form':form})
