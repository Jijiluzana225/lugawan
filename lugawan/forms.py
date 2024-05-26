from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList    
from . import models
from django.forms import ModelForm
from .models import expense


class CreateExpense(forms.ModelForm):

    class Meta:
        model = models.expense      
        fields = "__all__"

        widgets = {
            'branch': forms.TextInput(attrs={'readonly':True}),
            'transdate': forms.TextInput(attrs={'readonly':True})                               
                                        
        }
       



class expenseform(ModelForm):
    class Meta:
        model=expense
        fields = ['branch','transdate']
    
