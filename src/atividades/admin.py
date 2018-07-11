from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Atividade, Usuario, BaseUserManager
# Register your models here.
admin.site.register(Atividade)
#admin.site.register(Trofeu)

class UserCreationForm(forms.ModelForm):
    """ 
        Um formulario para criar novos usuários. Inclue todos os campos obrigatórios,
        mais uma senha repetida
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nome', 'cpf', 'email', 'sexo', 'professor', 'cpf')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Um formulario para atualizar usuários. Inclue todos os campos do usuário,
    mas substitui a senha pela senha hasheada do admin
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('nome', 'cpf', 'email', 'instituicao', 'sexo', 'professor', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'nome', 'cpf', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nome', 'cpf', 'instituicao', 'sexo', 'professor')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('nome',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(Usuario, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)