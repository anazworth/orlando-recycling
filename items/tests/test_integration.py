import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright.sync_api import sync_playwright
from ..models import Item, Tag


class IntegrationTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        Tag.objects.bulk_create([
            Tag(name="Tag 1", description="Tag 1 description"),
            Tag(name="Tag 2", description="Tag 2 description")
        ])

        item1 = Item.objects.create(id=1, name="Soda Can", description="Metal soda can")
        item2 = Item.objects.create(id=2, name="Plastic Bag", description="Plastic grocery store bag")

        tag1 = Tag.objects.get(name="Tag 1")
        tag2 = Tag.objects.get(name="Tag 2")

        item1.tags.add(tag1, tag2)
        item2.tags.add(tag1)

    def test_index_page(self):
        page = self.browser.new_page()
        page.goto(self.live_server_url)
        assert "Orlando Recycles" in page.title()
        assert "Search" in page.inner_text("form")
        page.close()

    def test_user_can_search(self):
        page = self.browser.new_page()
        page.goto(self.live_server_url)
        page.fill("input[name=q]", "soda")
        page.click("button[type=submit]")
        assert "Soda Can" in page.inner_text("body")
        assert "Plastic Bag" not in page.inner_text("body")
        page.close()
    
    def test_user_can_view_item(self):
        page = self.browser.new_page()
        page.goto(self.live_server_url + "/items/1")
        # wait for 3000ms to make sure the page is loaded
        assert "Soda Can" in page.inner_text("body")
        assert "Metal soda can" in page.inner_text("body")
        assert "Tag 1" in page.inner_text("body")
        assert "Tag 1 description" in page.inner_text("body")
        assert "Tag 2" in page.inner_text("body")
        assert "Tag 2 description" in page.inner_text("body")
        page.close()