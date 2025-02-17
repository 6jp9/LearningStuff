from django.shortcuts import render
from testapp.forms import StdDobForm

# Create your views here.
def form_display(request):
    submit = False
    if request.method == 'POST':
        form = StdDobForm(request.POST)
        if form.is_valid():
            # print('name:',form.cleaned_data['name'])
            # print('roll:',form.cleaned_data['roll_no'])
            # print('dob:',form.cleaned_data['date_of_birth'])
            # print('success!!!.....bro')
            form.save(commit=True)
            submit = True
    form = StdDobForm()
    return render(request,'testapp/index.html',{'form':form,'submit':submit})