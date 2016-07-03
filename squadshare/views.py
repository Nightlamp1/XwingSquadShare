from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, password_validation
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from squadbuilder.forms import LoginForm
from squadshare.models import SavedSquads, SquadComments, UserUpvotes
from squadbuilder.models import Pilots, Upgrades

# Create your views here.
def index(request):

    if request.method == 'POST':
        squad_id = request.POST['squadId']
        squad = SavedSquads.objects.get(id=squad_id)
        
        if request.user.is_authenticated():
            current_user = request.user
            check_if_voted = UserUpvotes.objects.filter(user=current_user, squad=squad).exists()

            if check_if_voted:
                return HttpResponse(squad.upvotes)
            else:
                previous_upvotes = squad.upvotes
                current_upvotes = previous_upvotes + 1
                squad.upvotes = current_upvotes
                user_upvote = UserUpvotes(user=current_user,squad=squad)
                user_upvote.save()
                squad.save()
                return HttpResponse(squad.upvotes)
        else:
            return HttpResponse(squad.upvotes)

    
    def squadReader(squad_query):
        squad_readout = []
        for squad in squad_query:
            query_array=[]
            pilot_list =[]
            squadcode = squad.squadcode
            squadcode = squadcode.split('p')
            for item in squadcode:
                if item == "":
                     pass
                else:
                    query_array.append(item.split('u'))
            for query in query_array:
                upgrade_array=[]
                pilot_dict=[]
                for index, query_id in enumerate(query):
                    if index == 0:
                        pilot = Pilots.objects.get(id=query_id)
                        pilot_dict.append(pilot.name)
                    else:
                        upgrade = Upgrades.objects.get(id=query_id)
                        upgrade_array.append(upgrade.name)
                pilot_dict.append(upgrade_array)
                pilot_list.append(pilot_dict)
            squad_readout.append({'name':squad.name ,'list':pilot_list, 'squadcode':squad.squadcode})
        return squad_readout
    recent_squads = SavedSquads.objects.all().order_by('-createdDate')[:5]
    squad_list = squadReader(recent_squads)
    hottest_squads = SavedSquads.objects.all().order_by('-upvotes')[:5]
    hot_list = squadReader(hottest_squads)
    return render(request, 'squadshare/home.html', {'recent_squads':recent_squads,'squad_list':squad_list
                                                    ,'hottest_squads':hottest_squads, 'hot_list':hot_list})
          

def contact(request):
    return render(request, 'squadshare/basic.html',{'content':['If you would like to contact me:',
                                                             'robert.britt2011@gmail.com']})

#Break out into seperate app?
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #see if username is already taken
        if form.is_valid():
            form.save()
            return render(request,'squadshare/basic.html',{'content':["Registration Successful"]})
        else:
            return render(request, 'squadshare/basic.html', {'content':["Failed Registration"]})
    else:
        form = UserCreationForm()
        c={}
        c.update(csrf(request))
        c['form'] = form
        help_text = password_validation.password_validators_help_texts()
        c['help_text']=help_text
        return render(request, 'squadshare/register.html',c)
    
#Break out into seperate app?
@csrf_protect
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return render(request, 'squadshare/basic.html', {'content':["Login successful"]})
            else:
                return render(request, 'squadshare/basic.html', {'content':["Failed Login"]})
        else:
            return render(request, 'squadshare/basic.html', {'content':["failed login"]})
    else:
        c={}
        c.update(csrf(request))
        return render(request, 'squadshare/login.html',c)

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')


def profile(request, username):
        user = User.objects.get(username=username)
        user_squads = SavedSquads.objects.filter(user=user)
        return render(request, 'squadshare/profile.html', {'user_squads':user_squads})

def squad(request, squadcode):

    def squadReader(squad_query):
        squad_readout = []
        for squad in squad_query:
            query_array=[]
            pilot_list =[]
            squadcode = squad.squadcode
            squadcode = squadcode.split('p')
            for item in squadcode:
                if item == "":
                        pass
                else:
                    query_array.append(item.split('u'))
            for query in query_array:
                upgrade_array=[]
                pilot_dict=[]
                for index, query_id in enumerate(query):
                    if index == 0:
                        pilot = Pilots.objects.get(id=query_id)
                        pilot_name = pilot.name.replace(" ","")
                        pilot_name = pilot_name.replace("'","")
                        if pilot.faction == "Scum":
                            pilot_dict.append(pilot_name+"Scum")
                        else:    
                            pilot_dict.append(pilot_name)
                    else:
                        upgrade = Upgrades.objects.get(id=query_id)
                        upgrade_array.append((upgrade.name).replace(" ",""))
                pilot_dict.append(upgrade_array)
                pilot_list.append(pilot_dict)
            squad_readout.append({'name':squad.name ,'list':pilot_list, 'squadcode':squad.squadcode, 'cost':squad.cost, 'creator':squad.user})
        return squad_readout
    
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        squadcode = request.POST['squadcode']
        squad = SavedSquads.objects.get(squadcode=squadcode)
        comments = SquadComments.objects.all().filter(squad=squad)
        entry = SquadComments(comment=comment, user=user, squad=squad)
        entry.save()
        squad_query = SavedSquads.objects.all().filter(squadcode=squadcode)
        squad_list = squadReader(squad_query)
        return render(request, 'squadshare/squad.html',{'squad':squad_list,'comments':comments})


    else:
        squad_code = squadcode
        squad=SavedSquads.objects.all().filter(id=squad_code)
        squad_list = squadReader(squad)
        comments = SquadComments.objects.all().filter(squad=squad_code)
        return render(request, 'squadshare/squad.html',{'squad':squad_list, 'comments':comments})
