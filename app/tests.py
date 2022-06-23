from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    """Test for the profile model class"""
    def setUp(self):
        self.user = User(username='')
        self.user.save()

        self.profile = Profile(id=4, image='profile.jpg', bio='this is a test profile',contacts='0700000000',user=self.user, )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

class NeighbourhoodTestCase(TestCase):
  '''
  test class for  the neighbour model
  '''
  def setUp(self):

    self.user = User(username = 'Suni')
    self.user.save()
    self.neighbourhood = NeighbourHood(id=1, name ='buruburu',location='eastlands', occupants_count='500000', image='hood.jpg', created_on='2022-01-10', admin=self.user )

  def test_instance(self):
    self.assertTrue(isinstance(self.neighbourhood,NeighbourHood))

  def test_create_neighbourhood(self):
    self.neighbourhood.save_neighbourhood()
    neighborhoods = NeighbourHood.objects.all()
    self.assertTrue(len(neighborhoods) > 0)


class BusinessTestCase(TestCase):
  '''
  test classs that test the business model and its functions
  '''
  def setUp(self):
    '''
    the functions that runs at the begin of the test
    '''
    self.new_user = User(username = 'suni')
    self.new_user.save()
    self.business = Business(name='spin', address='1234', create_date='2022-01-01', image='hood.jpg', details='carwash', owner='suni', hood='mirema', )



class AmenitiesTestCase(TestCase):
  '''
  test classs that test the amenities model and its functions
  '''
  def setUp(self):
    '''
    the functions that runs at the begin of the test
    '''
    self.new_user = User(username = 'suni')
    self.new_user.save()
    self.amenities = Amenities(name='kibandasky', location='juja', contact='0700000000', image='hood.jpg', created_on='2022-01-01', author='suni', hood='mirema', )
  

class AnnouncementsTestCase(TestCase):
  '''
  test classs that test the announcements model and its functions
  '''
  def setUp(self):
    '''
    the functions that runs at the begin of the test
    '''
    self.new_user = User(username = 'suni')
    self.new_user.save()
    self.announcements = Announcements(title='watershortage', created_on='22-01-01', details='expect watershortage', author='suni', hood='mirema', )
   