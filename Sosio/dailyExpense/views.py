from django.shortcuts import render

# Create your views here.
from dailyExpense.models import registerdb


def expenseIndex(request):
    return render(request, "expenses.html")



def loginData(request):
    if(request.method == 'POST'):
         name = request.POST.get("uname")
         password = request.POST.get("pass")
    return render(request, "login.html")



def registerData(request):
    if(request.method =='post'):
        firstname = request.POST.get("fname")
        lastname= request.POST.get("lname")
        ema = request.POST.get("email")
        phone =  request.POST.get("phno")
        passw = request.POST.get("pass")

        r = registerdb(first_name=firstname, last_name=lastname, email=ema,phone_no=phone,password=passw)
        r.save()
        message = {'message': "data saved"}
        return render(request, "registration.html", message)
    return render(request, "registration.html")


