from collection_argparse.cli import parse, main

if __name__ == "__main__":
    args = parse()
    print(main(args))
