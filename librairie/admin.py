from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from .models import Booking, Contact, Book, Author


class AdminURLMixin(object):
    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:store_%s_change" % (
            content_type.model),
            args=(obj.id,))


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin, AdminURLMixin):
    list_filter = ['created_at', 'contacted']
    fields = ["created_at", "contact_link", 'book_link', 'contacted']
    readonly_fields = ["created_at", "contact_link", "book_link", "contacted"]

    def has_add_permission(self, request):
        return False

    def contact_link(self, booking):
        url = self.get_admin_url(booking.contact)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.contact.name))

    def book_link(self, booking):
        url = self.get_admin_url(booking.book)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.book.title))

class BookingInline(admin.TabularInline, AdminURLMixin):
    model = Booking
    extra = 0
    readonly_fields = ["created_at", "book_link", "contacted"]
    fields = ["created_at", "book_link", "contacted"]
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"

    def has_add_permission(self, request):
        return False

    def book_link(self, booking):
        url = self.get_admin_url(booking.book)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.book.title))

    book_link.short_description = "Book"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,]

class BookAuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookAuthorInline,]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']
