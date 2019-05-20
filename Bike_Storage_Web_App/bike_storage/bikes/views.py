from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from bikes.models import Bike

class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = "__all__"

def bike_list(request, template_name='bikes/bike_list.html'):
    bike = Bike.objects.all()
    data = {}
    data['object_list'] = bike
    return render(request, template_name, data)

def bike_create(request, template_name='bikes/bike_form.html'):
    form = BikeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('bike_list')
    return render(request, template_name, {'form':form})

def bike_update(request, pk, template_name='bikes/bike_form.html'):
    bike = get_object_or_404(Bike, pk=pk)
    form = BikeForm(request.POST or None, request.FILES or None, instance=bike)
    if form.is_valid():
        form.save()
        return redirect('bike_list')
    return render(request, template_name, {'form':form})

def bike_delete(request, pk, template_name='bikes/bike_confirm_delete.html'):
    bike = get_object_or_404(Bike, pk=pk)    
    if request.method=='POST':
        bike.delete()
        return redirect('bike_list')
    return render(request, template_name, {'object':bike})

def bike_view(request, pk, template_name='bikes/bike_detail.html'):
    bike = get_object_or_404(Bike, pk=pk)   
    return render(request, template_name, {'object':bike})


