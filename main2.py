import pandas as pd


class Hotel:
    watermark = "HCH Hotels Group"

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


if __name__ == "__main__":
    df = pd.read_csv("hotels.csv", dtype={"id": str})
