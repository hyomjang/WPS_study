from django import forms
from .models import MyUser
from django.contrib.auth import password_validation

class SignupModelForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = MyUser
        fields = (
            'email',
            # 'password',
            'password1',
            'password2',
            'last_name',
            'first_name',
            'nickname',
        )

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
       # password 검증, is_valid(minimallength, numericPassword, password가 너무많이들어가는지 적게가는지를 확인 검증)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(
            self.cleaned_data['password1'],
            self.instance
        )
        return password1

    def save(self, commit=True): # 이건 Modelform에 있느 save
        user = super(SignupModelForm, self).save(commit=False) # super는 해당하는 함수의 부모객체를 의미
        # 해시되지않은 데이터를 db에 넣길 원하지 X -> 그러그로 commit=false를 넣는다            user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    # password 검증


class SignupForm (forms.Form):

    email = forms.EmailField(
        max_length=100,
        error_messages={
            'invalid':'이메일 형식이 아닙니다'
        },
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ))
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        max_length =30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    nickname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
