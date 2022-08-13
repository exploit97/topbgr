from django.test import TestCase
from django.urls import reverse

from .models import Book, Author, Contact, Booking


class IndexPageTestCase(TestCase):

    # test that index returns a 200
    # must start with `test`
    def test_index_page(self):
        # you must add a name to index view: `name="index"`
        response = self.client.get(reverse('store:index'))
        self.assertEqual(response.status_code, 200)

class DetailPageTestCase(TestCase):

    # ran before each test.
    def setUp(self):
        impossible = Book.objects.create(title="Transmission Impossible")
        self.book = Book.objects.get(title='Transmission Impossible')

    # test that detail page returns a 200 if the item exists
    def test_detail_page_returns_200(self):
        book_id = self.book.id
        response = self.client.get(reverse('store:detail', args=(book_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the items does not exist
    def test_detail_page_returns_404(self):
        book_id = self.book.id + 1
        response = self.client.get(reverse('store:detail', args=(book_id,)))
        self.assertEqual(response.status_code, 404)

class BookingPageTestCase(TestCase):

    def setUp(self):
        Contact.objects.create(name="Freddie", email="fred@queens.forever")
        impossible = Book.objects.create(title="Transmission Impossible")
        journey = Author.objects.create(name="Journey")
        impossible.authors.add(journey)
        self.book = book.objects.get(title='Transmission Impossible')
        self.contact = Contact.objects.get(name='Freddie')

    # test that a new booking is made
    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count()
        book_id = self.book.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(book_id,)), {
            'name': name,
            'email': email
        })
        new_bookings = Booking.objects.count()
        self.assertEqual(new_bookings, old_bookings + 1)

    # test that a booking belongs to a contact
    def test_new_booking_belongs_to_a_contact(self):
        book_id = self.book.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(book_id,)), {
            'name': name,
            'email': email
        })
        booking = Booking.objects.first()
        self.assertEqual(self.contact, booking.contact)

    # test that a booking belong to an book
    def test_new_booking_belongs_to_an_book(self):
        book_id = self.book.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(book_id,)), {
            'name': name,
            'email': email
        })
        booking = Booking.objects.first()
        self.assertEqual(self.book, booking.book)

    # test that a book is not available after a booking is made
    def test_book_not_available_if_booked(self):
        book_id = self.book.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('store:detail', args=(book_id,)), {
            'name': name,
            'email': email
        })
        # Make the query again, otherwise `available` will still be set at `True`
        self.book.refresh_from_db()
        self.assertFalse(self.book.available)
