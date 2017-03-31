from django.shortcuts import render



from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from django.contrib import messages
from .forms import GameForm
from .models import GamesModel

from django.http import HttpResponse



# Create your views here.


def home(request):
    return render(request=request, template_name='StoreHome/home.html')

def developer_games(request):
    if request.method == 'GET':
        dev_games = GamesModel.objects.filter(_developer=request.user.profile)

        response = {}
        games = []
        response['games'] = games
        for g in dev_games:
            tmp = g.to_json_dict()
            response['games'].append(tmp)

        if request.is_ajax():
            return JsonResponse(data=response)

        else:
            form = GameForm()
            return render(request, 'Developer/developed_games.html', {'form': form, 'user': request.user, 'games': games})
    elif request.method == 'POST':
        form = GameForm(request.POST)
        if not form.is_valid():
            return render(request, "Registration/register.html", {'form': form})
        else:
            form.instance._developer = request.user.profile
            game = form.save()
            dev_games = GamesModel.objects.filter(_developer=request.user.profile)
            games = [x.to_json_dict() for x in dev_games]
            messages.success(request=request, message='Added successfully!')
            return render(request, 'Developer/developed_games.html', {'form': GameForm, 'user': request.user, 'games':games})
    else:
        return HttpResponse(status=405, content="Invalid method.")
