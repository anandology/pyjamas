from django.forms import ModelForm
from django import forms 
from wanted.models import *

class FlagForm(ModelForm):
    item = forms.ModelChoiceField(queryset=Item.objects.all())
    type = forms.ModelChoiceField(queryset=FlagType.objects.all())
    value = forms.CharField(max_length=255)

class ItemForm(ModelForm):
    class Meta:
        model = Item
    name = forms.CharField(max_length=50, label="Name")
    short_description = forms.CharField(max_length=100, label="Description")
    description = forms.CharField(max_length=1000, label="Details")
    price = forms.FloatField(label="Price")

    def _is_valid(self):
        res = ModelForm.is_valid(self)
        if self.instance.id is None:
            return res
        for f in FlagType.objects.all():
            fv = self.data[f.name]
            d = {'item': self.instance.id, 'type': f.id, 'value': fv}
            try:
                fg = Flag.objects.get(item=self.instance.id, type=f.id)
            except Flag.DoesNotExist:
                continue
            ff = FlagForm(d, instance=fg)
            if not ff.is_valid():
                res = False
                self.errors[f.name] = ff.errors
        return res

    def delete(self, idx=None):
        if idx is None:
            instance = self.instance
        else:
            instance = Item.objects.get(id=idx)
        for f in FlagType.objects.all():
            try:
                fg = Flag.objects.get(item=instance.id, type=f.id)
            except Flag.DoesNotExist:
                continue
            fg.delete()
        instance.delete()

    def save(self):
        res = ModelForm.save(self)
        for f in FlagType.objects.all():
            fv = self.data[f.name]
            d = {'item': self.instance.id, 'type': f.id, 'value': fv}
            try:
                fg = Flag.objects.get(item=self.instance.id, type=f.id)
            except Flag.DoesNotExist:
                fg = Flag()
            ff = FlagForm(d, instance=fg)
            fv = ff.save()
            setattr(res, f.name, fv)
        return res

    for f in FlagType.objects.all():
        locals()[f.name] = forms.CharField(max_length=100, label=f.description)
    #ItemForm.Meta.fields.append(str(f.name))

def test_item_form():
    for idx in range(1,314):
        try:
            i = Item.objects.get(id=idx)
        except Item.DoesNotExist:
            i = Item()
            i.id = idx
        d = {'id': idx, 'name': 'fred %d' % (idx % 10), 'short_description': 'joe', 'description': 'longer', 'price': 20, 'vehicletype': 'a car', 'numdoors': 5}
        f = ItemForm(d, instance=i)
        if not f.is_valid():
            for (e, k) in f.errors.items():
                print e, k
        it = f.save()

        print it, it.id, it.price, it.vehicletype.id, it.vehicletype.value, it.numdoors.value

        it.price = 25
        if not f.is_valid():
            for (e, k) in f.errors.items():
                print e, k
        it = f.save()

        print it, it.id, it.price, it.vehicletype.id, it.vehicletype.value, it.numdoors.value

def test_add_flagtypes():
    f = FlagType(name="num_doors", description="Number of Doors")
    f.save()
    f = FlagType(name="max_climb_rate", description="Maximum Flying Climb Rate")
    f.save()
    f = FlagType(name="num_ballerinas", description="Maximum Ballerina Storage Capacity")
    f.save()
