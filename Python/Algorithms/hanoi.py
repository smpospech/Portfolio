
global moves
moves = 0


def main():
    disks = int(input("Enter the number of disks for towers of hanoi: "))
    hanoi(disks, "start", "a1", "a2", "a3", "a4", "dest")
    print("total moves for " + str(disks) + " disks:", moves)


def hanoi(disk, start, a1, a2, a3, a4, dest):
    if disk == 1:
        move(disk, start, a1)
        move(disk, a1, a2)
        move(disk, a2, a3)
        move(disk, a3, a4)
        move(disk, a4, dest)
    elif disk >= 2:
        start_to_a4(disk - 1, start, a1, a2, a3, a4)
        move(disk, start, 1)
        move(disk, a1, a2)
        move(disk, a2, a3)
        a4_to_a2(disk - 1, a4, a3, a2)
        move(disk, a3, a4)
        move(disk, a4, dest)
        a2_to_dest(disk-1, a2, a3, a4, dest)


def start_to_a4(disk, start, a1, a2, a3, a4):  # Hanoi 5 DONE
    if disk == 1:
        move(disk, start, a1)
        move(disk, a1, a2)
        move(disk, a2, a3)
        move(disk, a3, a4)
    elif disk >= 2:
        start_to_a4(disk - 1, start, a1, a2, a3, a4)
        move(disk, start, a1)
        move(disk, a1, a2)
        move(disk, a2, a3)
        a4_to_a2(disk - 1, a4, a3, a2)
        move(disk, a3, a4)
        a4_to_a2(disk - 1, a2, a3, a4)


def a4_to_a2(disk, a1, a2, a3):  # Hanoi 3
    if disk == 1:
        move(disk, a1, a2)
        move(disk, a2, a3)
    elif disk >= 2:
        a4_to_a2(disk - 1, a1, a2, a3)
        move(disk, a1, a2)
        a4_to_a2(disk - 1, a3, a2, a1)
        move(disk, a2, a3)
        a4_to_a2(disk - 1, a1, a2, a3)


def a2_to_dest(disk, a2, a3, a4, dest):  # Hanoi 4
    if disk == 1:
        move(disk, a2, a3)
        move(disk, a3, a4)
        move(disk, a4, dest)
    elif disk >= 2:
        a4_to_a2(disk - 1, a2, a3, a4)
        move(disk, a2, a3)
        a4_to_a2(disk-1, a4, a3, a2)
        move(disk, a3, a4)
        move(disk, a4, dest)
        a2_to_dest(disk-1, a2, a3, a4, dest)


def move(disk, start, dest):
    global moves
    moves += 1
    print(str(moves) + ": move disk", disk, "from", start, "to", dest)


if __name__ == "__main__":
    main()
