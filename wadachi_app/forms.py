from django import forms

from .models import Bridge, Brick


class BridgeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BridgeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    class Meta:
        model = Bridge
        fields = ('topic', 'context', 'goal',)


class BrickForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BrickForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Brick
        fields = ('title', 'author', 'url', 'memo',)



