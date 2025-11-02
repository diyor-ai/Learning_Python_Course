# I start
# Bir dictionary library yarating, unda kamida 5 ta kitob bo‘lsin. Har bir kitob quyidagi kalitlarni o‘z ichiga olsin:
# title (string) – kitob nomi.
# pages (int) – sahifa soni.
# genres (list) – janrlar ro‘yxati (masalan, ["fiction", "mystery"]).
# available (boolean) – kitob mavjudligi (True/False).
# Epublish_date (tuple) – nashr sanasi (yil, oy, kun sifatida, masalan, (2020, 5, 15)).

library = {
    "book1": {
        "title": "Harry Potter",
        "pages": 429,
        "genres": ["finction", "mystery"],
        "available": bool(True),
        "publish_date": (2020, 5, 15),
    },
    "book2": {
        "title": "Amir Temur",
        "pages": 929,
        "genres": ["Autobiography", "Historical"],
        "available": bool(True),
        "publish_date": (2000, 2, 5),
    },
    "book3": {
        "title": "Alamut",
        "pages": 529,
        "genres": ["Religious", "mystery"],
        "available": bool(False),
        "publish_date": (2010, 6, 25),
    },
    "book4": {
        "title": "Hunger Games",
        "pages": 300,
        "genres": ["Adventure", "mystery"],
        "available": bool(True),
        "publish_date": (2014, 7, 15),
    }, "book5": {
        "title": "Shumbola",
        "pages": 429,
        "genres": ["ROMAN"],
        "available": bool(False),
        "publish_date": (1988, 3, 15),
    }

}
for x in library.items():
    print(x)

# Foydalanuvchi kiritishi:

# Foydalanuvchidan yangi kitob qo‘shish uchun input() yordamida title, pages, va genres (vergul bilan ajratilgan) ni oling.
# available ni True, publish_date ni (hozirgi yil, oy, kun) sifatida avtomatik belgilang (hozirgi sana: 2025, 10, 29).
# Yangi kitobni library ga qo‘shing.

new_key = str(input("Please write new book's key name: "))
new_title = str(input("Enter book name: "))
new_pages = int(input("Page of book: "))
new_genres = input("Enter genres of book: ").split(", ")

new_book = {
    "title": new_title,
    "pages": new_pages,
    "genres": new_genres,
    "available": bool(True),
    "publish_date": (2025, 11, 31),
}
library[new_key] = new_book

print(f"New book: {new_book}")

# Shartli tekshirish (If...Else):
# Foydalanuvchidan sahifa soni 200 dan katta bo‘lgan kitoblarni ko‘rsatishni so‘rang (yes/no).
# Agar "yes" bo‘lsa, if sharti yordamida 200 dan katta sahifali kitoblarni chop eting.

answer = input("Do you want to see books which pages more than 200 (yes,no)? ").strip().lower()

if answer in ["yes", "yea", "y"]:
    answer = True
else:
    answer = False

if answer:
    print("This books pages more than 200: ")
    for key, inner_dict in library.items():
        pages = inner_dict["pages"]
        books = inner_dict["title"]
        if pages >= 200:
            print(books, pages)

# Tsikl (For Loop):
# Barcha kitob nomlarini va ularning mavjudligini for tsikli yordamida chiqaring.

print("All books and availability: ")
for key, value in library.items():
    name_book = value['title']
    available_book = value["available"]
    print(name_book, available_book)

# Tsikl (While Loop):
# Foydalanuvchidan kitob nomini so‘rang va while tsikli yordamida kitob topilmaguncha qidiruvni davom ettiring.
# Agar kitob topilsa, "Kitob topildi!" deb chiqaring va tsiklni break bilan to‘xtating.

print("Searching for book")
name_book2 = input("Enter book name : ")
keys = list(library.keys())

i = 0
found = None

while i < len(keys):
    key = keys[i]
    value = library[key]
    if value["title"] == name_book2:
        found = value
        break
    i += 1
if found:
    print(f"{name_book2} is found!!!")
else:
    print(f"{name_book2} is not found!!!")

# Set ishlatish:
# Barcha kitoblarning janrlarini (genres) bitta set ga joylashtiring va noyob janrlarni chiqaring.

genre = set()  # bironta dict, list, set dan malumotlarni bitta joyda joylashrimochi bo'lsak bosh set yaratamiz

for inner_dict in library.values():
    for genres in inner_dict["genres"]:
        genre.add(genres)
print(f"Unique genres: {genre}")

# Operatorlar va Casting:
# Jami sahifa sonini hisoblang (barcha kitoblarning pages qiymatini yig‘ing) va natijani float ga aylantirib (casting),
# har bir sahifaning o‘rtacha hajmini (masalan, 0.5 kb deb hisoblang) chiqaring: total_pages / 2.0.


total_pages = sum(book["pages"] for book in library.values())

total_pages_float = float(total_pages)

average_size_per_paper = total_pages_float / 2.0

print(f'Total page of Libarary(float): {total_pages_float}')
print(f"Avarage size of per page: {average_size_per_paper} 'kb'")
