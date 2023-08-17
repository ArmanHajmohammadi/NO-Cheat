############## NO-CHEAT ##############
######## By: Arman Hajmohammadi ########

# importing the dependencies
import os
import fitz


# A method to compare two pdf files:
def compare_pdf_files(pdf1_path, pdf2_path):
    pdf1 = fitz.open(pdf1_path)
    pdf2 = fitz.open(pdf2_path)

    if pdf1.page_count != pdf2.page_count:
        return False

    for page_num in range(pdf1.page_count):
        page1 = pdf1[page_num]
        page2 = pdf2[page_num]

        size1 = len(page1.get_text())
        size2 = len(page2.get_text())

        if size1 != size2:
            return False

    pdf1.close()
    pdf2.close()
    return True


def CompareScript(folder_path):
    result = ""
    pdf_files = [file for file in os.listdir(
        folder_path) if file.lower().endswith(".pdf")]

    for i in range(len(pdf_files)):
        for j in range(i + 1, len(pdf_files)):
            pdf1_path = os.path.join(folder_path, pdf_files[i])
            pdf2_path = os.path.join(folder_path, pdf_files[j])

            are_similar = compare_pdf_files(pdf1_path, pdf2_path)

            if are_similar:
                print(f"Similar PDFs: {pdf_files[i]} and {pdf_files[j]}")
                result += f"\"{pdf_files[i]}\" & \"{pdf_files[j]}\"\n"
    if (result == ""):
        return "Congratulations! There was NO CHEAT!"
    else:
        return result
