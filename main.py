import pandas as pd


class Hotel:
    def __init__(self, hotel_id):
        self.id = hotel_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()
        self.city = df.loc[df['id'] == self.id, 'city'].squeeze()

    def book(self):
        """Books a hotel by changing its availability to no"""
        df.loc[df['id'] == self.id, 'available'] = "no"
        df.to_csv("hotels.csv", index=False)

    def view(self):
        pass

    def available(self):
        """ Checks if the hotel is available"""
        availability = df.loc[df['id'] == self.id, 'available'].squeeze()
        if availability == "yes":
            print("hotel available!")
            return True
        else:
            print("No Room")
            return False


class SpaHotel(Hotel):
    def book(self):
        pass

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        print(f"Dear {self.customer_name.capitalize()}, \n"
              f"Your reservation at {self.hotel.name} in {self.hotel.city} is done.\n\n"
              f"Enjoy your stay!\n"
              f"HCH Hotels Group")
        return True


class SpaTicket(ReservationTicket):
    def generate(self):
        print(f"Dear {self.customer_name.capitalize()}, \n"
              f"Your SPA reservation at {self.hotel.name} in {self.hotel.city} is done.\n\n"
              f"Enjoy your SPA!\n"
              f"HCH Hotels Group")
        return True


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_to_check = {"number": self.number, "expiration": expiration,
                         "cvc": cvc, "holder": holder}

        if card_to_check in cards_df:
            print("credit card confirmed")
            return True
        else:
            print("invalid card")
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = secure_cards_df.loc[secure_cards_df["number"] == self.number, 'password'].squeeze()
        # if password == given_password:
        #     print("card authenticated!")
        #     return True
        # else:
        #     return False
        return password == given_password


if __name__ == "__main__":
    df = pd.read_csv("hotels.csv", dtype={"id": str})
    cards_df = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
    secure_cards_df = pd.read_csv("card_security.csv", dtype=str)
    print(df)
    h_id = input("Enter the id of the hotel: ")
    hotel = Hotel(h_id)
    if hotel.available():
        credit_card = SecureCreditCard(number="1234")
        if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
            if credit_card.authenticate(given_password="mypass"):
                print("card authenticated!")
                hotel.book()
                name = input("Enter your name: ")
                reservation_ticket = ReservationTicket(name, hotel)
                reservation_ticket.generate()
                wants_spa = input("Do you want to book a spa package? (y/n)")
                if wants_spa == "y":
                    spa_hotel = SpaHotel(h_id)
                    spa_hotel.book()
                    spa = SpaTicket(name, hotel)
                    spa.generate()
            else:
                print("password security failed")
        else:
            print("Payment problem about the credit card")
    else:
        print("Hotel is not free.")
