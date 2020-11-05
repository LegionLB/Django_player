from rest_framework import serializers
from .models import Author, Play_list

#создание плей-листа от имени автора
class Play_listSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    author_id = serializers.IntegerField()



    def create(self, validated_data):

        

        pass#return name.objects.create(**validated_data)

class Play_listSerializerModel(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'name',
            'author_id'
        )