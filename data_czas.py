from datetime import datetime, timedelta
import time
import pytz  # Biblioteka do obsługi stref czasowych

def formatowanie_dat():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Sformatowana data:", formatted_date)

def obliczenia_czasowe():
    now = datetime.now()
    future_date = now + timedelta(days=10)
    past_time = now - timedelta(hours=5)
    print("Aktualna data:", now)
    print("Za 10 dni:", future_date)
    print("5 godzin temu:", past_time)

def roznica_miedzy_datami():
    date1 = datetime(2024, 6, 1)
    date2 = datetime(2025, 2, 11)
    difference = date2 - date1
    print("Różnica w dniach:", difference.days)

def zaawansowane_operacje_na_czasie():
    utc_now = datetime.now(pytz.utc)
    print("Aktualny czas UTC:", utc_now.strftime("%Y-%m-%d %H:%M:%S %Z"))
    
    strefa_warszawa = utc_now.astimezone(pytz.timezone("Europe/Warsaw"))
    strefa_nowy_jork = utc_now.astimezone(pytz.timezone("America/New_York"))
    print("Czas w Warszawie:", strefa_warszawa.strftime("%Y-%m-%d %H:%M:%S %Z"))
    print("Czas w Nowym Jorku:", strefa_nowy_jork.strftime("%Y-%m-%d %H:%M:%S %Z"))
    
    roznica_czasu = strefa_warszawa.utcoffset() - strefa_nowy_jork.utcoffset()
    print("Różnica czasu między Warszawą a Nowym Jorkiem:", roznica_czasu)

def pomiar_czasu():
    start_time = time.time()
    print("Odliczanie...")
    for i in range(5, 0, -1):
        print(f"{i} sekund...")
        time.sleep(1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Czas wykonania odliczania: {elapsed_time:.2f} sekund")

def sprawdz_weekend():
    przyszla_data = datetime(2025, 3, 15)
    dzien_tygodnia = przyszla_data.strftime("%A")
    if przyszla_data.weekday() >= 5:
        print(f"{przyszla_data.strftime('%Y-%m-%d')} ({dzien_tygodnia}) to weekend!")
    else:
        print(f"{przyszla_data.strftime('%Y-%m-%d')} ({dzien_tygodnia}) to dzień roboczy.")

def dodawanie_czasu():
    data_pocz = datetime(2024, 2, 11, 14, 30)
    data_konc = data_pocz + timedelta(days=100, hours=5, minutes=45)
    print("Data początkowa:", data_pocz.strftime("%Y-%m-%d %H:%M:%S"))
    print("Data końcowa po dodaniu 100 dni, 5h i 45m:", data_konc.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    formatowanie_dat()
    obliczenia_czasowe()
    roznica_miedzy_datami()
    zaawansowane_operacje_na_czasie()
    pomiar_czasu()
    sprawdz_weekend()
    dodawanie_czasu()
