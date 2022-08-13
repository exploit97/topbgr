from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError

from .models import Book, Author, Contact, Booking
from .forms import ContactForm
from .forms import ContactForm, ParagraphErrorList


def index(request):
    books = Book.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'books': books
    }
    return render(request, 'store/index.html', context)

def listing(request):
    books_list = Book.objects.filter(available=True)
    paginator = Paginator(books_list, 9)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    context = {
        'books': books,
        'paginate': True
    }
    return render(request, 'store/listing.html', context)

@transaction.atomic
def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    authors = [author.name for author in book.authors.all()]
    authors_name = " ".join(authors)
    context = {
        'book_title': book.title,
        'authors_name': authors_name,
        'book_id': book.id,
        'thumbnail': book.picture
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            try:
                with transaction.atomic():
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                        # If a contact is not registered, create a new one.
                        contact = Contact.objects.create(
                            email=email,
                            name=name
                        )
                    else:
                        contact = contact.first()

                    book = get_object_or_404(Book, id=book_id)
                    booking = Booking.objects.create(
                        contact=contact,
                        book=book
                    )
                    book.available = False
                    book.save()
                    context = {
                        'book_title': book.title
                    }
                    return render(request, 'store/merci.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = ContactForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        books = Book.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        books = Book.objects.filter(title__icontains=query)
    if not books.exists():
        books = Book.objects.filter(authors__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'books': books,
        'title': title
    }
    return render(request, 'store/search.html', context)
