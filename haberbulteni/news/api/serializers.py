from rest_framework import serializers
from news.models import Makale, Gazeteci

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince


class MakaleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()

    class Meta:
        model = Makale
        fields = '__all__'                                                   # Makale modelindeki butun serializer bolumlerini almaq 
        #fields = ['yazar','baslik','metin']                                 # Makale modelindeki secilmis serializer bolumlerini almaq
        #exclude = ['yazar','baslik']                                        # exclude ise gonderilen bolmelerden basqa butun bolumleri almaq demekdir.
        read_only_fields = ['id','yaratilma_tarihi','guncellenme_tarihi']    # read only fieldsleride vere bilirik .
    
    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.yayinlanma_tarihi
        if object.aktif == True:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Makale aktif deyil'
    
    def validate_yayinlanma_tarihi(self, value):
        today = date.today()
        if value > today:
            raise serializers.ValidationError('Yayimlanma tarihi ireli bir tarih olamaz')
        return value


class GazeteciSerializer(serializers.ModelSerializer):
    #makaleler = MakaleSerializer(many=True, read_only=True)
    
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay'
    )
    
    class Meta:
        model = Gazeteci
        fields = '__all__'




### STANDART SERIALIZER ###
'''
class MakaleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin= serializers.CharField()
    sehir = serializers.CharField()
    yayinlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)


    def create(self , validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)

    def update(self, instance , validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayinlanma_tarihi = validated_data.get('yayinlanma_tarihi', instance.yayinlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError('Baslik kismiyla aciklama kismi ayni olamaz. ')
        return data
    
    def validate_baslik(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(f'Baslik minimum 20 karakter olmali. Girdiyiniz karakter {len(value)}')
        return value

        '''