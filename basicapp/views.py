from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('validation success!')
            print('NAME: '+ form.cleaned_data['name'])
            print('EMAIL: '+ form.cleaned_data['email'])
            print('MESSAGE: '+ form.cleaned_data['message'])

    form_dict = {'form_key':form}
    return render(request,'basicapp/form_page.html',context=form_dict)
