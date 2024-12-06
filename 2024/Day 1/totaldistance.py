def calculate_total_distance(file_path):
    left_ids = []
    right_ids = []
    total_distance = 0

    with open(file_path, "r") as file:
        for line in file:
            left_id = line[0:5]
            right_id = line[8:13]
            left_ids.append(int(left_id))
            right_ids.append(int(right_id))

    left_ids.sort()
    right_ids.sort()

    for left_num, right_num in zip(left_ids, right_ids):
        distance = abs(right_num - left_num)
        total_distance += distance

    return total_distance


def main():
    file_path = "distances.txt"
    total_distance = calculate_total_distance(file_path)
    print(f"Total distance: {total_distance}")


if __name__ == "__main__":
    main()
