books = []

def show_books():
    if not books:
        print("\nKutubxonada kitoblar mavjud emas.")
        return

    print("\n--- Kutubxonadagi kitoblar ---")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")

def add_book():
    title = input("\nKitob nomini kiriting: ").strip()

    if not title:
        print("Kitob nomi bo'sh bo'lishi mumkin emas.")
        return

    books.append(title)
    print(f'"{title}" kutubxonaga qo'shildi.')

def delete_book():
    if not books:
        print("\nO'chirish uchun kitob mavjud emas.")
        return

    show_books()

    try:
        number = int(input("\nO'chirmoqchi bo'lgan kitob raqamini kiriting: "))

        if 1 <= number <= len(books):
            removed = books.pop(number - 1)
            print(f'"{removed}" kutubxonadan o'chirildi.')
        else:
            print("Noto'g'ri kitob raqami.")
    except ValueError:
        print("Iltimos, raqam kiriting.")

def main():
    while True:
        print("\n===== KUTUBXONA DASTURI =====")
        print("1. Kitob qo'shish")
        print("2. Kitoblarni ko'rish")
        print("3. Kitob o'chirish")
        print("4. Dasturdan chiqish")

        choice = input("\nTanlang (1-4): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Dastur yakunlandi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov. 1 dan 4 gacha bo'lgan raqamni tanlang.")

if __name__ == "__main__":
    main()
