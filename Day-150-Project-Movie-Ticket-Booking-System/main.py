# Day 150 · Project: Movie Ticket Booking System — Movie Ticket Booking
# Run: python main.py

import random
import string
import sys

DEMO = not sys.stdin.isatty()
DEMO_INPUTS = iter(["1", "2", "A1 A2", "Prasanna", "1", "1", "H5 H6 H7", "Asha", "1", "1", "H6", "Ravi",
                    "3", "BK", "4", "0"])

def ask(prompt):
    if DEMO:
        v = next(DEMO_INPUTS); print(prompt + v); return v
    return input(prompt)

class Show:
    def __init__(self, movie, time, rows=8, cols=10):
        self.movie, self.time = movie, time
        self.rows, self.cols = rows, cols
        self.seats = [["." for _ in range(cols)] for _ in range(rows)]
        self.bookings = {}

    def price(self, r):
        return 350 if r >= self.rows - 2 else 250 if r >= self.rows // 2 else 180   # recliner/premium/classic

    def show_map(self):
        print(f"\n🎬 {self.movie} @ {self.time}\n      " + "".join(f"{c + 1:>3}" for c in range(self.cols)))
        for r, row in enumerate(self.seats):
            label = string.ascii_uppercase[r]
            print(f"  {label} ₹{self.price(r)} " + "".join(f"{s:>3}" for s in row))
        print("     " + "━" * (self.cols * 3 + 2) + "\n" + " " * 14 + "SCREEN THIS WAY   (X = booked)")

    def parse(self, code):
        r = string.ascii_uppercase.index(code[0].upper())
        c = int(code[1:]) - 1
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            raise ValueError(f"no seat {code}")
        return r, c

    def book(self, codes, name):
        cells = [self.parse(c) for c in codes]
        taken = [codes[i] for i, (r, c) in enumerate(cells) if self.seats[r][c] == "X"]
        if taken:
            raise ValueError(f"already booked: {', '.join(taken)}")
        for r, c in cells:
            self.seats[r][c] = "X"
        bid = "BK" + "".join(random.choices(string.digits, k=5))
        total = sum(self.price(r) for r, _ in cells)
        self.bookings[bid] = {"name": name, "seats": codes, "total": total}
        return bid, total

    def cancel(self, bid):
        b = self.bookings.pop(bid)
        for code in b["seats"]:
            r, c = self.parse(code)
            self.seats[r][c] = "."
        return b

SHOWS = [Show("Interstellar", "6:00 PM"), Show("3 Idiots", "9:15 PM")]

def main():
    while True:
        print("\n1.Book 2.View seats 3.Cancel 4.All bookings 0.Exit")
        c = ask("> ")
        try:
            if c in ("1", "2"):
                for i, s in enumerate(SHOWS, 1):
                    print(f"  {i}. {s.movie} ({s.time})")
                show = SHOWS[int(ask("Show: ")) - 1]
                show.show_map()
                if c == "1":
                    seats = ask("Seats (e.g. C4 C5): ").split()
                    bid, total = show.book(seats, ask("Name: "))
                    print(f"\n🎟️  TICKET {bid} | {show.movie} {show.time} | seats {' '.join(seats)} | ₹{total} (+ ₹{total * 0.18:.0f} GST)")
            elif c == "3":
                bid = ask("Booking ID: ")
                if DEMO:
                    bid = next(iter(SHOWS[0].bookings))
                for s in SHOWS:
                    if bid in s.bookings:
                        b = s.cancel(bid); print(f"Cancelled {bid}, refund ₹{b['total'] * 0.9:.0f} (10% fee)"); break
                else:
                    print("Booking not found")
            elif c == "4":
                for s in SHOWS:
                    for bid, b in s.bookings.items():
                        print(f"  {bid} {s.movie:<13} {b['name']:<10} {' '.join(b['seats']):<10} ₹{b['total']}")
            elif c == "0":
                break
        except (ValueError, IndexError) as e:
            print("❌", e)

if __name__ == "__main__":
    if DEMO:
        random.seed(9)
    main()
