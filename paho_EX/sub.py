import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

# ���Ŀ ���� �õ� ��� ó�� �ݹ� �Լ�
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    if rc == 0:
        client.subscribe("iot/#") # ���� ������ ���� ���� ��û
    else:
        print('���� ���� : ', rc)

# ���� ���� �޽��� ���� �ݹ� �Լ�
def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    print(f" {msg.topic} {value}")