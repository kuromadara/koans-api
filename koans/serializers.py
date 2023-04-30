from rest_framework import serializers
from .models import Koan

class KoanSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    error_messages = serializers.SerializerMethodField()
    class Meta:
        model = Koan
        fields = '__all__'

    def get_status(self, obj):
        return 'success'

    def get_error_messages(self, obj):
        return []

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'error_messages' in ret and not ret['error_messages']:
            ret.pop('error_messages')
            ret.pop('status')

        return ret
