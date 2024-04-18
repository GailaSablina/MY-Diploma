from django.apps import AppConfig
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class BackendConfig(AppConfig):
    name = "backend"


class AlbumViewset(viewset.ModelViewset) :
    serializer_class = AlbumSerializer

    @extend_schema(
        request=AlbumCreationSerializer ,
        responses={201 : AlbumSerializer} ,
    )
    def create(self , request) :
        # your non-standard behaviour
        return super().create(request)

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(name='artist' , description='Filter by artist' , required=False , type=str) ,
            OpenApiParameter(
                name='release' ,
                type=OpenApiTypes.DATE ,
                location=OpenApiParameter.QUERY ,
                description='Filter by release date' ,
                examples=[
                    OpenApiExample(
                        'Example 1' ,
                        summary='short optional summary' ,
                        description='longer description' ,
                        value='1993-08-23'
                    ) ,
                    ...
                ] ,
            ) ,
        ] ,
        # override default docstring extraction
        description='More descriptive text' ,
        # provide Authentication class that deviates from the views default
        auth=None ,
        # change the auto-generated operation name
        operation_id=None ,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None ,
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                'Example 1' ,
                description='более подробное описание' ,
                значение










            ответы

    ={204 : Нет} ,
    методы = ["POST"]
    )

    @extend_schema(description='Переопределить определенный метод' , методы=["GET"])
     @ action(detail=True , методы=['post' , 'get'])
    def set_password(self , запрос , pk=Нет) :