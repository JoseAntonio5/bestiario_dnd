from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

# MODELS
from .models import (Usuario,
                     Criatura,
                     Monstro,
                     Personagem)

#FORMS
from django.contrib.auth.forms import AuthenticationForm
from .forms import (loginForm, 
                    RegisterUsuarioForm, 
                    RegisterPersonagemForm, 
                    RegisterCriaturaForm, 
                    RegisterMonstroForm)

# Create your views here.

def indexRedirect(request):
    return redirect('painel')

def loginBestiario(request):
    if request.user.is_authenticated:
        return render(request, 'painel.html')

    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            usuario = Usuario.objects.get(nome=username)
            request.session['id_usuario'] = usuario.id
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'painel.html', {'usuario': usuario})
            else:
                messages.error(request, f'Usuario    ou senha incorretos. Tente novamente.')
                return redirect('/')

        form = loginForm()
        return render(request, 'login.html', {'form': form})

def registrarUsuario(request):
    form = RegisterUsuarioForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            login = form.save(commit=False)
            login.password = make_password(form.cleaned_data['password'])
            login.save()
            messages.success(request, "Usu??rio criado com sucesso!")
            logout(request)
            return redirect('login')
        
    return render(request, 'register.html', {'form': form})

def painel(request):
    return render(request, 'painel.html')

# CRIATURA 

@login_required
def criarCriatura(request):
    form = RegisterCriaturaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Nova criatura cadastrada com sucesso!")
            return redirect('criaturas-cadastradas')

    return render(request, 'cadastrar-criatura.html', {'form': form})

def criaturasCadastradas(request):
    criaturas = Criatura.objects.all()

    paginator = Paginator(criaturas, 10)

    page = request.GET.get('page')

    criatura = paginator.get_page(page)

    return render(request, 'criaturas-cadastradas.html', {'criaturas': criatura})

def detalhesCriaturas(request, id):
    #TODO: Try...except...
    criatura = Criatura.objects.get(id=id)
    return render(request, 'detalhes-criatura.html', {'criatura': criatura})

@login_required
def editarCriatura(request, id):
    try:
        criatura = Criatura.objects.get(id=id)
    except ObjectDoesNotExist or Exception:
        messages.error(request, "Erro, criatura n??o foi encontrada.")
        return redirect('painel')

    if request.method == 'POST':
        try:
            criatura.nickname = request.POST['nickname']
            criatura.acoes = request.POST['acoes']
            criatura.resistencia = request.POST['resistencia']
            criatura.magias = request.POST['magias']
            criatura.status_combate = request.POST['status_combate']
            criatura.alinhamento = request.POST['alinhamento']
            criatura.tamanho = request.POST['tamanho']
            criatura.conhecimento = request.POST['conhecimento']
            criatura.atributos = request.POST['atributos']
            criatura.save()
            messages.success(request, "A criatura foi atualizada com sucesso")
            return redirect('/criaturas-cadastradas/' + id)
        except Exception:
            messages.error(request, "Erro, criatura n??o foi encontrada.")
            return redirect('painel')

    return render(request, 'editar-criatura.html', {'criatura': criatura})

@login_required
def removerCriatura(request, id):
    try:
        criatura = Criatura.objects.get(id=id)
    except ObjectDoesNotExist or Exception:
        messages.error(request, "Erro, criatura n??o foi encontrada.")
        return redirect('painel')

    if request.method == 'POST':
        try:
            criatura.delete()
            messages.success(request, "Criatura removida com sucesso!")
            return redirect('criaturas-cadastradas')
        except Exception:
            messages.error(request, "Erro, criatura n??o foi encontrada.")
            return redirect('error')

    return render(request, 'remover-criatura.html', {'criatura': criatura})


# MONSTRO

@login_required
def criarMonstro(request):
    form = RegisterMonstroForm(request.POST or None)
    criaturas = Criatura.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Novo monstro cadastrado com sucesso!")
            return redirect('monstros-cadastrados')

    return render(request, 'cadastrar-monstro.html', {'form': form, 'criaturas': criaturas})

def monstrosCadastrados(request):
    monstros = Monstro.objects.all()
    return render(request, 'monstros-cadastrados.html', {'monstros': monstros})

def detalhesMonstros(request, id):
    monstro = Monstro.objects.get(id=id)
    return render(request, 'detalhes-monstro.html', {'monstro': monstro})

#FIXME: EDITAR MONSTRO
@login_required
def editarMonstro(request, id):
    criaturas = Criatura.objects.all()
    try:
        monstro = Monstro.objects.get(id=id)
    except ObjectDoesNotExist or Exception:
        messages.error(request, "Erro, monstro n??o foi encontrado.")
        return redirect('painel')

    if request.method == 'POST':
        try:
            monstro.nickname = request.POST['nickname']
            monstro.imagem_url = request.POST['imagem_url']
            monstro.tipo = request.POST['tipo']
            monstro.nivel_dificuldade = request.POST['nivel_dificuldade']
            monstro.vida_min = request.POST['vida_min']
            monstro.vida_max = request.POST['vida_max']
            monstro.save()
            messages.success(request, "O monstro foi atualizado com sucesso")
            return redirect('/monstros-cadastrados/' + id)
        except Exception:
            messages.error(request, "Erro ao editar monstro.")
            return redirect('painel')

    return render(request, 'editar-monstro.html', {'monstro': monstro, 'criaturas': criaturas})

@login_required
def removerMonstro(request, id):
    try:
        monstro = Monstro.objects.get(id=id)
    except ObjectDoesNotExist or Exception:
        messages.error(request, "Erro, monstro n??o foi encontrado.")
        return redirect('painel')

    if request.method == 'POST':
        try:
            monstro.delete()
            messages.success(request, "Monstro removido com sucesso!")
            return redirect('monstros-cadastrados')
        except Exception:
            messages.error(request, "Erro ao remover monstro.")
            return redirect('error')

    return render(request, 'remover-monstro.html', {'monstro': monstro})
# PERSONAGEM

@login_required
def criarPersonagem(request):
    form = RegisterPersonagemForm(request.POST or None)
    criaturas = Criatura.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Novo personagem cadastrado com sucesso!")
            return redirect('personagens-cadastrados')

    return render(request, 'cadastrar-personagem.html', {'form': form, 'criaturas': criaturas})

def personagensCadastrados(request):
    personagens = Personagem.objects.all()
    return render(request, 'personagens-cadastrados.html', {'personagens': personagens})

def detalhesPersonagens(request, id):
    personagem = Personagem.objects.get(id=id)
    return render(request, 'detalhes-personagem.html', {'personagem': personagem})

@login_required
def editarPersonagem(request, id):
    criaturas = Criatura.objects.all()
    usuarios = Usuario.objects.all()
    try:
        personagem = Personagem.objects.get(id=id)
    except ObjectDoesNotExist or Exception:
        messages.error(request, "Erro, personagem n??o foi encontrado.")
        return redirect('painel')

    if request.method == 'POST':
        try:
            personagem.nickname = request.POST['nickname']
            personagem.nome = request.POST['nome']
            personagem.nivel = request.POST['nivel']
            personagem.armas = request.POST['armas']
            personagem.talento = request.POST['talento']
            personagem.mochila = request.POST['mochila']
            personagem.classe = request.POST['classe']
            personagem.save()
            messages.success(request, "O personagem foi atualizado com sucesso")
            return redirect('/personagens-cadastrados/' + id)
        except Exception:
            messages.error(request, "Erro ao editar personagem.")
            return redirect('painel')

    return render(request, 'editar-personagem.html', {'personagem': personagem, 
                                                      'criaturas': criaturas, 
                                                       'usuarios': usuarios})

@login_required
def removerPersonagem(request, id):
    try:
        personagem = Personagem.objects.get(id=id)
    except ObjectDoesNotExist or Exception:
        messages.error(request, "Erro, Personagem n??o foi encontrado.")
        return redirect('painel')

    if request.method == 'POST':
        try:
            personagem.delete()
            messages.success(request, "Personagem removido com sucesso!")
            return redirect('personagens-cadastrados')
        except Exception:
            messages.error(request, "Erro ao remover personagem.")
            return redirect('error')

    return render(request, 'remover-personagem.html', {'personagem': personagem})

def logoutUsuario(request):
    try:
        logout(request)
        return redirect('login')
    except ObjectDoesNotExist or Exception:
        messages.error(request, "Ocorreu um erro.")
        return redirect('painel')