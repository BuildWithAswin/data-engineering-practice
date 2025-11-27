def hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, helper, source, destination)


print(hanoi(3, "A", "B", "C"))
