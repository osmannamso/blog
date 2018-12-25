import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Theme,Article,Topic,Type

class ThemeNode(DjangoObjectType):
    class Meta:
        model = Theme
        filter_fields = ['name']
        interfaces = (relay.Node, )
    oid = graphene.Field(graphene.Int)

    def resolve_oid(self, info, **kwargs):
        return self.id
class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = ['title']
        interfaces = (relay.Node, )

    oid = graphene.Field(graphene.Int)

    def resolve_oid(self, info, **kwargs):
        return self.id

class TopicNode(DjangoObjectType):
    class Meta:
        model = Topic
        filter_fields = ['name']
        interfaces = (relay.Node,)

    oid = graphene.Field(graphene.Int)

    def resolve_oid(self, info, **kwargs):
        return self.id

class TypeNode(DjangoObjectType):
    class Meta:
        model = Type
        filter_fields = ['name']
        interfaces = (relay.Node,)

    oid = graphene.Field(graphene.Int)

    def resolve_oid(self, info, **kwargs):
        return self.id

class Query(object):
    theme = DjangoFilterConnectionField(ThemeNode, oid=graphene.Int())
    article = DjangoFilterConnectionField(ArticleNode, oid=graphene.Int())
    topic = DjangoFilterConnectionField(TopicNode, oid=graphene.Int())
    all_themes = DjangoFilterConnectionField(ThemeNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)
    all_topics = DjangoFilterConnectionField(TopicNode)
    all_types = DjangoFilterConnectionField(TypeNode)

    def resolve_theme(self, info, oid):
        return Theme.objects.filter(pk=oid)
    def resolve_article(self,info,oid):
        return Article.objects.get(pk=oid)
    def resolve_topic(self,info,oid):
        return Topic.objects.get(pk=oid)
    # def resolve_type(self,info,oid):
    #     return Type.objects.get(pk=oid)