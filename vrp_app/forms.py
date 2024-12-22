# vrp_app/forms.py

from django import forms

class VRPForm(forms.Form):
    vehicle_capacities = forms.CharField(
        label='Vehicle Capacities (comma-separated integers)',
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 10,12,15'})
    )
    location_points = forms.CharField(
        label='Location Points (e.g., (x1,y1),(x2,y2),...)',
        widget=forms.TextInput(attrs={'placeholder': '(2,3),(4,5),(6,1)'})
    )
