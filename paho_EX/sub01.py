from sub import on_connect, on_message, mqtt

# 1. MQTT Ŭ���̾�Ʈ ��ü �ν��Ͻ�ȭ
client = mqtt.Client()

# 2. ���� �̺�Ʈ�� ���� �ݹ� �Լ� ���
client.on_connect = on_connect
client.on_message = on_message

try :
    # 3. ���Ŀ ����
    client.connect("localhost")
    # 4. �޽��� ���� - �̺�Ʈ �߻��� �ش� �ݹ� �Լ� ȣ���
    client.loop_forever()
except Exception as err:
    print('���� : %s'%err)

