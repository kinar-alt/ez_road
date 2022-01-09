from typing import cast
from django.shortcuts import render,HttpResponse
import datetime
from .forms import ContactUsform
from django.shortcuts import redirect
# Create your views here.
def home(request):
    form=ContactUsform
    context={'form':form}
    return render(request,'index.html',context)

# def contact(request):
#     form=ContactUsform
#     context={'form':form}

#     return render(request,'contact.html',context)

def instructors(request):
    return render(request,'instructors.html')

def booking(request):
    
    time={'6-8':'vacant','8-10':'vacant','10-12':'vacant','12-2':'no','2-4':'no','4-6':'vacant','6-8':'vacant','8-10':'vacant'}
    context={'data':time}
    print(context)
    return render(request,'booking.html',context
    # # ,context={
    # #     "current_day":current_day
    # }
    )


def reserve(request):
    return render(request,'reserve.html')



def post(request):
    if request.method=='POST':
        form=ContactUsform(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            address=request.POST.get('address')
            zipcode=request.POST.get('zipCode')
            queries=request.POST.get('queries')
            form.save()
            print(email,address,zipcode,queries)
        # if form.is_valid():
        #     email = user.POST.get("email") 
        #     print(email)
    return redirect('home')



























# def get_next_seven_days():
#     now=datetime.datetime.now()
#     current_day=now.weekday()
#     thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#     days={
#     '0':'Monday'
#     ,'1':'Tuesday'
#     ,'2':'Wednesday'
#     ,'3':'Thursday'
#     ,'4':'Friday'
#     ,'5':'Saturday'
#     ,'6': 'Sunday'}

#     for key_dict in days.keys():
#         if int(key_dict)==current_day:
#             print(days['0'])