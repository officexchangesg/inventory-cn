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
        
)

SpecificModels = (
        (0,'Unknown'),
        (1,'Herman Miller Aeron'),
        (2,'Vitra T Chair'),
        (3,'Benel EE'),
        (4,'Benel Freniq'),   
        (5,'Knoll Life'),
        (6,'Haworth Look'),
        (7,'Vitra Meda 2'),
        (8,'Fusys Pion'),
        (9,'Humanscale'),
        (10,'Steelcase Leap V1'),
        (11,'Steelcase Leap V2'),
        (12,'Steelcase Sensor'),
        (13,'Herman Miller Eames'),
        (14,'Benel Q-Mesh'),
        (15,'Steelcase Think 3D'),
        (16,'Enjoy'),
        (17,'Ergohuman'),
        (18,'Herman Miller Mirra 2'),
        (19,'Haworth Easy'),
        (20,'Haworth Zody'),
        (21,'Wilkhahn ON Task'),


)

Warehouses = (
        (1,'E9 Premium, #06-17'),
        (2,'Hiangkie Industrial Building, #04-14'),
        (3,'Mayfair Industrial Building, #05-30'),   
)

# Create your models here.
class Chair(models.Model):
    class Meta:
        db_table = 'Chairs'

    Back_N_Seat_Material = (
        (1,'Fabric'),
        (2,'Mesh'),
        (3,'Leather'),
        (4,'Wooden'),
    )
    Back_N_Seat_Color = (
        (1,'Black'),
        (2,'White'),
        (3,'Grey'),
        (4,'Red'),   
        (5,'Orange'),
        (6,'Yellow'),
        (7,'Green'),
        (8,'Blue'),
        (9,'Purple'),
        (10,'Brown'),

    )
    Leg_Material = (
        (1,'Metal or Alloy'),
        (2,'Wooden'),
        (3,'Nylon or plastic'),  
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
    #型号
    Specific_Model = models.IntegerField(

        choices=SpecificModels,
        default=""
    )

    # 椅背
    Back_Material = models.IntegerField(choices=Back_N_Seat_Material,default=0)
    Back_Color = models.IntegerField(choices=Back_N_Seat_Color,default=0)

    #坐垫
    Cushion_Material = models.IntegerField(choices=Back_N_Seat_Material,default=0)
    Cushion_Color = models.IntegerField(choices=Back_N_Seat_Color,default=0)

    #功能
    With_Lumbar_Support = models.BooleanField(default=False)
    With_Recline = models.BooleanField(default=True)
    With_MultiLock = models.BooleanField(default=False)
    With_Seat_Depth_Adjustment = models.BooleanField(default=False)
    With_Back_Height_Adjustment = models.BooleanField(default=False)
    With_Headrest = models.BooleanField(default=False)
    With_Gaslift_Adjustable = models.BooleanField(default=True)

    Armrest_Height_Adjustment = models.BooleanField(default=False)
    Armrest_Direction_Adjustment = models.BooleanField(default=False)

    #脚
    Leg_Material = models.IntegerField(choices=Leg_Material,default=0)
    Leg_Color = models.IntegerField(choices=Back_N_Seat_Color,default=0)

    #是否有问题
    Is_Faulty = models.BooleanField(default=False)
    Faulty_Description = models.TextField(
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
