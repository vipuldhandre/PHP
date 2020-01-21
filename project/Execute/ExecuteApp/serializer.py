from rest_framework import serializers
from .models import Attribute
class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attribute
        fields=['txn_id','Document_Name','Agreement_Title','Party1_Name','Party2_Name','Term','Assignment_Clause','Governing_Law','Effective_date','Return_of_material']
