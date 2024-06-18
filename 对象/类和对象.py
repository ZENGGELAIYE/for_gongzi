class Clock(): # 创建类
    name = None
    price = None
    def bee(self):
        import winsound
        winsound.Beep(2000,3000)

clock1 = Clock() # 创建对象
clock1.name = "牛逼牌闹钟"
clock1.price = 20.12
print(f"我是：{clock1.name}，我的价格是：{clock1.price}")
clock1.bee()