// Definición de pines para motores
int motor1Pin1 = 3;
int motor1Pin2 = 4;
int motor2Pin1 = 5;
int motor2Pin2 = 6;
int enableMotor1 = 9;
int enableMotor2 = 10;

void setup() {
  // Configurar pines como salidas
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);
  pinMode(enableMotor1, OUTPUT);
  pinMode(enableMotor2, OUTPUT);

  // Habilitar los motores
  digitalWrite(enableMotor1, HIGH);
  digitalWrite(enableMotor2, HIGH);

  // Inicializar comunicación serial
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char comando = Serial.read();

    if (comando == 'A') {
      // Estado inicial — motores apagados
      detenerMotores();
    } else if (comando == 'S') {
      // Detener motores
      detenerMotores();
    } else if (comando == 'B') {
      // Encender motores hacia adelante
      avanzarMotores();
    }
  }
}

void detenerMotores() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
}

void avanzarMotores() {
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);
}
