import pandas as pd

data = {
    "Brand" : ["Espressolab", "D&R", "Watsons", "Mavi", "Kırmızı Kedi"],
    "Boycott_Status" : ["Boycotted", "Boycotted", "Boycotted", "Not Boycotted", "Not Boycotted"],
    "Reason" : ["The partners are all realted to the former pro-government Mayor of Beyoğlu, Kadir Topbaş.", "Owned by Turkuvaz Media Group, which also owns 'A Haber' and 'Sabah Newspaper' both of which are pro-government and did not adequetly reflect news of İmamoğlu's arrest.", "Conducted a strip-search on suspicion of theft which is against human rights.", "Owned by the Akarlılar family with no ties to the government.", "Announced support for the April 2 national boycott and stopped businness on the day."],
    "Citation" : ["https://www.wald.org.tr/tr/kurullar/mutevelli-heyeti/mimar-dr-kadir-topbas", "https://www.aydinlik.com.tr/haber/dr-neden-chp-boykot-listesinde-dr-kimin-iste-yaniti-516973", "https://140journos.com/ma%C4%9Fazas%C4%B1nda-h%C4%B1rs%C4%B1zl%C4%B1k-yapt%C4%B1%C4%9F%C4%B1-belirtilen-%C3%A7ocu%C4%9Fa-%C3%A7%C4%B1plak-arama-yap%C4%B1ld%C4%B1%C4%9F%C4%B1-s%C3%B6ylendi-90875a453565", "https://www.mavicompany.com/tr/yonetim/yonetim-kurulu", "https://sonsoz.com.tr/kirmizi-kedi-yayinevi-satis-yapmayacak"]
}

df = pd.DataFrame(data)

df.to_csv("boycott_reasons.csv", index=False)