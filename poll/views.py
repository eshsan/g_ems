from django.shortcuts import render
from poll.models import *
from django.http import Http404

# Create your views here.
def index(request):
    context = {}
    context['title'] = 'polls'
    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, 'polls/index.html', context)


def details(request, id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
        context['question'] = question

    except:
        raise Http404

    return render(request, 'polls/details.html', context)
