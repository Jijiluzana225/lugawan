import datetime
from django.shortcuts import render, redirect
from .models import halin
from django.contrib import messages
from django.utils import timezone
from . import forms
from django.db.models import Sum, Avg, Count






# Create your views here.
def index(request):
    if request.method == "POST":
        if 'plain' in request.POST:

        
            branch= "Macabalan"
            item = "Plain Lugaw"
            price= "20"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Plain Lugaw - " + str(transdate))
        
        elif 'withegg' in request.POST:
            branch= "Macabalan"
            item = "Lugaw with Egg"
            price= "35"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Lugaw with Egg - " + str(transdate))

        elif 'laman' in request.POST:
            branch= "Macabalan"
            item = "Lugaw with Laman"
            price= "55"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Lugaw with Laman - " + str(transdate))
        
        elif 'extraegg' in request.POST:
            branch= "Macabalan"
            item = "Extra Egg"
            price= "15"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Extra Egg - " + str(transdate))
        
        elif 'lumpia' in request.POST:
            branch= "Macabalan"
            item = "Lumpia Toge"
            price= "10"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Lumpia Toge - " + str(transdate))


        elif 'softdrinks' in request.POST:
            branch= "Macabalan"
            item = "Softdrink"
            price= "15"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Softdrink - " + str(transdate))

        elif 'Canister' in request.POST:
            branch= "Macabalan"
            item = "Canister"
            price= "10"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Canister - " + str(transdate))
        
        elif 'sisigrice' in request.POST:
            branch= "Macabalan"
            item = "Sisig with Rice"
            price= "85"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Sisig with Rice - " + str(transdate))
        
        elif 'sisig' in request.POST:
            branch= "Macabalan"
            item = "Sisig Only"
            price= "75"
      
            transdate = datetime.datetime.now()
            halin1= halin(branch=branch,item=item, price=price, transdate=transdate)
            halin1.save()
            messages.success(request, "Sisig Only - " + str(transdate))
        
        
    
   
    today = timezone.now().date()
 

    plain = halin.objects.filter(item="Plain Lugaw", transdate__date=today).count()
    withegg= halin.objects.filter(item="Lugaw with Egg", transdate__date=today).count()
    laman= halin.objects.filter(item="Lugaw with Laman", transdate__date=today).count()
    extraegg= halin.objects.filter(item="Extra Egg", transdate__date=today).count()
    lumpia = halin.objects.filter(item="Lumpia Toge", transdate__date=today).count()
    softdrinks= halin.objects.filter(item="Softdrink", transdate__date=today).count()
    Canister= halin.objects.filter(item="Canister", transdate__date=today).count()
    sisigrice= halin.objects.filter(item="Sisig with Rice", transdate__date=today).count()
    sisig= halin.objects.filter(item="Sisig Only", transdate__date=today).count()


    totalhalin = list(halin.objects.filter(transdate__date=today).aggregate(Sum('price')).values())[0]

    data = halin.objects.all().filter(transdate__date=today).order_by('-transdate')

    order_by_item = halin.objects.all().filter(transdate__date=today).order_by('item')
    

    



    print(plain)
    print (today)

    context = {
        'plain': plain,
        'withegg':withegg,
        'laman': laman,
        'totalhalin': totalhalin,
        'extraegg': extraegg,
        'lumpia': lumpia,
        'softdrinks': softdrinks,
        'canister': Canister,
        'sisigrice': sisigrice,
        'sisig':sisig,
        'alldata': data,
        'order_by_item':order_by_item,
        


    }

    return  render(request, ('index.html'),context)
        
def macabalan(request):
    if request.method == "POST":
        pass

    return  render(request, ('macabalan.html'))



def expense(request):
 
    form = forms.CreateExpense

    initial_datax ={
        'branch':"Macabalan",
        'transdate': datetime.datetime.now(),
        }
    
    form = forms.CreateExpense(initial=initial_datax)    
    
    if request.method == "POST":
        form = forms.CreateExpense(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    
    return render(request, ('expenseform.html'), {'form':form})
