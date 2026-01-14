from django import forms
from .models import Resume

select_gender =(
    ("male","Male"),
    ("female","Female"),
    ("other", "other"),
)

class DateInput(forms.DateInput):
    input_type='date'


select_city=(
    ("new york", "New York"),
    ("los angeles","Los Angeles"),
    ("houston","Houston"),
    ("chicago","Chicago"),
    ("phoenix","Phoenix"),
    ("austin","Austin"),
    ("austin","Austin"),
    ("las vegas","Las vegas"),
    ("columbia","Columbia"),
    ("nigeria","Nigeria"),
)


select_state=(
    ("new york","New York"),
    ("california","California"),
    ("illinois","Illinois"),
    ("texas","texas"),
    ("texas","texas"),
    ("massachuetts","Masachuetts"),
    ("nevada","Nevada"),
    ("south carolin","South Carolina"),
 )

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields ='__all__'
        widgets={
            "gender": forms.RadioSelect(choices=select_gender),
            "date_of_birth": DateInput,
            "city": forms.Select(choices=select_city),
            "state": forms.Select(choices=select_state)
        }