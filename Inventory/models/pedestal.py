from django.db import models

Brands = (
        (0,'Unknown'),
        (1,'Herman Miller'),
        (2,'Steelcase'),
        (3,'Teknion'),
        (4,'Haworth'),   
        (5,'Knoll'),
        (6,'Wilkhahn'),
        (7,'Benel'),
        (8,'Fusys'),
        (9,'Humanscale'),
        (10,'Enjoy'),
        (11,'Ergohuman'),
        (12,'Artmatrix'),
        (13,'X3'),
        (14,'Unigroup'),
        
)

Warehouses = (
        (1,'E9 Premium, #06-17'),
        (2,'Hiangkie Industrial Building, #04-14'),
        (3,'Mayfair Industrial Building, #05-30'),   
)

# Create your models here.
class Pedestal(models.Model):
    class Meta:
        db_table = 'Pedestals'


    Colors = (
        (1,'Maple'),
        (2,'White'),
        (3,'Grey'),
        (4,'Cherry'),   
        (5,'Brown'),
        (6,'Beech'),
        (7,'Ivory'),
        (8,'Black'),

    )

    Wheels_Options = (
        (1,'No wheels'),
        (2,'4 wheels'),
        (3,'5 wheels'),        
    )
    Handles_Options = (
        (1,'With handle'),
        (2,'No Handle'),
    )
    Drawers = (
        (1,'2 Drawers'),
        (2,'2D1F'),
        (3,'3 Small Drawers')       
    )
    Materials = (
        (1,'Wooden'),
        (2,'Metal'),
    )
    #仓库号
    Warehouse_Code = models.IntegerField(
        choices=Warehouses,
        default=0
    )

    #区号
    Area_Code = models.IntegerField(
        default=0
    )


    #照片
    Image = models.CharField(
        max_length = 200,
        default=""
    )
    #牌子
    Brand = models.IntegerField(
        choices=Brands,
        default=0
    )

    # Color
    Color = models.IntegerField(choices=Colors,default=1)
    
    # Material

    Material = models.IntegerField(choices=Materials,default=1)

    # Drawer
    Drawer = models.IntegerField(choices=Drawers,default=1)

    # Measurements
    Height = models.IntegerField()
    Width = models.IntegerField()
    Depth = models.IntegerField()

    Wheel = models.IntegerField(choices=Wheels_Options,default=1)
    Handle = models.IntegerField(choices=Handles_Options,default=1)

    #是否有问题
    Is_Faulty = models.BooleanField(default=False)
    Description = models.TextField(
        max_length = 500,
        default=""
    )
    #Qty
    Quantity_For_This_Entry = models.IntegerField(
        
    )

    #Custom Code
    Custom_Code = models.CharField(
        max_length = 20,
        default=""
    )
