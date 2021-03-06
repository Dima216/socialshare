from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.EmailField(unique=True)
	friend = models.ForeignKey('self', related_name='Friend', \
									   null=True, blank=True)
	ref_id = models.CharField(max_length=100, default='abcdefg')
	ip_address = models.CharField(max_length=100, default='0.0.0.0')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return '%s'% (self.email)

	class Meta:
		unique_together = ('email','ref_id',)

"""
class JoinFriend(models.Model):
	friend_email = models.OneToOneField(Join,related_name='Sharer')
	friends = models.ManyToManyField(Join,related_name='Friend',
									null=True, blank=True)
	all_emails = models.ForeignKey(Join, related_name='all_emails')

	def __unicode__(self):
		return self.friend_email.email
"""