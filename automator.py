import subprocess

def main():
    base_command = input("What command would you like to run?\n").strip()
    if not base_command:
        print("No command entered. Exiting.")
        return

    print("Please paste an argument (Ctrl+C to quit):")
    while True:
        try:
            arg = input().strip()
            if not arg:
                continue
            # Construct the full command line
            full_command = f"{base_command} {arg}"
            print(f"\nRunning: {full_command}\n")

            # Run the command
            subprocess.run(full_command, shell=True)
            print("\nPlease paste another argument (Ctrl+C to quit):")
        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
