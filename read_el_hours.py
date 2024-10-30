# 1. Open WhatsApp web https://web.whatsapp.com/
# 2. Open "My EL" group chat
# 3. Copy all the hour numbers and paste it into "EL_hours.txt" and save it
# 4. Make sure the full path to the text file is correct
# 5. Run the following program

f = open("C:/Users/Asus/Desktop/EL_hours.txt", "r")
sum = 0
for line in f:
	line = line.split("9436:")[1]
	line = line.strip()
	num = int(line)
	sum += num

print(f"Sum: {sum}")