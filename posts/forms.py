# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from posts.models import Herramienta
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation


class HerramientaForm(ModelForm):
    nombre = forms.CharField(label="Nombre", max_length=100)
    logo = forms.FileField(label="Logo",required=False)
    fichaTecnica = forms.CharField(label="Ficha Técnica", widget=forms.Textarea, max_length=2000)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea, max_length=520)
    urlReferencia = forms.CharField(label="Url herramienta", max_length=500)

    ESTADO = (
        (6, 'Guardar en mis borradores'),
        (1, 'Enviar para revisión')
    )
    estado = forms.ChoiceField(required=True, widget=forms.RadioSelect,
                                                 label="Seleccione una acción",
                                                 choices=ESTADO)
    SISTEMAS_OPERATIVOS = (
        ('No aplica', 'No aplica'),
        ('MAC OS', 'MAC OS'),
        ('Windows', 'Windows'),
        ('IOS', 'IOS'),
        ('Android', 'Android'),
        ('Linux ', 'Linux'),
    )
    sistemaOperativo = forms.MultipleChoiceField(required=True,
                                                 widget=forms.CheckboxSelectMultiple,
                                                 label="Sistema Operativo",
                                                 choices=SISTEMAS_OPERATIVOS)
    PLATAFORMAS = (
        ('Plataforma 1', 'Plataforma 1'),
        ('Plataforma 2', 'Plataforma 2'),
        ('Plataforma 3', 'Plataforma 3'),
        ('Plataforma 4', 'Plataforma 4'),
    )
    plataforma = forms.ChoiceField(label="Plataforma", choices=PLATAFORMAS)
    LICENCIA = (
        ('Licencia 1', 'Licencia 1'),
        ('Licencia 2', 'Licencia 2'),
        ('Licencia 3', 'Licencia 3'),
        ('Licencia 4', 'Licencia 4'),
    )
    licencia = forms.ChoiceField(label="Licencia", choices=LICENCIA)

    class Meta:
        model = Herramienta
        fields = ['nombre', 'logo','urlReferencia', 'sistemaOperativo', 'plataforma',
                  'licencia', 'fichaTecnica', 'descripcion', 'estado']

class HerramientaUpdateForm(ModelForm):
    pk_herramienta = None
    nombre = forms.CharField(label="Nombre", max_length=100)
    logo = forms.FileField(label="Logo",required=False)
    fichaTecnica = forms.CharField(label="Ficha Técnica", widget=forms.Textarea, max_length=2000)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea, max_length=520)
    urlReferencia = forms.CharField(label="Url herramienta", max_length=500)

    SISTEMAS_OPERATIVOS = (
        ('No aplica', 'No aplica'),
        ('MAC OS', 'MAC OS'),
        ('Windows', 'Windows'),
        ('IOS', 'IOS'),
        ('Android', 'Android'),
        ('Linux ', 'Linux'),
    )
    sistemaOperativo = forms.MultipleChoiceField(required=True,
                                                 widget=forms.CheckboxSelectMultiple,
                                                 label="Sistema Operativo",
                                                 choices=SISTEMAS_OPERATIVOS)

    ESTADO = (
        (6, 'Guardar en mis borradores'),
        (1, 'Enviar para revisión')
    )
    estado = forms.ChoiceField(required=True, widget=forms.RadioSelect,
                               label="Seleccione una acción",
                               choices=ESTADO)

    PLATAFORMAS = (
        ('Plataforma 1', 'Plataforma 1'),
        ('Plataforma 2', 'Plataforma 2'),
        ('Plataforma 3', 'Plataforma 3'),
        ('Plataforma 4', 'Plataforma 4'),
    )
    plataforma = forms.ChoiceField(label="Plataforma", choices=PLATAFORMAS)
    LICENCIA = (
        ('Licencia 1', 'Licencia 1'),
        ('Licencia 2', 'Licencia 2'),
        ('Licencia 3', 'Licencia 3'),
        ('Licencia 4', 'Licencia 4'),
    )
    licencia = forms.ChoiceField(label="Licencia", choices=LICENCIA)


    class Meta:
        model = Herramienta
        fields = ['nombre', 'logo','urlReferencia', 'sistemaOperativo', 'plataforma',
                  'licencia', 'fichaTecnica', 'descripcion','estado']


class HerramientaRevisionForm(ModelForm):
    pk_herramienta = None
    nombre = forms.CharField(label="Nombre", max_length=100)
    logo = forms.FileField(label="Logo",required=False)
    fichaTecnica = forms.CharField(label="Ficha Técnica", widget=forms.Textarea, max_length=2000)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea, max_length=520)
    urlReferencia = forms.CharField(label="Url herramienta", max_length=500)

    SISTEMAS_OPERATIVOS = (
        ('No aplica', 'No aplica'),
        ('MAC OS', 'MAC OS'),
        ('Windows', 'Windows'),
        ('IOS', 'IOS'),
        ('Android', 'Android'),
        ('Linux ', 'Linux'),
    )
    sistemaOperativo = forms.MultipleChoiceField(required=True,
                                                 widget=forms.CheckboxSelectMultiple,
                                                 label="Sistema Operativo",
                                                 choices=SISTEMAS_OPERATIVOS)

    PLATAFORMAS = (
        ('Plataforma 1', 'Plataforma 1'),
        ('Plataforma 2', 'Plataforma 2'),
        ('Plataforma 3', 'Plataforma 3'),
        ('Plataforma 4', 'Plataforma 4'),
    )
    plataforma = forms.ChoiceField(label="Plataforma", choices=PLATAFORMAS)
    LICENCIA = (
        ('Licencia 1', 'Licencia 1'),
        ('Licencia 2', 'Licencia 2'),
        ('Licencia 3', 'Licencia 3'),
        ('Licencia 4', 'Licencia 4'),
    )
    licencia = forms.ChoiceField(label="Licencia", choices=LICENCIA)


    class Meta:
        model = Herramienta
        fields = ['nombre', 'logo','urlReferencia', 'sistemaOperativo', 'plataforma',
                  'licencia', 'fichaTecnica', 'descripcion']

class UserForm(ModelForm):
    username = forms.CharField(label="Usuario", max_length=20)
    first_name = forms.CharField(label="Nombres", max_length=20)
    last_name = forms.CharField(label="Apellidos", max_length=20)
    foto = forms.FileField(required=False)
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirmación Contraseña", widget=forms.PasswordInput())
    ADMINISTRADOR = 1
    USER_GTI = 2
    ROLE_CHOICES = (
        (USER_GTI, 'Miembro GTI'),
        (ADMINISTRADOR, 'Administrador'),
    )
    roles = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2', 'roles', 'foto']

    # Verificacion usuario unico
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya ha sido tomado')
        return username

    # verificacion correo unico
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Correo ya ha sido registrado')
        return email

    # verificacion las contraseñas coinciden y seguridad
    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        try:
            password_validation.validate_password(password2)
        except password_validation.ValidationError as errores:
            mensajes = []
            for m in errores.messages:
                if m == 'This password is too short. It must contain at least 8 characters.':
                    mensajes.append('Contraseña muy corta, debe contener más de 7 caracteres')
                if m == 'This password is too common.':
                    mensajes.append('Contraseña muy común')
                if m == 'This password is entirely numeric.':
                    mensajes.append('Contraseña no puede contener solo números')
                if m.startswith("The password is too similar"):
                    mensajes.append('Contraseña muy similar a los datos del usuario')
            raise forms.ValidationError(mensajes)
        return password2


class UserUpdateForm(ModelForm):
    pk_user = None
    username = forms.CharField(label="Usuario", max_length=20)
    first_name = forms.CharField(label="Nombres", max_length=20)
    last_name = forms.CharField(label="Apellidos", max_length=20)
    email = forms.EmailField(label="Correo electrónico")
    foto = forms.FileField(required=False)
    ADMINISTRADOR = 1
    USER_GTI = 2
    ROLE_CHOICES = (
        (USER_GTI, 'Miembro GTI'),
        (ADMINISTRADOR, 'Administrador'),
    )
    roles = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'roles','foto']

    # verificacion correo unico
    def clean_email(self):
        email = self.cleaned_data['email']
        busqueda = User.objects.filter(email=email)
        if busqueda:
            user = len(busqueda)
            if user > 1:
                raise forms.ValidationError('Correo ya ha sido registrado')
            else:
                return email
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError(u'Usuario "%s" ya esta en uso.' % username)
        return username


# Formulario para cambiar la contraseña
class UserChangePassword(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña actual", widget=forms.PasswordInput())
    new_password1 = forms.CharField(label="Contraseña nueva", widget=forms.PasswordInput())
    new_password2 = forms.CharField(label="Confirmar nueva contraseña", widget=forms.PasswordInput())

    # verificacion contaseña actual coincide
    def clean_old_password(self):
        try:
            return super(UserChangePassword, self).clean_old_password()
        except:
            raise forms.ValidationError("Contraseña actual incorrecta")

    # vericifacion contraseña nueva cumple con los parametros de seguridad
    def clean_new_password2(self):
        password1 = self.cleaned_data['new_password1']
        password2 = self.cleaned_data['new_password2']
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Contraseñas no coinciden')
        try:
            password_validation.validate_password(password2, self.user)
        except password_validation.ValidationError as errores:
            mensajes = []
            for m in errores.messages:
                if m == 'This password is too short. It must contain at least 8 characters.':
                    mensajes.append('Contraseña muy corta, debe contener más de 7 caracteres')
                if m == 'This password is too common.':
                    mensajes.append('Contraseña muy común')
                if m == 'This password is entirely numeric.':
                    mensajes.append('Contraseña no puede contener solo números')
                if m.startswith("The password is too similar"):
                    mensajes.append('Contraseña muy similar a los datos del usuario')
            raise forms.ValidationError(mensajes)
        return password2

class UserUpdateGTIForm(ModelForm):
    pk_user = None
    username = forms.CharField(label="Usuario", max_length=20)
    first_name = forms.CharField(label="Nombres", max_length=20)
    last_name = forms.CharField(label="Apellidos", max_length=20)
    email = forms.EmailField(label="Correo electrónico")
    foto = forms.FileField(required=False)
    USER_GTI = 2
    ROLE_CHOICES = (
        (USER_GTI, 'Miembro GTI'),
    )
    roles = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'roles', 'foto']

    # verificacion correo unico
    def clean_email(self):
        email = self.cleaned_data['email']
        busqueda = User.objects.filter(email=email)
        if busqueda:
            user = len(busqueda)
            if user > 1:
                raise forms.ValidationError('Correo ya ha sido registrado')
            else:
                return email
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError(u'Usuario "%s" ya esta en uso.' % username)
        return username
