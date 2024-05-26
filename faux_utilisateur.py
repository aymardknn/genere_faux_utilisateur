from faker import Faker
from faker.providers import internet

def create_user(user):
    fake = Faker()
    fake.add_provider(internet)
    user_data = []

    for _ in range(user):
        my_user = {
            "Nom": fake.name(),
            "Né(e) le": fake.date_of_birth(),
            "Email": fake.free_email(),
            "Telephone": fake.phone_number(),
            "Pays": fake.country(),
            "Ville": fake.city(),
            "Profession": fake.job(),
            "Carte de crédit": fake.credit_card_number(),
            "Code securité de la carte": fake.random_int(min=100, max=999)


        }

        user_data.append(my_user)

    return user_data


def lectureDesDonnées(data, filname):
    with open(filname ,'w') as output_file:
        for my_user in data:
            for key, Value in my_user.items():
                output_file.write(f'{key}: {Value}\n')

            output_file.write('\n')


    print(f"Sauvegarder effectué sous le nom de {filname}")


nombre_de_generation = int(input('Combien de user voulez-vous générer ?\n'))
user_data = create_user(nombre_de_generation)
sauvegarde = input('Voulez-vous faire une sauvegarde ? \n')

if sauvegarde == 'oui':
    nom_du_fichier = input("Entrez le nom du fichier de sauvegarde (sans extension)\n")
    fichier = f'{nom_du_fichier}.txt'
    lectureDesDonnées(user_data, fichier)

else:
    print(user_data)