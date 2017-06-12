from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from simplemooc.core.mail import send_mail_template
from simplemooc.core.utils import generate_hash_key

from .models import PasswordReset

User = get_user_model()

#sessão 4, aula 50
class PasswordResetForm(forms.Form):

	email = forms.EmailField(label='E-mail')

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			return email
		raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')

	def save():
		user = User.objects.get(email=form.cleaned_data['email'])
		key = generate_hash_key(user.username)
		reset = PasswordReset(key=key, user=user)
		reset.save()
		template_name = 'accounts/password_reset_mail.html'
		subject = 'Criar nova senha no Simple MOOC'
		context = {
			'reset': reset,
		}
		send_mail_template(subject, template_name, context, [user.email])

#sessão 4, aula 36
class RegisterForm(forms.ModelForm):

	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

	# sessão 4 aula 47
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('A confirmação de senha está incorreta')
		return password2

	#	conteúdo removido na sessão 4 aula 47, pois agora iremos trabalhar com um modelo de usuário criados por nós
	#	não o modelo fornecido pelo django
	#sessão 4, aula 37
	# def clean_email(self):
	# 	email = self.cleaned_data['email']
	# 	if User.objects.filter(email=email).exists():
	# 		raise forms.ValidationError('Já existe um usuário com este e-mail')
	# 	return email

	# o param commit é usado para validar o salvamento do form no banco, assim, é possível 
	# fazer algum tipo de alteração no usuário antes de salvar
	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		# user.email = self.cleaned_data['email']		#cleaned_data: contém os valores do Form já validados e transformados em objetos python -- Linha deletada na sessão 4 aula 47, não é mais necessária
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

	class Meta:
		model = User
		fields = ['username', 'email']

#sessão 4 aula 42
class EditAccountForm(forms.ModelForm):

	#	esse conteúdo foi removido na sessão 4 aula 47, pois iremos utilizar um sistema de usuário próprio, ao invés do fornecido
	#	pelo django, sendo assim, esse metódo não faz mais sentido, já que o e-mail é um campo único no nosso banco de dados
	#	enquando no model do django não era
	# def clean_email(self):
	# 	email = self.cleaned_data['email']
	# 	# o método exclude significa 'exceto', neste caso, estamos procurando se existe algum usuário com este email
	# 	# exceto essa instancia que estamos editando
	# 	# sessão 4 aula 42
	# 	queryset = 	User.objects.filter(email=email).exclude(pk=self.instance.pk)
	# 	if queryset.exists():
	# 		raise forms.ValidationError('Já existe um usuário com este e-mail')
	# 	return email

	class Meta:
		model = User
		fields = ['username', 'email', 'name']