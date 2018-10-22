import datetime

from django.shortcuts import render

# Create your views here.
from firebase import firebase as fab

from dailyExpense.models import registerdb, Userdetails, friendsList


fa = fab.FirebaseApplication("https://expense-f7db5.firebaseio.com/", None)
phone = 0
def expenseIndex(request):
    if 'phone' in request.session:
        del request.session['phone']
    return render(request, "expenses.html")



def loginData(request):
    if(request.method == 'POST'):
        l_email = request.POST.get("email")
        l_password = request.POST.get("pass")

        v = registerdb.objects.filter(email=l_email, password=l_password).all()
        if (len(v) == 1):

            mess = v[0].phone_no
            request.session['phone'] = mess
            return render(request, "home.html", {'phone': mess})
        else:
            msg = {'msg': "Invalid Email Id Or Password ! Dont have account please register"}
            return render(request, "login.html", msg)
    return render(request, "login.html")




def registerData(request):
    if(request.method =='POST'):
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        ema = request.POST.get("email")
        phone = request.POST.get("phno")
        passw = request.POST.get("pass")

        r = registerdb(first_name=firstname, last_name=lastname, email=ema, phone_no=phone, password=passw)
        e = registerdb.objects.filter(email=ema).all()
        #(list(e)[0].email)
        if (len(e) == 1):
            return render(request, "registration.html", {'invalid':"This email id is already Registered ! please choose another id or login"})
        else:
            r.save()
            message = {'message': "You are successfully registered Login using Email Id and Password"}
            return render(request, "login.html", message)

    return render(request, "registration.html")


def showdetails(request):

    ph = request.session['phone']
    dt = request.POST.get("date")
    it = request.POST.get("expenselist")
    ex = request.POST.get("exp")
    u = Userdetails(date=dt, list=it, expense=ex, phone_no=ph)
    u.save()
    e = Userdetails.objects.filter(phone_no=ph).all()
    if(e == None):
        return render(request, "home.html", {'fd': 'NO friends'})
    return render(request, "home.html")


def saveDetails(request):
    p = request.session['phone']
    f = request.POST.get("fname")
    fl = friendsList(phone_no=p, friend=f)
    fl.save()
    return render(request, "home.html", {'phone': p})

def showfriends(request):
    d3 = friendsList.objects.filter(phone_no=request.session['phone'])


    if d3==None:
        return render(request, 'home.html', {'msg': 'No Data Available'})
    else:
        return render(request, 'home.html', {'d3': d3})


def deleteRecord(request):
    i = request.POST.get('delete')
    friendsList.objects.filter(phone_no=request.session['phone']).delete()
    return showfriends(request)


def view(request):
    if (request.method=='POST'):
        s_date = request.POST.get('start')
        e_date = request.POST.get('end')

        format_str = '%Y-%m-%d'
        sdate_obj = datetime.datetime.strptime(s_date, format_str).date()
        edate_obj = datetime.datetime.strptime(e_date, format_str).date()

        ph = Userdetails.objects.filter(phone_no=request.session['phone'])
        res = list(ph)
        sum =0
        for x in res:
            if x.date >= sdate_obj and x.date<=edate_obj:
                sum += int(x.expense)
                return render(request, "view.html", {'sum':sum})
            else:
                f = friendsList.object.filter(phone_no=request.session['phone'])
                r = list(f)
                sum += int(x.expense)/len(r)
                return render(request, "view.html", {'sum': sum})
    return render(request, "view.html",)