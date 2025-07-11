To Update I run on shell the following command one by one:
>>>book=Book.objects.get(title="1984")
>>>book.title = "Nineteen Eighty-Four" #here the updated title
>>>book.save() #finally saving the updated title