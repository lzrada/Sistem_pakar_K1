import matplotlib.image as mpimg
import matplotlib.pyplot as plt

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}


def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open("penyakit.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open("Gejala penyakit2/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[disease] = s_list
        disease_s_file.close()

        disease_s_file = open("Deskripsi penyakit/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()

        disease_s_file = open("Obat penyakit/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


def identify_disease_backward():
    print("")
    print("Halo! Saya adalah Dok-bot, Saya akan mendiagnosa penyakit tanaman melon anda deengan metode backward!")
    print("Oleh karena itu anda harus menjawab beberapa gejala yang anda alami")
    print("Apakah anda merasakan beberapa gejala dibawah ini(yes/no):")
    print("")
    possible_diseases = diseases_list.copy()

    for disease in diseases_list:
        symptoms = symptom_map[disease]
        print(f"\nMengecek gejala untuk penyakit: {disease}")
        for symptom in symptoms:
            response = input(f"{symptom} (yes/no): ").strip().lower()
            if response == "no":
                possible_diseases.remove(disease)
                print(f"{disease} dikeluarkan karena gejala '{symptom}' tidak cocok.")
                break
        if len(possible_diseases) == 0:
            break

    if len(possible_diseases) == 1:
        disease = possible_diseases[0]
        print(f"\nKemungkinan penyakit adalah: {disease}")
        print("Deskripsi:")
        print(d_desc_map[disease])
        print("Pengobatan:")
        print(d_treatment_map[disease])

        plt.imshow(mpimg.imread("./img/" + disease + ".jpg"))
        plt.title(disease)
        plt.axis('off')
        plt.show()
    else:
        print("\nTidak dapat mendiagnosa penyakit dengan gejala yang diberikan.")


if __name__ == "__main__":
    preprocess()

    while True:
        identify_disease_backward()

        retry = input("Ingin mencoba lagi? (yes/no): ").strip().lower()
        if retry != "yes":
            break
