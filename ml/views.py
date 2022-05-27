from django.shortcuts import render, redirect
from ml.models import Tag
from ai.module import pred_tag,b
from db.db_dao import *
def output(request, id):
    data = request.POST
    print('입력한 정보 >> ', data)

    tag = Tag.objects.get(id=id)
    print('tag >> ', tag)
    b=[tag.holiday, tag.week, tag.time, tag.gender, tag.age, tag.size,tag.tag]
    tag =pred_tag(b)[0]
    image =pred_tag(b)[1]
    print(pred_tag(b))
    tag2={'tag':tag, 'img':image}
    return render(request, 'ml/output.html', context=tag2)


def input(request):
    return render(request, "ml/input.html")

def input2(request):
    data = request.POST
    print('입력한 정보 >> ', data)

    input_data = Tag(holiday=data['holiday'], week=data['week'], time=data['time'],
                     gender=data['gender'], age=data['age'], size=data['size'],
                     tag=data['tag'])
    input_data.save()
    print(input_data.id)
    return redirect('/ml/output/' + str(input_data.id))

def index(request):
    return render(request, "ml/index.html")

def chart2(req):
    data = [0.6297657326596233,0.816260909508498,0.6196600826825908,
            0.8171796049609554,0.6669728984841525]
    context = {
        'data' : data
    }
    return render(req, 'ml/statistics.html.', context)


def up(req):
    list1=readAll()
    num_list=[]
    for i in range(0,len(list1),1):
        print(list1[i][0])
        num_list.append(list1[i][0])
    print(num_list)
    for n in num_list:
        vo=read(n)
        print(vo[2])
        print(b(vo[2]))
        cate=b(vo[2])
        vo2=(cate,vo[0])
        update(vo2)

    context={
        'vo':readAll2()
    }
    return render(req, 'ml/up.html.', context)