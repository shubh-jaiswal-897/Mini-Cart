import os
import django
import random
from faker import Faker

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomerce.settings')
django.setup()

from home.models import Products

fake = Faker()

# Product data templates
SMARTPHONE_BRANDS = ['Samsung', 'Apple', 'OnePlus', 'Xiaomi', 'Google', 'Sony', 'Huawei', 'Oppo', 'Vivo', 'Realme', 'Poco', 'Motorola', 'Nokia', 'Asus', 'Lenovo']
LAPTOP_BRANDS = ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'MSI', 'Apple', 'Samsung', 'Sony', 'Toshiba', 'Microsoft', 'Razer', 'Alienware', 'LG']
SMARTWATCH_BRANDS = ['Samsung', 'Apple', 'Garmin', 'Fitbit', 'Huawei', 'Xiaomi', 'OnePlus', 'Fossil', 'TicWatch', 'Amazfit', 'Realme', 'Noise', 'Boat']
EARPHONE_BRANDS = ['Sony', 'Samsung', 'Apple', 'JBL', 'Bose', 'Sennheiser', 'Boat', 'OnePlus', 'Realme', 'Noise', 'Skullcandy', 'Marshall', 'Beats']

def generate_smartphone_products(count):
    products = []
    for i in range(count):
        brand = random.choice(SMARTPHONE_BRANDS)
        models = {
            'Samsung': ['Galaxy S23', 'Galaxy S22', 'Galaxy A54', 'Galaxy M34', 'Galaxy Z Fold', 'Galaxy Note 20'],
            'Apple': ['iPhone 15', 'iPhone 14', 'iPhone 13', 'iPhone SE', 'iPhone 12', 'iPhone 11'],
            'OnePlus': ['OnePlus 11', 'OnePlus 10T', 'OnePlus Nord CE', 'OnePlus 9', 'OnePlus Nord'],
            'Xiaomi': ['Mi 13', 'Redmi Note 12', 'Poco X4', 'Mi 12', 'Redmi K50', 'Poco M4'],
            'Google': ['Pixel 8', 'Pixel 7', 'Pixel 6a', 'Pixel 5', 'Pixel 4a'],
            'Sony': ['Xperia 5 IV', 'Xperia 1 IV', 'Xperia 10 IV', 'Xperia Pro-I'],
            'Huawei': ['Mate 50', 'P50', 'Mate 40', 'P40', 'Nova 10'],
            'Oppo': ['Find X5', 'Reno 8', 'A96', 'F21', 'K10'],
            'Vivo': ['X80', 'V25', 'S15', 'T1', 'Y75'],
            'Realme': ['GT Neo 3', 'Narzo 50', '9 Pro', 'C35', '10'],
            'Poco': ['X4 Pro', 'M4 Pro', 'C40', 'M3', 'X3'],
            'Motorola': ['Edge 30', 'Moto G Stylus', 'Moto G Power', 'Razr 40', 'Edge 20'],
            'Nokia': ['X30', 'G60', 'C32', 'G42', 'X20'],
            'Asus': ['Zenfone 9', 'ROG Phone 6', 'Zenfone 8', 'ROG Phone 5'],
            'Lenovo': ['Legion Phone Duel 2', 'K13 Note', 'K12 Pro']
        }

        model = random.choice(models.get(brand, [f'{brand} Model {i+1}']))
        name = f"{brand} {model}"

        descriptions = [
            f"Latest {brand} smartphone with advanced features",
            f"Powerful {model} with excellent camera and performance",
            f"Premium {brand} device with cutting-edge technology",
            f"Feature-rich {model} for modern smartphone users",
            f"High-performance {brand} smartphone with stunning display"
        ]

        price = random.randint(10000, 150000)  # Price in rupees

        product = Products(
            pro_name=name,
            pro_desc=random.choice(descriptions),
            pro_price=price,
            category='smartphone',
            pro_brand=brand,
            pro_rating=round(random.uniform(3.5, 5.0), 1),
            pro_image='uploads/demo.webp',  # Using existing demo image
            is_available=True
        )
        products.append(product)
    return products

def generate_laptop_products(count):
    products = []
    for i in range(count):
        brand = random.choice(LAPTOP_BRANDS)
        models = {
            'Dell': ['XPS 13', 'Latitude 5420', 'Inspiron 15', 'Alienware m15', 'G5 15', 'Precision 5570'],
            'HP': ['Pavilion 15', 'Envy 13', 'Spectre x360', 'Omen 16', 'EliteBook 840', 'ProBook 450'],
            'Lenovo': ['ThinkPad X1', 'IdeaPad 3', 'Yoga Slim 7', 'Legion 5', 'ThinkBook 14', 'IdeaPad Gaming 3'],
            'Asus': ['ZenBook 14', 'ROG Strix G15', 'TUF Gaming F15', 'VivoBook 15', 'ExpertBook B9450', 'Chromebook CX1'],
            'Acer': ['Aspire 5', 'Swift 3', 'Predator Helios', 'Nitro 5', 'TravelMate P2', 'Chromebook Spin 514'],
            'MSI': ['GF65 Thin', 'Sword 15', 'Prestige 14', 'Modern 14', 'Katana GF66', 'Creator Z16'],
            'Apple': ['MacBook Air M2', 'MacBook Pro 14"', 'MacBook Pro 16"', 'MacBook Air M1'],
            'Samsung': ['Galaxy Book2 Pro', 'Galaxy Book2', 'Galaxy Book Flex', 'Galaxy Book Ion'],
            'Sony': ['VAIO SX14', 'VAIO Z', 'VAIO FE14', 'VAIO S11'],
            'Toshiba': ['Portégé X30', 'Tecra A50', 'Satellite Pro', 'Dynabook'],
            'Microsoft': ['Surface Laptop 5', 'Surface Pro 8', 'Surface Book 3', 'Surface Go 3'],
            'Razer': ['Blade 15', 'Blade 14', 'Book 13', 'Blade Stealth 13'],
            'Alienware': ['m15 R6', 'x15 R2', 'm17 R4', 'Area-51m'],
            'LG': ['Gram 16', 'Gram 14', 'Gram 17', 'Ultra PC 15']
        }

        model = random.choice(models.get(brand, [f'{brand} Model {i+1}']))
        name = f"{brand} {model}"

        descriptions = [
            f"High-performance {brand} laptop for work and entertainment",
            f"Powerful {model} with latest processor and graphics",
            f"Premium {brand} laptop with excellent build quality",
            f"Versatile {model} suitable for various tasks",
            f"Advanced {brand} laptop with cutting-edge features"
        ]

        price = random.randint(30000, 300000)  # Price in rupees

        product = Products(
            pro_name=name,
            pro_desc=random.choice(descriptions),
            pro_price=price,
            category='laptops',
            pro_brand=brand,
            pro_rating=round(random.uniform(3.5, 5.0), 1),
            pro_image='uploads/macbook.webp',  # Using existing macbook image
            is_available=True
        )
        products.append(product)
    return products

def generate_smartwatch_products(count):
    products = []
    for i in range(count):
        brand = random.choice(SMARTWATCH_BRANDS)
        models = {
            'Samsung': ['Galaxy Watch 5', 'Galaxy Watch 4', 'Galaxy Watch Active 2', 'Galaxy Watch 3'],
            'Apple': ['Watch Series 8', 'Watch SE', 'Watch Series 7', 'Watch Ultra'],
            'Garmin': ['Forerunner 265', 'Venu 2', 'Fenix 7', 'Epix Pro'],
            'Fitbit': ['Sense 2', 'Versa 4', 'Charge 5', 'Luxury'],
            'Huawei': ['Watch GT 3', 'Watch GT Runner', 'Watch D', 'Watch GT 2'],
            'Xiaomi': ['Mi Watch', 'Mi Watch Lite', 'Mi Watch Revolve', 'Mi Watch Color 2'],
            'OnePlus': ['Watch', 'Watch Z'],
            'Fossil': ['Gen 6', 'Hybrid HR', 'Sport', 'Townsman'],
            'TicWatch': ['Pro 3', 'E3', 'C2', 'S2'],
            'Amazfit': ['GTR 4', 'GTS 4', 'T-Rex Pro', 'Bip U Pro'],
            'Realme': ['Watch 2 Pro', 'Watch S', 'Watch 3', 'Watch S Pro'],
            'Noise': ['ColorFit Pro 4', 'ColorFit Pro 3', 'ColorFit Pulse', 'ColorFit Brio'],
            'Boat': ['Storm', 'Xtend', 'Wave', 'Flash']
        }

        model = random.choice(models.get(brand, [f'{brand} Watch {i+1}']))
        name = f"{brand} {model}"

        descriptions = [
            f"Advanced {brand} smartwatch with health monitoring",
            f"Feature-rich {model} with fitness tracking",
            f"Premium {brand} wearable with smart features",
            f"Stylish {model} for daily fitness and notifications",
            f"High-tech {brand} smartwatch with long battery life"
        ]

        price = random.randint(2000, 50000)  # Price in rupees

        product = Products(
            pro_name=name,
            pro_desc=random.choice(descriptions),
            pro_price=price,
            category='smartwatch',
            pro_brand=brand,
            pro_rating=round(random.uniform(3.5, 5.0), 1),
            pro_image='uploads/smartwatch.jpeg',  # Using existing smartwatch image
            is_available=True
        )
        products.append(product)
    return products

def generate_earphone_products(count):
    products = []
    for i in range(count):
        brand = random.choice(EARPHONE_BRANDS)
        models = {
            'Sony': ['WH-1000XM5', 'WF-1000XM4', 'WH-CH720N', 'WF-C500', 'WI-C310'],
            'Samsung': ['Galaxy Buds2 Pro', 'Galaxy Buds Live', 'Galaxy Buds+', 'EO-EG920'],
            'Apple': ['AirPods Pro', 'AirPods 3rd Gen', 'AirPods Max', 'EarPods'],
            'JBL': ['T600NC', 'Live 400BTNC', 'Tune 600NC', 'Go 3', 'Clip 3'],
            'Bose': ['QuietComfort Earbuds II', 'Noise Cancelling Headphones 700', 'SoundSport', 'QuietComfort 35 II'],
            'Sennheiser': ['Momentum 4', 'HD 250BT', 'CX 400BT', 'IE 4', 'HD 206'],
            'Boat': ['Airdopes 131', 'Rockerz 255', 'Bassheads 100', 'Airdopes 441', 'Rockerz 450'],
            'OnePlus': ['Bullets Wireless Z2', 'Nord Buds', 'Buds Z2', 'Bullets Wireless 2'],
            'Realme': ['Buds Air 3', 'Buds Q2', 'TechLife Earbuds', 'Buds Wireless 2 Neo'],
            'Noise': ['Buds VS102', 'Air Buds', 'Buds VS201', 'Buds VS104'],
            'Skullcandy': ['Crusher ANC', 'Indy ANC', 'Push Ultra', 'Jib', 'Method'],
            'Marshall': ['Major III BT', 'Minor III', 'Woburn III', 'Stanmore II'],
            'Beats': ['Studio Buds', 'Powerbeats Pro', 'Solo Pro', 'Flex']
        }

        model = random.choice(models.get(brand, [f'{brand} Model {i+1}']))
        name = f"{brand} {model}"

        descriptions = [
            f"Premium {brand} wireless earphones with excellent sound",
            f"High-quality {model} with noise cancellation",
            f"Comfortable {brand} earbuds for music lovers",
            f"Advanced {model} with superior audio performance",
            f"Stylish {brand} wireless headphones with long battery"
        ]

        price = random.randint(500, 30000)  # Price in rupees

        product = Products(
            pro_name=name,
            pro_desc=random.choice(descriptions),
            pro_price=price,
            category='earphones',
            pro_brand=brand,
            pro_rating=round(random.uniform(3.5, 5.0), 1),
            pro_image='uploads/boult1.webp',  # Using existing boult image
            is_available=True
        )
        products.append(product)
    return products

def add_products():
    print("Starting to add 1000 products...")

    # Clear existing products
    Products.objects.all().delete()
    print("Cleared existing products")

    # Generate products for each category
    smartphones = generate_smartphone_products(400)  # 40% smartphones
    laptops = generate_laptop_products(300)         # 30% laptops
    smartwatches = generate_smartwatch_products(150) # 15% smartwatches
    earphones = generate_earphone_products(150)     # 15% earphones

    all_products = smartphones + laptops + smartwatches + earphones

    # Bulk create products
    Products.objects.bulk_create(all_products)
    print(f"Successfully added {len(all_products)} products!")

    # Print category counts
    smartphone_count = Products.objects.filter(category='smartphone').count()
    laptop_count = Products.objects.filter(category='laptops').count()
    smartwatch_count = Products.objects.filter(category='smartwatch').count()
    earphone_count = Products.objects.filter(category='earphones').count()

    print("\nProduct distribution:")
    print(f"Smartphones: {smartphone_count}")
    print(f"Laptops: {laptop_count}")
    print(f"Smartwatches: {smartwatch_count}")
    print(f"Earphones: {earphone_count}")
    print(f"Total: {smartphone_count + laptop_count + smartwatch_count + earphone_count}")

if __name__ == '__main__':
    add_products()
