# Fonte https://www.youtube.com/watch?v=r7Am-ZGMef8

if __name__ == "__main__":
    import torch

# Verifica se há dispositivos disponíveis
if torch.cuda.is_available():
    print("GPU encontrada. Detalhes:")
    for i in range(torch.cuda.device_count()):
        print("GPU {}: {}".format(i, torch.cuda.get_device_name(i)))
else:
    print("Nenhuma GPU encontrada. O treinamento será realizado na CPU.")

# Exemplo de código para verificar a utilização da GPU enquanto treina um modelo (opcional)
# Aqui, estamos simplesmente verificando a existência de GPUs, não estamos treinando um modelo
# Se estiver treinando um modelo, você pode monitorar a utilização da GPU com ferramentas como nvidia-smi
