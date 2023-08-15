import pandas as pd
from fpdf import FPDF


class Item:
    def __init__(self, product_id):
        self.id = product_id
        self.stock = self.availability()
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.id, 'price'].squeeze()

    def availability(self):
        stock = df.loc[df['id'] == self.id, 'in stock'].squeeze()
        return stock

    def buy(self):
        self.stock -= 1
        df.loc[df['id'] == self.id, 'in stock'] = self.stock
        df.to_csv("articles.csv", index=False)

    def generate_pdf(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        pdf.output(f"{self.name}_receipt.pdf")


if __name__ == "__main__":
    df = pd.read_csv("articles.csv", dtype={"id": str})
    print(df)
    item_id = input("Choose an item to buy: ")
    item = Item(item_id)

    if item.availability() > 0:
        item.buy()
        item.generate_pdf()
