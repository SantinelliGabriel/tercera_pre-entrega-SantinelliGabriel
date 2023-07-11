from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description=forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))
    

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    apellido = forms.CharField(label="Apellido", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    mail = forms.CharField(label="e-Mail", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    pwd = forms.CharField(label="Contraseña", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))