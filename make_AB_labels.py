# PRINT OUT UP TO 37 SHEETS OF A/B BARCODES, JUST SCAN THE LAST BARCODE YOU HAVE

barcodes_to_print = int(raw_input("How many pages do you want to print?\n")) * 80
if (barcodes_to_print > 1480):
	barcodes_to_print = 1480
	print("Avery will only allow for 3000 rows, creating 37 sheets.")
prefix = "GBIA"
barcode_number = int(raw_input("Scan the last barcode you have printed:\n")[4:-1]) + 1
zero_pad = 1000000
while (barcode_number < zero_pad):
	zero_pad /= 10
	prefix += "0"
filename = str(barcode_number) + " - " + str(barcode_number + 400) + ".csv"

f = open(filename, 'w+')

# change the argument of range() if you want to change the amount
for i in range(barcodes_to_print):
	f.write(prefix + str(barcode_number) + "A\n")
	f.write(prefix + str(barcode_number) + "B\n")
	barcode_number += 1
	if (barcode_number < zero_pad):		
		zero_pad *= 10
		prefix = prefix[0:-1]
	if (barcode_number > 9999999):
		print("ALERT! WE HAVE REACHED OUR LIMIT FOR iARCHIVE RECORDS")
		
# leaves an extra newline, but Avery doesn't read these
f.close()
print("New CSV file " + filename + " created." )