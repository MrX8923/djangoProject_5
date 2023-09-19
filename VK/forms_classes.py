from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(
        required=False,
        label='Имя'
    )
    job = forms.CharField(
        required=False,
        label='Род занятий'
    )
    age = forms.IntegerField(
        required=False,
        label='Возраст'
    )
    email = forms.EmailField(
        required=False,
        label='e-mail'
    )
    lang = forms.TypedChoiceField(
        required=False,
        label='Язык',
        choices=(
            ('RU', 'RU'),
            ('EN', 'EN'),
            ('FR', 'FR'),
        )
    )
    mate = forms.NullBooleanField(
        required=False,
        label='Помощники',
    )
    color = forms.TypedChoiceField(
        required=False,
        label='Цвет',
        choices=(
            ('red', 'Красный'),
            ('white', 'Белый'),
            ('gold', 'Золотой')
        )
    )
    age_18 = forms.BooleanField(
        required=False,
        label='18+'
    )
    text = forms.CharField(
        required=False,
        label='Описание',
        widget=forms.Textarea(
            attrs={"cols": "18", "rows": "5"}
        )
    )
    img = forms.ImageField(
        required=False,
        label='Фото'
    )
