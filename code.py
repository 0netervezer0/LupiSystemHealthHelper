from elevate import elevate
import time
import platform
import os
from colorama import init
init()
from colorama import Fore, Back, Style
elevate()
command_r = 1

print( Fore.YELLOW )
print( 'Lupi System Health Helper' )
print( 'v 1.0' )
print( '' )
print( '' )
time.sleep( 1 )
print( 'Проверка совместимости с вашей системой...' )
time.sleep( 3 )
osc = platform.platform()
osr = '-'.join( osc.split ( '-', 2 )[ :2 ] )
print( '...' )
time.sleep ( 2 )
if osr == 'Windows-7' or 'Windows-10' or 'Windows-11':
	print( 'Ваша система совместима с консольным скриптом!' )
	print( '' )
	print( 'Далее вам потребуется использовать внутренние команды скрипта' )
	print( 'Для получения списка команд напишите команду "help"' )
	print( '' )
	while command_r == 1:
		command_r == 0
		command = input( '>> ' )
		if command == 'help':
			print( 'total-chek   Скрипт запускает полную проверку вашей системы' )
			print( 'sysf-chek    Скрипт запускает проверку системных файлов вашей системы' )
			print( 'dsk-chek     Срипт запускает проверку диска, на который установлена система' )
			print( 'mem-chek     Скрипт запускает проверку оперативной памяти (потребуется перезагрузка)' )
			print( 'info         Информация о скрипте и разработчике' )
			print( 'cls          Закрыть скрипт и сохранить изменения' )
			print( 'help         Список доступных команд' )
			print( '' )
			command_r = 1
		elif command == 'total-chek':
			print( 'Запущенное средство обнаружит общие системные неполадки и постарается исправить их' )
			ready = input( 'Вы готовы выполнить команду? (Y/N) ' )
			if ready == 'Y':
				os.system( 'DISM /Online /Cleanup-Image /RestoreHealth' )
				print( '' )
			elif ready == 'N':
				print( '' )
			else:
				print( Fore.RED )
				print( 'Недопустимый аргумент!' )
				print( Fore.YELLOW )
		elif command == 'sysf-chek':
			print( 'Запущенное средство обнаружит проблемы с системными файлами и постарается исправить их' )
			ready = input( 'Вы готовы выполнить команду? (Y/N) ' )
			if ready == 'Y':
				os.system( 'sfc /scannow' )
				print( '' )
			elif ready == 'N':
				print( '' )
			else:
				print( Fore.RED )
				print( 'Недопустимый аргумент!' )
				print( Fore.YELLOW )
		elif command == 'dsk-chek':
			print( 'Запущенное средство обнаружит проблемы с системными файлами и постарается исправить их' )
			ready = input( 'Вы готовы выполнить команду? (Y/N) ' )
			if ready == 'Y':
				os.system( 'chkdsk c: /f /r' )
				print( '' )
			elif ready == 'N':
				print( '' )
			else:
				print( Fore.RED )
				print( 'Недопустимый аргумент!' )
				print( Fore.YELLOW )
		elif command == 'mem-chek':
			print( 'Запущенное средство обнаружит проблемы оператиной памяти во время следующей перезагрузки' )
			print( 'Следуйте указаниям в открывшемся окне' )
			ready = input( 'Вы готовы выполнить команду? (Y/N) ' )
			if ready == 'Y':
				os.system( 'mdsched' )
				print( '' )
			elif ready == 'N':
				print( '' )
			else:
				print( Fore.RED )
				print( 'Недопустимый аргумент!' )
				print( Fore.YELLOW )
		elif command == 'info':
			print( 'Lupi System Health Helper v1.0' )
			print( 'Разработчик - LupiSoft (NETERVEZER)' )
			print( '' )
			print( 'Посетите GitHub - https://github.com/0netervezer0' )
			print( 'Новые версии можно отслеживать на официальном GitHub разработчика' )
			print( 'При возникновении вопросов или ошибок свяжитесь с разработчиком (Discord - netervezer)' )
			print( '' )
		elif command == 'cls':
			print( 'Закрытие...' )
			time.sleep( 2 )
			sys.exit()
else:
	print( Fore.RED )
	print( 'Система несовместима! Сожалею...' )
	print( Fore.YELLOW )
	print( 'Нажмите любую клавишу или закройте окно консоли для выхода из скрипта' )