import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def find_numbers(text):
    pattern = r"\d+"
    return re.findall(pattern, text)

def replace_multiple_spaces(text):
    pattern = r"\s+"
    return re.sub(pattern, " ", text)

def validate_phone(phone):
    pattern = r"^\d{3}-\d{3}-\d{3}$"
    return bool(re.match(pattern, phone))

def find_ip_addresses(text):
    ipv4_pattern = r"\b((25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\b"
    ipv6_pattern = r"\b(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|" \
                  r"([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|" \
                  r"([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|" \
                  r"([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|" \
                  r":((:[0-9a-fA-F]{1,4}){1,7}|:))\b"
    ipv4_matches = re.findall(ipv4_pattern, text)
    ipv6_matches = re.findall(ipv6_pattern, text)
    ipv4_matches = [match[0] for match in ipv4_matches]
    return ipv4_matches, ipv6_matches

if __name__ == "__main__":
    test_email = "test@example.com"
    test_text = "Cena wynosi 150 zł, a rabat to 20%."
    test_spaces = "To    jest   test."
    test_phone = "123-456-789"
    test_ip_text = """
    Serwer 1: 192.168.1.1
    Serwer 2: 255.255.255.255
    Serwer 3: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
    Serwer 4: ::1
    Serwer 5: fe80::1%lo0
    Niepoprawny IP: 999.999.999.999
    """

    print("Email poprawny:", validate_email(test_email))
    print("Znalezione liczby:", find_numbers(test_text))
    print("Tekst bez nadmiarowych spacji:", replace_multiple_spaces(test_spaces))
    print("Numer telefonu poprawny:", validate_phone(test_phone))
    ipv4, ipv6 = find_ip_addresses(test_ip_text)
    print("Znalezione adresy IPv4:", ipv4)
    print("Znalezione adresy IPv6:", ipv6)
