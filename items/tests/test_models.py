from django.test import TestCase
from ..models import Item, Tag

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