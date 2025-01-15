import experta
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
        disease_s_file = open("Gejala penyakit/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Deskripsi penyakit/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Obat penyakit/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]


def get_details(disease):
    return d_desc_map[disease]


def get_treatments(disease):
    return d_treatment_map[disease]


def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("Kemungkinan penyakit yang kamu miliki adalah %s\n" % id_disease)

    print("Sedikit deskripsi tentang penyakit yang diberikan :")
    print(disease_details + "\n")
    print("Pengobatan umum dan prosedur yang disarankan adalah :")
    print(treatments + "\n")

    plt.imshow(mpimg.imread("./img/" + id_disease + ".jpg"))
    plt.title(id_disease)
    plt.axis('off')
    plt.show()



class Greetings(experta.KnowledgeEngine):
    @experta.DefFacts()
    def _initial_action(self):
        print("")
        print("Halo! Saya adalah Dok-bot, Saya akan mendiagnosa penyakit tanaman melon anda dengan metode forward!")
        print("Oleh karena itu anda harus menjawab beberapa gejala yang anda alami")
        print("Apakah anda merasakan beberapa gejala dibawah ini(yes/no):")
        print("")
        yield experta.Fact(action="find_disease")

    # Gejala
    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah=experta.W())), salience=1)
    def symptom_0(self):
        self.declare(experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah=input("Apakah semai busuk sebelum atau sesudah muncul dari tanah?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil=experta.W())), salience=1)
    def symptom_1(self):
        self.declare(experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil=input("Apakah tanaman tumbuh menjadi tanaman kerdil?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_terlihat_pucat=experta.W())), salience=1)
    def symptom_2(self):
        self.declare(experta.Fact(Daun_terlihat_pucat=input("Apakah daun terlihat pucat?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Bagian_atas_daun_terlihat_layu=experta.W())), salience=1)
    def symptom_3(self):
        self.declare(experta.Fact(Bagian_atas_daun_terlihat_layu=input("Apakah bagian atas daun terlihat layu?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Tanaman_layu_dan_mati=experta.W())), salience=1)
    def symptom_4(self):
        self.declare(experta.Fact(Tanaman_layu_dan_mati=input("Apakah tanaman layu dan mati?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Batang_terdapat_coreng_kecoklatan=experta.W())), salience=1)
    def symptom_5(self):
        self.declare(experta.Fact(Batang_terdapat_coreng_kecoklatan=input("Apakah batang terdapat coreng kecoklatan?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Batang_memiliki_massa_spora_merah_jambu=experta.W())), salience=1)
    def symptom_6(self):
        self.declare(experta.Fact(Batang_memiliki_massa_spora_merah_jambu=input("Apakah batang memiliki massa spora merah jambu?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat=experta.W())), salience=1)
    def symptom_7(self):
        self.declare(experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat=input("Apakah batang terlihat pecah mengeluarkan cairan berwarna cokelat?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat=experta.W())), salience=1)
    def symptom_8(self):
        self.declare(experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat=input("Apakah jika batang dibelah tampak bagian kayu dari batang berwarna cokelat?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan=experta.W())), salience=1)
    def symptom_9(self):
        self.declare(experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan=input("Apakah bagian bawah daun terdapat bercak agak bulat keputihan?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan=experta.W())), salience=1)
    def symptom_10(self):
        self.declare(experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan=input("Apakah batang terdapat bercak coreng kecoklatan?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan=experta.W())), salience=1)
    def symptom_11(self):
        self.declare(experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan=input("Apakah bagian atas daun terdapat bercak bulat keputihan?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih=experta.W())), salience=1)
    def symptom_12(self):
        self.declare(experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih=input("Apakah seluruh daun tampak dilapisi tepung putih?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning=experta.W())), salience=1)
    def symptom_13(self):
        self.declare(experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning=input("Apakah bagian atas daun terdapat bercak kuning?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan=experta.W())), salience=1)
    def symptom_14(self):
        self.declare(experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan=input("Apakah pada cuaca lembab, sisi bawah bercak terdapat jamur berbulu berwarna keunguan atau keabuan?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_terlihat_menjadi_coklat=experta.W())), salience=1)
    def symptom_15(self):
        self.declare(experta.Fact(Daun_terlihat_menjadi_coklat=input("Apakah daun terlihat menjadi coklat?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_terlihat_mengeriput=experta.W())), salience=1)
    def symptom_16(self):
        self.declare(experta.Fact(Daun_terlihat_mengeriput=input("Apakah daun terlihat mengeriput?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda=experta.W())), salience=1)
    def symptom_17(self):
        self.declare(experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda=input("Apakah daun terdapat bercak bulat berwarna coklat muda?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan=experta.W())), salience=1)
    def symptom_18(self):
        self.declare(experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan=input("Apakah daun terdapat bercak coklat tua kemerahan?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering=experta.W())), salience=1)
    def symptom_19(self):
        self.declare(experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering=input("Apakah bercak coklat tua kemerahan pada daun meluas, saling berhubungan sehingga daun mengering?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat=experta.W())), salience=1)
    def symptom_20(self):
        self.declare(experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat=input("Apakah batang atau tangkai terdapat daun dengan bercak sempit memanjang, kebasahan, mengendap berwarna kuning atau coklat?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm=experta.W())), salience=1)
    def symptom_21(self):
        self.declare(experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm=input("Apakah pada buah yang masih muda terdapat bercak melekuk (mengendap) dalam, garis tengahnya dapat mencapai 1 cm?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet=experta.W())), salience=1)
    def symptom_22(self):
        self.declare(experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet=input("Apakah pada tepi buah mengeluarkan cairan yang mengering seperti karet?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan=experta.W())), salience=1)
    def symptom_23(self):
        self.declare(experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan=input("Apakah pada bercak di buah terbentuk spora patogen berwarna hijau kecoklatan?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus=experta.W())), salience=1)
    def symptom_24(self):
        self.declare(experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus=input("Apakah pada buah yang lebih tua terdapat kudis coklat yang bergabus?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat=experta.W())), salience=1)
    def symptom_25(self):
        self.declare(experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat=input("Apakah daun terdapat bercak kuning kecil bersudut, pada bagian bawah mengeluarkan eksudat berwarna cokelat?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu=experta.W())), salience=1)
    def symptom_26(self):
        self.declare(experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu=input("Apakah daun terdapat bercak coklat muda kelabu?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Bercak_di_daun_berlubang=experta.W())), salience=1)
    def symptom_27(self):
        self.declare(experta.Fact(Bercak_di_daun_berlubang=input("Apakah bercak di daun berlubang?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah=experta.W())), salience=1)
    def symptom_28(self):
        self.declare(experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah=input("Apakah pada buah terjadi pembusukan yang masuk sampai ke dalam daging buah?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati=experta.W())), salience=1)
    def symptom_29(self):
        self.declare(experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati=input("Apakah daun layu tetapi warna daun tetap hijau kemudian semua daun layu dan mati?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket=experta.W())), salience=1)
    def symptom_30(self):
        self.declare(experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket=input("Apakah batang layu, jika dipotong akan mengeluarkan lendir bakteri berwarna putih kental dan lengket?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut=experta.W())), salience=1)
    def symptom_31(self):
        self.declare(experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut=input("Apakah pada buah terdapat bercak kebasahan dan lunak berwarna coklat yang pada akhirnya bercak mengendap dan berkerut?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan=experta.W())), salience=1)
    def symptom_32(self):
        self.declare(experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan=input("Apakah pada buah terdapat bercak kebasahan, lunak, lembek dan akan pecah jika sedikit ditekan?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat=experta.W())), salience=1)
    def symptom_33(self):
        self.declare(experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat=input("Apakah pada bagian buah yang busuk terbentuk miselium yang hebat?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak=experta.W())), salience=1)
    def symptom_34(self):
        self.declare(experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak=input("Apakah daun mengalami kloris (perubahan warna menjadi menguning) tanpa adanya bercak?: ")))

    @experta.Rule(experta.Fact(action='find_disease'), experta.NOT(experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya=experta.W())), salience=1)
    def symptom_35(self):
        self.declare(experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya=input("Apakah daun mengalami perubahan bentuk (daun menjadi kriting dan lebih kecil dari biasanya)?: ")))



    @experta.Rule(experta.Fact(action='find_disease'), experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="yes"), experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"), experta.Fact(Bagian_atas_daun_terlihat_layu="yes"), experta.Fact(Tanaman_layu_dan_mati="yes"), experta.Fact(Batang_terdapat_coreng_kecoklatan="yes"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="yes"), experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="yes"), experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="yes"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"), experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"), experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"), experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="no"), experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"), experta.Fact(Daun_terlihat_menjadi_coklat="no"),
                  experta.Fact(Daun_terlihat_mengeriput="no"), experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"), experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"), experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"), experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="no"), experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"), experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"), experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="no"), experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"), experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="no"), experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="yes"), experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="no"), experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="no"), experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"), experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Layu Fusarium"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="no"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="yes"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="yes"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="yes"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="yes"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="no"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="no"),
                  experta.Fact(Daun_terlihat_mengeriput="no"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="no"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="no"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="no"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="no"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Embun Tepung"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="no"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="yes"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="yes"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="yes"),
                  experta.Fact(Daun_terlihat_mengeriput="yes"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="no"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="yes"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="no"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="no"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="no"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Busuk Daun"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="no"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="no"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="no"),
                  experta.Fact(Daun_terlihat_mengeriput="no"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="yes"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="yes"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="yes"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="yes"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="yes"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="yes"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="no"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="no"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Antraknos"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="no"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="no"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="no"),
                  experta.Fact(Daun_terlihat_mengeriput="no"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="yes"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="yes"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="yes"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="yes"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="no"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="no"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="no"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Kudis"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="no"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="yes"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="yes"),
                  experta.Fact(Daun_terlihat_mengeriput="yes"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="no"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="yes"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="yes"),
                  experta.Fact(Bercak_di_daun_berlubang="yes"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="yes"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="no"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="no"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Bercak Daun Bersudut"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="yes"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="no"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="no"),
                  experta.Fact(Daun_terlihat_mengeriput="no"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="no"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="no"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="yes"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="yes"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="no"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Layu Bakteri"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="no"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="no"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="no"),
                  experta.Fact(Daun_terlihat_mengeriput="no"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="yes"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="yes"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="no"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="yes"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="yes"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Busuk Phytophthora"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="no"),
                  experta.Fact(Daun_terlihat_pucat="no"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="no"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="no"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="no"),
                  experta.Fact(Daun_terlihat_mengeriput="no"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="yes"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="yes"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="no"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="yes"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="yes"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="yes"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="no"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="no"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Busuk Pythium"))

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah="no"),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil="yes"),
                  experta.Fact(Daun_terlihat_pucat="yes"),
                  experta.Fact(Bagian_atas_daun_terlihat_layu="no"),
                  experta.Fact(Tanaman_layu_dan_mati="no"),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan="no"),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu="no"),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat="no"),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat="no"),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan="no"),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan="no"),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih="no"),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning="no"),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan="no"),
                  experta.Fact(Daun_terlihat_menjadi_coklat="no"),
                  experta.Fact(Daun_terlihat_mengeriput="no"),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan="no"),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering="no"),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat="no"),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm="no"),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet="no"),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan="no"),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus="no"),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat="no"),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu="no"),
                  experta.Fact(Bercak_di_daun_berlubang="no"),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah="no"),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati="no"),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut="no"),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan="no"),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat="no"),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak="yes"),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya="yes"))
    def disease_0(self):
        self.declare(experta.Fact(disease="Mosaik"))



    @experta.Rule(experta.Fact(action='find_disease'), experta.Fact(disease=experta.MATCH.disease), salience=-998)
    def disease(self, disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("Kemungkinan terbesar tanaman anda mengalami penyakit %s\n" % id_disease)

        plt.imshow(mpimg.imread("./img/" + id_disease + ".jpg"))
        plt.title(id_disease)
        plt.axis('off')
        plt.show()

        print("Berikut deskripsi singkat dari penyakit yang diberikan :")
        print(disease_details + "\n")
        print("Beberapa pengobatan yang disarankan :")
        print(treatments + "\n")

    @experta.Rule(experta.Fact(action='find_disease'),
                  experta.Fact(semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah=experta.MATCH.semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah),
                  experta.Fact(Tanaman_tumbuh_menjadi_tanaman_kerdil=experta.MATCH.Tanaman_tumbuh_menjadi_tanaman_kerdil),
                  experta.Fact(Daun_terlihat_pucat=experta.MATCH.Daun_terlihat_pucat),
                  experta.Fact(Bagian_atas_daun_terlihat_layu=experta.MATCH.Bagian_atas_daun_terlihat_layu),
                  experta.Fact(Tanaman_layu_dan_mati=experta.MATCH.Tanaman_layu_dan_mati),
                  experta.Fact(Batang_terdapat_coreng_kecoklatan=experta.MATCH.Batang_terdapat_coreng_kecoklatan),
                  experta.Fact(Batang_memiliki_massa_spora_merah_jambu=experta.MATCH.Batang_memiliki_massa_spora_merah_jambu),
                  experta.Fact(Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat=experta.MATCH.Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat),
                  experta.Fact(Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat=experta.MATCH.Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat),
                  experta.Fact(Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan=experta.MATCH.Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan),
                  experta.Fact(Batang_terdapat_bercak_coreng_kecoklatan=experta.MATCH.Batang_terdapat_bercak_coreng_kecoklatan),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_bulat_keputihan=experta.MATCH.Bagian_atas_daun_terdapat_bercak_bulat_keputihan),
                  experta.Fact(Seluruh_daun_tampak_dilapisi_tepung_putih=experta.MATCH.Seluruh_daun_tampak_dilapisi_tepung_putih),
                  experta.Fact(Bagian_atas_daun_terdapat_bercak_kuning=experta.MATCH.Bagian_atas_daun_terdapat_bercak_kuning),
                  experta.Fact(Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan=experta.MATCH.Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan),
                  experta.Fact(Daun_terlihat_menjadi_coklat=experta.MATCH.Daun_terlihat_menjadi_coklat),
                  experta.Fact(Daun_terlihat_mengeriput=experta.MATCH.Daun_terlihat_mengeriput),
                  experta.Fact(Daun_terdapat_bercak_bulat_berwarna_coklat_muda=experta.MATCH.Daun_terdapat_bercak_bulat_berwarna_coklat_muda),
                  experta.Fact(Daun_terdapat_bercak_coklat_tua_kemerahan=experta.MATCH.Daun_terdapat_bercak_coklat_tua_kemerahan),
                  experta.Fact(Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering=experta.MATCH.Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering),
                  experta.Fact(Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat=experta.MATCH.Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat),
                  experta.Fact(Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm=experta.MATCH.Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm),
                  experta.Fact(Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet=experta.MATCH.Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet),
                  experta.Fact(Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan=experta.MATCH.Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan),
                  experta.Fact(Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus=experta.MATCH.Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus),
                  experta.Fact(Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat=experta.MATCH.Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat),
                  experta.Fact(Daun_terdapat_bercak_coklat_muda_kelabu=experta.MATCH.Daun_terdapat_bercak_coklat_muda_kelabu),
                  experta.Fact(Bercak_di_daun_berlubang=experta.MATCH.Bercak_di_daun_berlubang),
                  experta.Fact(Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah=experta.MATCH.Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah),
                  experta.Fact(Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati=experta.MATCH.Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati),
                  experta.Fact(Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket=experta.MATCH.Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut=experta.MATCH.Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut),
                  experta.Fact(Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan=experta.MATCH.Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan),
                  experta.Fact(Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat=experta.MATCH.Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat),
                  experta.Fact(Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak=experta.MATCH.Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak),
                  experta.Fact(Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya=experta.MATCH.Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya),

                  experta.NOT(experta.Fact(disease=experta.MATCH.disease)), salience=-999)
    def not_matched(self, semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah,
                    Tanaman_tumbuh_menjadi_tanaman_kerdil,
                    Daun_terlihat_pucat,
                    Bagian_atas_daun_terlihat_layu,
                    Tanaman_layu_dan_mati,
                    Batang_terdapat_coreng_kecoklatan,
                    Batang_memiliki_massa_spora_merah_jambu,
                    Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat,
                    Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat,
                    Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan,
                    Batang_terdapat_bercak_coreng_kecoklatan,
                    Bagian_atas_daun_terdapat_bercak_bulat_keputihan,
                    Seluruh_daun_tampak_dilapisi_tepung_putih,
                    Bagian_atas_daun_terdapat_bercak_kuning,
                    Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan,
                    Daun_terlihat_menjadi_coklat,
                    Daun_terlihat_mengeriput,
                    Daun_terdapat_bercak_bulat_berwarna_coklat_muda,
                    Daun_terdapat_bercak_coklat_tua_kemerahan,
                    Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering,
                    Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat,
                    Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm,
                    Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet,
                    Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan,
                    Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus,
                    Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat,
                    Daun_terdapat_bercak_coklat_muda_kelabu,
                    Bercak_di_daun_berlubang,
                    Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah,
                    Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati,
                    Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket,
                    Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut,
                    Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan,
                    Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat,
                    Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak,
                    Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya):
        print("\nTidak menemukan penyakit yang sangat pas dengan gejala yang anda alami")
        lis = [semai_busuk_sebelum_atau_sesudah_muncul_dari_tanah,
                    Tanaman_tumbuh_menjadi_tanaman_kerdil,
                    Daun_terlihat_pucat,
                    Bagian_atas_daun_terlihat_layu,
                    Tanaman_layu_dan_mati,
                    Batang_terdapat_coreng_kecoklatan,
                    Batang_memiliki_massa_spora_merah_jambu,
                    Batang_terlihat_pecah_mengeluarkan_cairan_berwarna_cokelat,
                    Jika_batang_dibelah_tampak_bagian_kayu_dari_batang_berwarna_cokelat,
                    Bagian_bawah_daun_terdapat_bercak_agak_bulat_keputihan,
                    Batang_terdapat_bercak_coreng_kecoklatan,
                    Bagian_atas_daun_terdapat_bercak_bulat_keputihan,
                    Seluruh_daun_tampak_dilapisi_tepung_putih,
                    Bagian_atas_daun_terdapat_bercak_kuning,
                    Pada_cuaca_lembab_sisi_bawah_bercak_terdapat_jamur_berbulu_berwarna_keunguan_atau_keabuan,
                    Daun_terlihat_menjadi_coklat,
                    Daun_terlihat_mengeriput,
                    Daun_terdapat_bercak_bulat_berwarna_coklat_muda,
                    Daun_terdapat_bercak_coklat_tua_kemerahan,
                    Bercak_coklat_tua_kemerahan_pada_daun_meluas_saling_berhubungan_sehingga_daun_mengering,
                    Batang_atau_tangkai_terdapat_daun_terdapat_bercak_sempit_memanjang_kebasahan_mengendap_berwarna_kuning_atau_coklat,
                    Pada_buah_yang_masih_muda_terdapat_bercak_melekuk_mengendap_dalam_garis_tengahnya_dapat_mencapai_1_cm,
                    Pada_tepi_buah_mengeluarkan_cairan_yang_mengering_seperti_karet,
                    Pada_bercak_di_buah_terbentuk_spora_patogen_berwarna_hijau_kecoklatan,
                    Pada_buah_yang_lebih_tua_terdapat_kudis_coklat_yang_bergabus,
                    Daun_terdapat_bercak_kuning_kecil_bersudut_pada_bagian_bawah_mengeluarkan_eksudat_berwarna_cokelat,
                    Daun_terdapat_bercak_coklat_muda_kelabu,
                    Bercak_di_daun_berlubang,
                    Pada_buah_terjadi_pembusukan_yang_masuk_sampai_ke_dalam_daging_buah,
                    Daun_layu_tetapi_warna_daun_tetap_hijau_kemudian_semua_daun_layu_dan_mati,
                    Batang_layu_jika_dipotong_akan_mengeluarkan_lendir_bakteri_berwarna_putih_kental_dan_lengket,
                    Pada_buah_terdapat_bercak_kebasahan_dan_lunak_berwarna_coklat_yang_pada_akhirnya_bercak_mengendap_dan_berkerut,
                    Pada_buah_terdapat_bercak_kebasahan_lunak_lembek_dan_akan_pecah_jika_sedikit_ditekan,
                    Pada_bagian_buah_yang_busuk_terbentuk_miselium_yang_hebat,
                    Daun_mengalami_kloris_perubahan_warna_menjadi_menguning_tanpa_adanya_bercak,
                    Daun_mengalami_perubahan_bentuk_daun_menjadi_kriting_dan_lebih_kecil_dari_biasanya]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and lis[j] == "yes":
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)


if __name__ == "__main__":
    preprocess()
    engine = Greetings()
    while 1:
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Ingin mencoba diagnosa dengan gejala yang lain?")
        if input() == "no":
            exit()
    # print(engine.facts)
