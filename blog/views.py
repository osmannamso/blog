from django.shortcuts import render
import random
from django.http import HttpResponse
from blog.models import Theme, Topic, Article

# Create your views here.
def tol(request):
    imgs = ['https://media.self.com/photos/58adf9d18557fe118ba6098a/4:3/w_728,c_limit/gigi-hadid-reebok.png', 'https://www.esquire.my/uploadfiles/images/contents/women/horizontal/emrata_photoshop.jpg', 'http://celebrityinsider.org/wp-content/uploads/2018/09/Leonardo-DiCaprio-WallPapersr.FilmiBeat.com_-e1538073010143.jpg', 'https://static.independent.co.uk/s3fs-public/thumbnails/image/2016/01/01/09/amber-heard_0.jpg?w968h681']
    allTopics = Topic.objects.all()
    q = ''
    Article.objects.all().delete()
    for topic in allTopics:
        a = random.randint(0, 3)
        article1 = Article(title='Диета после праздников', description='Диета это пресс', content='This is content of article', author_id=15, img_url=imgs[a], helpful=True, seen=random.randint(1,100), topic_id=topic.id)
        article2 = Article(title='Диета после праздников', description='Диета это пресс',content='This is content of article', author_id=15, img_url=imgs[a], helpful=False,seen=random.randint(1, 100), topic_id=topic.id)
        article3 = Article(title='Диета после праздников', description='Диета это пресс',
                           content='This is content of article', author_id=15, img_url=imgs[a], helpful=True,
                           seen=random.randint(1, 100), topic_id=topic.id)
        article4 = Article(title='Диета после праздников', description='Диета это пресс',
                           content='This is content of article', author_id=15, img_url=imgs[a], helpful=True,
                           seen=random.randint(1, 100), topic_id=topic.id)
        article5 = Article(title='Диета после праздников', description='Диета это пресс',
                           content='This is content of article', author_id=15, img_url=imgs[a], helpful=False,
                           seen=random.randint(1, 100), topic_id=topic.id)
        article6 = Article(title='Диета после праздников', description='Диета это пресс',
                           content='This is content of article', author_id=15, img_url=imgs[a], helpful=False,
                           seen=random.randint(1, 100), topic_id=topic.id)
        article1.save()
        article2.save()
        article3.save()
        article4.save()
        article5.save()
        article6.save()

    return HttpResponse(q)
def alu(request):
    themes = Theme.objects.all()
    for theme in themes:
        theme.icon = 'asd'
        theme.click_icon = 'asd'
        theme.save()

    return HttpResponse('asd')