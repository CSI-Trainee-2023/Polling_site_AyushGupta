from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
def index(request):
    que_list=Question.objects.order_by("-pub_text")[:5]
    context={'que_list':que_list}
    return render(request,'polls.html',context)
def detail(request,question_id):
    question=Question.objects.get(pk=question_id)
    return render(request, 'ques_choice.html',{'question':question})