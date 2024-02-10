from django.test import Client, TestCase
from .models import Item, Tag

# Create your tests here.
class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Item 1",
                            description="Item 1 description").save()
        Tag.objects.create(name="Tag 1").save()

    def test_item_can_have_tag(self):
        item = Item.objects.get(name="Item 1")
        self.assertEqual(item.name, "Item 1")

        tag = Tag.objects.get(name="Tag 1")
        self.assertEqual(tag.name, "Tag 1")

        item.tags.add(tag)
        self.assertEqual(item.tags.count(), 1)
        self.assertEqual(item.tags.first().name, "Tag 1")

class ClientViewTest(TestCase):
    def setUp(self):
        Tag.objects.create(name="Tag 1").save()
        Tag.objects.create(name="Tag 2").save()
        Item.objects.create(name="Soda Can",
                            description="Metal soda can").save()
        
        item = Item.objects.get(name="Soda Can")
        tag1 = Tag.objects.get(name="Tag 1")
        tag2 = Tag.objects.get(name="Tag 2")
        item.tags.add(tag1)
        item.tags.add(tag2)

    def test_index_page_loads(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert "Orlando Recycles" in str(response.content)
        # make sure the search form is present
        assert "Search" in str(response.content)
        assert "<form" in str(response.content)

    def test_user_can_search(self):
        response = self.client.get("/items?q=soda")
        assert response.status_code == 200
        assert "Soda Can" in str(response.content)

    def test_search_results_are_paginated(self):
        # create 20 items
        for i in range(20):
            Item.objects.create(name=f"Item {i}",
                                description=f"Item {i} description").save()
        response = self.client.get("/items?q=item")
        assert response.status_code == 200
        assert "Item 0" in str(response.content)
        assert "Item 14" in str(response.content)
        assert "Item 20" not in str(response.content)

    def test_user_can_view_item(self):
        item = Item.objects.get(name="Soda Can")
        response = self.client.get(f"/items/{item.id}")
        assert response.status_code == 200
        assert "Soda Can" in str(response.content)
        assert "Metal soda can" in str(response.content)
        assert "Tag 1" in str(response.content)
        assert "Tag 2" in str(response.content)

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