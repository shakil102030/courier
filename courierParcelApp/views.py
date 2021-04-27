from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Order, OrderForm, Merchants
from django.contrib import messages

def OrderView(request):
    merchnts = Merchants.objects.all()
    if request.method == "POST":
        form = OrderForm(request.POST)
        print("checkout...")
        if form.is_valid():
            dat = Order()
            dat.merchant_nm = merchant_nm = form.cleaned_data['merchant_nm']
            dat.product_type = form.cleaned_data['product_type']
            dat.status = form.cleaned_data['status']
            dat.location = form.cleaned_data['location']
            dat.weight = form.cleaned_data['weight']
            dat.delivery_charge = form.cleaned_data['delivery_charge']
            dat.cod_charge = form.cleaned_data['cod_charge']
            dat.return_charge = form.cleaned_data['return_charge']
            dat.save()
            messages.warning(request, "Successfully submitted")
            return redirect('OrderView')
    form = OrderForm()

    context = {
        'form': form,
        'merchnts': merchnts,
    }
    return render(request, "base.html", context)

def OrderTable(request):
    order_charge  = Order.objects.all().order_by('-id')
    context = {
        'order_charge': order_charge,
    }
    return render(request, 'order_table.html', context)



