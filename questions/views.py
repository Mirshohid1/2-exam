from django.shortcuts import render, HttpResponse
from .forms import QuestionsForm
from .models import Questions

def questions(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'questions_success.html')
        else:
            return render(request, 'questions.html', {'form': form})
    else:
        form = QuestionsForm()

    return render(request, 'questions.html', {'form': form})

def questions_all(request):
    questions_ = Questions.objects.all()
    ctx = {'questions': questions_}

    return render(request, 'questions_all.html', ctx)