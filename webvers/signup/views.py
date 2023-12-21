from django.shortcuts import render
import mysql.connector as sql

# Create your views here.
def signupact(request):
    global fn, ln, s, em, pw
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="1122", database='webvers')
        cursor = m.cursor()
        fn = request.POST.get('first_name', '')
        ln = request.POST.get('last_name', '')
        s = request.POST.get('sex', '')
        em = request.POST.get('email', '')
        pw = request.POST.get('password', '')

        c = "insert into users (first_name, last_name, sex, email, password) values ('{}', '{}', '{}', '{}', '{}')".format(fn, ln, s, em, pw)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')
