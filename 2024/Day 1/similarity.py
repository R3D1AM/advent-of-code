def read_distances(file_path):
    left_ids = []
    right_ids = []

    with open(file_path, "r") as file:
        for line in file:
            left_id = line[0:5]
            right_id = line[8:13]
            left_ids.append(int(left_id))
            right_ids.append(int(right_id))

    return left_ids, right_ids


def calculate_similarity_score(left_ids, right_ids):
    total_score = 0

    for left_id in set(left_ids):
        count_in_right = right_ids.count(left_id)
        total_score += left_id * count_in_right

    return total_score


def main():
    file_path = "distances.txt"
    left_ids, right_ids = read_distances(file_path)
    similarity_score = calculate_similarity_score(left_ids, right_ids)

    print(f"Similarity score: {similarity_score}")


if __name__ == "__main__":
    main()
