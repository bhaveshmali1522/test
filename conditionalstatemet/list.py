
#List are ordered collection of items
#[]
#list is like a shopping bag which can store everything
type([])
grocery_list = ["Milk", "Orange", 1, 2, 3, True, 2+4j, 2.3]
type(grocery_list)
grocery_list
#lists are mutable
grocery_list[0]
grocery_list[-1]
grocery_list[1:]
grocery_list[1:4]
movies = ["Action1", "Action2", "Action3","comedy1"]
movies[0:3]
pages = ["Title page", "chap1", "chap2", "conclusion", "index"]
pages[-1]
pages[-2]
queue = ["Ajay", "Bijay", "Sanjay", "Anjay"]
queue[-1]
queue[-2]
lis1 = ["Apple", "Banana"]
lis1
#append >> add element to the end of list

lis1.append("orange")
lis1
playlist = []
playlist.append("Sare jhan se acha")
playlist.append("Ae mere watan ke logo")
playlist
bookshelf = []
bookshelf.append("book1")
bookshelf.append("book2")
bookshelf
lis1
lis1[1] = "brinjal"
lis1 #list are mutable
lis1
lis1.insert(1, "banana")
lis1
bus_seat = ["Ajay", "Bob", "Sanjay"]
bus_seat.insert(1, "Ram")
bus_seat
#extend>> used to append elements from another iterable
my_list = ["Apple", "Banana", "orange"]
brothers_list = ["brinjal", "potato"]

my_list.extend(brothers_list)
my_list
my_list = ["Apple", "Banana", "orange"]
brothers_list = ["brinjal", "potato"]
my_list
brothers_list
#concatenate

my_list + brothers_list
#repeatation operation

"*" * 5
"-" * 50
[0] * 10
[1, 2, 3] * 10
list(range(1, 6)) * 3
msg = "your appointment is tomorrow \n"
print(msg * 3)
#membership in , not in


grocery_list
"Milk" in grocery_list
"Banana" in grocery_list
"Banana" not in grocery_list
grocery_list
#shallow copy>> value will change with change in other list|
a = grocery_list
a
grocery_list[0]  = "Banana"
grocery_list
a
#deep copy will not change with change in other list
b = grocery_list.copy()
grocery_list
b
grocery_list[0] = "Guava"
grocery_list
b
#sorting lists

book_list = ["Data Structure", "Algorithm", "Web dev"]
sorted(book_list)
book_list
book_list.index("Algorithm")
book_list.index("Web dev")
book_list = ['Data Structure',"Data Structure", 'Algorithm', 'Web dev']
book_list
book_list.count('Data Structure')
book_list.remove('Data Structure')
book_list
book_list.sort()
book_list
del book_list
book_list = ['Algorithm', 'Data Structure', 'Web dev']
book_list
book_list.clear()
book_list
book_list = ['Algorithm', 'Data Structure', 'Web dev']
book_list.pop()
book_list
book_list = ['Algorithm', 'Data Structure', 'Web dev']
book_list.pop(1)
book_list
#list comprehension
prices = [10, 20, 30, 40, 50]
doubled_price = []
for i in prices:
    doubled_price.append(i*2)
doubled_price
doubled_price = [price * 2 for price in prices]
doubled_price
names = ["Ajay", "bijay", "sanjay"]

[name.capitalize() for name in names]
numbers = [1, 2, 3, 4, 5]
[num ** 2 for num in numbers]
str1 = "doc1.ppt"

str1.split(".")[-1]
file_name = ["doc1.ppt", "doc2.pdf", "doc3.jpg", "doc4.py"]

[file.split(".")[-1] for file in file_name]
#conditional list comprehension


email_address = ["aj@gmail.com", "sj@yahoo.com", "rj@yahoo.com", "mj@gmail.com"]

[email for email in email_address if email.endswith("@yahoo.com")]
#Nested list comprehension


pairs = []

for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        pairs.append([x, y])
pairs
[[x, y] for x in [1, 2, 3] for y in [4, 5, 6]]
#list as stack and queue


#stack >> last in first out principle > the last element added to the stack will be the first one to be removed


stack_of_plates = []
stack_of_plates.append("plate1")
stack_of_plates.append("plate2")
stack_of_plates.append("plate3")
stack_of_plates.append("plate4")
stack_of_plates
stack_of_plates.pop()
stack_of_plates
browsing_history = []
browsing_history.append("home_page")
browsing_history.append("about us")
browsing_history.append("contact")
browsing_history
browsing_history.pop()
browsing_history
#Queue >> FIFO>> FIRST IN FIRST OUT
#ORDERLY SEQUENTIAL MANNER
# TWO ENDS


from collections import deque


checkout = deque()

checkout.append("cus1")
checkout.append("cus2")
checkout.append("cus3")
checkout.append("cus4")
checkout
while checkout:
    customer = checkout.popleft()
    print("serving", customer)
from queue import Queue
print_queue = Queue()

from queue import Queue

print_queue = Queue()

print_queue.put("Print job 1")
print_queue.put("Print job 2")
print_queue.put("Print job 3")


while not print_queue.empty():
    print_job = print_queue.get()
    print("Printing:", print_job)