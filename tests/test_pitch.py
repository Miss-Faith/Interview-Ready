import unittest
from app.models import *
from app import db


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_James = User(id = 12345, username = 'James', email = 'james@ms.com')
        self.new_pitch = Pitch(id=12345,title="Hey hey hey",post="Lovely day",category="Happy")

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,12345)
        self.assertEquals(self.new_pitch.title,'Hey hey hey')
        self.assertEquals(self.new_pitch.post,'Lovely day')
        self.assertEquals(self.new_pitch.category,'Happy')

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
