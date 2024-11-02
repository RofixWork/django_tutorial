from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    # comment = forms.CharField(
    #     label="Write Comment",
    #     widget=forms.Textarea(attrs={"class": "form-control", "cols": 5, "rows": 5}),
    # )

    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(
                attrs={"class": "form-control", "cols": 5, "rows": 5}
            )
        }
        labels = {"comment": "Write Comment"}
