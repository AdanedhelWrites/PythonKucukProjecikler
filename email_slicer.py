print("Hello welcome to emailSlicer")

email = input("Enter your email address:").strip()

kullanici_adi = email[:email.index("@")]

domain = email[email.index("@")+1:]

sonuc = "Sizin email kullanıcı adınız: {}.Domaininiz ise: {}'dır".format(kullanici_adi, domain)
print(sonuc)