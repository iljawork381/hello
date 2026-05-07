import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 12)
ax.set_aspect('equal')
ax.axis('off')

# Цвета
beer_color = '#F4A460'  # Янтарный цвет пива
foam_color = '#FFFFF0'  # Цвет пены
glass_color = '#E0F7FA'  # Цвет стекла
handle_color = '#B0BEC5'  # Цвет ручки

# Рисуем тело кувшина (основной цилиндр)
mug_body = patches.Rectangle((-2, 0), 4, 9, linewidth=3, 
                              edgecolor='#90A4AE', facecolor=glass_color, 
                              alpha=0.6, label='Стекло')
ax.add_patch(mug_body)

# Рисуем пиво внутри
beer_level = 7.5
beer = patches.Rectangle((-1.8, 0), 3.6, beer_level, 
                         linewidth=0, facecolor=beer_color, alpha=0.8, label='Пиво')
ax.add_patch(beer)

# Рисуем пену сверху
foam_height = 1.2
foam = patches.Rectangle((-1.9, beer_level), 3.8, foam_height, 
                         linewidth=0, facecolor=foam_color, alpha=0.95, label='Пена')
ax.add_patch(foam)

# Добавляем пузырьки в пиво
np.random.seed(42)
for _ in range(50):
    x = np.random.uniform(-1.5, 1.5)
    y = np.random.uniform(0.5, beer_level - 0.5)
    size = np.random.uniform(0.05, 0.15)
    bubble = patches.Circle((x, y), size, color='#FFD700', alpha=0.6)
    ax.add_patch(bubble)

# Рисуем ручку кувшина (полуовал справа)
handle_x = 2.0
handle_y = 3.5
handle_width = 1.2
handle_height = 5.0

# Создаем путь для ручки
theta = np.linspace(-np.pi/2, np.pi/2, 100)
handle_outer_x = handle_x + handle_width * np.cos(theta)
handle_outer_y = handle_y + handle_height/2 + handle_height/2 * np.sin(theta)

handle_inner_x = handle_x + (handle_width - 0.3) * np.cos(theta)
handle_inner_y = handle_y + handle_height/2 + (handle_height/2 - 0.3) * np.sin(theta)

# Рисуем внешнюю и внутреннюю часть ручки
ax.plot(handle_outer_x, handle_outer_y, color='#90A4AE', linewidth=8, alpha=0.7)
ax.plot(handle_inner_x, handle_inner_y, color=glass_color, linewidth=6, alpha=0.9)

# Добавляем ободок сверху
rim = patches.Ellipse((0, 9), 4.2, 0.3, linewidth=3, 
                      edgecolor='#90A4AE', facecolor='none', alpha=0.8)
ax.add_patch(rim)

# Добавляем дно
bottom = patches.Ellipse((0, 0), 3.8, 0.3, linewidth=2, 
                         edgecolor='#78909C', facecolor='#B0BEC5', alpha=0.5)
ax.add_patch(bottom)

# Добавляем блики на стекле
highlight1 = patches.Rectangle((-1.9, 2), 0.3, 5, 
                               linewidth=0, facecolor='white', alpha=0.4)
ax.add_patch(highlight1)

highlight2 = patches.Rectangle((1.6, 4), 0.2, 3, 
                               linewidth=0, facecolor='white', alpha=0.3)
ax.add_patch(highlight2)

# Заголовок
plt.title('Кувшин с пивом 🍺', fontsize=20, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('/workspace/beer_mug.png', dpi=150, bbox_inches='tight')
plt.show()

print("Изображение сохранено как beer_mug.png")
