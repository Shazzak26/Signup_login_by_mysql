from django.shortcuts import render
import mysql.connector as sql
em=""
pw=""

# Create your views here.
def loginact(request):
    global em, pw
    if request.method=="POST":
        m=sql.connect(host='localhost', user='root', passwd='1122',database='webvers')
        cursor=m.cursor()
        em=request.POST.get("email",'')
        pw=request.POST.get("password",'')

        c="select * from users where email='{}' and password = '{}'".format(em,pw)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, "error.html")
        else:
            return render(request, "welcome.html")
        
    return render(request, "login_page.html")
