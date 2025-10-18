app_name = "Фильмдер рейтингі базасы"        
VERSION = (1, 0)                             

movies = {}

def add_movie():
    title = input("Фильм атауын енгізіңіз: ").strip()
    if not title:
        print("Атау бос болмау керек.")
        return
    key = title.lower().replace("  ", " ")
    year_str = input("Жылы (мысалы 2023) енгізіңіз: ").strip()
    if not year_str.isdigit():
        print("Жыл сан болуы керек.")
        return
    year = int(year_str)
    try:
        rating = float(input("Рейтинг (0.0 - 10.0) енгізіңіз: ").strip())
    except ValueError:
        print("Рейтинг дұрыс форматта емес.")
        return
    if not (0.0 <= rating <= 10.0):   
        print("Рейтинг 0.0 мен 10.0 арасында болуы тиіс.")
        return
    genres_raw = input("Жанрларды үтір арқылы енгізіңіз (мысалы: drama,comedy): ").strip()
    genres = [g.strip().lower() for g in genres_raw.split(",") if g.strip()]
    if key in movies:
        print(f"'{title}' базада бар. Қайта жазамын ба? (иә/жоқ)")
        ans = input().strip().lower()
        if ans not in ("иә","и", "yes", "y"):
            print("Қосу болмады.")
            return
    movies[key] = {"title": title, "year": year, "rating": rating, "genres": genres}
    print(f"Фильм қосылды: {title} ({year}) - рейтинг: {rating}")

def list_movies():
    if not movies:
        print("База бос.")
        return
    for k, v in movies.items():
        print(f"- {v['title']} ({v['year']}) | Рейтинг: {v['rating']} | Жанрлар: {', '.join(v['genres'])}")

def average_rating():
    if not movies:
        print("База бос. Орташа рейтинг есептелмейді.")
        return
    total = sum(v['rating'] for v in movies.values())
    avg = total / len(movies)           
    print(f"Фильмдер саны: {len(movies)}. Орташа рейтинг: {avg:.2f}")

def search_movie():
    q = input("Іздеу (атау немесе жыл): ").strip().lower()
    results = []
    terms = q.split()
    for v in movies.values():
        hay = f"{v['title'].lower()} {v['year']}"
        if all(t in hay for t in terms):  
            results.append(v)
    if not results:
        print("Табылған жоқ.")
        return
    for r in results:
        print(f"{r['title']} ({r['year']}) - {r['rating']}")

def remove_duplicates_genres():
    all_genres = []
    for v in movies.values():
        all_genres.extend(v['genres'])
    unique = set(all_genres) 
    print(f"Барлық жанрлар (қайталанбайтын): {', '.join(sorted(unique))}")

def demo_sample_data():
    sample = [
        ("The Shawshank Redemption", 1994, 9.3, "drama,crime"),
        ("Inception", 2010, 8.8, "sci-fi,thriller"),
        ("Interstellar", 2014, 8.6, "sci-fi,drama"),
        ("Inception", 2010, 8.8, "sci-fi,thriller"),  
    ]
    for t,y,r,g in sample:
        k = t.lower()
        genres = [x.strip() for x in g.split(",")]
        movies[k] = {"title": t, "year": y, "rating": r, "genres": genres}
    print("Үлгі мәліметтер қосылды.")

def delete_movie():
    title = input("Жойғыңыз келетін фильм атауы: ").strip().lower()
    if title in movies:
        del movies[title]
        print("Фильм жойылды.")
    else:
        print("Мұндай фильм табылмады.")

def stats():
    if not movies:
        print("База бос.")
        return
    ratings = [(v['rating'], v['title']) for v in movies.values()]
    maxr, maxt = max(ratings)
    minr, mint = min(ratings)
    print(f"Ең жоғары рейтинг: {maxt} - {maxr}")
    print(f"Ең төмен рейтинг: {mint} - {minr}")

def main_menu():
    print(f"{app_name} v{VERSION[0]}.{VERSION[1]}")
    while True:
        print("\nМәзір: 1) Фильм қосу  2) Барлығын көру  3) Орташа рейтинг  4) Іздеу")
        print("5) Жанрларды тазалау (жиын) 6) Үлгі мәліметтер қосу 7) Жою 8) Статистика 9) Шығу")
        choice = input("Таңдауыңыз (1-9): ").strip()
        if choice == "1":
            add_movie()
        elif choice == "2":
            list_movies()
        elif choice == "3":
            average_rating()
        elif choice == "4":
            search_movie()
        elif choice == "5":
            remove_duplicates_genres()
        elif choice == "6":
            demo_sample_data()
        elif choice == "7":
            delete_movie()
        elif choice == "8":
            stats()
        elif choice == "9":
            print("Шығу. Сау болыңыз!")
            break
        else:
            print("Қате таңдау. 1-9 аралығындағы санды енгізіңіз.")

if __name__ == "__main__":
    main_menu()
