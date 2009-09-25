from django.forms import ModelForm
from django import forms 
from wanted.models import *

class FlagForm(ModelForm):
    item = forms.ModelChoiceField(queryset=Item.objects.all())
    type = forms.ModelChoiceField(queryset=FlagType.objects.all())
    value = forms.CharField(max_length=255)

class ItemForm(ModelForm):
    name = forms.CharField(max_length=50)
    short_description = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    price = forms.IntegerField()
    def form_is_valid(self):
        print self.instance.id
        res = {}
        for f in FlagType.objects.all():
            fv = self.data[f.name]
            print "field", f.name, fv
            d = {'item': self.instance.id, 'type': f.id, 'value': fv}
            try:
                fg = Flag.objects.get(item=self.instance.id, type=f.id)
            except Flag.DoesNotExist:
                fg = Flag()
            ff = FlagForm(d, instance=fg)
            res[f.name] = ff.is_valid()
        return res

    def form_save(self):
        print self.instance.id
        res = {}
        for f in FlagType.objects.all():
            fv = self.data[f.name]
            print "field", f.name, fv
            d = {'item': self.instance.id, 'type': f.id, 'value': fv}
            try:
                fg = Flag.objects.get(item=self.instance.id, type=f.id)
            except Flag.DoesNotExist:
                fg = Flag()
            ff = FlagForm(d, instance=fg)
            res[f.name] = ff.save()
        return res

    for f in FlagType.objects.all():
        locals()[f.name] = forms.CharField(max_length=100)
    #ItemForm.Meta.fields.append(str(f.name))

def test_item_form():
    i = Item()
    d = {'name': 'fred', 'short_description': 'joe', 'description': 'longer', 'price': 20, 'vehicletype': 'a car', 'numdoors': '5'}
    f = ItemForm(d, instance=i)
    print f.is_valid()
    it = f.save()
    print f.form_is_valid()
    f.form_save()

    print it

    print f.describe()
