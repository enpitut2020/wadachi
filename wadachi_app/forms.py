from django import forms

from .models import Bridge, Brick


class BridgeForm(forms.ModelForm):

    class Meta:
        model = Bridge
        fields = ('topic',)

# TODO: BrickFormの作成formを作る
class BrickForm(forms.ModelForm):
    
    class Meta:
        model = Brick
        fields = ('title', 'author', 'url', 'bridge',)
