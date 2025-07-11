To retrieve the date I run the python command bellow on the shell:

>>>Book.objects.all() 
<QuerySet [<Book: Book object (1)>]> #it will retrieve the created instance. To show specifically the title we can modify on the model.py; just adding def __str__(self) to return the title.
