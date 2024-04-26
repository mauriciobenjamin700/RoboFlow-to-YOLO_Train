# Tutorial: Convertendo Coordenadas Poligonais para Formato YOLO

**Objetivo:** Converter coordenadas poligonais que definem objetos em imagens para o formato YOLO, compatível com o framework YOLOv8.

**Pré-requisitos:**

- Ter as coordenadas poligonais dos seus objetos anotadas em pares de valores (x, y) para cada ponto do polígono.
- Saber o tamanho das suas imagens (por exemplo, 640x640 pixels).
- Ter o Python instalado em seu computador.

**Passos a Seguir:**

**1. Definindo a Função de Conversão:**

```python
def convert_polygon_to_yolo(polygon, image_width, image_height):
    """
    Converte coordenadas poligonais para o formato YOLO.

    Args:
        polygon (list): Lista de pares de coordenadas (x, y) para cada ponto do polígono.
        image_width (int): Largura da imagem em pixels.
        image_height (int): Altura da imagem em pixels.

    Returns:
        list: Coordenadas no formato YOLO [x_min, y_min, x_max, y_max].
    """

    x_min = min(point[0] for point in polygon)
    y_min = min(point[1] for point in polygon)
    x_max = max(point[0] for point in polygon)
    y_max = max(point[1] for point in polygon)

    # Normalização para o tamanho da imagem
    x_min_norm = x_min / image_width
    y_min_norm = y_min / image_height
    x_max_norm = x_max / image_width
    y_max_norm = y_max / image_height

    yolo_coords = [x_min_norm, y_min_norm, x_max_norm, y_max_norm]
    return yolo_coords
```

**2. Usando a Função:**

```python
# Exemplo de uso
polygon = [(0, 0.8406), (0.2956, 0.0282), (0.4942, 0.5718), (0.0746, 0.4210)]
image_width = 640  # Largura da imagem em pixels
image_height = 640  # Altura da imagem em pixels

yolo_coords = convert_polygon_to_yolo(polygon, image_width, image_height)
print(yolo_coords)  # Output: [0, 0.0044, 0.0772, 0.1313]
```

**Explicação do Código:**

- A função `convert_polygon_to_yolo` recebe como entrada uma lista de coordenadas poligonais (`polygon`) e as dimensões da imagem (`image_width` e `image_height`).
- A função calcula os valores mínimos e máximos de x e y a partir dos pontos do polígono.
- Em seguida, normaliza os valores dividindo-os pela largura e altura da imagem, convertendo-os para o formato YOLO entre 0 e 1.
- Por fim, retorna a lista de coordenadas no formato YOLO (`[x_min_norm, y_min_norm, x_max_norm, y_max_norm]`).

**Observações:**

- Certifique-se de que as coordenadas poligonais representem corretamente a localização e o tamanho dos objetos nas imagens.
- A normalização garante que as coordenadas sejam independentes da resolução da imagem, permitindo que o modelo YOLO seja aplicado em imagens de tamanhos diferentes.
- Você pode adaptar a função para lidar com diferentes formatos de entrada para as coordenadas poligonais.

**Recursos Adicionais:**

- Ferramentas online e bibliotecas de código aberto podem te auxiliar na conversão de coordenadas poligonais para o formato YOLO.
- Algumas opções incluem:
  - **YOLO Annotation Tool:** [https://github.com/topics/annotation-tool](https://github.com/topics/annotation-tool)
  - **Roboflow:** [https://roboflow.com/](https://roboflow.com/)
  - **LabelImg:** [https://github.com/topics/image-labeling](https://github.com/topics/image-labeling)

**Lembre-se:**

- A precisão da detecção de objetos no YOLO depende da qualidade da anotação das imagens.
- Utilize este tutorial como um guia para converter suas coordenadas poligonais para o formato YOLO e adaptar o processo de acordo com suas necessidades específicas.
