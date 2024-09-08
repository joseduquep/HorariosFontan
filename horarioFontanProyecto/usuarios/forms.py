# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

class SignUpForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('tutor', 'Tutor'),
        ('admin', 'Admin'),
    ]
    
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Tipo de usuario',
        }),
        label=''
    )

    foto = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'placeholder': 'Foto del Tutor',
        }),
        label='Foto del Tutor'
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
        }),
        label='',
        help_text=mark_safe('<span class="form-text text-muted"><small>Debe ser un correo que termine en @colegiofontan.edu.co.</small></span>')
    )

    invitation_code = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Código de invitación',
        }),
        label='',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'invitation_code', 'user_type', 'foto')

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

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['last_name'].label = ''

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

        self.fields['invitation_code'].widget.attrs['class'] = 'form-control'
        self.fields['invitation_code'].widget.attrs['placeholder'] = 'Ingrese código de verificación'
        self.fields['invitation_code'].label = ''

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@colegiofontan.edu.co'):
            raise ValidationError('El correo electrónico debe terminar en @colegiofontan.edu.co')
        return email

    def clean_invitation_code(self):
        code = self.cleaned_data.get('invitation_code')
        valid_codes = ['J3n@9Fq$LbZ2']  # Ejemplo de códigos válidos
        if code not in valid_codes:
            raise ValidationError('El código de invitación no es válido.')
        return code
