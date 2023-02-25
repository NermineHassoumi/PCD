from rest_framework import serializers
from Credit.models import Demande

class DemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Demande
        fields=('DemandeId',
                'ClientId',
                'Montant',
                'Status',
                'But'
                )