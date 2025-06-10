from colorama import Fore, Style

def complete(message: str, *other) -> None:
	print(Style.BRIGHT + Fore.GREEN + "[+] {}".format(message))
	for o in other:
		print(f" | {o}")
	print(Style.RESET_ALL, end="")

def error(message: str, *other) -> None:
	print(Style.BRIGHT + Fore.RED + "[-] {}".format(message))
	for o in other:
		print(f" | {o}")
	print(Style.RESET_ALL, end="")

def warning(message: str, *other) -> None:
	print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[!] {}".format(message))
	for o in other:
		print(f" | {o}")
	print(Style.RESET_ALL, end="")


def info(message: str, *other) -> None:
	print(Style.BRIGHT + "[*] {}".format(message))
	for o in other:
		print(f" | {o}")
	print(Style.RESET_ALL, end="")




if __name__ == '__main__':
	complete("Test", "cool")
	error("Test", "cool")
	warning("Test", "cool")
	info("Test", "cool")
