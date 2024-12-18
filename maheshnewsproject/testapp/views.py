from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')
def movies_info(request):
    head_msg = 'welcome to movies information '
    sub_msg1 = 'devara crosess the 500cr collections'
    sub_msg2 = 'gamechenger will relese soon '
    sub_msg3 = 'venkatesh is buesy with sankranthikivastunnam'
    type = 'movies'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
def sports_info(request):
    head_msg = 'welcome to sports information '
    sub_msg1 = 'aus vs ind 2nd test match will be scheduled from 6th dec to 10th dec'
    sub_msg2 = 'virat kohili completed his 81st international century '
    sub_msg3 = 'yeshshvi jaiswal have a bright feuture in cricket '
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
def politics_info(request):
    head_msg = 'welcome to politics information '
    sub_msg1 = 'execution of hydra in hyderabad will impact govt'
    sub_msg2 = 'ktr will come bake with good plan'
    sub_msg3 = 'jagan will fall down day by day'
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
