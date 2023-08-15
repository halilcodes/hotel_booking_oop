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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        cards_df = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
        card_to_check = {"number": self.number, "expiration": expiration,
                         "cvc": cvc, "holder": holder}

        if card_to_check in cards_df:
            print("credit card confirmed")
            return True
        else:
            print("invalid card")
            return False


if __name__ == "__main__":
    df = pd.read_csv("hotels.csv", dtype={"id": str})
    print(df)
    h_id = input("Enter the id of the hotel: ")
    hotel = Hotel(h_id)
    if hotel.available():
        credit_card = CreditCard(number="1234")
        if credit_card.validate(expiration="12/26", holder="JON SMITH", cvc="123"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            reservation_ticket.generate()
        else:
            print("Payment problem, you are poor or a thief!")
    else:
        print("Hotel is not free.")
