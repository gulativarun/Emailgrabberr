from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.EmailField()
	friend = models.ForeignKey("self",related_name = 'referral',\
											null=True,blank=True)
	ip_address = models.CharField(max_length=120,default='ABC')
	ref_id = models.CharField(max_length=120, default='XYZ',blank=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return ("%s" %(self.email))

	class Meta:
		unique_together = ("email","ref_id",)


'''class JoinFriends(models.Model):
	email=models.OneToOneField(Join,related_name="sharer")
	friends = models.ManyToManyField(Join,related_name="friends",\
					null=True,blank=True)
	emailall = models.ForeignKey(Join,related_name = 'emailall')

	def __unicode__(self):
		print "friends are", self.friends.all()
		print self.emailall
		print self.email
		return self.friends.all()[0].email
'''