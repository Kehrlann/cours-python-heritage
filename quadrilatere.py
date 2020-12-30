class Quadrilatere:
    def __init__(self, s1, s2, s3, s4):
        self.x1, self.y1 = s1
        self.x2, self.y2 = s2
        self.x3, self.y3 = s3
        self.x4, self.y4 = s4

    def __repr__(self):
        return (f"Quadrilatere ["
                f"({self.x1}, {self.y1}), "
                f"({self.x2}, {self.y2}), "
                f"({self.x3}, {self.y3}), "
                f"({self.x4}, {self.y4})]")

    def aire(self):
        return (
            abs((self.x1 - self.x3) * (self.y2 - self.y4))
            + abs((self.x2 - self.x4) * (self.y1 - self.y3))
        ) / 2


if __name__ == "__main__":
    q = Quadrilatere(
        (4, 4),
        (4, 5),
        (5, 5),
        (5, 4)
    )
    print("q:", q)
    print("Aire de q:", q.aire())
