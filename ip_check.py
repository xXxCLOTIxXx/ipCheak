import os
import requests

try:
	import pyfiglet
	from rich.console import Console
except:
	print("устанрвка модулей...")
	os.system("pip install rich")
	os.system("pip install pyfiglet")
	print("Выполнено")
	import pyfiglet
	from rich.console import Console

os.system('cls')
console = Console()
console.print("[magenta]" + pyfiglet.figlet_format("Ip check", font="slant") + "[/magenta]")
console.print("[bold cyan] made by CLOTI (Xsarz)[/] [bold yellow]Telegram: t.me/DXsarz[/]")


def get_info_by_ip(ip='127.0.0.1'):
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
		try:
			console.print(f"[bold green]Соединение: {response['status']}[/]\n[bold cyan]Страна: {response['country']}\nКод страны: {response['countryCode']}\nРегион: {response['regionName']}({response['region']})\nГород: {response['city']}\nВременная зона: {response['timezone']}[/]")
			console.print(f"[bold red]Широта: {response['lat']}\nДолгота: {response['lon']}\nIP: {response['query']}\nПровайдер: {response['org']}[/]")
		except:
			print("Ошибка вывода информации")
	except requests.exceptions.ConnectionError:
		console.print('[bold red][!] Проблемы с подключением к интернету![/]')

def main():
	ip = input("Введите ip цели>> ")
	get_info_by_ip(ip=ip)
main()