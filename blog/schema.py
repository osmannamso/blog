import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import InputObjectType
from .models import Theme,Article,Topic

class ThemeNode(DjangoObjectType):
    class Meta:
        model = Theme
        filter_fields = ['name']
        interfaces = (relay.Node, )
    oid = graphene.Field(graphene.Int)

    def resolve_oid(self, info, **kwargs):
        return self.id
    def resolve_helpful(self, info, **kwargs):
        return self.helpful


class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = {
            'title': ['exact', 'icontains'],
            'helpful': ['exact']
        }
        interfaces = (relay.Node, )

    oid = graphene.Field(graphene.Int)

    def resolve_oid(self, info, **kwargs):
        return self.id


class AddSeen(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    ok = graphene.Boolean()

    def mutate(self, info, id):
        Article.AddSeen(Article, id)
        return AddSeen(ok=True)


class TopicNode(DjangoObjectType):
    class Meta:
        model = Topic
        filter_fields = ['name']
        interfaces = (relay.Node,)

    oid = graphene.Field(graphene.Int)

    def resolve_oid(self, info, **kwargs):
        return self.id

class Mutation(graphene.ObjectType):
    add_seen = AddSeen.Field()

class Query(graphene.ObjectType):
    theme = DjangoFilterConnectionField(ThemeNode, oid=graphene.Int())
    article = DjangoFilterConnectionField(ArticleNode, oid=graphene.Int())
    topic = DjangoFilterConnectionField(TopicNode, oid=graphene.Int())
    all_themes = DjangoFilterConnectionField(ThemeNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)
    all_helpful_articles = DjangoFilterConnectionField(ArticleNode)
    all_topics = DjangoFilterConnectionField(TopicNode)

    def resolve_theme(self, info, oid):
        return Theme.objects.filter(pk=oid)
    def resolve_article(self,info,oid):
        return Article.objects.filter(pk=oid)
    def resolve_topic(self,info,oid):
        return Topic.objects.filter(pk=oid)
    def resolve_all_articles(self, info, **kwargs):
        return Article.objects.all().order_by('created_at', 'seen')
    def resolve_all_helpful_articles(self, info, **kwargs):
        return Article.objects.filter(helpful=True).order_by('created_at', 'seen')