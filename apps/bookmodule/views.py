from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, Count, Sum, Avg, Max, Min
import random

from django.shortcuts import redirect

from apps.bookmodule import forms

from .models import *


def index(request): 
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1):
    if not val1.isdigit():
        return HttpResponse("Error: expected val1 to be an integer", status=400)

    return HttpResponse(f"value1 = {val1}")

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley', 'price' : 80}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam', 'price' : 50}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov', 'price' :100}
    return [book1, book2, book3]

def add_book():
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save()

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def task1(request):
    mybooks=Book.objects.filter(Q(price__lte=80))
    print(f"Found {mybooks.count()} books")
    return render(request, 'bookmodule/lab8/task1.html', {'books': mybooks})

def task2(request):
    mybooks=Book.objects.filter(Q(edition__gte=3) & (Q(title__icontains='co') | Q(author__icontains='co')))
    print(f"Found {mybooks.count()} books")
    return render(request, 'bookmodule/lab8/task2.html', {'books': mybooks})

def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8/task4.html', {'books': books})

def task5(request):
    query = Book.objects.aggregate(
        total=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/lab8/task5.html', {'query': query})

def task7(request):
    students_by_city = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8/task7.html', {'students_by_city': students_by_city})

def generate_random_student():
    names = ["John", "Alice", "Bob", "Eve", "Charlie", "Diana", "Liam", "Sophia"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
    
    name = random.choice(names)
    age = random.randint(18, 30)
    city = random.choice(cities)
    
    # Create Address object
    address = Address(city=city)
    address.save()  # Save the address first, as we need it for the ForeignKey

    # Create Student object
    student = Student(name=name, age=age, address=address)
    student.save()
    
    return student, address

generate_random_student()


def task9_1(request):
    departments = Department.objects.annotate(student_count=Count('students'))
    return render(request, 'bookmodule/lab9/task1.html', {'departments': departments})

def task9_2(request):
    courses = Course.objects.annotate(student_count=Count('students'))
    return render(request, 'bookmodule/lab9/task2.html', {'courses': courses})

def task9_3(request):
    departments = Department.objects.annotate(oldest_student_id=Min('students__id'))
    for dept in departments:
        oldest = Student2.objects.filter(
            department=dept,
            id=dept.oldest_student_id
        ).first()
        dept.oldest_student_name = oldest.name if oldest else "None"
    return render(request, 'bookmodule/lab9/task3.html', {'departments': departments})

def task9_4(request):
    departments = Department.objects.annotate(
        student_count=Count('students')
    ).filter(
        student_count__gt=2
    ).order_by(
        '-student_count'
    )
    return render(request, 'bookmodule/lab9/task4.html', {'departments': departments})

def task9_1_1(request):
    mybooks=Book.objects.all()
    books = mybooks[995:]
    return render(request, 'bookmodule/lab10/lab9_BookList.html', {'books' : books})

def task9_1_2(request):
    if request.method=='POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        author = request.POST.get('author')
        
        book = Book(title=title, price=float(price), edition=edition, author=author)
        book.save()
        return redirect('books.BookList')
    return render(request, 'bookmodule/lab10/lab9_add_book.html')

def task9_1_3(request, bookId):
    book=Book.objects.get(id=bookId)
    if request.method=='POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        author = request.POST.get('author')
        
        book.title = title
        book.price = float (price)
        book.edition = edition
        book.author = author
        book.save()
        return redirect('books.BookList')
    
    return render(request, 'bookmodule/lab10/lab9_edit_book.html', {'book' : book})

def task9_1_4(request, bookId):
    book=Book.objects.get(id=bookId)
    if request.method=='POST':
        book.delete()
        return redirect('books.BookList')

    return render(request, 'bookmodule/lab10/lab9_delete_book.html', {'book':book})



def task9_2_1(request):
    mybooks=Book.objects.all()
    books = mybooks[995:]
    return render(request, 'bookmodule/lab10_part2/lab9_BookList.html', {'books' : books})

def task9_2_2(request):
    obj = None
    if request.method=='POST':
        form = forms.BookForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('books.BookList2')
    else: form = forms.BookForm(None)
    return render(request, 'bookmodule/lab10_part2/lab9_add_book.html', {'form':form})

def task9_2_3(request, bookId):
    book = Book.objects.get(id=bookId)  

    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.BookList2')
    else:
        form = forms.BookForm(instance=book)

    return render(request, 'bookmodule/lab10_part2/lab9_edit_book.html', {'form': form})

def task9_2_4(request, bookId):
    book=Book.objects.get(id=bookId)
    if request.method=='POST':
        book.delete()
        return redirect('books.BookList2')

    return render(request, 'bookmodule/lab10_part2/lab9_delete_book.html', {'book':book})

