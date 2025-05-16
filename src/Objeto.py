import cv2
import numpy as np
import serial
import time
import os

def detectar_colores(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Rango para el color rojo
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    # Rango para el color verde
    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    red_detected = cv2.countNonZero(mask_red) > 5000
    green_detected = cv2.countNonZero(mask_green) > 5000

    return red_detected, green_detected

def conectar_arduino():
    try:
        arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        time.sleep(2)
        print("✅ Arduino conectado en /dev/ttyACM0")
        return arduino
    except Exception as e:
        print(f"❌ No se pudo conectar al Arduino: {e}")
        return None

def encontrar_camara():
    for i in range(0, 10):
        if not os.path.exists(f"/dev/video{i}"):
            continue
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, _ = cap.read()
            if ret:
                print(f"📷 Cámara detectada en /dev/video{i}")
                return cap
        cap.release()
    print("❌ No se encontró una cámara funcional.")
    return None

def main():
    cap = encontrar_camara()
    if cap is None:
        return

    arduino = conectar_arduino()
    if arduino is None:
        cap.release()
        return

    estado = 'INICIAL'
    color_detectado = False
    t_apagado = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ No se pudo leer el frame.")
            break

        rojo, verde = detectar_colores(frame)
        color_ahora = rojo or verde

        if rojo and verde:
            print("🟡 Ambos colores detectados")
        elif rojo:
            print("🔴 Rojo detectado")
        elif verde:
            print("🟢 Verde detectado")

        if estado == 'INICIAL':
            arduino.write(b'A\n')
            if color_ahora:
                print("🛑 Color detectado — apagando motores")
                arduino.write(b'S\n')
                time.sleep(2)
                arduino.write(b'B\n')
                estado = 'AMBOS_ENCENDIDOS'
                color_detectado = True

        elif estado == 'AMBOS_ENCENDIDOS':
            if not color_ahora and color_detectado:
                print("🕒 Color perdido — manteniendo motores encendidos 4s")
                t_apagado = time.time()
                color_detectado = False
                estado = 'ESPERA_POST_COLOR'

        elif estado == 'ESPERA_POST_COLOR':
            arduino.write(b'B\n')
            if time.time() - t_apagado >= 4:
                print("↩️ Volviendo al estado inicial")
                estado = 'INICIAL'

        cv2.imshow("Camara", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    arduino.close()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
