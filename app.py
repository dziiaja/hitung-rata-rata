input_str = input("Masukan Nilai-Nilai Numeric, pisahkan dengan ',': ")
nilai_list =  input_str.split(",")
nilai_list = [float(nilai) for nilai in nilai_list]
rata_rata =  sum(nilai_list) / len(nilai_list)
print("nilai rata ratanya adalah: ", rata_rata)