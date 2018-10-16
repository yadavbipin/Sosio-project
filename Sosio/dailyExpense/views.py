from django.shortcuts import render

# Create your views here.
from firebase import firebase as fab

from dailyExpense.models import registerdb

fa = fab.FirebaseApplication("https://expense-f7db5.firebaseio.com/", None)
def expenseIndex(request):
    return render(request, "expenses.html")



def loginData(request):
    if(request.method == 'POST'):
        l_email = request.POST.get("email")
        l_password = request.POST.get("pass")

        v = registerdb.objects.filter(email=l_email, password=l_password).all()
        if (len(v) == 1):
            message = {'message': "welcome"}
            return render(request, "home.html", message)
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
    dt = request.POST.get("date")
    it = request.POST.get("items")
    ex = request.POST.get("exp")

    # fa = fab.FirebaseApplication("https://expense-f7db5.firebaseio.com/",None)
    # d2 = fa.get("dailyexpenditure/", None)
    # if d2 == None:
    #     key = 101
    #     d1 = {key:{'date': dt, 'items': it, 'expense': ex}}
    #     fa.put("https://expense-f7db5.firebaseio.com/dailyexpenditure/", key, d1)
    # else:
    #     for x in d2:
    #         key = x
    #     key = int(key) + 1
    #     d1 = {key:{'date': dt, 'items': it, 'expense': ex}}
    #     fa.put("https://expense-f7db5.firebaseio.com/dailyexpenditure/", key, d1)
    #     for k in d1:
    #         print(k, "--", d1[k])
    #     return render(request, "home.html", {"dic": d1})
    return render(request, "home.html")

def saveDetails(request):
    f = request.POST.get("fname")

    d2= fa.get("friendsList/", None)
    if d2 == None:
        key = 101
        d1 = {key: f}
        print(d1)
        fa.put("https://expense-f7db5.firebaseio.com/friendsList/", key, d1)
    else:
        for x in d2:
            key = x
        key = int(key) + 1
        d1 = {key: f}
        fa.put("https://expense-f7db5.firebaseio.com/friendsList/", key, d1)
        for k in d1:
            print(k, "--", d1[k])
        return render(request, "home.html", {"dic": d1})
    m = {'m': 'friend added'}
    return render(request, "home.html", m)

def showfriends(request):
    d3 = fa.get('friendsList/', None)
    if d3==None:
        return render(request, 'home.html', {'msg': 'No Data Available'})
    else:
        return render(request, 'home.html', {'d3': d3})
    return render(request, "home.html")


def deleteRecord(request):
    i = request.POST.get('delete')
    fa.delete('friendsList/', i)
    return showfriends(request)