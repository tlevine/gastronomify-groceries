Gastronomify
=====

We can order food from Safeway, though their website isn't great.
Here are some notes on that.

## Foods
As a start for gastronomification, we might try fancy fruit juices
because their identification codes are less likely to change over time.
Here are some helpful URLs on that front.

* http://shop.safeway.com/superstore/searchShelf.asp?ShelfId=5_3_15&search=64
* http://shop.safeway.com/superstore/default.asp?page=d&navURL=/dNet/shelves.aspx?ID=5_3&mainURL=/dNet/IconShelves.aspx?ID=5_3
* http://shop.safeway.com/superstore/shelf.asp?shelfId=5_3_15&DeptName=Beverages&AisleName=Juice%20%26%20Nectars&ShelfName=Specialty%20Juice%20%26%20Drinks

Some obvious variables are here.

* Brand
* Fruit
* Size of bottle
* Number of bottles ordered

## Safeway API
Safeway's website isn't the most exciting, but we can work with it.


## Data source
We'll use the daily treasury data compiled by CSV Soundsystem.

## How to run

    export SAFEWAY_EMAIL=foo@datapad.io
    export SAFEWAY_PASSWORD=abcdefg
    ./gastronomify.py
