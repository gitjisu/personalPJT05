from dataclasses import field
from secrets import choice
from tkinter.tix import Select
from .models import Movie
from django import forms



class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    title = forms.CharField(
        max_length=20,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class':'my-title form-control',
                'placeholder':'제목 입력'
            }
        )
    )
    audience = forms.IntegerField(
        label='Audience',
        widget=forms.TextInput(
            attrs={
                'class':'my_audience form-control',
                'placeholder':'관람객 수'
            }
        )
    )
    release_date = forms.DateField(
        label='Release date',
        widget=forms.NumberInput(
            attrs={
                'type':'date',
                'class':'my_release form-control',
                'placeholder':'YYYY-M-D'
            }
        )
    )

    CHOICES = [('공포', '공포'), ('멜로', '멜로'), ('코미디', '코미디'),('범죄', '범죄'),('애니메이션','애니메이션')]
    genre = forms.ChoiceField(
        label= 'Genre',
        widget= forms.Select(
            attrs={
                'class':'movie-genre form-control',
                'placeholder':'장르'
            },
        ),
        choices=CHOICES,
    )


    score = forms.FloatField(
        label='Score',
        widget=forms.TextInput(
            attrs={
                'class':'movie-score form-control',
                'placehloder':'평점을입력하세요.'
            }
        )
    )
    poster_url = forms.CharField(
        label='Poster url',
        widget=forms.Textarea(
            attrs={
                'class':'movie-poster form-control',
                'placeholder':'포스터 링크를 삽입하세요.'
            }
        )
    )
    
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={
                'class':'movie-description form-control',
                'placeholder':'영화정보를입력하세요.'
            }
        )
    )

