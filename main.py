import os

TEXT = (
    "Visited twice: once as a tourist, once to return a small determined dog "
    "that had followed our ship. Recommend the first."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
