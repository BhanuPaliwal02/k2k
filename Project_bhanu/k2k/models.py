from django.db import models

# Create your models here.
class r_lookupdata(models.Model):
    PrimaryFunction = models.CharField(max_length=112)
    SecondaryFunction = models.CharField(max_length=50)
    PrimaryFunction_ImageName = models.CharField(max_length=50)
    SecondaryFunction_ImageName = models.CharField(max_length=50)
    canDemandSecondaryFunction = models.CharField(max_length=50)
    isAvailableSecondaryFunction = models.CharField(max_length=50)
    areFunctionInUse = models.CharField(max_length=50)
    PrimaryFunction_hindi = models.CharField(max_length=50)
    SecondaryFunction_hindi = models.CharField(max_length=50)
    # date = models.DateField( default='2023-02-20')
    
    def __str__(self):
        return self.PrimaryFunction
    
class r_k2support(models.Model):
    id = models.IntegerField(primary_key=True)
    vedioLink = models.URLField(max_length=225)
    vedioType = models.CharField(max_length=112)
    vediok2Page = models.CharField(max_length=112)
    vedioLinkHindi = models.URLField(max_length=225)
    vedioLinkLocal = models.URLField(max_length=225)
    state = models.CharField(max_length=112)
    district = models.CharField(max_length=112)
    activeInK2App = models.CharField(max_length=112)
    last_updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.district
    
class r_district_data(models.Model):
    id = models.IntegerField(primary_key=True)
    village = models.CharField(max_length=50)
    village_hindi = models.CharField(max_length=50)
    gram_panchayat = models.CharField(max_length=50)
    tehsil = models.CharField(max_length=50)
    tehsil_hindi = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    district_hindi = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    state_hindi = models.CharField(max_length=50)
    last_updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.district

class r_farmingassets(models.Model):
    id = models.IntegerField(primary_key=True)
    seqNo = models.IntegerField()
    assetType = models.CharField(max_length=50)
    assetsubType= models.CharField(max_length=50)
    assetNameEnglish= models.CharField(max_length=50)
    assetNamehindi= models.CharField(max_length=50)
    assetCapacityUnit= models.CharField(max_length=50)
    district= models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    inUse= models.CharField(max_length=50)
    activeInK2App= models.CharField(max_length=50)
    last_updated_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.district
    
class d_user_data (models.Model):
    id= models.IntegerField(primary_key=True)
    first_name = models.CharField( max_length=50)
    last_name= models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    village = models.CharField(max_length=50)
    pincode= models.IntegerField()
    PrimaryFunction= models.CharField(max_length=50)
    SecondaryFunction= models.CharField(max_length=50)
    tehsil= models.CharField(max_length=50)
    district= models.CharField(max_length=50)
    last_updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.district
    
class r_state_district(models.Model):
    id= models.CharField(primary_key=True, max_length=50)
    state= models.CharField(max_length=50)
    state_hindi= models.CharField(max_length=50)
    district= models.CharField(max_length=50)
    district_hindi= models.CharField(max_length=50)
    activeInK2App= models.CharField(max_length=50)
    population2021= models.CharField(max_length=50)
    areaInKmSquare= models.CharField(max_length=50)
    densityPerKm= models.CharField(max_length=50)
    last_updated_at= models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.district