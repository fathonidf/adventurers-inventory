from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_response_has_utf8_charset(self): # Mengecek apakah respons HTTP URL main memiliki standar peraturan UTF-8 atau tidak
        response = Client().get('/main/')
        content_type = response.get('Content-Type', '')
        self.assertIn('utf-8', content_type.lower())
    
    # def setUp(self):
    #     """Menginisiasi dua object pada models"""
    #     Item.objects.create(name = "Wand of Sparking", 
    #                         amount = 1, 
    #                         description = "a basic magic weapon",
    #                         price = 5, 
    #                         item_level = 1, 
    #                         use = "attack the enemy for 3 Damage points")
    #     Item.objects.create(name = "Healing Potion", 
    #                         amount = 5, 
    #                         description = "a basic healing potion",
    #                         price = 10, 
    #                         item_level = 1, 
    #                         use = "increase your health for 25 Health points")
    
    # def test_item_attribute(self):
    #     """Mengecek tiap object yang terinisiasi memiliki atribut yang sesuai ketika diakses"""
    #     item_1 = Item.objects.get(name = "Wand of Sparking")
    #     item_2 = Item.objects.get(name = "Healing Potion")

    #     self.assertEqual(item_1.price, 5)
    #     self.assertEqual(item_2.price, 10)
    #     self.assertEqual(item_1.use, "attack the enemy for 3 Damage points")
    #     self.assertEqual(item_2.use, "increase your health for 25 Health points")