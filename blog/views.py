from django.shortcuts import render
from django.http import HttpResponse

posts = [    {        "name": "Whiskers",        "title": "My mischievous Siamese cat",           "content": "Meet Whiskers, my beloved Siamese cat with a mischievous streak. She loves to play hide-and-seek and will often jump out from unexpected places to surprise me. Siamese cats are known for their intelligence and vocal nature, and Whiskers is no exception. She'll often meow to get my attention or to let me know when she's hungry. If you're looking for a smart and entertaining feline companion, consider getting a Siamese like Whiskers.",        "pet_type": "Cat",        "date": "April 3, 2023"    },    {        "name": "Rocky",        "title": "My energetic Jack Russell Terrier",        "content": "Say hello to Rocky, my energetic Jack Russell Terrier. He's always on the go, whether it's chasing after a ball or sniffing around for new scents. Jack Russells are known for their high energy and intelligence, and Rocky is no exception. He loves to learn new tricks and is always eager to please. If you're looking for a small dog with a big personality, consider getting a Jack Russell like Rocky.",        "pet_type": "Dog",        "date": "April 6, 2023"    },    {        "name": "Gizmo",        "title": "My cuddly guinea pig",        "content": "Meet Gizmo, my cuddly guinea pig who loves to snuggle up in my lap. Guinea pigs are known for their gentle nature and affectionate personalities, and Gizmo is no exception. He loves to munch on fresh veggies and hay, and will often purr with contentment when he's happy. If you're looking for a low-maintenance pet that's easy to care for, consider getting a guinea pig like Gizmo.",        "pet_type": "Small Animal",        "date": "April 9, 2023"    }]



def blog(request):
    context={
    'posts': posts
    }
    return render(request,'blog/blog.html',context)
