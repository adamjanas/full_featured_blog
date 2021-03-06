from django import forms
from .models import Comment, Post
from django.shortcuts import get_object_or_404
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class CommentForm(forms.ModelForm):
	captcha = ReCaptchaField(widget=ReCaptchaWidget())
	class Meta:
		model = Comment
		fields = ['content']
