from django.forms import ModelForm
from django import forms

from .models import Player, Article

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
    three_point_field_goal_percentage = forms.FloatField(min_value=0.0, max_value=100.0)
    free_throw_percentage = forms.FloatField(min_value=0.0, max_value=100.0)
    

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    date = forms.DateTimeField(input_formats=['%d-%m-%Y %H:%M:%S'])
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = '01-01-2000 00:00:00'

class StatFilter(forms.Form):
    STAT_CHOICE = [('', 'Any'),('points_per_game', 'Point/game'),('rebounds_per_game', 'Rebounds/game'),('assists_per_game', 'Assists/game'),
    ('steals_per_game', 'Steals/game'),(' blocks_per_game', 'Blocks/game'),('fieldgoals_per_game', 'FG/game'),('three_point_field_goal_percentage', '3P%'),('free_throw_percentage', 'FT%')
    ]
    stat = forms.ChoiceField(choices=STAT_CHOICE, required=False)