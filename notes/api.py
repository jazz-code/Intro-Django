from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSeralizer(serializers.HyperlinkedModelSerializer):

    # Inner class nested inside PersonalNoteSerializer  to tell it what parts of the model we want to access:
    class Meta:
        model = PersonalNote
        fields = ('title, content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSeralizer
    queryset = PersonalNote.objects.all()