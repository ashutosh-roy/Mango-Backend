from django.db import models
class users(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(null=True,max_length=100)
    uemail = models.CharField(blank=False,max_length=100,unique=True)
    upass = models.CharField(null=True,max_length=100)
    
    
    def __str__(self):
        return str((self.uid))

class users_details(models.Model):
    uid = models.ForeignKey(users,on_delete=models.CASCADE)
    fname = models.CharField(max_length=16)
    upass = models.CharField(max_length=16)
    uemail = models.CharField(max_length=16)
    def __str__(self):
        return self.fname
#activation_key = models.CharField(max_length=16,default="nokey")

