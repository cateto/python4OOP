from duck import Duck

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")

drake.quack()
print(duckling.height)

setattr(duckling, 'height', 50)
print(getattr(duckling, 'height'))