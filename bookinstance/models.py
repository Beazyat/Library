from django.contrib.auth.models import User
from django.db import models
from datetime import date
import uuid
# Create your models here.

# Library => class : Book , Author , Genre


class Genre(models.Model):
    name = models.CharField(max_length=200 , help_text="The name of the genre")

    def __str__(self):
        return self.name
    #str baray taeen onvan namayesh dar nazar gerefte mishavad


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000, help_text="Enter The summary of the book")
    isbn = models.CharField(max_length=13, help_text="Enter The ISBN of the book")
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    """
    chon gharar ast yek nevisande ra be chand ketab nesbat dahim az 'one to many' estefade mikonim ke haman primary key ast
    fagat baray in ke agar nam nevisande hazf shod be moshkell nakhorim az 'on_delete' estefade mikonim ke meghdar null jaygozin an koand
    va bad null ra True gharar dade ke meghdar null gereftan mojaz gardad.
    modele ke primary key darad mitavanad pas az class asli tarif shavad vali bayad dakhel qoute gharar girad.
    """
    # genre = models.ManyToManyField(Genre, help_text="Enter The Genre of the book")
    """
    zamani ke mikhahim chand chiz ra be chand chiz mortabet konim va miyan an ha relate bargharar konim az
    'many to many estefade mikonim.
    nokte haez ahamiyat niz an ast ke class asli ke gharar ast az maghadir yek class digar estefade konad bad az an tarif mishavad
    mesle alan ke Genre zod tar az Book tarif shode ast.
    va nabayad dakhel Genre nabayad dakhele qoute tarif shavad.
    """

    def __str__(self):
        return self.title


class Book_Genre(models.Model):
    book = models.ForeignKey(Book,on_delete=models.DO_NOTHING, null=False,
                             blank=False, help_text="Enter your book name ")
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=False,
                              blank=False, help_text="Enter your genre")

    class Meta:
        verbose_name = "Set genre"


class Author(models.Model):
    LIVE = [
        ("yes", "Yes"),
        ("no", "No")
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(
        help_text="Enter The date of birth of the author")
    live = models.CharField(max_length=3, choices=LIVE)
    date_of_death = models.DateField(
        null=True, blank=True,
        help_text="Enter The date of death of the author")

    def save(self, *args, **kwargs):
        if self.live == "yes":
            self.date_of_death = None
        else:
            if not self.date_of_death:
                raise ValueError("Please enter the date of death.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s , %s" % (self.last_name, self.first_name)


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200, help_text="Enter The imprint")
    due_back = models.DateField(help_text="Enter The due back date")

    STATUS = (
            ('a', 'Available'),
            ('b', 'Borrowed'),
            ('r', 'Reserved'),
            )
    status = models.CharField(max_length=1, choices=STATUS,
                              help_text="Book availability")
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s , %s" % (self.book.title, self.status)

    class Meta:
        ordering = ['status']
        """
        bara in ke tartib dade hay in class bar asas 'status' taeen shavad
        """
        permissions = (
            ("normal", "Normal"),
            ("vip", "Vip"),            
        )
        '''
        dar asl to inja permissions hay in model ro terif mikone va badan mitoni 
        toy admin ham beheshon dastresi dashte bashi.
        hala toy template mitoni ba dastor {%if perms.appname.permission_name%}
        azash estefade koni va bazi chiza ro bayad afrad dastresi dashte bashan ta 
        betonan bahash dastresi dashte bashan!
        '''

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    # dar asl inja miyay va ye shart tarif mikonim va badantoy
    # template estefade mikonim migim agar in shart ro dasht neshon bede.
    # albate az in estefade nakardam dakhel template vali mishe estefade kard.