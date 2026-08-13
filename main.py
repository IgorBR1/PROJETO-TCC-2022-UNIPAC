import pickle
import cv2

ARQUIVO_POSICOES = "TESTE1"

largura, altura = 90, 55

# Carrega posições salvas
try:
    with open(ARQUIVO_POSICOES, "rb") as c:
        posList = pickle.load(c)

    print(f"{len(posList)} vagas carregadas.")

except (FileNotFoundError, EOFError, pickle.PickleError):
    posList = []
    print("Nenhuma posição salva. Criando uma nova lista.")


drawing = False
start_x = 0
start_y = 0
current_x = 0
current_y = 0


def salvar_posicoes():
    with open(ARQUIVO_POSICOES, "wb") as c:
        pickle.dump(posList, c)


def mouseClick(event, x, y, flags, params):

    global drawing
    global start_x, start_y
    global current_x, current_y

    # Começou a arrastar
    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True

        start_x = x
        start_y = y

        current_x = x
        current_y = y

    # Enquanto arrasta
    elif event == cv2.EVENT_MOUSEMOVE and drawing:

        current_x = x
        current_y = y

    # Soltou o botão
    elif event == cv2.EVENT_LBUTTONUP:

        drawing = False

        current_x = x
        current_y = y

        # Calcula coordenadas
        x1 = min(start_x, current_x)
        y1 = min(start_y, current_y)

        x2 = max(start_x, current_x)
        y2 = max(start_y, current_y)

        nova_largura = x2 - x1
        nova_altura = y2 - y1

        # Só salva se tiver tamanho razoável
        if nova_largura > 20 and nova_altura > 20:

            posList.append(
                (x1, y1, nova_largura, nova_altura)
            )

            salvar_posicoes()

            print(
                f"Vaga criada: "
                f"x={x1}, y={y1}, "
                f"largura={nova_largura}, "
                f"altura={nova_altura}"
            )

    # Botão direito remove uma vaga
    elif event == cv2.EVENT_RBUTTONDOWN:

        for i, pos in enumerate(posList):

            x1, y1, w, h = pos

            if (
                x1 < x < x1 + w
                and
                y1 < y < y1 + h
            ):

                posList.pop(i)

                salvar_posicoes()

                print("Vaga removida.")

                break


while True:

    img = cv2.imread("car_park_test.png")

    if img is None:
        print("Erro: não foi possível carregar car_park_test.png")
        break

    # Desenha vagas já salvas
    for pos in posList:

        x, y, w, h = pos

        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (255, 255, 0),
            2
        )

    # Desenha o retângulo enquanto está arrastando
    if drawing:

        x1 = min(start_x, current_x)
        y1 = min(start_y, current_y)

        x2 = max(start_x, current_x)
        y2 = max(start_y, current_y)

        cv2.rectangle(
            img,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

    cv2.imshow("Estacionamento", img)

    cv2.setMouseCallback(
        "Estacionamento",
        mouseClick
    )

    # Q para sair
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()