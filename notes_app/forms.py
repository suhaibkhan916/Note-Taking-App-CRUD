from .models import Notes
from django.forms import ModelForm


class NoteForm(ModelForm):
    class Meta:
        model = Notes
        # fields = ('note_title', 'content_field')
        fields = '__all__'
