from django.test import TestCase
from ..models import Item, Tag

class ApiViewTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name="Tag 1").save()
        Tag.objects.create(name="Tag 2").save()
        Item.objects.create(name="Soda Can",
                            description="Metal soda can").save()
        Item.objects.create(name="Soda Bottle",
                            description="Plastic soda bottle").save()
        
        item = Item.objects.get(name="Soda Can")
        tag1 = Tag.objects.get(name="Tag 1")
        tag2 = Tag.objects.get(name="Tag 2")
        item.tags.add(tag1)
        item.tags.add(tag2)

    def test_api_can_return_search_results(self):
        response = self.client.get("/api/v1/items?q=soda", HTTP_ACCEPT="application/json")
        assert response.status_code == 200
        assert "Soda Can" in str(response.content)
        assert "Soda Bottle" in str(response.content)

    def test_api_can_return_item(self):
        item = Item.objects.get(name="Soda Can")
        response = self.client.get(f"/api/v1/items/{item.id}", HTTP_ACCEPT="application/json")
        assert response.status_code == 200
        assert "Soda Can" in str(response.content)
        assert "Metal soda can" in str(response.content)
        assert "Tag 1" in str(response.content)
        assert "Tag 2" in str(response.content)