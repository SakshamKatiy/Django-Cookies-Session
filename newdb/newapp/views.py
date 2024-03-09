from django.shortcuts import render
from tablib import Dataset
from .resources import studentResources
# from .models import students
# Create your views here.

def upload(request):
    if request.method =='POST':
        student_re = studentResources()
        datas = Dataset()
        new_st = request.FILES['myfile']
        imported_d = datas.load(new_st.read())

        result = student_re.import_data(datas , dry_run = True)
            
    return render(request,'index.html')
