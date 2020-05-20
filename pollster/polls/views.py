from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import Http404,HttpResponse,request,HttpResponseRedirect #for http404 error in detail class
# Create your views here.
from .models import Choice,Question

#get question and display them
def index(request):
    # there is minus sign for decending order  

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    context = { 'latest_question_list': latest_question_list }
    
    return render(request, 'polls/index.html', context)

    
#show specific question and choices
def detail(request, question_id):
    try:
        question_id = int(question_id)  #question id parameter is string so we r just converting in to integer
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question Does Not Exist')
    return render(request, 'polls/detail.html', {'question':question})
    
def results(request,question_id):
    question_id = int(question_id)
    question = get_object_or_404(Question,pk=question_id)#cool one
    return render(request, 'polls/results.html', {'question':question})

     
def vote(request,question_id):
    question_id = int(question_id)
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk= request.POST['choice'])
        
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'polls/details.html',
                {
                    'question' : question,
                    'error_message' : "You didn't select a choice."
                }
                )
    else:
        selected_choice.votes  +=  1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))