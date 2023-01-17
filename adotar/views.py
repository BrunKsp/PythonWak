from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from divulgar.models import Pet , Raca
from django.contrib import messages
from django.contrib.messages import constants
from .models import PedidoAdocao
from datetime import datetime



def listar_pets (request):
    if request.method == 'GET':
        pets = Pet.objects.filter(status = "P")
        racas = Raca.objects.all()
        


    cidade = request.GET.get('cidade')
    raca_filter = request.GET.get('raca')

    if cidade :
        pets = pets.filter(cidade__icontains=cidade)

    if raca_filter :
        pets = pets.filter(raca_id=raca_filter)
        raca_filter = Raca.objects.get(id = raca_filter)
    return render(request, 'listar_pet.html',{'pets':pets ,'racas': racas , 'cidade':cidade ,'raca_filter':raca_filter})



@login_required
def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status="P")

    
    if not pet.exists():
        messages.add_message(request, constants.WARNING, 'Esse pet já foi adotado :)')
        return redirect('/adotar')
    
    
    
    pedido = PedidoAdocao(pet=pet.first(),
                          usuario=request.user,
                          data=datetime.now())
    pedido.save()

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    return redirect('/adotar')


@login_required
def ver_pedido_adocao(request):
    if request.method == "GET":
        pedidos = PedidoAdocao.objects.filter(usuario=request.user).filter(status="AG")
        return render(request, 'ver_pedido_adocao.html', {'pedidos': pedidos})

