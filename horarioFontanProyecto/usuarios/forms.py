from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
        }),
        label='',
        help_text=mark_safe('<span class="form-text text-muted"><small>Debe ser un correo que termine en @colegiofontan.edu.co.</small></span>')
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = mark_safe(
            '<span style="color:blue;" class="form-text text-muted"><small>Debe ser 20 caracteres o menos. Solo letras, números y @/./+/-/_</small></span>'
        )

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['email'].label = ''
        self.fields['email'].help_text = mark_safe('<span class="form-text text-muted"><small>Debe ser un correo que termine en @colegiofontan.edu.co.</small></span>')

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = mark_safe(
            '<ul class="form-text text-muted small">'
            '<li>Tu contraseña no puede ser muy parecida a tu nombre de usuario.</li>'
            '<li>Tu contraseña debe tener al menos 8 caracteres.</li>'
            '<li>Tu contraseña no puede ser una contraseña comúnmente usada.</li>'
            '<li>Tu contraseña no puede consistir únicamente en números.</li>'
            '</ul>'
        )

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirma contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = mark_safe('<span class="form-text text-muted"><small>Ingresa la misma contraseña de antes, para confirmar.</small></span>')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@colegiofontan.edu.co'):
            raise ValidationError('El correo electrónico debe terminar en @colegiofontan.edu.co')
        return email
