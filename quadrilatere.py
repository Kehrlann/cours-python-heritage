from math import sqrt


class Quadrilatere:

    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def __repr__(self):
        return (f"Quadrilatere ["
                f"{self.s1}, "
                f"{self.s2}, "
                f"{self.s3}, "
                f"{self.s4}]")

    def aire(self):
        x1, y1 = self.s1
        x2, y2 = self.s2
        x3, y3 = self.s3
        x4, y4 = self.s4
        # Ne fonctionne que pour les quadrilateres convexes, oups
        return (abs((x1 - x3) * (y2 - y4)) + abs((x2 - x4) * (y1 - y3))) / 2

    def perimetre(self):
        return sum(self.__longueur(segment)
                   for segment in self.__segments())

    def __segments(self):
        return (
            (self.s1, self.s2),
            (self.s2, self.s3),
            (self.s3, self.s4),
            (self.s4, self.s1)
        )

    def __longueur(_, segment):
        s1, s2 = segment
        x1, y1 = s1
        x2, y2 = s2
        return sqrt((x1-x2)**2 + (y1-y2)**2)


if __name__ == "__main__":
    q = Quadrilatere(
        (4, 4),
        (4, 5),
        (5, 5),
        (5, 4)
    )
    print("q:", q)
    print("Périmètre de q:", q.perimetre())
    print("Aire de q:", q.aire())
    print("~~~~~~~~~~~~~~~")
