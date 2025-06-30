reference = input("Enter the reference genome :")
patient = input("Enter the patient genome: ")
if len(reference) == len(patient):
    for i in range(len(reference)):
        if reference[i] != patient[i]:
            print(f"SNP at position {i + 1}: {reference[i]}+{patient[i]}")
        else:
            print("Error: Sequences must be the same length.")


