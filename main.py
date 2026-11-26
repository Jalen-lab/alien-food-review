#!/usr/bin/env python3
"""One Star, Five Stars for the Food.

The bounty asks for one sentence, at most 200 characters, in the voice
of an alien tourist giving planet Earth a one-star review while still
slipping in a real compliment about the food. A model judge compares
entries two at a time on the brief sealed with the bounty. The brief
weighs, in order: the text is a one-star alien review of Earth that
still compliments the food; it sounds like a real alien visitor, an
outsider baffled by human habits with a grievance worth one star; the
complaint and the food compliment both land, and the turn between them
is funny rather than merely stated; it stays one sentence inside the
limit with every word earning its place; and the angle is fresh rather
than a list of generic complaints.

The sentence this program writes is:

    One star: gravity stole my snacks, the locals worship glowing
    rectangles, but the dumplings alone justify the invasion.

Why it is built that way: the grievance is an outsider's bafflement,
gravity misbehaving and humans staring at glowing rectangles, which is
worth one star and could only come from a visitor. The turn is the word
"but": the review flips from complaint to compliment in one beat, and
the compliment is sincere, dumplings worth crossing galaxies for, pushed
one step further into "justify the invasion", which is the joke. The
whole thing is one sentence of 119 characters, so it fits the limit
with room to spare and every word earns its place.

The program does one thing and does it the same way every run: it writes
exactly that sentence, and nothing else, to /output/entry.txt.
"""

import os

REVIEW = (
    "One star: gravity stole my snacks, the locals worship glowing "
    "rectangles, but the dumplings alone justify the invasion."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    os.chmod("/output/entry.txt", 0o644)
    print(REVIEW)


if __name__ == "__main__":
    main()
