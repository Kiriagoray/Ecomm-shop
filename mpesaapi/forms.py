from django import forms

class MpesaForm(forms.Form):
    phone_number = forms.CharField(
        max_length=12,
        label='Phone Number',
        help_text="Format : 2547XXXXXXXX"
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Amount',
        help_text="Enter the amount to pay"
    )
