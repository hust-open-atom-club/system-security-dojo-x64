#!/opt/pwn.college/python


def main():
    file_path = "/challenge/elf-crackme-level3.1"

    try:
        with open(file_path, "r+b") as file:
            position = int(
                input(
                    "[+] Please enter the position to modify (in hexadecimal, e.g., 0x1000): "
                ),
                16,
            )
            new_data = input(
                "[+] Please enter the new data in seperate bytes (in hexadecimal, e.g., 01 be ef): "
            )

            file.seek(position)
            file.write(bytes.fromhex(new_data))

        print("[+] Modification completed!")
    except FileNotFoundError:
        print("[-] Unable to open the file")
    except Exception as e:
        print("[-] An error occurred:", e)


if __name__ == "__main__":
    print("###")
    print("### Welcome to ./elf-crackme-level3.1!")
    print("###")
    print("")
    print(
        "We have provided a binary with a corrupted PLT table jumping to the GOT table."
    )
    print(
        "Please follow the PLT table jump order, use the script, and execute it to obtain the flag."
    )
    main()
