from django.shortcuts import render, redirect
from ml.models import Tag
from ai.module import pred_tag
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