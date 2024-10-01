seconds = int(input("Enter seconds: "))

properTime = seconds % (24 * 3600)

print(f'Seconds you entered: {seconds} \nMinutes: {seconds // 60} : Seconds: {seconds % 60}')
